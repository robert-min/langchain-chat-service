from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from auth.presentation.rest.api import api as auth
from shared.infra.container import AppContainer
from shared.infra.fastapi.errorhandler import error_handlers


def create_app():
    app = FastAPI()

    # dependency
    app.container = AppContainer()

    # Router
    app.include_router(auth)

    # Handler
    error_handlers(app)

    # CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    return app
