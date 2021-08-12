"""
Prints the list of samples value in the entire scene

NOTE---------------------------------------
- - - - - - ONLY WORKS WITH CLARISSE 5
-------------------------------------------

Output Example:
----------------------------------------------------------------------------------------------------
Lights Data:
sphere  | sample_count:5 ----------------------- (build://project/material/prop/sphere)
environment  | sample_count:4 ----------------------- (build://project/material/prop/environment)
distant  | sample_count:16 ----------------------- (build://project/material/prop/distant)
----------------------------------------------------------------------------------------------------
Materials Data:
autodesk_standard_surface  | material_sample_count:23 ----------------------- (build://project/material/prop/autodesk_standard_surface)
disney_principled  | material_sample_count:23 ----------------------- (build://project/material/prop/disney_principled)
sss  | material_sample_count:55 ----------------------- (build://project/material/prop/sss)
"""

# Defining Globals

ATTR_LIST = [
    'sample_count',
    'material_sample_count'
]


def get_objects(filter_rule="**", obj_type="*"):
    """
    FOR CLARISSE 5.0+

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


def print_data(ctx="project*light*shot**",
               obj_typ="Light",
               attrib_list=ATTR_LIST):
    """
    Prints Object Name, Samples and Full Object Path

    Args:
        ctx (str): Object Path
        obj_typ (str): Object Type, Ex: Light, Material
        attrib_list (list): List of Attributes to get value for

    Returns:

    """

    all_lights = get_objects(ctx, obj_typ)

    for light in all_lights:

        light_name = light.get_name()
        attr_val = str()

        for attrib in attrib_list:

            if light.attribute_exists(attrib):

                value = light.get_attribute(attrib).get_long()

                if value == -1:
                    # Ignore materials without any samples
                    return

                attr_val = f"{attr_val} | {attrib}:{value}"

        print(f"{light_name} {attr_val} ----------------------- ({light})")


# Light Data
print("-"*100)
print("Lights Data:")
print_data(ctx="project*", obj_typ="Light")

# Material Data
print("-"*100)
print("Materials Data:")
print_data(ctx="project*", obj_typ="Material")
