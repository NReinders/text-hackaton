from dataclasses import dataclass
from pathlib import Path
from tomllib import load
from typing import Self

from loguru import logger

__all__ = (
    "UnknownTableError",
    "MLflowConfig",
)


class UnknownTableError(Exception):
    """Unknown table in TOML file."""


def _load_toml(toml_path: str | Path) -> dict:
    if isinstance(toml_path, str):
        toml_path = Path(toml_path)
    else:
        raise TypeError(
            f"Parameter `toml_path` should be `{str}` or `{Path}`, "
            f"not `{type(toml_path)}`!"
        )
    with toml_path.open(mode="rb") as toml_handle:
        toml_raw = load(toml_handle)
    return toml_raw


@dataclass(frozen=True)
class MLflowConfig:
    """Confuguration for MLflow"""

    tracking_uri: str

    @classmethod
    def from_toml(cls, config_path: str | Path, table="mlflow") -> Self:
        """Load MLflow configuration from a TOML file."""
        config_raw = _load_toml(config_path)
        try:
            return cls(**config_raw[table])
        except KeyError as e:
            logger.exception(
                "Cannot find table `{table}` in config file `{config_path}`!",
                table=table,
                config_path=config_path,
            )
            raise UnknownTableError(f"Unknown table `{table}`!") from e
