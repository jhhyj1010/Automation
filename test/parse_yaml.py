# It then prepares each case by adding a command based on the case parameters.

import yaml
import sys
#import typing

def prepare_case(condition_yaml):
    """
    Parse the cases from yaml file, and return the case list like:
        [
            "1": {"case": "negative_02", "cmd": "/opt/bgpu:v20.23.4.bin --qos WorstEffort --timeout 30"},
            "4": {"case": "full", "cmd": "/opt/bgpu:v20.23.5.bin -gpu --timeout 30"},
        ]
    Request:
        1. If gpu is true, add -gpu parameter. Otherwise, ignore the parameter
        2. For other values, append them to the parameter in the specified format: --<key> <value>
        3. Sort the dict by index in ascending order
    Tips:
        You can use the "checker" tool to verify your Python code.
        To do so, simply run "./checker" in the current directory.
    """
    import pdb; pdb.set_trace()
    with open(condition_yaml, "r", encoding="utf-8") as f:
        cases = yaml.load(f, Loader=yaml.FullLoader)
        new_cases = []
        # Complete your code here
        
        for value in cases.values():
            for val in value:
                cmd = ""
                index_cmd_dict = {}
                cmd_dict = {}
                
                cmd_dict["case"] = val["case"] if val.get("case", None) else ""
                cmd_dict["cmd"] = val["bin"] if val.get("bin", None) else ""
                cmd += " -gpu" if val.get("gpu", None) else ""
                for key, dict_val in val.items():
                    if (key != "gpu" or (key == "gpu" and val == False)) and \
                        key != "bin" and key != "case" and key != "index":
                        cmd += f" --{key} {dict_val}"
                cmd_dict["cmd"] += cmd
                index_cmd_dict[str(val["index"])] = cmd_dict
                #print(key, val)

                new_cases.append(index_cmd_dict)
                # sort new_cases by index
                
                #new_cases.sort()
            '''cmd = value["cmd"]
            if value["gpu"]:
                cmd += " -gpu"
            for key, val in value.items():
                if key != "gpu" and key != "cmd":
                    cmd += f" --{key} {val}"
            new_cases.append(cmd)'''
        #for _, value in cases.values().items():
        #    print(value)
    pdb.set_trace()
    '''sorted_cases = []
    min_index = new_cases[0]["index"]
    for i in new_cases:
        sorted_cases.append(i)
        if i["index"] < min_index:
            min_index = i["index"]'''
    #for i in range(0, len(new_cases)):
    #    #if new_cases[i]["index"] == min_index:
    #    #    continue
    #    for j in range(1, len(new_cases)):
    #        if new_cases[i]["index"] > new_cases[j]["index"]:
    #            new_cases[i], new_cases[j] = new_cases[j], new_cases[i]
    print(new_cases)
    return sorted(new_cases,key=lambda x: int(list(x.keys())[0])) # KEY point
    #sorted(new_cases, key=lambda x: x["index"])
    #return new_cases
            

ret = prepare_case(sys.argv[1])
print(ret)