from minio.error import S3Error
from fastapi import UploadFile
from minio import Minio
from io import BytesIO


minio_client = Minio(
    "localhost:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
    secure=False
)


def upload_file(file: UploadFile, bucket: str, file_id: str) -> None:
    print(file)
    try:
        if not minio_client.bucket_exists(bucket):
            minio_client.make_bucket(bucket)

        file_data = file.file.read()

        minio_client.put_object(
            bucket,
            file_id,
            BytesIO(file_data),
            len(file_data),
            content_type=file.content_type
        )

        print(f"message: File '{file.filename}' uploaded successfully!")
    except Exception as err:
        print("error " + str(err))


def get_files_url(bucket_name: str, image_key: str) -> str | None:
    try:
        url = minio_client.presigned_get_object(bucket_name, image_key)
        return url
    except S3Error as err:
        print(f"Error while fetching file from MinIO: {err}")
        return


def delete_file(bucket_name: str, file_id: str) -> None:
    try:
        minio_client.remove_object(bucket_name, file_id)
    except S3Error as err:
        print(f"Ошибка при удалении файла из MinIO: {err}")