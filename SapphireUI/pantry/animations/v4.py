import reflex as rx


def animation_v4() -> rx.Component:
    return rx.vstack(
        rx.heading(
            "buridan/ui",
            size="6",
            font_weight="900",
            color="#0ff",
            style={
                "fontFamily": "monospace",
                "letterSpacing": "0.1em",
                "animation": "neonFlicker 3s infinite",
                "@keyframes neonFlicker": {
                    "0%, 19%, 21%, 23%, 25%, 54%, 56%, 100%": {
                        "text-shadow": (
                            "0 0 5px #0ff,"
                            "0 0 10px #0ff,"
                            "0 0 20px #0ff,"
                            "0 0 40px #0ff"
                        ),
                        "opacity": "1",
                    },
                    "20%, 24%, 55%": {
                        "text-shadow": "none",
                        "opacity": "0.3",
                    },
                },
            },
        ),
        width="100%",
        height="20em",
        bg="#000",
        align="center",
        justify="center",
    )
