# coding=utf-8

import os
from utils.cfgtmpl import CfgTemplate


if __name__ == "__main__":
    current_dir = os.path.dirname(__file__)

    source_file = os.path.join(current_dir, "supervisord.conf.source")
    dest_file = os.path.join(current_dir, "supervisord.conf")

    variables = {
        'prj_name': 'test',
        'prj_path': current_dir,
        'log_path': os.path.join(current_dir, 'log'),
        'start_script': 'test.py'
    }

    CfgTemplate(source_file, dest_file, variables)()
