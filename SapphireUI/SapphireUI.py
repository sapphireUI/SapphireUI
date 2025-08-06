import reflex as rx

from SapphireUI.export import export_app

app = rx.App(
    stylesheets=["css/globals.css"],
    # head_components=[
    #     rx.script(
    #         src="https://gc.zgo.at/count.js",
    #         custom_attrs={
    #             "data-goatcounter": "https://.goatcounter.com/count",
    #         },
    #     )
    # ],
)
export_app(app)
