import bpy

bpy.data.scenes["Scene"].use_nodes = True
"""IDK how to turn on auto render"""

"""All the nodes:"""
scene = bpy.context.scene
nodes = bpy.context.scene.node_tree.nodes
links = bpy.context.scene.node_tree.links
NODE_SPACER = 200
#we are gonna work backwards.
composite = nodes.get("Composite")
render_layers = nodes.get("Render Layers")
#first add
firstTemp = nodes.new(type="CompositorNodeMixRGB")
firstTemp.blend_type = "ADD"
firstTemp.name = "add1"
firstTemp.location = 1000, 1000
links.new(firstTemp.outputs[0], composite.inputs[0])
#second add
secondTemp = nodes.new(type="CompositorNodeMixRGB")
secondTemp.blend_type = "ADD"
secondTemp.name = "add2"
secondTemp.location = firstTemp.location.x - NODE_SPACER, firstTemp.location.y + NODE_SPACER
links.new(secondTemp.outputs[0], nodes["add1"].inputs[2])
#movie clip - connects to first add
secondTemp = nodes.new(type="CompositorNodeMovieClip")
secondTemp.name = "movieClip1"
secondTemp.location = firstTemp.location.x - NODE_SPACER, firstTemp.location.y - NODE_SPACER
links.new(secondTemp.outputs[0], nodes["add1"].inputs[1])

firstTemp = nodes["add2"]
#blur - connects to second add
secondTemp = nodes.new(type="CompositorNodeBlur")
secondTemp.filter_type = "GAUSS"
secondTemp.name = "blur1"
secondTemp.location = firstTemp.location.x - NODE_SPACER, firstTemp.location.y + NODE_SPACER
links.new(secondTemp.outputs[0], firstTemp.inputs[2])
#RGB Curves - connects to second add
secondTemp = nodes.new(type="CompositorNodeCurveRGB")
secondTemp.name = "RGBCurve1"
secondTemp.location = firstTemp.location.x - NODE_SPACER, firstTemp.location.y - NODE_SPACER
links.new(secondTemp.outputs[0], firstTemp.inputs[1])
#2nd blur - connecs to RGB curve
firstTemp = nodes.new(type="CompositorNodeBlur")
firstTemp.filter_type = "GAUSS"
firstTemp.name = "blur2"
firstTemp.location = secondTemp.location.x - NODE_SPACER, secondTemp.location.y + NODE_SPACER
links.new(firstTemp.outputs[0], secondTemp.inputs[1])

#connect both blurs to Vector Blur
secondTemp = nodes.new(type="CompositorNodeVecBlur")
secondTemp.name = "vectorBlur1"
secondTemp.location = firstTemp.location.x - NODE_SPACER, firstTemp.location.y + NODE_SPACER
links.new(secondTemp.outputs[0], nodes["blur1"].inputs[0])
links.new(secondTemp.outputs[0], nodes["blur2"].inputs[0])

#connect render layers to Vector Blur
render_layers.location = firstTemp.location.x - NODE_SPACER, firstTemp.location.y
links.new(render_layers.outputs[0], nodes["vectorBlur1"].inputs[0])
links.new(render_layers.outputs[1], nodes["vectorBlur1"].inputs[1])
links.new(render_layers.outputs[2], nodes["vectorBlur1"].inputs[2])
