/**
 * Build cinematic demo landing page.
 * 
 * Usage: node scripts/cinematic/build-demo-site.js <brand_name>
 */

require('dotenv').config();
const fs = require('fs');
const path = require('path');

async function main() {
    const brandName = process.argv[2];
    if (!brandName) {
        console.error('Usage: node scripts/cinematic/build-demo-site.js <brand_name>');
        process.exit(1);
    }

    const brandDir = path.join(__dirname, '..', '..', 'outputs', 'cinematic', brandName);
    const analysisPath = path.join(brandDir, 'brand-analysis.json');
    if (!fs.existsSync(analysisPath)) {
        console.error('Run analyze-site.js first.');
        process.exit(1);
    }

    const analysis = JSON.parse(fs.readFileSync(analysisPath));
    const color = analysis.colors;
    const name = analysis.brand_name;

    const html = `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>${name} — Cinematic</title>
<style>
:root{--bg:#0a0a0a;--text:#f5f5f5;--muted:#a0a0a0;--accent:${color.accent}}
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:-apple-system,BlinkMacSystemFont,sans-serif;background:var(--bg);color:var(--text);line-height:1.6}
section{padding:5rem 2rem;max-width:1100px;margin:0 auto}
h1{font-size:clamp(2rem,5vw,3.5rem);line-height:1.1;margin-bottom:1rem}
h2{font-size:clamp(1.5rem,3vw,2rem);margin-bottom:1rem}
p{color:var(--muted);font-size:1rem;line-height:1.7}
.hero{min-height:100vh;display:flex;align-items:center;justify-content:center;text-align:center;position:relative;overflow:hidden}
.hero-video{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;opacity:.6}
.hero-content{position:relative;z-index:1;max-width:700px}
.btn{display:inline-block;padding:.8rem 1.8rem;background:var(--accent);color:#fff;text-decoration:none;font-weight:600;border-radius:4px;margin-top:1.5rem;transition:transform .2s}
.btn:hover{transform:translateY(-2px)}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:2rem;margin-top:2rem}
.card{background:#161616;border:1px solid #2a2a2a;padding:1.5rem;border-radius:8px}
.card h3{font-size:1.1rem;margin-bottom:.5rem}
.how-grid{display:flex;flex-direction:column;gap:1.5rem;margin-top:2rem}
.step{display:flex;gap:1.5rem;align-items:flex-start;background:#161616;border:1px solid #2a2a2a;padding:1.5rem;border-radius:8px}
.step-num{width:40px;height:40px;min-width:40px;background:var(--accent);display:flex;align-items:center;justify-content:center;font-weight:700;border-radius:6px;font-size:1.1rem}
.cta-section{text-align:center;padding:6rem 2rem;background:linear-gradient(to bottom,transparent,rgba(229,57,53,.03))}
.cta-section a{color:var(--text);font-size:1.1rem;font-weight:600;border-bottom:2px solid var(--accent);padding-bottom:.2rem;text-decoration:none}
footer{text-align:center;padding:2rem;border-top:1px solid #2a2a2a;color:var(--muted);font-size:.8rem}
@media(prefers-reduced-motion:reduce){*{animation:none!important}}
@media(max-width:768px){.hero{padding:4rem 1.5rem}.step{flex-direction:column;gap:1rem}}
</style>
</head>
<body>
<section class="hero">
  <video class="hero-video" autoplay muted loop playsinline preload="none" loading="lazy" poster="images/hero-poster.jpg">
    <source src="videos/hero.webm" type="video/webm">
    <source src="videos/hero.mp4" type="video/mp4">
  </video>
  <div class="hero-content">
    <h1>${name}</h1>
    <p>${analysis.offer}</p>
    <a href="#contact" class="btn">${analysis.missing_cta || 'Get Started'}</a>
  </div>
</section>

<section id="story">
  <h2>Brand Story</h2>
  <p>${analysis.notes || 'A premium brand built for people who value quality, experience, and attention to detail.'}</p>
</section>

<section id="product">
  <h2>What We Offer</h2>
  <div class="grid">
    <div class="card"><h3>Premium Quality</h3><p>Every detail considered. Every experience crafted.</p></div>
    <div class="card"><h3>Trusted Process</h3><p>Built on reputation. Proven by results.</p></div>
    <div class="card"><h3>Lasting Impact</h3><p>Not just a transaction. A relationship.</p></div>
  </div>
</section>

<section id="how">
  <h2>How It Works</h2>
  <div class="how-grid">
    <div class="step"><div class="step-num">1</div><div><h3>Discover</h3><p>We learn about your needs, preferences, and goals.</p></div></div>
    <div class="step"><div class="step-num">2</div><div><h3>Create</h3><p>We build your solution with premium attention to detail.</p></div></div>
    <div class="step"><div class="step-num">3</div><div><h3>Deliver</h3><p>You receive a finished experience that exceeds expectations.</p></div></div>
  </div>
</section>

<section id="trust">
  <h2>Trusted By</h2>
  <div class="grid">
    <div class="card"><h3>${analysis.trust_signals[0] || 'Quality Guaranteed'}</h3><p>We stand behind every experience we create.</p></div>
    <div class="card"><h3>${analysis.trust_signals[1] || 'Proven Results'}</h3><p>Our clients return and refer. That says everything.</p></div>
  </div>
</section>

<section class="cta-section" id="contact">
  <h2>Ready to Experience ${name}?</h2>
  <p>Let's create something memorable together.</p>
  <a href="#">Contact Us</a>
</section>

<footer><p>${name}. Premium experience. Built with care.</p></footer>
</body>
</html>`;

    fs.writeFileSync(path.join(brandDir, 'index.html'), html);
    console.log(`Demo site built: ${path.join(brandDir, 'index.html')}`);
    console.log('Preview: open ' + path.join(brandDir, 'index.html'));
    console.log('\nTo deploy to Vercel: vercel ' + brandDir);
}

main();
