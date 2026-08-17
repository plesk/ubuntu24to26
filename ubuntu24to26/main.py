#!/usr/bin/python3
# Copyright 2024. Plesk International GmbH. All rights reserved.

import sys

import pleskdistup.main
import pleskdistup.registry

import ubuntu24to26.upgrader

if __name__ == "__main__":
    pleskdistup.registry.register_upgrader(ubuntu24to26.upgrader.Ubuntu24to26Factory())
    sys.exit(pleskdistup.main.main())
