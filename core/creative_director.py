"""
Creative Director Orchestrator.
Generates complete creative direction packages: audits, spec ads, campaign systems, and reports.
"""
import os
from datetime import datetime
from prompts.creative_director_prompts import (
    build_creative_director_prompt,
    build_single_spec_ad_prompt,
    build_campaign_system_prompt,
    build_hook_bank_prompt,
    build_brand_world_prompt,
    build_competitor_gap_prompt
)
from prompts.audit_prompts import (
    build_creative_audit_prompt,
    build_revenue_loss_prompt,
    build_200_blueprint_prompt
)
from core.ai_analyzer import AIAnalyzer
from config.settings import DOCS_DIR, SPEC_AD_LAB_DIR
from config.niches import get_niche_config


class CreativeDirector:
    """
    The Master High-Arousal Ad Director.
    Generates premium creative direction packages using AI.
    """
    
    def __init__(self):
        self.ai = AIAnalyzer()
        os.makedirs(SPEC_AD_LAB_DIR, exist_ok=True)
        os.makedirs(DOCS_DIR, exist_ok=True)
    
    def generate_spec_ad_concepts(self, niche, business_type, offer, emotion, brand_voice="premium"):
        """
        Generate 3 spec ad concepts for a brand.
        
        Returns:
            dict with 3 ad concepts
        """
        prompt = build_creative_director_prompt(niche, business_type, offer, emotion, brand_voice)
        print(f"[Creative Director] Generating 3 spec ad concepts for {business_type}...")
        
        result = self.ai.analyze_website(prompt)
        return {
            "niche": niche,
            "business_type": business_type,
            "concepts": result,
            "generated_at": datetime.now().isoformat()
        }
    
    def generate_single_spec_ad(self, campaign_name, niche, goal, ad_style, emotion, hook, visual_description):
        """
        Generate a single detailed spec ad brief.
        """
        prompt = build_single_spec_ad_prompt(campaign_name, niche, goal, ad_style, emotion, hook, visual_description)
        print(f"[Creative Director] Generating spec ad brief for '{campaign_name}'...")
        
        result = self.ai.analyze_website(prompt)
        return {
            "campaign_name": campaign_name,
            "brief": result,
            "generated_at": datetime.now().isoformat()
        }
    
    def generate_creative_audit(self, brand_name, niche, current_state, website_url=None, instagram_handle=None):
        """
        Generate a full Creative Direction Audit report.
        
        Returns:
            str: The audit content
        """
        prompt = build_creative_audit_prompt(brand_name, niche, current_state, website_url, instagram_handle)
        print(f"[Creative Director] Generating creative audit for {brand_name}...")
        
        return self.ai.analyze_website(prompt)
    
    def generate_revenue_loss_analysis(self, niche, monthly_traffic, conversion_rate, average_order_value, current_marketing_spend=None):
        """
        Generate a revenue loss quantification.
        """
        prompt = build_revenue_loss_prompt(niche, monthly_traffic, conversion_rate, average_order_value, current_marketing_spend)
        print(f"[Creative Director] Generating revenue loss analysis...")
        
        return self.ai.analyze_website(prompt)
    
    def generate_200_blueprint(self, brand_name, niche, current_state, goals, timeline="90 days"):
        """
        Generate a 200% revenue blueprint.
        """
        prompt = build_200_blueprint_prompt(brand_name, niche, current_state, goals, timeline)
        print(f"[Creative Director] Generating 200% blueprint for {brand_name}...")
        
        return self.ai.analyze_website(prompt)
    
    def generate_campaign_system(self, brand_name, niche, current_state, goals, competitor_landscape):
        """
        Generate a full monthly campaign system.
        """
        prompt = build_campaign_system_prompt(brand_name, niche, current_state, goals, competitor_landscape)
        print(f"[Creative Director] Generating campaign system for {brand_name}...")
        
        return self.ai.analyze_website(prompt)
    
    def generate_hook_bank(self, niche, count=20):
        """
        Generate a bank of scroll-stopping hooks.
        """
        prompt = build_hook_bank_prompt(niche, count)
        print(f"[Creative Director] Generating {count} hooks for {niche}...")
        
        return self.ai.analyze_website(prompt)
    
    def generate_brand_world(self, brand_name, niche, current_content_style, target_audience, brand_values):
        """
        Generate a brand world system.
        """
        prompt = build_brand_world_prompt(brand_name, niche, current_content_style, target_audience, brand_values)
        print(f"[Creative Director] Generating brand world for {brand_name}...")
        
        return self.ai.analyze_website(prompt)
    
    def generate_competitor_gap(self, brand_name, niche, top_competitors, brand_strengths, brand_weaknesses):
        """
        Generate a competitor gap report.
        """
        prompt = build_competitor_gap_prompt(brand_name, niche, top_competitors, brand_strengths, brand_weaknesses)
        print(f"[Creative Director] Generating competitor gap report for {brand_name}...")
        
        return self.ai.analyze_website(prompt)
    
    def save_spec_ad_package(self, brand_name, niche, package_content):
        """
        Save a spec ad package to the spec-lab directory.
        """
        filename = f"{brand_name.lower().replace(' ', '_')}_{niche}_spec_ad.md"
        filepath = os.path.join(SPEC_AD_LAB_DIR, filename)
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"# Spec Ad Package: {brand_name}\n\n")
            f.write(f"Niche: {niche}\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
            f.write("---\n\n")
            f.write(package_content)
        
        print(f"[Creative Director] Saved spec ad package: {filepath}")
        return filepath
    
    def save_audit_report(self, brand_name, audit_content):
        """
        Save an audit report.
        """
        filename = f"{brand_name.lower().replace(' ', '_')}_audit.md"
        filepath = os.path.join(DOCS_DIR, filename)
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"# Creative Direction Audit: {brand_name}\n\n")
            f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
            f.write("---\n\n")
            f.write(audit_content)
        
        print(f"[Creative Director] Saved audit report: {filepath}")
        return filepath
    
    def generate_full_diagnosis_package(self, brand_name, niche, current_state, website_url=None, instagram_handle=None):
        """
        Generate the complete Creative Diagnosis package:
        1. Creative Direction Audit
        2. Revenue Loss Analysis
        3. 200% Blueprint
        4. 3 Spec Ad Concepts
        
        Returns:
            dict with all components
        """
        print(f"\n{'='*60}")
        print(f"GENERATING FULL CREATIVE DIAGNOSIS: {brand_name}")
        print(f"{'='*60}")
        
        niche_config = get_niche_config(niche)
        
        # 1. Creative Audit
        print("\n[1/4] Creative Direction Audit...")
        audit = self.generate_creative_audit(brand_name, niche, current_state, website_url, instagram_handle)
        
        # 2. Revenue Loss (using niche default example)
        print("\n[2/4] Revenue Loss Analysis...")
        revenue_loss = "Revenue loss analysis based on niche benchmarks. " + niche_config.get("revenue_loss_example", "")
        
        # 3. 200% Blueprint
        print("\n[3/4] 200% Revenue Blueprint...")
        blueprint = self.generate_200_blueprint(
            brand_name, niche, current_state, 
            goals=f"Double monthly revenue through premium creative direction"
        )
        
        # 4. Spec Ad Concepts
        print("\n[4/4] Spec Ad Concepts...")
        spec_ads = self.generate_spec_ad_concepts(
            niche=niche,
            business_type=brand_name,
            offer=niche_config["examples"][0] if niche_config["examples"] else "premium offering",
            emotion="desire",
            brand_voice="premium"
        )
        
        package = {
            "brand_name": brand_name,
            "niche": niche,
            "audit": audit,
            "revenue_loss": revenue_loss,
            "blueprint": blueprint,
            "spec_ads": spec_ads,
            "generated_at": datetime.now().isoformat()
        }
        
        print(f"\n{'='*60}")
        print(f"CREATIVE DIAGNOSIS COMPLETE: {brand_name}")
        print(f"{'='*60}")
        
        return package
