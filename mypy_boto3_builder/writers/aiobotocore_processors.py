"""
Processors for parsing and writing `aiobotocore` modules.
"""

from collections.abc import Iterable
from pathlib import Path

from boto3.session import Session

from mypy_boto3_builder.constants import TEMPLATES_PATH
from mypy_boto3_builder.logger import get_logger
from mypy_boto3_builder.package_data import (
    BasePackageData,
    TypesAioBotocoreLitePackageData,
    TypesAioBotocorePackageData,
)
from mypy_boto3_builder.parsers.parse_wrapper_package import parse_aiobotocore_stubs_package
from mypy_boto3_builder.service_name import ServiceName
from mypy_boto3_builder.structures.types_aiobotocore_package import TypesAioBotocorePackage
from mypy_boto3_builder.utils.path import print_path
from mypy_boto3_builder.writers.package_writer import PackageWriter


def process_aiobotocore_stubs(
    session: Session,
    output_path: Path,
    service_names: Iterable[ServiceName],
    generate_setup: bool,
    version: str,
    static_files_path: Path,
) -> TypesAioBotocorePackage:
    """
    Parse and write stubs package `aiobotocore-stubs`.

    Arguments:
        session -- boto3 session
        output_path -- Package output path
        service_names -- List of known service names
        generate_setup -- Generate ready-to-install or to-use package
        version -- Package version
        static_files_path -- Path to static files

    Return:
        Parsed TypesAioBotocorePackage.
    """
    logger = get_logger()
    types_aiobotocore_package = parse_aiobotocore_stubs_package(
        session, service_names, TypesAioBotocorePackageData
    )
    types_aiobotocore_package.version = version
    logger.debug(f"Writing {types_aiobotocore_package.pypi_name} to {print_path(output_path)}")

    package_writer = PackageWriter(
        output_path=output_path, generate_setup=generate_setup, cleanup=True
    )
    package_writer.write_package(
        types_aiobotocore_package,
        templates_path=TEMPLATES_PATH / "aiobotocore-stubs",
        static_files_path=static_files_path,
    )
    return types_aiobotocore_package


def process_aiobotocore_stubs_lite(
    session: Session,
    output_path: Path,
    service_names: Iterable[ServiceName],
    generate_setup: bool,
    version: str,
    static_files_path: Path,
) -> TypesAioBotocorePackage:
    """
    Parse and write stubs package `aiobotocore-stubs-lite`.

    Arguments:
        session -- boto3 session
        output_path -- Package output path
        service_names -- List of known service names
        generate_setup -- Generate ready-to-install or to-use package
        version -- Package version
        static_files_path -- Path to static files

    Return:
        Parsed TypesAioBotocorePackage.
    """
    logger = get_logger()
    types_aiobotocore_package = parse_aiobotocore_stubs_package(
        session, service_names, TypesAioBotocoreLitePackageData
    )
    types_aiobotocore_package.version = version
    logger.debug(f"Writing {types_aiobotocore_package.pypi_name} to {print_path(output_path)}")

    package_writer = PackageWriter(
        output_path=output_path,
        generate_setup=generate_setup,
        cleanup=True,
    )
    package_writer.write_package(
        types_aiobotocore_package,
        templates_path=TEMPLATES_PATH / "aiobotocore-stubs",
        static_files_path=static_files_path,
        exclude_template_names=["session.pyi.jinja2"],
    )
    return types_aiobotocore_package


def process_aiobotocore_stubs_docs(
    session: Session,
    output_path: Path,
    service_names: Iterable[ServiceName],
) -> TypesAioBotocorePackage:
    """
    Parse and write master package docs.

    Arguments:
        session -- boto3 session
        output_path -- Package output path
        service_names -- List of known service names

    Return:
        Parsed TypesAioBotocorePackage.
    """
    logger = get_logger()
    types_aiobotocore_package = parse_aiobotocore_stubs_package(
        session, service_names, TypesAioBotocorePackageData
    )

    logger.debug(f"Writing {types_aiobotocore_package.pypi_name} to {print_path(output_path)}")

    package_writer = PackageWriter(output_path=output_path, generate_setup=False, cleanup=True)
    package_writer.write_docs(
        types_aiobotocore_package,
        templates_path=TEMPLATES_PATH / "aiobotocore_stubs_docs",
    )

    return types_aiobotocore_package


def process_aiobotocore_stubs_full(
    session: Session,
    output_path: Path,
    service_names: Iterable[ServiceName],
    generate_setup: bool,
    version: str,
    package_data: type[BasePackageData],
    static_files_path: Path,
) -> TypesAioBotocorePackage:
    """
    Parse and write stubs package `types-aiobotocore-full`.

    Arguments:
        session -- boto3 session
        output_path -- Package output path
        service_names -- List of known service names
        generate_setup -- Generate ready-to-install or to-use package
        version -- Package version
        package_data -- Package data
        static_files_path -- Path to static files

    Return:
        Parsed TypesAioBotocorePackage.
    """
    logger = get_logger()
    logger.debug(f"Parsing {package_data.PYPI_NAME}")
    types_aiobotocore_package = parse_aiobotocore_stubs_package(
        session=session,
        service_names=service_names,
        package_data=package_data,
    )
    types_aiobotocore_package.version = version
    logger.debug(f"Writing {package_data.PYPI_NAME} to {print_path(output_path)}")

    package_writer = PackageWriter(
        output_path=output_path, generate_setup=generate_setup, cleanup=True
    )
    package_writer.write_package(
        types_aiobotocore_package,
        templates_path=TEMPLATES_PATH / "types-aiobotocore-full",
        static_files_path=static_files_path,
    )

    return types_aiobotocore_package
