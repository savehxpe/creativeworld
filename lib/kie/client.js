/**
 * Kie API Client
 * Outworld Creative — Internal
 * 
 * Usage:
 *   const kie = require('./lib/kie/client');
 *   const task = await kie.createNanoBananaTask({ prompt: '...' });
 *   const result = await kie.getTaskDetails(task.taskId);
 * 
 * Security: Never logs the API key. Never prints raw responses containing keys.
 * Reads from process.env.KIE_AI_API (matching .env var name).
 */

const https = require('https');
const http = require('http');

const BASE_URL = 'https://api.kie.ai/api/v1/jobs';

function getApiKey() {
    const key = process.env.KIE_AI_API;
    if (!key) {
        throw new Error('KIE_AI_API not found in environment. Check your .env file.');
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
                        reject(new Error(`Kie HTTP error ${res.statusCode}: ${JSON.stringify(parsed)}`));
                    } else if (parsed.code && parsed.code !== 200) {
                        reject(new Error(`Kie API error ${parsed.code}: ${parsed.msg}`));
                    } else {
                        resolve(parsed);
                    }
                } catch (e) {
                    reject(new Error(`Failed to parse Kie API response: ${data.slice(0, 200)}`));
                }
            });
        });

        req.on('error', (e) => reject(new Error(`Kie API request failed: ${e.message}`)));
        
        if (body) {
            req.write(JSON.stringify(body));
        }
        req.end();
    });
}

/**
 * Create a Nano Banana 2 image generation task.
 * @param {Object} input
 * @param {string} input.prompt - Image generation prompt
 * @param {string} [input.aspect_ratio='4:5'] - Aspect ratio
 * @param {string} [input.resolution='1K'] - Resolution (1K, 2K, 4K)
 * @param {string} [input.output_format='jpg'] - Output format (png, jpg)
 * @returns {Promise<Object>} Task response with taskId
 */
async function createNanoBananaTask(input) {
    const body = {
        model: 'nano-banana-2',
        input: {
            prompt: input.prompt,
            image_input: input.image_input || [],
            aspect_ratio: input.aspect_ratio || 'auto',
            resolution: input.resolution || '1K',
            output_format: input.output_format || 'png'
        }
    };
    console.log(`[Kie] Creating Nano Banana 2 task... (prompt: ${input.prompt.length} chars, ratio: ${body.input.aspect_ratio}, res: ${body.input.resolution}, fmt: ${body.input.output_format})`);
    const result = await apiRequest('/createTask', 'POST', body);
    const taskId = result.taskId || result.data?.taskId;
    console.log(`[Kie] Task created: ${taskId || JSON.stringify(result).slice(0, 100)}`);
    return result;
}

/**
 * Create a Seedance 1.5 Pro video generation task.
 * @param {Object} input
 * @param {string} input.prompt - Video generation prompt
 * @param {string[]} [input.image_urls] - Optional reference image URLs
 * @param {string} [input.aspect_ratio='9:16'] - Aspect ratio
 * @param {string} [input.duration='4'] - Duration (4, 8, 12)
 * @param {boolean} [input.generate_audio=false] - Generate audio
 * @returns {Promise<Object>} Task response with taskId
 */
async function createSeedanceTask(input) {
    const body = {
        model: 'bytedance/seedance-1.5-pro',
        input: {
            prompt: input.prompt,
            aspect_ratio: input.aspect_ratio || '9:16',
            duration: input.duration || '4',
            fixed_lens: input.fixed_lens !== undefined ? input.fixed_lens : false,
            generate_audio: input.generate_audio !== undefined ? input.generate_audio : false,
            nsfw_checker: false
        }
    };
    
    if (input.image_urls && input.image_urls.length > 0) {
        body.input.image_urls = input.image_urls;
    }
    
    console.log('[Kie] Creating Seedance 1.5 Pro task...');
    const result = await apiRequest('/createTask', 'POST', body);
    const taskId = result.taskId || result.data?.taskId;
    console.log(`[Kie] Task created: ${taskId || JSON.stringify(result).slice(0, 100)}`);
    return result;
}

/**
 * Create a Kling 3.0 motion control video generation task.
 * @param {Object} input
 * @param {string[]} input.image_urls - Reference image URLs (required)
 * @param {string[]} input.video_urls - Motion video URLs (required)
 * @param {string} [input.mode='720p'] - Resolution mode
 * @returns {Promise<Object>} Task response with taskId
 */
async function createKlingMotionTask(input) {
    if (!input.image_urls || input.image_urls.length === 0) {
        throw new Error('Kling motion control requires image_urls');
    }
    if (!input.video_urls || input.video_urls.length === 0) {
        throw new Error('Kling motion control requires video_urls');
    }
    
    const body = {
        model: 'kling-3.0/motion-control',
        image_urls: input.image_urls,
        video_urls: input.video_urls,
        mode: input.mode || '720p',
        character_orientation: input.character_orientation || 'video',
        background_source: input.background_source || 'input_video'
    };
    
    console.log('[Kie] Creating Kling 3.0 motion control task...');
    const result = await apiRequest('/createTask', 'POST', body);
    console.log(`[Kie] Task created: ${result.taskId || result.data?.taskId || JSON.stringify(result).slice(0, 100)}`);
    return result;
}

/**
 * Get task details and status.
 * @param {string} taskId - The task ID
 * @returns {Promise<Object>} Task details including status, output URLs
 */
async function getTaskDetails(taskId) {
    console.log(`[Kie] Fetching details for task: ${taskId}`);
    const result = await apiRequest('/recordInfo?taskId=' + taskId, 'GET', null);
    return result;
}

module.exports = {
    createNanoBananaTask,
    createSeedanceTask,
    createKlingMotionTask,
    getTaskDetails
};
