# Manual Testing

## Overview
This document explains what testing is made to assure that the solution is performing well.

## Pre-requisites
Ensure that the script is set up and configured correctly before performing tests. Refer to README file to see instructions.

## Testing Scenarios

### 1. Initial Synchronization
- **Objective:** Verify that the script synchronizes the source and replica folders initially.

- **Steps:**
  1. Execute the script with source and replica folders.
  2. Check that the script creates replica folders and copies files from the source.

- **Expected Result:** Replica folders mirror the content of the source.

### 2. File Copy/Update
- **Objective:** Ensure that the script copies and updates files correctly.

- **Steps:**
  1. Modify a file in the source folder.
  2. Execute the script.
  3. Check that the modified file is copied/updated in the replica folder.

- **Expected Result:** Modified files are reflected in the replica.

### 3. File Removal
- **Objective:** Confirm that the script removes files from the replica if deleted in the source.

- **Steps:**
  1. Delete a file from the source folder.
  2. Execute the script.
  3. Check that the deleted file is removed from the replica folder.

- **Expected Result:** Deleted files are removed from the replica.

### 4. Directory Creation and Removal
- **Objective:** Validate the handling of directory creation and removal.

- **Steps:**
  1. Create a new directory in the source.
  2. Execute the script.
  3. Check that the new directory is created in the replica.

- **Expected Result:** New directories are created in the replica.

### 5. Logging
- **Objective:** Ensure that log files are created and updated during synchronization.

- **Steps:**
  1. Execute the script with source and replica folders.
  2. Check the log file for entries related to folder synchronization.

- **Expected Result:** Log file contains entries for folder synchronization actions.
