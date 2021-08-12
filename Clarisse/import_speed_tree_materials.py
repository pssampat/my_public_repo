import sys
import os
# sys.path.append('C:\Program Files\Isotropix\Clarisse 5.0\Clarisse\python3')

# Importing Modules
import ix
from os import walk

# main_obj = ix.get_item("build://project/scene/ASSET/pine_a/pine_a")

MATERIAL_NAME = ["Bark"]
MATERIAL_TYPE = "MaterialPhysicalDisneyPrincipled"
MATERIAL_CONTEXT = "build://project/scene/ASSET/material"
OS_TEX_PATH = "C:\\Work\\Clarisse\\BurningForest\\assets\\tree\\pine_a"


def create_context(path):
    """
        Deletes old Occlusion Utility context and creates a new one

    Args:
        path (str): Path of the context in string

    Returns:

    """
    occ_utils_ctx = ix.item_exists(path)

    if not occ_utils_ctx:
        ix.create_context(path)


def check_path(path):
    """
    Check if the each context in the specified path exists
    Args:
        path (str): Path of the context in string

    Returns:
    """
    _base_path = "build://project/"
    all_ctx = path.replace(_base_path, "").split("/")
    new_path = _base_path

    for ctx in all_ctx:
        new_path += ("/" + ctx)
        create_context(new_path)
    return path


for mtl in MATERIAL_NAME:

    diff = f"{mtl}.png"
    ao = f"{mtl}_AO.png"
    gloss = f"{mtl}_Gloss.png"
    nrm = f"{mtl}_Normal.png"
    opa = f"{mtl}_Opacity.png"

    mat_path = check_path(f"build://project/scene/ASSET/material/{mtl}/maps")
    all_files = next(walk(OS_TEX_PATH), (None, None, []))[2]

    for mtl_type in [diff, ao, gloss, nrm, opa]:

        if mtl_type in all_files:

            obj = mtl_type.replace(".png", "")
            item = ix.item_exists(f"{mat_path}/{obj}")

            if not item:
                item = ix.cmds.CreateObject(mtl_type.replace(".png", ""),
                                            "TextureMapFile", "Global",
                                            mat_path)

            tex_path = f"{OS_TEX_PATH}\\{mtl_type}"

            item.get_attribute("filename").set_string(tex_path)

            print(item)
