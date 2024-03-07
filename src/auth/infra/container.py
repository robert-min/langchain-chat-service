from dependency_injector import containers, providers
from auth.infra.database.repository import AuthRepository
from auth.domain.service.sign_up import SignUpService
from auth.application.query import AuthQueryUseCase
from auth.application.command import AuthCommandUseCase
from shared.infra.database.connection import get_postgre_session


class AuthContainer(containers.DeclarativeContainer):
    auth_repo = providers.Factory(AuthRepository)
    sign_up_service = providers.Factory(SignUpService)

    auth_query = providers.Factory(
        AuthQueryUseCase,
        auth_repository=auth_repo,
        session=get_postgre_session
    )

    auth_command = providers.Factory(
        AuthCommandUseCase,
        auth_repository=auth_repo,
        sign_up_service=sign_up_service,
        auth_query=auth_query,
        session=get_postgre_session
    )
