#!/usr/bin/env python3
# -*- coding: utf-8 -*-
def get_content(filename: str) -> str:
    with open(filename) as f:
        content = f.read()
    return content


def set_content(filename: str, content: str):
    with open(filename, 'w') as f:
        f.write(content)


def main():
    debian = {
        'current': 'bullseye',
        'new': 'bookworm',
    }
    list_file = [
        '/etc/apt/sources.list.d/cros.list',
        '/etc/apt/sources.list',
    ]

    for file in list_file:
        content = get_content(file)
        content = content.replace(debian['current'], debian['new'])
        set_content(file, content)


if __name__ == "__main__":
    main()
