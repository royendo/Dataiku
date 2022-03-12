def construct_app(app):
    import time
    import dash_html_components as html
    from dash.long_callback import DiskcacheLongCallbackManager
    import diskcache
    from dash.dependencies import Input, Output

    cache = diskcache.Cache("./cache")
    long_callback_manager = DiskcacheLongCallbackManager(cache)

    app._long_callback_manager = long_callback_manager

    # DEFINE APP LAYOUT
    app.layout = html.Div(
        [
            html.Div(
                [
                    html.P(id="paragraph_id", children=["Button not clicked"]),
                    html.Progress(id="progress_bar"),
                ]
            ),
            html.Button(id="button_id", children="Run Job!"),
            html.Button(id="cancel_button_id", children="Cancel Running Job!"),
        ]
    )

    @app.long_callback(
        output=Output("paragraph_id", "children"),
        inputs=Input("button_id", "n_clicks"),
        running=[
            (Output("button_id", "disabled"), True, False),
            (Output("cancel_button_id", "disabled"), False, True),
            (
                Output("paragraph_id", "style"),
                {"visibility": "hidden"},
                {"visibility": "visible"},
            ),
            (
                Output("progress_bar", "style"),
                {"visibility": "visible"},
                {"visibility": "hidden"},
            ),
        ],
        cancel=[Input("cancel_button_id", "n_clicks")],
        progress=[Output("progress_bar", "value"), Output("progress_bar", "max")],
    )
    def callback(set_progress, n_clicks):
        total = 10
        for i in range(total):
            time.sleep(0.5)
            set_progress((str(i + 1), str(total)))
        return [f"Clicked {n_clicks} times"]