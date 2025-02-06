import logging
import os

import azure.functions as func
import requests

app = func.FunctionApp()


def get_service_url():
    return os.environ.get('SERVICE_URL')


@app.route(route="call_echo_server", auth_level=func.AuthLevel.ANONYMOUS)
def call_echo_server(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Get the url of the service where we have to send the content of the user request
    logging.debug("Accessing env variable for service URL")
    service_url = get_service_url()
    if service_url is None:
        return func.HttpResponse("Service URL not set in the env", status_code=500)

    # Get the content from the user's request
    content = req.params.get('content')
    if not content:
        return func.HttpResponse("Missing param 'content' in the input", status_code=400)

    # Request the echo service
    response = requests.get(service_url, params={'content': content})

    return func.HttpResponse(
        "Successfully transmitted content. Output of the service: " + response.content.decode(),
        status_code=200
    )
