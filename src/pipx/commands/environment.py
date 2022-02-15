from pipx.constants import (
    EXIT_CODE_OK,
    LOCAL_BIN_DIR,
    PIPX_HOME,
    PIPX_LOCAL_VENVS,
    PIPX_LOG_DIR,
    PIPX_SHARED_LIBS,
    PIPX_TRASH_DIR,
    PIPX_VENV_CACHEDIR,
    ExitCode,
)
from pipx.util import PipxError


def environment(value: str) -> ExitCode:
    """Print a list of variables used in `pipx.constants`"""
    environment_variables = {
        "PIPX_HOME": PIPX_HOME,
        "PIPX_BIN_DIR": LOCAL_BIN_DIR,
        "PIPX_SHARED_LIBS": PIPX_SHARED_LIBS,
        "PIPX_LOCAL_VENVS": PIPX_LOCAL_VENVS,
        "PIPX_LOG_DIR": PIPX_LOG_DIR,
        "PIPX_TRASH_DIR": PIPX_TRASH_DIR,
        "PIPX_VENV_CACHEDIR": PIPX_VENV_CACHEDIR,
    }
    if value is None:
        for env_variable in environment_variables:
            print(f"{env_variable}={environment_variables[env_variable]}")
        print(
            "\n"
            "Only PIPX_HOME and PIPX_BIN_DIR are settable by users in the above list.\n"
        )
    elif value in environment_variables:
        print(environment_variables[value])
    else:
        raise PipxError("Variable not found.")

    return EXIT_CODE_OK