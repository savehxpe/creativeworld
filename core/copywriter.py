"""
Outreach Copywriter — Creative Director Branch.
Generates premium outreach messages for high-ticket creative direction.
"""
import os
from config.settings import OUTREACH_DIR
from config.niches import get_niche_config


class OutreachCopywriter:
    """
    Generates outreach messages for the creative director positioning.
    No prices. No packages. Just creative direction and spec ad previews.
    """
    
    def __init__(self):
        os.makedirs(OUTREACH_DIR, exist_ok=True)
    
    def generate_instagram_dm(self, brand_name, niche_key, observation, spec_ad_campaign_name):
        """
        Generate an Instagram DM for creative direction outreach.
        """
        niche_config = get_niche_config(niche_key)
        
        message = f"""Hey {brand_name}, I'm Tshepo from Outworld Creative.

I came across your brand and saw a clear creative opportunity with how your content could drive more {niche_config['examples'][0] if niche_config['examples'] else 'engagement'}.

{observation}

Not selling a random template — I put together a quick creative direction preview showing how a {niche_key.replace('_', ' ')} in your space could look with stronger campaign thinking.

Mind if I send it through?

Tshepo
Creative Director, Outworld Creative"""
        
        return message.strip()
    
    def generate_linkedin_message(self, brand_name, niche_key, competitor_observation):
        """
        Generate a LinkedIn connection message for creative direction outreach.
        """
        niche_config = get_niche_config(niche_key)
        
        message = f"""{brand_name}, I've been analyzing creative direction in the SA {niche_key.replace('_', ' ')} space and your brand caught my attention.

{competitor_observation}

I put together a creative direction concept for a brand in your space showing how to bridge that gap. It's not a pitch — it's a strategic preview of what stronger creative direction looks like.

Worth a look?"""
        
        return message.strip()
    
    def generate_cold_email(self, brand_name, niche_key, specific_gap, revenue_loss_example):
        """
        Generate a cold email for creative direction outreach.
        """
        niche_config = get_niche_config(niche_key)
        niche_name = niche_config['name']
        
        subject_options = [
            f"A creative gap I noticed with {brand_name}",
            f"The {niche_name.lower()} opportunity most brands miss",
            f"Your brand vs. your content — a quick thought"
        ]
        
        subject = subject_options[0]
        
        email = f"""Subject: {subject}

{brand_name},

I've spent the last week analyzing how {niche_name.lower()}s in Johannesburg turn Instagram attention into actual {niche_config['examples'][0] if niche_config['examples'] else 'results'}.

Most are losing 30-40% of potential revenue to a simple friction: {specific_gap}

{revenue_loss_example}

I created a creative direction concept showing how a {niche_name.lower()} in your space could close that gap. It's not a template. It's a strategic preview of what your brand could look like with an external creative department focused on one thing: turning scrolls into {niche_config['examples'][0] if niche_config['examples'] else 'results'}.

Worth a 15-minute conversation?

Tshepo Motolo
Creative Director, Outworld Creative
team@outworldcreative.com
outworldcreative.com"""
        
        return subject, email.strip()
    
    def generate_spec_ad_send_message(self, brand_name, campaign_name, niche_key, key_insight):
        """
        Generate the follow-up message after they say yes to seeing the spec ad.
        """
        message = f"""Here it is — "{campaign_name}"

[Attach image or send link]

Campaign concept for a {niche_key.replace('_', ' ')} in your space. The goal: {key_insight}

The gap I see: most {niche_key.replace('_', ' ')}s post {self._get_typical_post_type(niche_key)}. The ones that win post the feeling that drives action.

This is what that looks like in creative direction.

Happy to talk through how this could apply to {brand_name} specifically.

Tshepo"""
        
        return message.strip()
    
    def generate_follow_up_day3(self, brand_name, channel="dm"):
        """Generate day 3 follow-up."""
        if channel == "dm":
            return f"""Hey {brand_name}, quick follow-up on the creative direction concept I mentioned.

No pressure at all — just wanted to make sure it didn't get lost in the DMs.

If you're open to seeing how your brand could look with stronger campaign creative, I'm happy to send it over.

Tshepo""".strip()
        else:
            return f"""Subject: Re: Creative direction for {brand_name}

{brand_name},

Quick follow-up on my email from a few days ago.

I know inboxes are crowded. If the creative direction angle isn't a priority right now, I completely understand.

If it is, I'm happy to send over the spec concept I created for your space — no call needed, just value.

Tshepo Motolo
Outworld Creative""".strip()
    
    def generate_follow_up_day7(self, brand_name, channel="dm"):
        """Generate day 7 follow-up."""
        if channel == "dm":
            return f"""Hey {brand_name}, last follow-up from me.

I know DMs get crowded. If creative direction isn't on your radar right now, totally get it.

If it ever becomes relevant, my door's open. Good luck with the weekend rush.

Tshepo
Outworld Creative""".strip()
        else:
            return f"""Subject: Last follow-up: {brand_name} creative direction

{brand_name},

Last follow-up from me. I don't want to crowd your inbox.

If creative direction becomes relevant for {brand_name} down the line, feel free to reach out.

Best of luck with the upcoming season.

Tshepo Motolo
Outworld Creative""".strip()
    
    def save_outreach_package(self, brand_name, niche_key, messages):
        """
        Save a complete outreach package to a file.
        """
        filename = f"{brand_name.lower().replace(' ', '_')}_outreach.txt"
        filepath = os.path.join(OUTREACH_DIR, filename)
        
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(f"Outreach Package for {brand_name}\n")
            f.write(f"Niche: {niche_key}\n")
            f.write("=" * 50 + "\n\n")
            
            for msg_type, content in messages.items():
                f.write(f"--- {msg_type.upper()} ---\n")
                f.write(content + "\n\n")
        
        print(f"  [Outreach] Saved package: {filepath}")
        return filepath
    
    def _get_typical_post_type(self, niche_key):
        """Get the typical post type for a niche (for contrast in messaging)."""
        typical = {
            "restaurant": "food",
            "fashion": "product",
            "hospitality": "rooms",
            "beauty": "treatments",
            "events": "venue photos",
            "musician": "performance clips",
            "clothing_brand": "flat lays"
        }
        return typical.get(niche_key, "content")
    
    def generate_proposal_email(self, brand_name, proposal_summary, next_steps):
        """
        Generate the proposal delivery email.
        """
        email = f"""Subject: Your Creative Direction Proposal — {brand_name}

{brand_name},

As promised, here's your custom creative direction proposal based on our conversation.

{proposal_summary}

Next Steps:
{next_steps}

This proposal is scoped specifically for {brand_name} and your current goals. If anything needs adjustment or if you have questions, let's jump on a quick call.

No pressure. Just clarity.

Tshepo Motolo
Creative Director, Outworld Creative
team@outworldcreative.com
outworldcreative.com"""
        
        return email.strip()
    
    def generate_thank_you_email(self, brand_name):
        """
        Generate post-call thank you email.
        """
        email = f"""Subject: Great speaking, {brand_name}

{brand_name},

Thanks for the time today. I enjoyed learning about your brand and seeing the potential in what you're building.

As promised, I'll have your custom creative direction proposal to you within 48 hours.

In the meantime, feel free to send over any campaign dates, launch timelines, or specific goals you want me to factor in.

Tshepo Motolo
Creative Director, Outworld Creative
team@outworldcreative.com"""
        
        return email.strip()
