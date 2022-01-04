import bpy

bottomEmpty = bpy.data.objects["Hilt"]
topEmpty = bpy.data.objects["top"]
#bpy.ops.object.empty_add(type='PLAIN_AXES')
#add the armature wheere the top is
bpy.ops.object.armature_add(enter_editmode=False, location=topEmpty.location)
ob = bpy.context.active_object
ob.name = 'handle'
bpy.ops.object.editmode_toggle()

#snap selected no work
handle=ob
bone = handle.data.edit_bones["Bone"]
bone.tail.x = bottomEmpty.location.x - topEmpty.location.x
bone.tail.y = bottomEmpty.location.y - topEmpty.location.y
bone.tail.z = bottomEmpty.location.z - topEmpty.location.z
#parenting
bpy.ops.object.constraint_add(type='CHILD_OF')
bpy.context.object.constraints['Child Of'].target = topEmpty
#switch back to object mode
bpy.ops.object.editmode_toggle()
#make sure ur active object is still the handle for the constraint thing
bpy.ops.object.constraint_add(type='STRETCH_TO')
bpy.context.object.constraints['Stretch To'].target = bottomEmpty
bpy.context.object.constraints['Stretch To'].volume = 'NO_VOLUME'
#snap selected
bone.tail.x = bottomEmpty.location.x - topEmpty.location.x
bone.tail.y = bottomEmpty.location.y - topEmpty.location.y
bone.tail.z = bottomEmpty.location.z - topEmpty.location.z
bpy.ops.object.editmode_toggle()
