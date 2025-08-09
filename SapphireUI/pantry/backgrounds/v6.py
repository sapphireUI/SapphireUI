import reflex as rx


def background_v6():
    # Define keyframes for background movement and heading fade-slide
    keyframes = {
        # Background movement keyframes
        "@keyframes moveDots": {
            "0%": {
                # Start position for the dot grid
                "background-position": "0 0, 0 0",
            },
            "100%": {
                # End position (diagonal shift) to create motion
                "background-position": "100px 100px, 50px 50px",
            },
        },
        # Light glow animation for heading
        "@keyframes lightGlow": {
            "0%": {
                "text-shadow": "0 0 5px rgba(255,255,255,0.3)",
            },
            "50%": {
                "text-shadow": "0 0 20px rgba(255,255,255,0.8)",
            },
            "100%": {
                "text-shadow": "0 0 5px rgba(255,255,255,0.3)",
            },
        },
    }

    return rx.box(
        # Moving background layer
        rx.box(
            background_size="20px 20px",  # Size of the repeated dot pattern
            background_image=(
                "radial-gradient(circle, hsl(0, 0%, 39%) 1px, transparent 1px), "
                "radial-gradient(circle, hsl(0, 0%, 45%) 1px, transparent 1px)"
            ),  # Two layered dot gradients for depth
            mask="linear-gradient(to bottom, hsl(0, 0%, 0%, 0.5), hsl(0, 0%, 0%, 0))",  # Soft fade effect at bottom
            width="100%",  # Full width
            height="65vh",  # 65% of viewport height
            animation="moveDots 25s linear infinite",  # Smooth infinite motion
        ),
        # Centered heading with glow animation
        rx.center(
            rx.heading(
                "SapphireUI",
                size="7",
                weight="bold",
                z_index="20",  # Stay above the background
                animation="lightGlow 3s ease-in-out infinite",  # Glow loop
            ),
            position="absolute",  # Absolute so it stays over background
            top="50%",  # Vertically center
            left="50%",  # Horizontally center
            transform="translate(-50%, -50%)",  # Perfect centering
        ),
        width="100%",  # Outer container full width
        height="65vh",  # Outer container height
        position="relative",  # So inner absolute elements are positioned relative to this
        **keyframes,  # Inject keyframes into component
    )
