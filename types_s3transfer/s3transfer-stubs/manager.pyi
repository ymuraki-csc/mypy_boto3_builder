from _typeshed import Incomplete
from s3transfer.bandwidth import BandwidthLimiter as BandwidthLimiter, LeakyBucket as LeakyBucket
from s3transfer.constants import ALLOWED_DOWNLOAD_ARGS as ALLOWED_DOWNLOAD_ARGS, KB as KB, MB as MB
from s3transfer.copies import CopySubmissionTask as CopySubmissionTask
from s3transfer.delete import DeleteSubmissionTask as DeleteSubmissionTask
from s3transfer.download import DownloadSubmissionTask as DownloadSubmissionTask
from s3transfer.exceptions import CancelledError as CancelledError, FatalError as FatalError
from s3transfer.futures import BoundedExecutor as BoundedExecutor, IN_MEMORY_DOWNLOAD_TAG as IN_MEMORY_DOWNLOAD_TAG, IN_MEMORY_UPLOAD_TAG as IN_MEMORY_UPLOAD_TAG, TransferCoordinator as TransferCoordinator, TransferFuture as TransferFuture, TransferMeta as TransferMeta
from s3transfer.upload import UploadSubmissionTask as UploadSubmissionTask
from s3transfer.utils import CallArgs as CallArgs, OSUtils as OSUtils, SlidingWindowSemaphore as SlidingWindowSemaphore, TaskSemaphore as TaskSemaphore, get_callbacks as get_callbacks, signal_not_transferring as signal_not_transferring, signal_transferring as signal_transferring

logger: Incomplete

class TransferConfig:
    multipart_threshold: Incomplete
    multipart_chunksize: Incomplete
    max_request_concurrency: Incomplete
    max_submission_concurrency: Incomplete
    max_request_queue_size: Incomplete
    max_submission_queue_size: Incomplete
    max_io_queue_size: Incomplete
    io_chunksize: Incomplete
    num_download_attempts: Incomplete
    max_in_memory_upload_chunks: Incomplete
    max_in_memory_download_chunks: Incomplete
    max_bandwidth: Incomplete
    def __init__(self, multipart_threshold=..., multipart_chunksize=..., max_request_concurrency: int = ..., max_submission_concurrency: int = ..., max_request_queue_size: int = ..., max_submission_queue_size: int = ..., max_io_queue_size: int = ..., io_chunksize=..., num_download_attempts: int = ..., max_in_memory_upload_chunks: int = ..., max_in_memory_download_chunks: int = ..., max_bandwidth: Incomplete | None = ...) -> None: ...

class TransferManager:
    ALLOWED_DOWNLOAD_ARGS: Incomplete
    ALLOWED_UPLOAD_ARGS: Incomplete
    ALLOWED_COPY_ARGS: Incomplete
    ALLOWED_DELETE_ARGS: Incomplete
    VALIDATE_SUPPORTED_BUCKET_VALUES: bool
    def __init__(self, client, config: Incomplete | None = ..., osutil: Incomplete | None = ..., executor_cls: Incomplete | None = ...) -> None: ...
    @property
    def client(self): ...
    @property
    def config(self): ...
    def upload(self, fileobj, bucket, key, extra_args: Incomplete | None = ..., subscribers: Incomplete | None = ...): ...
    def download(self, bucket, key, fileobj, extra_args: Incomplete | None = ..., subscribers: Incomplete | None = ...): ...
    def copy(self, copy_source, bucket, key, extra_args: Incomplete | None = ..., subscribers: Incomplete | None = ..., source_client: Incomplete | None = ...): ...
    def delete(self, bucket, key, extra_args: Incomplete | None = ..., subscribers: Incomplete | None = ...): ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_value, *args) -> None: ...
    def shutdown(self, cancel: bool = ..., cancel_msg: str = ...) -> None: ...

class TransferCoordinatorController:
    def __init__(self) -> None: ...
    @property
    def tracked_transfer_coordinators(self): ...
    def add_transfer_coordinator(self, transfer_coordinator) -> None: ...
    def remove_transfer_coordinator(self, transfer_coordinator) -> None: ...
    def cancel(self, msg: str = ..., exc_type=...) -> None: ...
    def wait(self) -> None: ...
