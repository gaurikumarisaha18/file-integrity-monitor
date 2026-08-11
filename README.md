# File Integrity Monitoring Tool

## Overview

A beginner-friendly cybersecurity tool developed in Python to detect unexpected changes in files using SHA-256 hashing.

## Features

- Generates SHA-256 hashes for files
- Creates a baseline of file hashes
- Detects modified files
- Detects newly added files
- Detects deleted files
- Reports files with no changes

## Technologies Used

- Python
- SHA-256
- JSON
- File Handling

## How It Works

The tool creates a baseline containing the SHA-256 hash of files in the test folder.

When the tool is run again, it calculates the current file hashes and compares them with the stored baseline.

If a file is modified, its hash changes and the tool reports the file as modified.

## Testing

The tool was tested by creating a baseline for `sample.txt`, verifying `[NO CHANGE]`, then modifying the file and detecting `[MODIFIED]`.

## Learning Outcomes

- Understanding file integrity
- Understanding cryptographic hashing
- Using SHA-256 for integrity verification
- Python file handling
- Basic cybersecurity concepts