# coding=utf-8

import os
import string

class CfgTemplate(object):

    @staticmethod
    def ensure_dir(dir_path):
        if not os.path.exists(dir_path):
            os.mkdir(os.path)

    def __init__(self, tmpl_file, dest_file, variables):
        self.tmpl_file = tmpl_file
        self.dest_file = dest_file
        self.variables = variables

    def load_file(self, file_path):
        try:
            with open(file_path, 'r') as f:
                content = f.read()
            return content
        except IOError as e:
            print "load_file error, path=%s, e=%s" % (file_path, e)
            return ''

    def save_file(self, file_path, content):
        try:
            self.ensure_dir(os.path.dirname(file_path))
            with open(file_path, 'w') as f:
                f.write(content)
            return True
        except IOError as e:
            print "save_cfg error, path=%s, e=%s" % (file_path, e)
            return False

    def __call__(self):
        template = self.load_file(self.tmpl_file)
        if not template:
            raise Exception("tmpl_file does not exist or is empty, path=%s" % self.tmpl_file)

        te = string.Template(template)
        content = te.safe_substitute(self.variables)
        result = self.save_file(self.dest_file, content)
        if not result:
            raise Exception("dest_file save error, check is path exists: %s" % self.dest_file)
        print "genrate config file OK, dest_path=%s" % self.dest_file