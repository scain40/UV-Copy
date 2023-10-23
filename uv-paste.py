bl_info = {
    "name": "Paste All UV",
    "blender": (2, 80, 0),
    "category": "UV",
}

import bpy
import bmesh

class PasteUV(bpy.types.Operator):
    bl_idname = "uv.paste_all_uv"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Paste All UV"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # Enable undo for the operator.

    def execute(self, context):        # execute() is called when running the operator.  
        bpy.ops.uv.select_box(pinned=False, xmin=0, xmax=1920, ymin=0, ymax=1080, wait_for_input=False, mode='SET')
        bpy.ops.uv.paste()
        return {'FINISHED'}            # Lets Blender know the operator finished successfully.

def menu_func(self, context):
    self.layout.operator(CopyUV.bl_idname)

def register():
    bpy.utils.register_class(CopyUV)
    bpy.types.VIEW3D_MT_object.append(menu_func)  # Adds the new operator to an existing menu.

def unregister():
    bpy.utils.unregister_class(CopyUV)


# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()