import reflex as rx


def background_v5():
    keyframes = {
        "@keyframes moveDots": {
            "0%": {
                "background-position": "0 0",
            },
            "100%": {
                "background-position": "100px 100px",
            },
        }
    }
    return rx.center(
        rx.heading("SapphireUI ", size="8", weight="bold", z_index="1"),
        background_image="radial-gradient(circle, #888 1px, transparent 1px)",
        background_size="20px 20px",
        width="100%",
        height="65vh",
        animation="moveDots 20s linear infinite",
        **keyframes,
    )
