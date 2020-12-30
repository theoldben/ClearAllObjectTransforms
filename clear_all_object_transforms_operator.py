bl_info = {
    "name": "Clear All Transforms",
    "author": "xxxKenseIxxx, crute",
    "version": (1, 0),
    "blender": (2, 90, 0),
    "location": "View3D > Object",
    "description": "Clears object location, rotation and scale. Does NOT apply",
    "warning": "",
    "doc_url": "",
    "category": "3D View",
}


import bpy


def main(context):
    for ob in context.scene.objects:
        print(ob)


class ClearAllTransform(bpy.types.Operator):
    """Clear location, rotation and scale. Does NOT apply"""
    bl_idname = "object.transform_all_clear"
    bl_label = "Clear All Transforms"

    @classmethod # Will never run when poll returns false
    def poll(cls, context):
        return context.active_object is not None

    def execute(self, context):
        main(context)
        
        # reset scale (1;1;1)
        bpy.context.active_object.scale[0] = bpy.context.active_object.scale[1] = bpy.context.active_object.scale[2] = 1
        #reset rotation (0;0;0)
        bpy.context.active_object.rotation_euler[0] = bpy.context.active_object.rotation_euler[1] = bpy.context.active_object.rotation_euler[2] = 0
        #reset location (0;0;0)
        bpy.context.active_object.location[0] = bpy.context.active_object.location[1] = bpy.context.active_object.location[2] = 0
        
        return {'FINISHED'}
    
def menu_draw(self, context):
    layout = self.layout   
    layout.operator("object.transform_all_clear", text="Clear All Transformations", icon="X")
    


def register():
    bpy.utils.register_class(ClearAllTransform)
    bpy.types.VIEW3D_MT_object.append(menu_draw) # Add Operator to Object menu

def unregister():
    bpy.utils.unregister_class(ClearAllTransform)
    bpy.types.VIEW3D_MT_object.Clear.remove(menu_draw) # Remove Operator from Object menu

if __name__ == "__main__":
    register()
