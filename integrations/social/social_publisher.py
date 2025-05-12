from visual_creativity import Client, GenerationConfig
from typing import List, Dict
import tweepy
from discord_webhook import DiscordWebhook, DiscordEmbed
import asyncio

class SocialMediaPublisher:
    def __init__(self, vc_api_key: str, twitter_creds: Dict[str, str], discord_webhook_url: str):
        self.vc_client = Client(api_key=vc_api_key)
        
        # Initialize Twitter client
        self.twitter = tweepy.Client(
            consumer_key=twitter_creds['consumer_key'],
            consumer_secret=twitter_creds['consumer_secret'],
            access_token=twitter_creds['access_token'],
            access_token_secret=twitter_creds['access_token_secret']
        )
        
        # Initialize Discord webhook
        self.discord_webhook_url = discord_webhook_url
    
    async def generate_viral_content(self, prompt: str) -> Dict[str, str]:
        """Generate visually appealing content for social media"""
        config = GenerationConfig(
            subjects=[
                {
                    "type": "scene",
                    "description": prompt,
                    "style": "viral_worthy",
                    "composition": "social_media_optimized"
                }
            ],
            style={
                "artistic_style": "trending",
                "color_palette": "vibrant",
                "quality": "premium"
            },
            output_size=(1200, 1200)  # Square format for social media
        )
        
        response = await self.vc_client.generate_async(config)
        return {
            'image_url': response.get_url(),
            'prompt': prompt
        }
    
    async def publish_to_twitter(self, content: Dict[str, str]) -> str:
        """Publish generated content to Twitter/X"""
        tweet = await self.twitter.create_tweet(
            text=f"🎨 AI-generated art: {content['prompt']}\n#VisualCreativity #AIArt",
            media_ids=[content['image_url']]
        )
        return tweet.data['id']
    
    async def publish_to_discord(self, content: Dict[str, str]) -> bool:
        """Share generated content on Discord"""
        webhook = DiscordWebhook(url=self.discord_webhook_url)
        
        embed = DiscordEmbed(
            title="New AI-Generated Artwork",
            description=content['prompt'],
            color=0x00ff00
        )
        embed.set_image(url=content['image_url'])
        embed.set_footer(text="Created with Visual Creativity AI")
        
        webhook.add_embed(embed)
        response = webhook.execute()
        return response.status_code == 200
    
    async def viral_campaign(self, prompts: List[str], interval_hours: int = 4):
        """Run a viral social media campaign with multiple posts"""
        for prompt in prompts:
            try:
                # Generate and publish content
                content = await self.generate_viral_content(prompt)
                
                # Publish to all platforms
                tweet_id = await self.publish_to_twitter(content)
                discord_success = await self.publish_to_discord(content)
                
                print(f"Published content:\nTwitter ID: {tweet_id}\nDiscord: {'Success' if discord_success else 'Failed'}")
                
                # Wait for specified interval
                if prompt != prompts[-1]:  # Don't wait after last prompt
                    await asyncio.sleep(interval_hours * 3600)
                    
            except Exception as e:
                print(f"Error processing prompt '{prompt}': {str(e)}")

# Usage example
async def main():
    publisher = SocialMediaPublisher(
        vc_api_key='your_visual_creativity_api_key',
        twitter_creds={
            'consumer_key': 'your_twitter_consumer_key',
            'consumer_secret': 'your_twitter_consumer_secret',
            'access_token': 'your_twitter_access_token',
            'access_token_secret': 'your_twitter_access_token_secret'
        },
        discord_webhook_url='your_discord_webhook_url'
    )
    
    campaign_prompts = [
        "Futuristic city with floating gardens and bio-luminescent architecture",
        "Ancient wisdom meets modern technology - a meditation room with holographic mandalas",
        "Sustainable fashion showcase in a crystal dome under northern lights"
    ]
    
    await publisher.viral_campaign(campaign_prompts, interval_hours=4)

if __name__ == '__main__':
    asyncio.run(main())