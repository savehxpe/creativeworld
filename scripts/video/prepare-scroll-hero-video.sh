#!/usr/bin/env bash
# prepare-scroll-hero-video.sh
# Generate poster, WebM, and MP4 from a source hero video.
# Usage:
#   bash scripts/video/prepare-scroll-hero-video.sh "/Volumes/T7 Shield/Downloads/7536a0aa9ba6a01e1487568a92bec3ce_1780451715_tbboj8bh.mp4"
#
# Targets:
#   - WebM  under 2-3MB
#   - MP4   under 3-5MB
#   - Poster under 300KB
#   - No audio track
#   - 12s source → smooth background motion at reduced fps

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(cd "$SCRIPT_DIR/../.." && pwd)"
cd "$PROJECT_ROOT"

INPUT="${1:-}"
if [ -z "$INPUT" ]; then
    echo "Usage: bash scripts/video/prepare-scroll-hero-video.sh <input.mp4>"
    echo ""
    echo "Example:"
    echo '  bash scripts/video/prepare-scroll-hero-video.sh "/Volumes/T7 Shield/Downloads/7536a0aa9ba6a01e1487568a92bec3ce_1780451715_tbboj8bh.mp4"'
    exit 1
fi

if [ ! -f "$INPUT" ]; then
    echo "Error: input file not found: $INPUT"
    exit 1
fi

OUTDIR="landing_page/assets/video"
mkdir -p "$OUTDIR"

POSTER="$OUTDIR/outworld-scroll-hero-poster.jpg"
WEBM="$OUTDIR/outworld-scroll-hero.webm"
MP4="$OUTDIR/outworld-scroll-hero.mp4"

echo "=== Outworld Scroll-Hero Video Preparation ==="
echo "Input:  $INPUT"
echo "Output: $OUTDIR"
echo ""

# --- Poster (frame at 1s) ---
echo "[1/3] Generating poster..."
ffmpeg -y -ss 00:00:01 -i "$INPUT" -frames:v 1 -q:v 3 "$POSTER"
ls -lh "$POSTER"

# --- WebM (VP9, no audio) ---
echo ""
echo "[2/3] Generating WebM (VP9, CRF 38, 1600px, 20fps)..."
ffmpeg -y -i "$INPUT" -vf "scale=1600:-2,fps=20" \
    -c:v libvpx-vp9 -crf 38 -b:v 0 -an \
    -deadline good -cpu-used 4 -row-mt 1 "$WEBM"
ls -lh "$WEBM"

# Check size; if over 3MB, retry with higher CRF and lower scale
WEBM_SIZE=$(stat -f%z "$WEBM" 2>/dev/null || stat -c%s "$WEBM")
if [ "$WEBM_SIZE" -gt 3145728 ]; then
    echo ""
    echo "WebM too large ($WEBM_SIZE bytes). Re-encoding with CRF 40 / scale 1400 / fps 18..."
    ffmpeg -y -i "$INPUT" -vf "scale=1400:-2,fps=18" \
        -c:v libvpx-vp9 -crf 40 -b:v 0 -an \
        -deadline good -cpu-used 4 -row-mt 1 "$WEBM"
    ls -lh "$WEBM"
fi

WEBM_SIZE=$(stat -f%z "$WEBM" 2>/dev/null || stat -c%s "$WEBM")
if [ "$WEBM_SIZE" -gt 3145728 ]; then
    echo ""
    echo "WebM still too large ($WEBM_SIZE bytes). Re-encoding with CRF 42 / scale 1200 / fps 16..."
    ffmpeg -y -i "$INPUT" -vf "scale=1200:-2,fps=16" \
        -c:v libvpx-vp9 -crf 42 -b:v 0 -an \
        -deadline good -cpu-used 4 -row-mt 1 "$WEBM"
    ls -lh "$WEBM"
fi

# --- MP4 fallback (H.264, no audio) ---
echo ""
echo "[3/3] Generating MP4 fallback (H.264, CRF 30, 1600px, 20fps)..."
ffmpeg -y -i "$INPUT" -vf "scale=1600:-2,fps=20" \
    -c:v libx264 -crf 30 -preset medium -movflags +faststart -an "$MP4"
ls -lh "$MP4"

# Check size; if over 5MB, retry with higher CRF and lower scale
MP4_SIZE=$(stat -f%z "$MP4" 2>/dev/null || stat -c%s "$MP4")
if [ "$MP4_SIZE" -gt 5242880 ]; then
    echo ""
    echo "MP4 too large ($MP4_SIZE bytes). Re-encoding with CRF 32 / scale 1400 / fps 18..."
    ffmpeg -y -i "$INPUT" -vf "scale=1400:-2,fps=18" \
        -c:v libx264 -crf 32 -preset medium -movflags +faststart -an "$MP4"
    ls -lh "$MP4"
fi

echo ""
echo "=== Done ==="
echo "Poster: $POSTER"
echo "WebM:   $WEBM"
echo "MP4:    $MP4"
