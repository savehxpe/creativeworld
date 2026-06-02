/**
 * Check task status by ID.
 * 
 * Usage: node scripts/kie/test-task-status.js <taskId>
 * 
 * Requires .env with KIE_AI_API set.
 */

require('dotenv').config();
const kie = require('../../lib/kie/client');

async function main() {
    const taskId = process.argv[2];
    
    if (!taskId) {
        console.error('Usage: node scripts/kie/test-task-status.js <taskId>');
        process.exit(1);
    }
    
    console.log(`=== Task Status: ${taskId} ===\n`);
    
    try {
        const details = await kie.getTaskDetails(taskId);
        console.log(JSON.stringify(details, null, 2));
    } catch (e) {
        console.error('Failed:', e.message);
        process.exit(1);
    }
}

main();
