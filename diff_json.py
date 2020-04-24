from jsondiff import diff
import json
from ansible.module_utils.basic import AnsibleModule

DOCUMENTATION = '''
---
module: diff_json
short_description: Compare json files and show differences.
version_added: "0.1"
description:
    - Receive two json files
    - Define the first one as original, and the second one as compared
    - Compare both files
    - Display the summary of the comparison

options:
    original:
        description:
            - Original Json file
        required: true
    new:
        description:
            - Compared Json file
        required: true

author:
    - Roberto Carratala (@rcarrata)
'''

EXAMPLES = '''
original = {
    "jsonrpc": "2.0",
    "method": "substract",
    "params": [42],
    "id": 5,
    "newversion": "true",
}

modified = {
    "jsonrpc": "2.0",
    "method": "substract",
    "params": [31],
}

# Pass in a message
- name: Test with a message
  my_test:
    name: hello world

# pass in a message and have changed true
- name: Test with a message and changed output
  my_test:
    name: hello world
    new: true

# fail the module
- name: Test failure of the module
  my_test:
    name: fail me
'''

def compare(orig_json,comp_json):
    

    result = diff(orig_json,comp_json)
    strresult = str(result)
    return strresult

def run_module():
    """Run Ansible Module with parameters"""
    module_args = dict(
        original = dict(type='dict', required=True),
        compared = dict(type='dict', required=True)            
    )

    result = dict(
        changed = False,
        original_json='',
        compared_json='',
        message=''
    )

    module = AnsibleModule(
        argument_spec = module_args,
        supports_check_mode=True
    )

    if module.check_mode:
        module.exit_json(**result)

    # Assign the entry parameters from the compare module
    orig_json = module.params['original']
    comp_json = module.params['compared']

    resume = compare(orig_json, comp_json)    

    result['original_json'] = module.params['original']
    result['compared_json'] = module.params['compared']
    result['comparison'] = resume
    result['message'] = 'Module is working correctly'

    module.exit_json(**result)

def main():
    """Execute the main Ansible program"""
    run_module()

if __name__ == '__main__':
    main()
    