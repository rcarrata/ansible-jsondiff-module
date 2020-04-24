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

authors:
    - Roberto Carratala (@rcarrata)
    - Asier Cidón (@acidonpe)
'''

EXAMPLES = '''
- name: Run and test the diff json module
    diff_json:
    original: "{'a': 1, 'b': 2}"
    compared: "{'a': 1, 'b': 3, 'c': 4}"
    register: diff
'''

def compare(orig_json,comp_json):
    """Function for compare two json files """
    result = diff(orig_json,comp_json)
    return result

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

    # Instantiation of the AnsibleModule as module with argument_specs
    # assigned in a dict before.
    module = AnsibleModule(
        argument_spec = module_args,
        supports_check_mode=True
    )

    # Check mode - Dry run
    if module.check_mode:
        module.exit_json(**result)

    # Assign the entry parameters from the compare module
    orig_json = module.params['original']
    comp_json = module.params['compared']

    # Execute the comparation fromt he original and compared json files
    # Assign the comparation to a string to be processed properly
    resume = str(compare(orig_json, comp_json))    

    # Fill the different result key/values
    result['original_json'] = module.params['original']
    result['compared_json'] = module.params['compared']
    result['comparisons'] = resume
    result['message'] = 'It works!'

    module.exit_json(**result)

def main():
    """Execute the main Ansible program"""
    run_module()

if __name__ == '__main__':
    main()
    