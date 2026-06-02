/**
 * Check Suno task status by ID.
 * 
 * Usage: node scripts/suno/test-task-status.js <taskId>
 * 
 * Requires .env with SUNO_API_KEY set.
 */

require('dotenv').config();
const suno = require('../../lib/suno/client');

async function main() {
    const taskId = process.argv[2];
    
    if (!taskId) {
        console.error('Usage: node scripts/suno/test-task-status.js <taskId>');
        process.exit(1);
    }
    
    console.log(`=== Suno Task Status: ${taskId} ===\n`);
    
    try {
        const details = await suno.getSunoTaskDetails(taskId);
        console.log(JSON.stringify(details, null, 2));
    } catch (e) {
        console.error('Failed:', e.message);
        process.exit(1);
    }
}

main();
