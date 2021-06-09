from typing import Any, Dict

import requests
import urllib3

class BotoCoreError(Exception):
    fmt: str
    def __init__(self, **kwargs: Any) -> None: ...

class DataNotFoundError(BotoCoreError): ...
class UnknownServiceError(DataNotFoundError): ...
class ApiVersionNotFoundError(BotoCoreError): ...

class HTTPClientError(BotoCoreError):
    def __init__(self, request: Any = ..., response: Any = ..., **kwargs: Any) -> None: ...

class ConnectionError(BotoCoreError): ...
class InvalidIMDSEndpointError(BotoCoreError): ...
class EndpointConnectionError(ConnectionError): ...
class SSLError(ConnectionError, requests.exceptions.SSLError): ...
class ConnectionClosedError(HTTPClientError): ...
class ReadTimeoutError(
    HTTPClientError, requests.exceptions.ReadTimeout, urllib3.exceptions.ReadTimeoutError
): ...
class ConnectTimeoutError(ConnectionError, requests.exceptions.ConnectTimeout): ...
class ProxyConnectionError(ConnectionError, requests.exceptions.ProxyError): ...
class NoCredentialsError(BotoCoreError): ...
class PartialCredentialsError(BotoCoreError): ...
class CredentialRetrievalError(BotoCoreError): ...
class UnknownSignatureVersionError(BotoCoreError): ...
class ServiceNotInRegionError(BotoCoreError): ...
class BaseEndpointResolverError(BotoCoreError): ...
class NoRegionError(BaseEndpointResolverError): ...
class UnknownEndpointError(BaseEndpointResolverError, ValueError): ...
class UnknownFIPSEndpointError(BaseEndpointResolverError): ...
class ProfileNotFound(BotoCoreError): ...
class ConfigParseError(BotoCoreError): ...
class ConfigNotFound(BotoCoreError): ...
class MissingParametersError(BotoCoreError): ...
class ValidationError(BotoCoreError): ...
class ParamValidationError(BotoCoreError): ...
class UnknownKeyError(ValidationError): ...
class RangeError(ValidationError): ...
class UnknownParameterError(ValidationError): ...
class InvalidRegionError(ValidationError, ValueError): ...
class AliasConflictParameterError(ValidationError): ...
class UnknownServiceStyle(BotoCoreError): ...
class PaginationError(BotoCoreError): ...
class OperationNotPageableError(BotoCoreError): ...
class ChecksumError(BotoCoreError): ...
class UnseekableStreamError(BotoCoreError): ...

class WaiterError(BotoCoreError):
    def __init__(self, name: str, reason: Any, last_response: Dict[str, Any]) -> None: ...

class IncompleteReadError(BotoCoreError): ...
class InvalidExpressionError(BotoCoreError): ...
class UnknownCredentialError(BotoCoreError): ...
class WaiterConfigError(BotoCoreError): ...
class UnknownClientMethodError(BotoCoreError): ...
class UnsupportedSignatureVersionError(BotoCoreError): ...

class ClientError(Exception):
    MSG_TEMPLATE: str
    def __init__(self, error_response: Dict[str, Any], operation_name: str) -> None: ...

class EventStreamError(ClientError): ...
class UnsupportedTLSVersionWarning(Warning): ...
class ImminentRemovalWarning(Warning): ...
class InvalidDNSNameError(BotoCoreError): ...
class InvalidS3AddressingStyleError(BotoCoreError): ...
class UnsupportedS3ArnError(BotoCoreError): ...
class UnsupportedS3ControlArnError(BotoCoreError): ...
class InvalidHostLabelError(BotoCoreError): ...
class UnsupportedOutpostResourceError(BotoCoreError): ...
class UnsupportedS3ConfigurationError(BotoCoreError): ...
class UnsupportedS3AccesspointConfigurationError(BotoCoreError): ...
class InvalidEndpointDiscoveryConfigurationError(BotoCoreError): ...
class UnsupportedS3ControlConfigurationError(BotoCoreError): ...
class InvalidRetryConfigurationError(BotoCoreError): ...
class InvalidMaxRetryAttemptsError(InvalidRetryConfigurationError): ...
class InvalidRetryModeError(InvalidRetryConfigurationError): ...
class InvalidS3UsEast1RegionalEndpointConfigError(BotoCoreError): ...
class InvalidSTSRegionalEndpointsConfigError(BotoCoreError): ...
class StubResponseError(BotoCoreError): ...
class StubAssertionError(StubResponseError, AssertionError): ...
class UnStubbedResponseError(StubResponseError): ...
class InvalidConfigError(BotoCoreError): ...
class InfiniteLoopConfigError(InvalidConfigError): ...
class RefreshWithMFAUnsupportedError(BotoCoreError): ...
class MD5UnavailableError(BotoCoreError): ...
class MetadataRetrievalError(BotoCoreError): ...
class UndefinedModelAttributeError(Exception): ...
class MissingServiceIdError(UndefinedModelAttributeError): ...
class SSOError(BotoCoreError): ...
class SSOTokenLoadError(SSOError): ...
class UnauthorizedSSOTokenError(SSOError): ...
class CapacityNotAvailableError(BotoCoreError): ...
class InvalidProxiesConfigError(BotoCoreError): ...
