from visual_creativity import Client, GenerationConfig, Effect, Animation

# Initialize the client
client = Client(api_key="your_api_key")

# Define complex scene with multiple subjects
config = GenerationConfig(
    subjects=[
        {
            "type": "person",
            "clothing": "futuristic_suit",
            "pose": "dynamic",
            "expression": "confident",
            "position": {"x": 0.3, "y": 0.5},
            "effects": [Effect.GLOW, Effect.MOTION_BLUR]
        },
        {
            "type": "robot",
            "design": "sleek_humanoid",
            "action": "interacting",
            "position": {"x": 0.7, "y": 0.5},
            "effects": [Effect.METALLIC_SHEEN]
        }
    ],
    background={
        "scene": "futuristic_city",
        "time": "night",
        "weather": "clear",
        "lighting": {
            "type": "neon",
            "intensity": 0.8,
            "color": "#00ff88"
        }
    },
    style={
        "artistic_style": "cyberpunk",
        "color_palette": "neon_noir",
        "post_processing": ["bloom", "chromatic_aberration"]
    },
    animation=Animation(
        type="subtle_movement",
        duration=5.0,
        fps=30
    ),
    output_size=(3840, 2160)  # 4K resolution
)

# Generate the animated scene
response = client.generate_animated(config)

# Save the generated animation
response.save("futuristic_interaction.mp4")

print("Animated scene generated successfully!")