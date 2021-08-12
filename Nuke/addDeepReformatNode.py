# Creates a Deep Reformat after selected node and connects it to its dependents

# Get Selected Nodes
nodes = nuke.selectedNodes()

for node in nodes:

    # Get Inputs and Outputs
    inputs = node
    outputs = node.dependent()[0]

    # Get Node Positions
    in_x, in_y = inputs['xpos'].value(), inputs['ypos'].value()

    # Create DeepReformat Node
    new_node = nuke.nodes.DeepReformat()

    # Set Position of the new node
    new_node['xpos'].setValue(in_x + 150)
    new_node['ypos'].setValue(in_y + 40)

    # Set Inputs to the DeepReformat and to the Dependent Node.
    outputs.setInput(1, new_node)
    new_node.setInput(0, inputs)
