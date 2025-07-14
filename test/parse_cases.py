import yaml

def parse_case(conditions):
    import pdb; pdb.set_trace()
    original_cmds = []
    with open(conditions, 'r') as cf:
        data = yaml.safe_load(cf)

    for item in data.values():
        if not item.get('bin', None):
            continue

        cmd_dict = {}
        cmd_str = f"{item['bin']}"

        if item.get('gpu', None):
            cmd_str += ' -gpu'

        for k, v in item.items():
            if k == 'case':
                cmd_dict[k] = v
            if k not in ('case', 'bin', 'gpu', 'index'):
                cmd_str += f' --{k} {v}'

        cmd_dict['cmd'] = cmd_str
        index_mapping = {str(item['index']): cmd_dict}
        original_cmds.append(index_mapping)

    new_cmds = sorted(original_cmds, key=lambda x: int(list(x.keys())[0]))
    return new_cmds


parse_case('test_condition.yaml')
