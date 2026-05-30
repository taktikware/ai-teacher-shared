# AI Teacher Shared

Shared utilities and validators for AI Teacher microservices.

## Installation

### From GitHub

```bash
pip install git+https://github.com/taktikware/ai-teacher-shared.git@v1.0.0
```

### For development

```bash
git clone https://github.com/taktikware/ai-teacher-shared.git
cd ai-teacher-shared
pip install -e .
```

## Usage

```python
from ai_teacher_shared.utils import create_job_directories, cleanup_job_directories
from ai_teacher_shared.validators import (
    validate_language,
    validate_transcript,
    validate_speed,
    validate_dictionary
)

# Create job directories
upload_dir, output_dir = create_job_directories("job-uuid-123")

# Validate inputs
validate_language("us")
validate_transcript("Hello world")
validate_speed("medium")
validate_dictionary("us", 2, ["HH AH0 L OW1", "W ER1 L D"])

# Cleanup
cleanup_job_directories("job-uuid-123")
```

## Modules

### `ai_teacher_shared.utils`

Utilities for managing job directories:
- `create_job_directories(job_uuid)`: Creates upload and output directories
- `cleanup_job_directories(job_uuid)`: Removes job directories

### `ai_teacher_shared.validators`

Input validators for FastAPI endpoints:
- `validate_language(language)`: Validates language code (us/uk)
- `validate_transcript(transcript)`: Validates transcript is not empty
- `validate_speed(speed)`: Validates speed parameter
- `validate_dictionary(language, expected_size, dictionary)`: Validates IPA phoneme dictionary

## Development

### Running tests

```bash
pytest
```

### Building

```bash
python -m build
```

## License

MIT License - see LICENSE file for details.

## Versioning

This project follows [Semantic Versioning](https://semver.org/).

- v1.0.0 - Initial release
