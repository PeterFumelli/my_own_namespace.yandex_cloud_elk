#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

DOCUMENTATION = r'''
---
module: my_test

short_description: Create a text file with specified content
version_added: "1.0.0"

description:
  - This module creates or updates a text file on the target host with given content.

options:
  path:
    description: Path to the file that should be created.
    required: true
    type: str
  content:
    description: Content to be written into the file.
    required: true
    type: str

extends_documentation_fragment:
  - my_own_namespace.yandex_cloud_elk.my_doc_fragment_name

author:
  - "PeterFumelli (@PeterFumelli)"
'''

EXAMPLES = r'''
- name: Create file with hello world
  my_own_namespace.yandex_cloud_elk.my_test:
    path: /tmp/hello.txt
    content: "Hello, World!"

- name: Update file content
  my_own_namespace.yandex_cloud_elk.my_test:
    path: /tmp/hello.txt
    content: "New content"
'''

RETURN = r'''
changed:
  description: Whether the file was created or modified.
  type: bool
  returned: always
path:
  description: Path to the managed file.
  type: str
  returned: always
content:
  description: Content written to the file.
  type: str
  returned: always
'''

import os
from ansible.module_utils.basic import AnsibleModule


def run_module():
    module_args = dict(
        path=dict(type='str', required=True),
        content=dict(type='str', required=True),
    )

    result = dict(
        changed=False,
        path='',
        content='',
    )

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=True,
    )

    path = module.params['path']
    content = module.params['content']

    result['path'] = path
    result['content'] = content

    # если check_mode — просто выходим
    if module.check_mode:
        module.exit_json(**result)

    file_exists = os.path.exists(path)
    current_content = ""

    if file_exists:
        try:
            with open(path, 'r', encoding='utf-8') as f:
                current_content = f.read()
        except Exception:
            pass

    if not file_exists or current_content != content:
        try:
            os.makedirs(os.path.dirname(path), exist_ok=True)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
            result['changed'] = True
        except Exception as e:
            module.fail_json(msg=f"Failed to write file {path}: {e}", **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()