from flask import request
@app.callback(
    Output(component_id='my-output', component_property='children'),
    [Input(component_id='my-input', component_property='value')]
)
def update_output_div(input_value):
    request_headers = dict(request.headers)
    auth_info_brower = dataiku.api_client().get_auth_info_from_browser_headers(request_headers)
    return auth_info_brower["authIdentifier"]