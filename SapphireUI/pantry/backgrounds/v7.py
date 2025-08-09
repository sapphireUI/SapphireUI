import reflex as rx


def background_v7():
    keyframes = {
        # Grid movement
        "@keyframes moveGrid": {
            "0%": {"background-position": "0 0, 0 0"},
            "100%": {"background-position": "100px 100px, 100px 100px"},
        },
        # Shine sweep over text
        "@keyframes shine": {
            "0%": {"background-position": "-200% center"},
            "100%": {"background-position": "200% center"},
        },
        # Fade-in hero
        "@keyframes fadeIn": {
            "0%": {"opacity": "0"},
            "100%": {"opacity": "1"},
        },
    }

    return rx.center(
        rx.heading(
            "SapphireUI",
            size="8",
            weight="bold",
            z_index="10",
            background_image="linear-gradient(90deg, #fff, #8ab4f8, #fff)",
            background_clip="text",
            color="transparent",
            background_size="200% auto",
            animation="shine 3s linear infinite",
        ),
        background_size="100px 100px",
        background_image=(
            "linear-gradient(hsl(0, 0%, 39%) 1px, transparent 1px), "
            "linear-gradient(to right, transparent 99%, hsl(0, 0%, 39%) 100%)"
        ),
        mask="radial-gradient(50% 100% at 50% 50%, hsl(0, 0%, 0%, 1), hsl(0, 0%, 0%, 0))",
        width="100%",
        height="65vh",
        animation="moveGrid 20s linear infinite, fadeIn 1.5s ease-out",
        **keyframes,
    )
