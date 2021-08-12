
def filter_selection(node_name="", node_type=""):
    """
    Filters selected nodes by Name / NodeType
    Args:
        node_name ():
        node_type:

    Returns:

    """
    selection = nuke.selectedNodes()

    if not node_name and not node_type:
        print(
            "Please specify the node name or "
            "node type before running the script"
        )
        return

    if not selection:
        print("Nothing Selected")
        return

    filter_list = list()

    for node in selection:

        if node_name:
            if node_name in node['name'].getValue():
                filter_list.append(node)
                node.setSelected(True)
            else:
                node.setSelected(False)

        if node_type:
            if node_type == node.Class():
                filter_list.append(node)
                node.setSelected(True)
            else:
                node.setSelected(False)

    print filter_list

filter_selection(node_type="DeepReformat")