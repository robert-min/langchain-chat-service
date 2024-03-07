from fastapi import APIRouter, Depends
from dependency_injector.wiring import Provide, inject
from auth.domain.entity import Auth, Token
from auth.application.command import AuthCommandUseCase
from auth.presentation.rest.response import SignUpResponse, LogInResponse
from auth.presentation.rest.request import SignUpUserRequest, LogInUserRequest
from shared.infra.container import AppContainer

api = APIRouter(prefix="/auth")


@api.post("/signup")
@inject
async def auth_sign_up(
    request: SignUpUserRequest,
    auth_command: AuthCommandUseCase = Depends(
      Provide[AppContainer.auth.auth_command]
    ),
):
    entity: Auth = Auth.new(request.email, request.password)
    auth_info: Auth = auth_command.sign_up_user(entity)
    return SignUpResponse(auth_info=auth_info).build()


@api.post("/login")
@inject
async def auth_log_in(
    request: LogInUserRequest,
    auth_command: AuthCommandUseCase = Depends(
       Provide[AppContainer.auth.auth_command]
    ),
):
    entity: Auth = Auth.new(request.email, request.password)
    token_info: Token = auth_command.log_in_user(entity)
    return LogInResponse(token_info=token_info).build()
