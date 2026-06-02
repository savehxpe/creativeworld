/**
 * Generate cinematic hero scenes for brand remix.
 * 
 * Usage: node scripts/cinematic/generate-scenes.js <brand_name>
 * 
 * Requires KIE_AI_API in .env (not committed).
 */

require('dotenv').config();
const fs = require('fs');
const path = require('path');

async function main() {
    const brandName = process.argv[2];
    if (!brandName) {
        console.error('Usage: node scripts/cinematic/generate-scenes.js <brand_name>');
        process.exit(1);
    }

    const brandDir = path.join(__dirname, '..', '..', 'outputs', 'cinematic', brandName);
    const analysisPath = path.join(brandDir, 'brand-analysis.json');
    if (!fs.existsSync(analysisPath)) {
        console.error('Run analyze-site.js first to create brand analysis.');
        process.exit(1);
    }

    const analysis = JSON.parse(fs.readFileSync(analysisPath));
    console.log(`=== Generating Scenes: ${brandName} ===\n`);

    const scenes = [
        {
            scene_title: 'The Hook',
            emotional_angle: 'Curiosity + Desire',
            product_focus: analysis.offer,
            camera_direction: 'Slow push-in on hero subject. Start wide, end tight.',
            lighting: 'Cinematic amber key light with soft fill.',
            motion_idea: '5-second slow zoom with subtle parallax.',
            nano_banana_prompt: `Premium 16:9 cinematic hero image for ${brandName}. ${analysis.industry}. Stop scrolling in 1 second. Strong subject focus. Negative space for headline. Warm amber lighting. No text. No logos.`,
            seedance_prompt: `Turn this into a 4-second cinematic hero video. Slow push-in. Subtle motion. First second = hook. 16:9. No shake. No warping.`
        },
        {
            scene_title: 'The Product',
            emotional_angle: 'Aspiration + Trust',
            product_focus: `${analysis.offer} in use`,
            camera_direction: 'Locked-off wide shot transitioning to detail macro.',
            lighting: 'Natural daylight. Clean. Premium.',
            motion_idea: 'Static to slow reveal of product detail.',
            nano_banana_prompt: `Premium 16:9 product showcase image for ${brandName}. Clean composition. Natural lighting. Premium feel. Space for text. No text. No logos.`,
            seedance_prompt: `Turn this into a 4-second cinematic product video. Subtle reveal. Clean motion. 16:9. No shake. No warping.`
        },
        {
            scene_title: 'The Feeling',
            emotional_angle: 'Belonging + Identity',
            product_focus: 'Brand lifestyle and atmosphere',
            camera_direction: 'Handheld feel. Candid moments. Warm tones.',
            lighting: 'Golden hour. Soft and warm. Natural.',
            motion_idea: 'Montage of slow-motion lifestyle shots.',
            nano_banana_prompt: `Premium 16:9 lifestyle image for ${brandName}. Golden hour lighting. Warm atmosphere. People enjoying the experience. Editorial feel. No text. No logos.`,
            seedance_prompt: `Turn this into a 4-second cinematic lifestyle video. Slow montage feel. Golden hour. 16:9. No shake. No warping.`
        }
    ];

    const imagesDir = path.join(brandDir, 'images');
    fs.mkdirSync(imagesDir, { recursive: true });
    fs.writeFileSync(path.join(brandDir, 'scenes.json'), JSON.stringify(scenes, null, 2));

    console.log(`Generated 3 scene concepts.`);
    console.log(`Scenes saved: ${path.join(brandDir, 'scenes.json')}`);
    console.log('\nKie image prompts are ready. To generate stills:');
    scenes.forEach((s, i) => {
        console.log(`\nScene ${i + 1}: ${s.scene_title}`);
        console.log(`  Prompt: ${s.nano_banana_prompt}`);
    });

    console.log('\n--- PAUSE ---');
    console.log('Generate stills via Kie, then run: node scripts/cinematic/build-demo-site.js <brand_name>');
}

main();
