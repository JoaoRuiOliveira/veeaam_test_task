# VEEAM Technical Interview Test Task: Folder Synchronization

## Overview
This Python script was created as part of a technical interview test for Veeam.
The solution maintains a full copy of the source folder at the replica folder. It also removes files and directories from the replica that no longer exist in the source.

## Features
- **Efficient Synchronization**: Copying and updating files with automatic directory creation.
- **Logging Activities**: Comprehensive logging of synchronization activities for easy tracking.

## Installation & Usage
1. Have python installed in your PC. [Check this link](https://www.python.org/downloads/) to download python.
2. Clone this repository. [Check this link](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository#cloning-a-repository) to see how to clone a rep.
3. Open a terminal and navigate to the project directory.
4. Run the script using the following command:

   - python sync_folders.py <source_path> <replica_path> <interval_seconds> <log_file>

   - Replace `<source_path>`, `<replica_path>`, `<interval_seconds>`, and `<log_file>` with your specific values.

## Usefull knowledge
- `<source_path>`: The path of the source folder.
- `<replica_path>`: The path of the replica folder.
- `<interval_seconds>`: The time interval (in seconds) between synchronization cycles.
- `<log_file>`: The path of the log file to record synchronization activities.


## Contacts
- **João Oliveira**
  - GitHub: [JoaoRuiOliveira](https://github.com/JoaoRuiOliveira)
  - LinkedIn: [João Oliveira](https://www.linkedin.com/in/joao-oliveira-5044171b1/)


## Acknowledgments
- This project was developed as part of a technical interview test for VEEAM.

