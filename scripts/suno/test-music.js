/**
 * Test Suno full music generation.
 * 
 * Usage: node scripts/suno/test-music.js
 * 
 * Requires .env with SUNO_API_KEY set.
 */

require('dotenv').config();
const suno = require('../../lib/suno/client');

async function main() {
    console.log('=== Suno Music Test ===\n');
    
    const prompt = `Modern instrumental brand anthem for a premium South African creative studio.
Style: cinematic, minimal, confident.
No vocals. Clean production. Memorable after one listen.`;

    try {
        const result = await suno.createMusicTask({
            prompt: prompt,
            instrumental: true
        });
        
        console.log('\nTask created successfully.');
        console.log('Response:', JSON.stringify(result, null, 2).slice(0, 500));
        
        const taskId = result.taskId;
        if (taskId) {
            console.log(`\nTo check status: node scripts/suno/test-task-status.js ${taskId}`);
            console.log('Note: Full music takes ~2-3 minutes for downloadable URLs.');
        }
    } catch (e) {
        console.error('Test failed:', e.message);
        process.exit(1);
    }
}

main();
