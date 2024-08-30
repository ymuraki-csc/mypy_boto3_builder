"""
Version manager for PyPI packages.
"""

import requests

from mypy_boto3_builder.constants import REQUEST_TIMEOUT
from mypy_boto3_builder.utils.version import bump_postrelease, get_release_version


class PyPIManager:
    """
    Version manager for PyPI packages.

    Arguments:
        package -- PyPI package name
    """

    JSON_URL = "https://pypi.org/pypi/{package}/json"

    def __init__(self, package: str) -> None:
        self.package = package
        self._versions: set[str] | None = None

    @property
    def json_url(self) -> str:
        """
        Package JSON URL on PyPI.
        """
        return self.JSON_URL.format(package=self.package)

    def has_version(self, version: str) -> bool:
        """
        Check if version is already uploaded to PyPI.

        Arguments:
            version -- Target version
        """
        return version in self._get_versions()

    def get_next_version(self, version: str) -> str:
        """
        Get not existing version or closest not existing post-release.

        Arguments:
            version -- Target version
        """
        versions = self._get_versions()
        new_version = version
        while new_version in versions:
            new_version = bump_postrelease(new_version)
        return new_version

    def _get_versions(self) -> set[str]:
        if self._versions is not None:
            return self._versions

        response = requests.get(self.json_url, timeout=REQUEST_TIMEOUT)
        if response.status_code == 404:
            return set()
        if not response.ok:
            raise RuntimeError(
                f"Cannot retrieve {self.json_url}: {response.status_code} {response.text}"
            ) from None

        data = response.json()

        if "releases" not in data:
            return set()

        version_strs = set(data["releases"].keys())
        self._versions = {get_release_version(i) for i in version_strs}
        return self._versions
