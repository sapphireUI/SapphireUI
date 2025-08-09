import reflex as rx


def background_v8():
    keyframes = {
        # Box breathing + rotation
        "@keyframes boxBreath": {
            "0%": {"transform": "scale(1) rotate(0deg)"},
            "50%": {"transform": "scale(1.05) rotate(1deg)"},
            "100%": {"transform": "scale(1) rotate(0deg)"},
        },
        # Fade in effect
        "@keyframes fadeIn": {
            "0%": {"opacity": "0"},
            "100%": {"opacity": "1"},
        },
    }

    return rx.box(
        rx.heading(
            "SapphireUI",
            size="8",
            weight="bold",
            z_index="10",
        ),
        background_size="100px 100px",
        background_image=(
            "linear-gradient(hsl(0, 0%, 39%) 1px, transparent 1px), "
            "linear-gradient(to right, transparent 99%, hsl(0, 0%, 39%) 100%)"
        ),
        mask="radial-gradient(50% 100% at 50% 50%, hsl(0, 0%, 0%, 1), hsl(0, 0%, 0%, 0))",
        width="100%",
        height="65vh",
        display="flex",
        align_items="center",
        justify_content="center",
        animation="boxBreath 8s ease-in-out infinite, fadeIn 1.5s ease-out",
        **keyframes,
    )
