# Filoverførsler

## Intro

This robot simply moves files from one folder to another.
It only moves files from the source folder that doesn't already exist in the target folder.
Files are compared by name only.

## Arguments

The robot expects a json string in the following format:

```json
{
    "source_folder": "Ny mappe",
    "target_folder": "Ny mappe (2)"
}
```
