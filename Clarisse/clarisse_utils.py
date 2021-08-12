""" Important Clarisse Functions"""

# Importing Modules
import os


def get_objects(filter_rule="**", obj_type="*"):
    """
    Get the list of all the objects of specified type
    Args:
        filter_rule (str): OPTIONAL - Context Path where to query the search
        obj_type (str): Object Type

    Returns (list ofObject): List of objects.

    """
    objects = ix.api.OfObjectVector()
    project_root = ix.application.get_factory().get_project()
    ix.application.get_matching_objects(objects, filter_rule, project_root,
                                        obj_type)
    return objects


def create_context(path):
    """
        Check if a context exists. If not, Create one

    Args:
        path (str): Path of the context in string

    Returns (bool): True if the context is created

    """
    ctx_item = ix.item_exists(path)

    try:
        if not ctx_item:
            ix.create_context(path)
        return True
    except:
        return False


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
        print(new_path)
        create_context(new_path)
