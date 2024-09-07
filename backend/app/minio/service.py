from minio import Minio


minio_client = Minio(
    "localhost:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
    secure=False
)


def upload_image_to_minio(file_path, bucket_name):
    image_key = file_path.split("/")[-1]  # Используем имя файла как ключ
    minio_client.fput_object(bucket_name, image_key, file_path)
    return image_key


bucket = "my-bucket"
file_path = "path/to/image.jpg"

image_key = upload_image_to_minio(file_path, bucket)

print(f"Image saved with ID: and MinIO key: {image_key}")
