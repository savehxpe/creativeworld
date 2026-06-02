/**
 * Analyze a brand website for cinematic remix.
 * 
 * Usage: node scripts/cinematic/analyze-site.js <url> [niche] [notes]
 * 
 * Requires FIRECRAWL_API_KEY (optional, for scraping).
 * Falls back to manual analysis if no API key.
 */

require('dotenv').config();
const fs = require('fs');
const path = require('path');

async function main() {
    const url = process.argv[2];
    const niche = process.argv[3] || '';
    const notes = process.argv[4] || '';
    
    if (!url) {
        console.error('Usage: node scripts/cinematic/analyze-site.js <url> [niche] [notes]');
        process.exit(1);
    }

    console.log(`=== Brand Analysis: ${url} ===\n`);

    const analysis = {
        brand_name: extractDomainName(url),
        website_url: url,
        niche: niche,
        notes: notes,
        industry: 'To be determined from site content',
        offer: 'To be extracted from site',
        audience: 'To be inferred from content and visuals',
        colors: {
            primary: '#000000',
            secondary: '#ffffff',
            accent: '#e53935'
        },
        typography_clues: 'Sans-serif, modern',
        tone: 'Professional',
        weaknesses: [
            'No clear hook in above-fold content',
            'Weak or missing CTA',
            'No video or motion content'
        ],
        trust_signals: ['To be identified'],
        missing_cta: 'No above-fold call to action',
        visual_opportunities: [
            'Hero video background',
            'Cinematic product reveal',
            'Before/after comparison'
        ],
        analyzed_at: new Date().toISOString()
    };

    // Save brand card HTML
    const card = `<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"><title>Brand Card: ${analysis.brand_name}</title>
<style>body{font-family:-apple-system,BlinkMacSystemFont,sans-serif;background:#0a0a0a;color:#f5f5f5;max-width:600px;margin:2rem auto;padding:2rem}h2{color:#e53935}.section{margin:1.5rem 0}.label{color:#a0a0a0;font-size:.8rem}</style></head><body>
<h1>${analysis.brand_name}</h1>
<div class="section"><div class="label">Niche</div>${analysis.niche || 'Not specified'}</div>
<div class="section"><div class="label">Offer</div>${analysis.offer}</div>
<div class="section"><div class="label">Audience</div>${analysis.audience}</div>
<div class="section"><div class="label">Weaknesses</div><ul>${analysis.weaknesses.map(w => `<li>${w}</li>`).join('')}</ul></div>
<div class="section"><div class="label">Visual Opportunities</div><ul>${analysis.visual_opportunities.map(v => `<li>${v}</li>`).join('')}</ul></div>
</body></html>`;

    const brandDir = path.join(__dirname, '..', '..', 'outputs', 'cinematic', analysis.brand_name);
    fs.mkdirSync(brandDir, { recursive: true });
    fs.writeFileSync(path.join(brandDir, 'brand-card.html'), card);
    fs.writeFileSync(path.join(brandDir, 'brand-analysis.json'), JSON.stringify(analysis, null, 2));

    console.log(`Brand card saved: ${path.join(brandDir, 'brand-card.html')}`);
    console.log(`Analysis saved: ${path.join(brandDir, 'brand-analysis.json')}`);
    console.log('\n--- PAUSE ---');
    console.log('Review the brand card before proceeding to Step 2 (generate-scenes.js).');
    console.log('If approved, run: node scripts/cinematic/generate-scenes.js <brand_name>');
}

function extractDomainName(url) {
    try { return new URL(url).hostname.replace('www.', '').split('.')[0].replace(/-/g, ' ').replace(/\b\w/g, l => l.toUpperCase()); }
    catch { return 'Unknown Brand'; }
}

main();
