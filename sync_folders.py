import os
import sys
import time
import shutil
import filecmp

def create_folders(path):
    """Create folders if they don't exist."""
    os.makedirs(path, exist_ok=True)

def synchronize_directories(source_path, replica_path, log_file):
    """Synchronize source folder with replica folder."""
    for root, dirs, files in os.walk(source_path):
        synchronize_directories_recursive(root, dirs, files, source_path, replica_path, log_file)

def synchronize_directories_recursive(root, dirs, files, source_path, replica_path, log_file):
    """Handle directories and files recursively during synchronization."""
    for directory in dirs:
        source_dir_path = os.path.join(root, directory)
        replica_dir_path = os.path.join(replica_path, os.path.relpath(source_dir_path, source_path))

        if not os.path.exists(replica_dir_path) or not os.path.isdir(replica_dir_path):
            create_folders(replica_dir_path)
            log_message = f"Directory created: {replica_dir_path}"
            print(log_message)
            log_file.write(log_message + "\n")
            log_file.flush()

    for file in files:
        source_file_path = os.path.join(root, file)
        replica_file_path = os.path.join(replica_path, os.path.relpath(source_file_path, source_path))

        if not os.path.exists(replica_file_path) or not filecmp.cmp(source_file_path, replica_file_path, shallow=False):
            shutil.copy2(source_file_path, replica_file_path)
            log_message = f"File copied/updated: {replica_file_path}"
            print(log_message)
            log_file.write(log_message + "\n")
            log_file.flush()

def remove_extra_files(source_path, replica_path, log_file):
    """Remove files and directories from replica folder that don't exist in source folder."""
    for root, dirs, files in os.walk(replica_path):
        for file in files:
            replica_file_path = os.path.join(root, file)
            source_file_path = os.path.join(source_path, os.path.relpath(replica_file_path, replica_path))

            if not os.path.exists(source_file_path):
                os.remove(replica_file_path)
                log_message = f"File removed: {replica_file_path}"
                print(log_message)
                log_file.write(log_message + "\n")
                log_file.flush()

        for directory in dirs:
            replica_dir_path = os.path.join(root, directory)
            source_dir_path = os.path.join(source_path, os.path.relpath(replica_dir_path, replica_path))

            if not os.path.exists(source_dir_path):
                remove_directory_recursive(replica_dir_path, log_file)

def remove_directory_recursive(directory_path, log_file):
    """Remove a directory and log its contents."""
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            file_path = os.path.join(root, file)
            log_message = f"File removed: {file_path}"
            print(log_message)
            log_file.write(log_message + "\n")
            log_file.flush()

        for subdirectory in dirs:
            subdirectory_path = os.path.join(root, subdirectory)
            log_message = f"Directory removed: {subdirectory_path}"
            print(log_message)
            log_file.write(log_message + "\n")
            log_file.flush()

    shutil.rmtree(directory_path)
    log_message = f"Directory removed: {directory_path}"
    print(log_message)
    log_file.write(log_message + "\n")
    log_file.flush()

def sync_folders(source_path, replica_path, interval, log_file_path):
    """Main function for folder synchronization."""
    try:
        create_folders(source_path)
        create_folders(replica_path)

        with open(log_file_path, "a") as log_file:
            while True:
                print("Synchronizing folders...")
                log_file.write(f"Synchronization started at {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                log_file.flush()

                synchronize_directories(source_path, replica_path, log_file)
                remove_extra_files(source_path, replica_path, log_file)

                log_file.write(f"Synchronization completed at {time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                log_file.flush()

                print("Synchronization completed.")
                time.sleep(interval)  # Wait for the specified interval
    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Invalid input! Please provide the source path, replica path, interval in seconds, and log file path as command line arguments")
        print("Usage: python sync_folders.py <source_path> <replica_path> <interval_seconds> <log_file>")
        sys.exit(1)

    source_path = sys.argv[1]
    replica_path = sys.argv[2]
    interval = int(sys.argv[3])
    log_file_path = sys.argv[4]

    sync_folders(source_path, replica_path, interval, log_file_path)
