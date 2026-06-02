/**
 * Lead research via Firecrawl.
 * 
 * Usage: node scripts/firecrawl/research-leads.js "<niche>" "<location>" "<search_query>"
 * 
 * Requires FIRECRAWL_API_KEY in .env (not committed).
 */

require('dotenv').config();
const fc = require('../../lib/firecrawl/client');

async function main() {
    const niche = process.argv[2] || 'restaurant';
    const location = process.argv[3] || 'Johannesburg';
    const query = process.argv[4] || `${niche} ${location} Instagram`;
    
    console.log(`=== Lead Research: ${niche} in ${location} ===\n`);
    
    try {
        const data = await fc.search(query, 10);
        const results = data?.data || [];
        
        const leads = results.map(r => ({
            lead_name: r.title || 'Unknown',
            url: r.url || '',
            niche: niche,
            reason_fits_outworld: `${niche} in ${location} with digital presence`,
            visible_pain_point: 'Content shows product but lacks campaign direction and sound identity.',
            outreach_angle: `Creative direction preview for ${niche}`
        }));
        
        console.log(JSON.stringify({ count: leads.length, leads }, null, 2));
    } catch (e) {
        console.error('Research failed:', e.message);
        process.exit(1);
    }
}

main();
