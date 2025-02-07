import azure.functions as func

from server import app

func_app = func.WsgiFunctionApp(app=app, http_auth_level=func.AuthLevel.ANONYMOUS)
