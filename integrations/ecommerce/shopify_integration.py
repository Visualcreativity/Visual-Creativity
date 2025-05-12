from visual_creativity import Client, GenerationConfig
from shopify import Shopify
from typing import List
import asyncio

class ShopifyProductVisualizer:
    def __init__(self, vc_api_key: str, shopify_api_key: str, shop_url: str):
        self.vc_client = Client(api_key=vc_api_key)
        self.shopify = Shopify(api_key=shopify_api_key, shop_url=shop_url)
    
    async def generate_product_images(self, product_id: str, views: List[str] = ['front', 'side', 'detail']):
        """Generate multiple product images using Visual Creativity AI"""
        product = await self.shopify.get_product(product_id)
        
        generated_images = []
        for view in views:
            config = GenerationConfig(
                subjects=[
                    {
                        "type": "product",
                        "category": product['product_type'],
                        "attributes": product['tags'],
                        "view_angle": view,
                        "lighting": "studio"
                    }
                ],
                background={
                    "type": "studio_white",
                    "shadows": True
                },
                style={
                    "artistic_style": "product_photography",
                    "quality": "commercial"
                },
                output_size=(2048, 2048)
            )
            
            response = await self.vc_client.generate_async(config)
            generated_images.append(response.get_url())
        
        # Update product images in Shopify
        await self.shopify.update_product_images(product_id, generated_images)
        return generated_images

    async def bulk_generate_collection_images(self, collection_id: str):
        """Generate images for all products in a collection"""
        products = await self.shopify.get_collection_products(collection_id)
        
        tasks = [self.generate_product_images(product['id']) for product in products]
        results = await asyncio.gather(*tasks)
        
        return {
            'collection_id': collection_id,
            'processed_products': len(products),
            'generated_images': sum(len(imgs) for imgs in results)
        }

# Usage example
async def main():
    visualizer = ShopifyProductVisualizer(
        vc_api_key='your_visual_creativity_api_key',
        shopify_api_key='your_shopify_api_key',
        shop_url='your-store.myshopify.com'
    )
    
    # Generate images for a single product
    product_images = await visualizer.generate_product_images('product_id_here')
    print(f"Generated {len(product_images)} images for product")
    
    # Generate images for an entire collection
    collection_result = await visualizer.bulk_generate_collection_images('collection_id_here')
    print(f"Processed {collection_result['processed_products']} products")
    print(f"Generated {collection_result['generated_images']} total images")

if __name__ == '__main__':
    asyncio.run(main())