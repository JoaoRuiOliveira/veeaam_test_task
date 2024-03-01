import os
import sys
import time
import shutil
import filecmp

def sync_folders(source_path, replica_path, interval, log_file_path):
    try:
        # Create source and replica folders if they don't exist
        os.makedirs(source_path, exist_ok=True)
        os.makedirs(replica_path, exist_ok=True)

        # Open the log file in append mode
        with open(log_file_path, "a") as log_file:
            while True:
                print("Synchronizing folders...")
                log_file.write(f"Synchronization started at {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
                log_file.flush()

                # Synchronize source folder with replica folder
                for root, dirs, files in os.walk(source_path):
                    # Handle directories
                    for directory in dirs:
                        source_dir_path = os.path.join(root, directory)
                        replica_dir_path = os.path.join(replica_path, os.path.relpath(source_dir_path, source_path))

                        if not os.path.exists(replica_dir_path):
                            os.makedirs(replica_dir_path)
                            print(f"Directory created: {replica_dir_path}")
                            log_file.write(f"Directory created: {replica_dir_path}\n")
                            log_file.flush()

                    # Handle files
                    for file in files:
                        source_file_path = os.path.join(root, file)
                        replica_file_path = os.path.join(replica_path, os.path.relpath(source_file_path, source_path))

                        # Copy file to replica folder if it doesn't exist or if it's different
                        if not os.path.exists(replica_file_path) or not filecmp.cmp(source_file_path, replica_file_path, shallow=False):
                            shutil.copy2(source_file_path, replica_file_path)
                            print(f"File copied/updated: {replica_file_path}")
                            log_file.write(f"File copied/updated: {replica_file_path}\n")
                            log_file.flush()

                # Remove files and directories from replica folder that don't exist in source folder
                for root, dirs, files in os.walk(replica_path):
                    for file in files:
                        replica_file_path = os.path.join(root, file)
                        source_file_path = os.path.join(source_path, os.path.relpath(replica_file_path, replica_path))

                        if not os.path.exists(source_file_path):
                            os.remove(replica_file_path)
                            print(f"File removed: {replica_file_path}")
                            log_file.write(f"File removed: {replica_file_path}\n")
                            log_file.flush()

                    for directory in dirs:
                        replica_dir_path = os.path.join(root, directory)
                        source_dir_path = os.path.join(source_path, os.path.relpath(replica_dir_path, replica_path))

                        if not os.path.exists(source_dir_path):
                            # Log files within the directory before removing it
                            for root_sub, dirs_sub, files_sub in os.walk(replica_dir_path):
                                for file_sub in files_sub:
                                    file_sub_path = os.path.join(root_sub, file_sub)
                                    print(f"File removed: {file_sub_path}")
                                    log_file.write(f"File removed: {file_sub_path}\n")
                                    log_file.flush()

                                for directory_sub in dirs_sub:
                                    dir_sub_path = os.path.join(root_sub, directory_sub)
                                    print(f"Directory removed: {dir_sub_path}")
                                    log_file.write(f"Directory removed: {dir_sub_path}\n")
                                    log_file.flush()

                            shutil.rmtree(replica_dir_path)
                            print(f"Directory removed: {replica_dir_path}")
                            log_file.write(f"Directory removed: {replica_dir_path}\n")
                            log_file.flush()

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

    # Call sync_folders function with command line arguments
    sync_folders(source_path, replica_path, interval, log_file_path)