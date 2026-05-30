import os
import shutil

# Directorios para almacenar los archivos subidos y los resultados
UPLOAD_DIR = "/tmp/alignment/uploads"
OUTPUT_DIR = "/tmp/alignment/outputs"

os.makedirs(UPLOAD_DIR, exist_ok=True)
os.chmod(UPLOAD_DIR, 0o777)
os.makedirs(OUTPUT_DIR, exist_ok=True)
os.chmod(OUTPUT_DIR, 0o777)

def create_job_directories(job_uuid: str) -> tuple[str, str]:
    """
    Creates upload and output directories for a job.
    
    Args:
        job_uuid: The job UUID

    Returns:
        tuple containing (job_upload_dir, job_output_dir)
    """
    job_upload_dir = os.path.join(UPLOAD_DIR, str(job_uuid))
    os.makedirs(job_upload_dir, exist_ok=True)

    job_output_dir = os.path.join(OUTPUT_DIR, str(job_uuid))
    os.makedirs(job_output_dir, exist_ok=True)
    
    return job_upload_dir, job_output_dir

def cleanup_job_directories(job_uuid: str) -> None:
    """
    Removes the upload and output directories for a job.
    
    Args:
        job_uuid: The job UUID
    """
    try:
        job_upload_dir = os.path.join(UPLOAD_DIR, str(job_uuid))
        if os.path.exists(job_upload_dir):
            shutil.rmtree(job_upload_dir)
        job_output_dir = os.path.join(OUTPUT_DIR, str(job_uuid))
        if os.path.exists(job_output_dir):
            shutil.rmtree(job_output_dir)
    except Exception as e:
        print(f"Error cleaning up directories: {e}")
