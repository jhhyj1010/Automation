#/usr/bin/env python

import yaml
import sys


def generate_cmd(condition):
    with open(condition, "r", encoding="utf-8") as f:
        yaml_content = yaml.load(f, Loader=yaml.FullLoader)
        import pdb; pdb.set_trace()
        for testset, cases in yaml_content.items():
            for case in cases:
                cmd = ""
                index_cmd_dict = {}
                cmd_dict = {}

                cmd_dict['case'] = case['case'] if case.get('case', None) else ""
                cmd_dict['cmd'] = case['bin'] if case.get('bin', None) else ""
                cmd += ' -gpu' if case.get('gpu', None) else ""
                for k, v in case.items():
                    if (k != 'gpu' or (k == 'gpu' and v.upper() == 'FALSE')) and k not in ('bin', 'case', 'index'):
                        cmd += f" --{k} {v}"
                cmd_dict['cmd'] += cmd

                index_cmd_dict[str(case['index'])] = cmd_dict


generate_cmd(sys.argv[1])            
