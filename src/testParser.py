# testParser.py
# --------------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.

import os
import re

class TestParser:
    def __init__(self, path):
        self.path = path

    def parse(self):
        test = {}
        with open(self.path, 'r') as f:
            lines = f.readlines()
        
        current_key = None
        current_val = []

        for line in lines:
            line_str = line.strip()
            if line_str.startswith('#') and not line_str.startswith('##'):
                continue
            match = re.match(r'^([a-zA-Z0-9_]+):\s*"(.*)"\s*$', line_str)
            if not match:
                match = re.match(r'^([a-zA-Z0-9_]+):\s*"""(.*)$', line_str)
                if match:
                    current_key = match.group(1)
                    current_val = [match.group(2)]
                    continue
                match = re.match(r'^([a-zA-Z0-9_]+):\s*(.*)$', line_str)

            if match:
                if current_key:
                    test[current_key] = "\n".join(current_val).strip()
                    current_key = None
                    current_val = []
                key, val = match.group(1), match.group(2)
                test[key] = val
            elif current_key:
                if line_str == '"""':
                    test[current_key] = "\n".join(current_val).strip()
                    current_key = None
                    current_val = []
                else:
                    current_val.append(line.rstrip('\n'))

        if current_key:
            test[current_key] = "\n".join(current_val).strip()

        return test
