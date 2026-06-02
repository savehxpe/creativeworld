/**
 * Competitor scan via Firecrawl.
 * 
 * Usage: node scripts/firecrawl/competitor-scan.js <brand_url> <competitor1_url> [competitor2_url] [competitor3_url]
 * 
 * Requires FIRECRAWL_API_KEY in .env (not committed).
 */

require('dotenv').config();
const fc = require('../../lib/firecrawl/client');

async function main() {
    const urls = process.argv.slice(2);
    if (urls.length < 2) { console.error('Usage: node scripts/firecrawl/competitor-scan.js <brand> <competitor1> [competitor2] [competitor3]'); process.exit(1); }

    console.log(`=== Competitor Scan: ${urls.length} sites ===\n`);
    
    try {
        const results = [];
        for (const url of urls) {
            console.log(`Scanning: ${url}`);
            const data = await fc.scrapePage(url, ['markdown']);
            results.push({ url, content: (data?.data?.markdown || data?.markdown || '').slice(0, 2000) });
        }

        const brand = results[0];
        const competitors = results.slice(1);
        
        const output = {
            brand_url: brand.url,
            competitors: competitors.map(c => ({
                url: c.url,
                positioning: extractSection(c.content, 'about|who.we.are|our.story'),
                visual_gaps: ['Analyze competitor visuals against brand direction.'],
                offer_gaps: ['Compare competitor offers to brand offer.'],
                cta_gaps: ['Compare competitor CTAs to brand CTA.'],
                proof_gaps: ['Compare competitor social proof to brand proof.']
            })),
            content_angles: [
                'Hook-driven social ads outperforming competitor content.',
                'Brand sound identity differentiating from visual-only competitors.',
                'Campaign system vs. random posting advantage.'
            ],
            ad_ideas: [
                '5-second competitor comparison hook.',
                '15-second social proof ad contrasting results.',
                'Brand sound tag for instant recognition vs. competitor silence.'
            ]
        };
        
        console.log(JSON.stringify(output, null, 2));
    } catch (e) {
        console.error('Scan failed:', e.message);
        process.exit(1);
    }
}

function extractSection(c, keywords) {
    const idx = c.search(new RegExp(keywords, 'i'));
    return idx > -1 ? c.slice(idx, idx + 300).trim() : 'Section not found.';
}

main();
