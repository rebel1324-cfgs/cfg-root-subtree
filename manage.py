#Jumpstart economy

# let's be more professional
# todo: register this function as pre-commit hook and pre-push hook.
def stop_wtf():
    # todo: detect profanity
    # todo: detect credentials
    # todo: detect company related files (PLEASE!)
    pass

jetbrain_ide_list = [ "clion", "pycharm", "webstorm", "rider", "goland" ]

import os
def get_jetbrain_keymaps():
    for ide_path in jetbrain_ide_list:
        # specify target directory
        keymap_path = os.path.join(ide_path, "keymaps")

        if not os.path.exists(keymap_path):
            # create missing directory
            os.makedirs(keymap_path)
            
            # add fillers and close the file
            with open(os.path.join(keymap_path, "common-keymaps.xml"), "w+") as f:
                f.write("<keymap version=\"1\" name=\"Common Keymaps\" parent=\"Sublime Text (Mac OS X)\">\n</keymap>")

        # just return things again
        for p in os.listdir(keymap_path):
            yield os.path.join(keymap_path, p)

import xml.etree.ElementTree as ElementTree
import itertools
import copy
import logging
def sync_keybinds():
    logging.info("keybind:0000:KEYBIND_START")
    common_keymaps = dict()
    common_keybind_path = ".resources/common-keymaps.xml"
    rtree = ElementTree.parse(common_keybind_path)
    logging.info(f"keybind:0002:KEYBIND_PARSED:{common_keybind_path}")

    for a in rtree.findall("action"):
        common_keymaps[ a.attrib.get('id')  ] = a

    logging.info(f"keybind:0003:KEYBIND_KEYLEN:{len(common_keymaps.keys())}")

    for iter in get_jetbrain_keymaps():
        logging.info(f"keybind:0004:KEYBIND_OPEN:{iter}")
        etree = ElementTree.parse(iter)

        # copy the action id keys from the common keymaps
        # create a hashset to determine which key will get inserted if it does not exists
        action_sets = set(common_keymaps.keys())

        root = etree.getroot()
        index = 0
        for a in root:
            if a.tag != "action":
                continue
            action_id = a.attrib.get('id')  

            if action_id in action_sets:
                element = copy.deepcopy( common_keymaps[action_id])
                # deepcopy the element to prevent any kind of interferences
                root[index] = element
                action_sets.remove(action_id)
                logging.info(f"keybind:0005:KEYBIND_REPLACE:{action_id}")
            index = index + 1

        for action_id in action_sets:
            element = copy.deepcopy( common_keymaps[action_id])
            root.append(element)
            logging.info(f"keybind:0006:KEYBIND_APPEND:{action_id}")

        logging.info(f"keybind:0007:KEYBIND_WRITE:{iter}")
        etree.write(iter)

    logging.info("keybind:0001:KEYBIND_END")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    # todo: cli-fy
    sync_keybinds()
