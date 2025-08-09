import reflex as rx


def background_v9():
    keyframes = {
        # Background parallax animation
        "@keyframes moveDots": {
            "0%": {
                "background-position": "0 0, 0 0",
            },
            "100%": {
                "background-position": "80px 80px, 40px 40px",
            },
        },
        # Text shine sweep
        "@keyframes shine": {
            "0%": {
                "background-position": "-200% center",
            },
            "100%": {
                "background-position": "200% center",
            },
        },
        # Fade-in for the whole hero section
        "@keyframes fadeIn": {
            "0%": {
                "opacity": "0",
            },
            "100%": {
                "opacity": "1",
            },
        },
    }

    return rx.box(
        # Animated moving dots
        rx.box(
            background_size="20px 20px",
            background_image=(
                "radial-gradient(circle, hsl(0, 0%, 39%) 1px, transparent 1px), "
                "radial-gradient(circle, hsl(0, 0%, 45%) 1px, transparent 1px)"
            ),
            mask="linear-gradient(to bottom, hsl(0, 0%, 0%, 0.5), hsl(0, 0%, 0%, 0))",
            width="100%",
            height="65vh",
            animation="moveDots 30s linear infinite",  # Slow movement for elegance
        ),
        # Centered heading with shine effect
        rx.center(
            rx.heading(
                "SapphireUI",
                size="7",
                weight="bold",
                z_index="20",
                background_image="linear-gradient(90deg, #fff, #8ab4f8, #fff)",
                background_clip="text",
                color="transparent",
                background_size="200% auto",
                animation="shine 3s linear infinite",
            ),
            position="absolute",
            top="50%",
            left="50%",
            transform="translate(-50%, -50%)",
        ),
        width="100%",
        height="65vh",
        position="relative",
        animation="fadeIn 1.5s ease-out",
        **keyframes,
    )
