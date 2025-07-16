#!/usr/bin/env python

import json

def get_inventory():
    """
    Generates the inventory in the format Ansible expects.
    """
    inventory = {
        "_meta": {
            "hostvars": {
                "webserver01.example.com": {
                    "ansible_host": "192.168.1.10",
                    "http_port": 8080
                },
                "dbserver01.example.com": {
                    "ansible_host": "192.168.1.20"
                }
            }
        },
        "all": {
            "children": [
                "webservers",
                "dbservers",
                "ungrouped"
            ]
        },
        "webservers": {
            "hosts": [
                "webserver01.example.com"
            ],
            "vars": {
                "service_name": "nginx"
            }
        },
        "dbservers": {
            "hosts": [
                "dbserver01.example.com"
            ]
        }
    }
    return inventory

if __name__ == "__main__":
    print(json.dumps(get_inventory(), indent=4))
