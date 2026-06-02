/**
 * Firecrawl API Client
 * Outworld Creative — Internal
 * 
 * Usage:
 *   const fc = require('./lib/firecrawl/client');
 *   const data = await fc.scrapePage('https://example.com');
 * 
 * Never logs the API key. Never prints raw responses containing keys.
 */

const https = require('https');

const BASE_URL = 'https://api.firecrawl.dev/v1';

function getApiKey() {
    const key = process.env.FIRECRAWL_API_KEY;
    if (!key) {
        throw new Error('FIRECRAWL_API_KEY not found in environment. Set it in .env (not committed).');
    }
    return key;
}

function getAuthHeaders() {
    return {
        'Authorization': `Bearer ${getApiKey()}`,
        'Content-Type': 'application/json'
    };
}

function apiRequest(path, method, body) {
    return new Promise((resolve, reject) => {
        const url = new URL(BASE_URL + path);
        const options = {
            hostname: url.hostname,
            path: url.pathname,
            method: method,
            headers: getAuthHeaders()
        };
        const req = https.request(options, (res) => {
            let data = '';
            res.on('data', chunk => data += chunk);
            res.on('end', () => {
                try {
                    resolve(JSON.parse(data));
                } catch (e) {
                    reject(new Error(`Firecrawl parse error: ${data.slice(0, 200)}`));
                }
            });
        });
        req.on('error', (e) => reject(new Error(`Firecrawl request failed: ${e.message}`)));
        if (body) req.write(JSON.stringify(body));
        req.end();
    });
}

/**
 * Scrape a single page for analysis.
 */
async function scrapePage(url, formats = ['markdown']) {
    console.log(`[Firecrawl] Scraping: ${url}`);
    return apiRequest('/scrape', 'POST', { url, formats });
}

/**
 * Search and scrape results.
 */
async function search(query, limit = 5) {
    console.log(`[Firecrawl] Searching: ${query}`);
    return apiRequest('/search', 'POST', { query, limit });
}

module.exports = { scrapePage, search };
