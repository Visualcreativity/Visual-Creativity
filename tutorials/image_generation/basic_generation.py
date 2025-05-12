from visual_creativity import Client, GenerationConfig

# Initialize the client
client = Client(api_key="your_api_key")

# Define generation configuration
config = GenerationConfig(
    subjects=[
        {
            "type": "person",
            "clothing": "bohemian_dress",
            "pose": "standing",
            "expression": "happy"
        }
    ],
    background={
        "scene": "sunset_beach",
        "lighting": "golden_hour",
        "atmosphere": "warm"
    },
    style={
        "artistic_style": "realistic",
        "color_palette": "warm_tones"
    },
    output_size=(3840, 2160)  # 4K resolution
)

# Generate the image
response = client.generate(config)

# Save the generated image
response.save("generated_beach_portrait.png")

print("Image generated successfully!")