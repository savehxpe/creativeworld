/**
 * Test Nano Banana 2 still image generation.
 * 
 * Usage: node scripts/kie/test-nano-banana.js
 * 
 * Requires .env with KIE_AI_API set.
 */

require('dotenv').config();
const kie = require('../../lib/kie/client');

async function main() {
    console.log('=== Nano Banana 2 Test ===\n');
    
    const prompt = `Premium social media advertising image for a luxury South African restaurant.
Campaign: The Reservation You Can't Get
Goal: Weekend bookings through scarcity
Emotion: FOMO, exclusivity, desire

High-arousal commercial advertising.
Cinematic but realistic.
Premium South African / African-global visual language.
Designed to stop scrolling in under 1 second.
Strong subject focus: intimate restaurant interior, candlelit table, blurred diners in background.
Clear negative space for headline.
Bold contrast between warm interior and dark exterior visible through window.
Luxury but accessible.
Hero subject in foreground: a single reserved table with a candle.
Intentional premium lighting: warm amber, soft shadows.
Looks like a campaign still from a serious modern creative agency.
Vertical 4:5.

No text.
No logos.
No fake brand names.`;

    try {
        const result = await kie.createNanoBananaTask({
            prompt: prompt,
            aspect_ratio: '4:5',
            resolution: '1K',
            output_format: 'jpg'
        });
        
        console.log('\nTask created successfully.');
        console.log('Response:', JSON.stringify(result, null, 2).slice(0, 500));
        
        // Poll for completion
        const taskId = result.taskId || result.data?.taskId;
        if (taskId) {
            console.log(`\nPolling task: ${taskId}`);
            
            let attempts = 0;
            const maxAttempts = 20;
            const pollInterval = 5000; // 5 seconds
            
            const poll = setInterval(async () => {
                attempts++;
                try {
                    const details = await kie.getTaskDetails(taskId);
                    console.log(`  Attempt ${attempts}: Progress details fetched`);
                    
                    const status = details.status || details.data?.status;
                    if (status === 'completed' || status === 'success') {
                        clearInterval(poll);
                        console.log('\nTask completed!');
                        console.log('Details:', JSON.stringify(details, null, 2).slice(0, 1000));
                    } else if (status === 'failed' || status === 'error') {
                        clearInterval(poll);
                        console.log('\nTask failed:', JSON.stringify(details, null, 2).slice(0, 500));
                    }
                } catch (e) {
                    console.log(`  Attempt ${attempts}: ${e.message.slice(0, 100)}`);
                }
                
                if (attempts >= maxAttempts) {
                    clearInterval(poll);
                    console.log('\nMax polling attempts reached. Check task manually:');
                    console.log(`  node scripts/kie/test-task-status.js ${taskId}`);
                }
            }, pollInterval);
        }
    } catch (e) {
        console.error('Test failed:', e.message);
        process.exit(1);
    }
}

main();
