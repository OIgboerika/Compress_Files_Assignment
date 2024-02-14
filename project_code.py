import os
import tarfile
import zipfile
from datetime import datetime

def get_compression_types():
    return {
        '1': '.zip',
        '2': '.tar',
        '3': '.tgz'
    }

def compress_folder(folder_path, compression_type):
    if compression_type == '.zip':
        return compress_zip(folder_path)
    elif compression_type == '.tar':
        return compress_tar(folder_path)
    elif compression_type == '.tgz':
        return compress_tgz(folder_path)
    else:
        raise ValueError(f'Unsupported compression type: {compression_type}')

def compress_zip(folder_path):
    archive_name = f"{os.path.basename(folder_path)}_" \
                    f"{datetime.now().strftime('%Y_%m_%d')}.zip"
    with zipfile.ZipFile(archive_name, 'w') as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                zipf.write(os.path.join(root, file),
                            os.path.relpath(os.path.join(root, file), folder_path))
    return archive_name

def compress_tar(folder_path):
    archive_name = f"{os.path.basename(folder_path)}_" \
                    f"{datetime.now().strftime('%Y_%m_%d')}.tar"
    with tarfile.open(archive_name, 'w') as tarf:
        tarf.add(folder_path, arcname=os.path.basename(folder_path))
    return archive_name

def compress_tgz(folder_path):
    archive_name = f"{os.path.basename(folder_path)}_" \
                    f"{datetime.now().strftime('%Y_%m_%d')}.tgz"
    with tarfile.open(archive_name, 'w:gz') as tarf:
        tarf.add(folder_path, arcname=os.path.basename(folder_path))
    return archive_name

def main():
    folder_path = input("Enter the path of the folder to compress: ")
    compression_types = get_compression_types()
    print("Available compression types:")
    for i, compression_type in compression_types.items():
        print(f"{i}: {compression_type}")
    selected_compression_type = input("Enter the number of the desired compression type: ")
    try:
        archive_name = compress_folder(folder_path, compression_types[selected_compression_type])
        print(f"Successfully compressed folder to {archive_name}")
    except Exception as e:
        print(f"Failed to compress folder: {e}")

if __name__ == "__main__":
    main()
