# Json Diff Ansible Module

## Synopsys

Ansible Module for simple comparation between two json files

## Parameters

| Parameter | Choices/Defaults |         Comments         |
|---------- |:----------------:|-------------------------:|
| original  |                  | Original file to compare |
| compared  |                  | File for compare for     |

## Examples:

```bash
# Define the vars or files that you want to compare:

vars:
  - json1: {'a': 1, 'b': 2}
  - json2: {'b': 3, 'c': 4}

# Use it into your playbook and define the original and the compared:

- name: Run and test the diff json module
  diff_json:
    original: "{{ json1 }}"
    compared: "{{ json2 }}"
  register: diff

- name: Debug the full output
  debug:
    msg: "{{ diff }}"

- name:
  debug:
    msg:
    - "This is the original message {{ diff.original_json }}"
    - "This is the message to compare {{ diff.compared_json }}"
    - "This is the comparison {{ diff.comparisons }}"
```

## Status:

* Tested and working with Python3 and Ansible 2.8 and 2.9.x
* This module is maintained by @rcarrata

## Authors:

* Roberto Carratalá
