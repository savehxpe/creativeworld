/**
 * Suno API Client
 * Outworld Creative — Internal
 * 
 * Usage:
 *   const suno = require('./lib/suno/client');
 *   const task = await suno.createSoundTask({ prompt: '...' });
 *   const result = await suno.getSunoTaskDetails(task.taskId);
 * 
 * Security: Never logs the API key. Never prints raw responses containing keys.
 * Reads from process.env.SUNO_API_KEY.
 */

const https = require('https');

const BASE_URL = 'https://api.sunoapi.org/api/v1';

function getApiKey() {
    const key = process.env.SUNO_API_KEY;
    if (!key) {
        throw new Error('SUNO_API_KEY not found in environment. Check your .env file.');
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
                    const parsed = JSON.parse(data);
                    if (res.statusCode >= 400) {
                        reject(new Error(`Suno API error ${res.statusCode}: ${JSON.stringify(parsed)}`));
                    } else {
                        resolve(parsed);
                    }
                } catch (e) {
                    reject(new Error(`Failed to parse Suno API response: ${data.slice(0, 200)}`));
                }
            });
        });

        req.on('error', (e) => reject(new Error(`Suno API request failed: ${e.message}`)));
        
        if (body) {
            req.write(JSON.stringify(body));
        }
        req.end();
    });
}

/**
 * Create a sound/loop generation task.
 * Best for brand tags, social loops, and audio cues.
 * 
 * @param {Object} input
 * @param {string} input.prompt - Sound generation prompt
 * @param {string} [input.model='V5'] - Model version
 * @param {boolean} [input.soundLoop=true] - Create loopable output
 * @param {number} [input.soundTempo=100] - BPM (85-150 depending on niche)
 * @param {string} [input.soundKey='Any'] - Musical key
 * @param {boolean} [input.grabLyrics=false] - Extract lyrics
 * @returns {Promise<Object>} Task response with taskId
 */
async function createSoundTask(input) {
    const body = {
        model: input.model || 'V5',
        prompt: input.prompt,
        soundLoop: input.soundLoop !== undefined ? input.soundLoop : true,
        soundTempo: input.soundTempo || 100,
        soundKey: input.soundKey || 'Any',
        grabLyrics: input.grabLyrics !== undefined ? input.grabLyrics : false
    };
    console.log('[Suno] Creating sound task...');
    const result = await apiRequest('/generate/sounds', 'POST', body);
    console.log(`[Suno] Task created: ${result.taskId || JSON.stringify(result).slice(0, 100)}`);
    return result;
}

/**
 * Create a full music generation task.
 * Returns 2 songs per request. Stream URL in ~30-40s, download URL in ~2-3min.
 * 
 * @param {Object} input
 * @param {string} input.prompt - Music generation prompt
 * @param {string} [input.model='V5'] - Model version
 * @param {boolean} [input.instrumental=true] - Instrumental only (brand use = instrumental)
 * @param {boolean} [input.make_instrumental=false] - Convert to instrumental
 * @returns {Promise<Object>} Task response with taskId
 */
async function createMusicTask(input) {
    const body = {
        model: input.model || 'V5',
        prompt: input.prompt,
        instrumental: input.instrumental !== undefined ? input.instrumental : true,
        make_instrumental: input.make_instrumental !== undefined ? input.make_instrumental : false
    };
    console.log('[Suno] Creating music task...');
    const result = await apiRequest('/generate/music', 'POST', body);
    console.log(`[Suno] Task created: ${result.taskId || JSON.stringify(result).slice(0, 100)}`);
    return result;
}

/**
 * Get task details and status.
 * @param {string} taskId - The task ID
 * @returns {Promise<Object>} Task details including status, stream URLs, download URLs
 */
async function getSunoTaskDetails(taskId) {
    console.log(`[Suno] Fetching details for task: ${taskId}`);
    const result = await apiRequest('/tasks/status', 'POST', { taskId });
    return result;
}

module.exports = {
    createSoundTask,
    createMusicTask,
    getSunoTaskDetails
};
