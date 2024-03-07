from dependency_injector import containers, providers
from auth.infra.container import AuthContainer


class AppContainer(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(
        modules=[
            "auth.presentation.rest.api"
        ]
    )
    auth = providers.Container(AuthContainer)
