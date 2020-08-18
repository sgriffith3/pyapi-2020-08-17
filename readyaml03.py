#!/usr/bin/python3

# YAML is NOT part of the standard library
# python3 -m pip install pyyaml
import yaml

def main():
    ## Open a blob of YAML data
    #with open("myYAML.yml", "r") as yf:
        ## convert YAML into Python data structures (lists and dictionaries)
    yf = "[{'name': 'Alta3 Research', 'hosts': 'all', 'apps': ['htop', 'sshd', 'iptables']}]"
    print(type(yf))
    pyyammy = yaml.load(yf, Loader=yaml.SafeLoader)
    # display our new Python data
    print(pyyammy)
    print(type(pyyammy))

if __name__ == "__main__":
    main()

