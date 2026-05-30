"""
AI Teacher Shared - Utilities and validators for AI Teacher microservices
"""

__version__ = "1.0.0"

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
