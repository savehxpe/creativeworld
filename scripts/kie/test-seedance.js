/**
 * Test Seedance 1.5 Pro video generation.
 * 
 * Usage: node scripts/kie/test-seedance.js [image_url]
 * 
 * Requires .env with KIE_AI_API set.
 * Optionally pass an image URL to use as the starting frame.
 */

require('dotenv').config();
const kie = require('../../lib/kie/client');

async function main() {
    const imageUrl = process.argv[2] || null;
    
    console.log('=== Seedance 1.5 Pro Test ===\n');
    
    const prompt = `Turn this image into a 5-second high-converting social media ad.

Slow cinematic push-in.
Subtle realistic movement.
Strong subject focus.
First second must feel like a hook.
Movement should increase desire and FOMO.
Premium but relatable.
Designed for Instagram Reels, TikTok, Meta Stories, and paid ads.

No random shake.
No warping.
No distorted faces.
No unreadable text.
No unnatural hands.
No fake logos.

Style:
Premium social ad.
Culture-aware.
High-arousal.
Modern African/global creative direction.
Commercial but not corporate.
Sharp, stylish, emotionally clear.

Duration: 5 seconds.
Audio: subtle ambient sound design.`;

    try {
        const input = {
            prompt: prompt,
            aspect_ratio: '9:16',
            duration: '4',
            generate_audio: false
        };
        
        if (imageUrl) {
            input.image_urls = [imageUrl];
            console.log(`Using reference image: ${imageUrl}`);
        }
        
        const result = await kie.createSeedanceTask(input);
        
        console.log('\nTask created successfully.');
        console.log('Response:', JSON.stringify(result, null, 2).slice(0, 500));
        
        const taskId = result.taskId || result.data?.taskId;
        if (taskId) {
            console.log(`\nTo check status: node scripts/kie/test-task-status.js ${taskId}`);
        }
    } catch (e) {
        console.error('Test failed:', e.message);
        process.exit(1);
    }
}

main();
