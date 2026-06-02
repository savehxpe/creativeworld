/**
 * Test Suno sound/loop generation.
 * 
 * Usage: node scripts/suno/test-sound.js
 * 
 * Requires .env with SUNO_API_KEY set.
 */

require('dotenv').config();
const suno = require('../../lib/suno/client');

async function main() {
    console.log('=== Suno Sound Test ===\n');
    
    const prompt = `Create a short loopable brand sound for a luxury restaurant campaign.

Mood: warm, hungry, premium
Use case: 3-second brand tag
Tempo: 100
Style: modern, clean, memorable, minimal, premium
Avoid: vocals, copyrighted melodies, artist imitation, busy drums, long build-ups

The sound should feel like a brand cue people can remember after hearing it once.`;

    try {
        const result = await suno.createSoundTask({
            prompt: prompt,
            soundLoop: true,
            soundTempo: 100,
            soundKey: 'Any'
        });
        
        console.log('\nTask created successfully.');
        console.log('Response:', JSON.stringify(result, null, 2).slice(0, 500));
        
        const taskId = result.taskId;
        if (taskId) {
            console.log(`\nTo check status: node scripts/suno/test-task-status.js ${taskId}`);
        }
    } catch (e) {
        console.error('Test failed:', e.message);
        process.exit(1);
    }
}

main();
