"""
AI Teacher Shared - Utilities and validators for AI Teacher microservices
"""

__version__ = "1.2.0"

from .maps import (
    get_timit_to_mfa_map,
    get_mfa_to_timit_map,
)

from .utils import (
    UPLOAD_DIR,
    OUTPUT_DIR,
    create_job_directories,
    cleanup_job_directories,
)

from .validators import (
    validate_language,
    validate_transcript,
    validate_speed,
    validate_dictionary,
    UK_VALID_PHONEMES,
    US_VALID_PHONEMES,
)

__all__ = [
    # Maps
    "get_timit_to_mfa_map",
    "get_mfa_to_timit_map",
    # Constants
    "UPLOAD_DIR",
    "OUTPUT_DIR",
    "UK_VALID_PHONEMES",
    "US_VALID_PHONEMES",
    # Utils
    "create_job_directories",
    "cleanup_job_directories",
    # Validators
    "validate_language",
    "validate_transcript",
    "validate_speed",
    "validate_dictionary",
]
