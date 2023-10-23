bl_info = {
    "name": "Copy Paste Shortcuts",
    "blender": (3, 5, 0),
    "category": "UV",
}

import bpy

class CopyUV(bpy.types.Operator):
    bl_idname = "uv.custom_copy_uv"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Custom Copy UV"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Finding a correct area type for the operator
        area_type = 'IMAGE_EDITOR'
        areas  = [area for area in bpy.context.window.screen.areas if area.type == area_type]

        if len(areas) <= 0:
            raise Exception(f"Make sure an Area of type {area_type} is open or visible in your screen!")

        # Setting the override context
        with bpy.context.temp_override(
            window=bpy.context.window,
            area=areas[0],
            region=[region for region in areas[0].regions if region.type == 'WINDOW'][0],
            screen=bpy.context.window.screen
        ):
            bpy.ops.uv.select_box(pinned=False, xmin=0, xmax=1920, ymin=0, ymax=1080, wait_for_input=False, mode='SET')
            bpy.ops.uv.copy()
        return {'FINISHED'}

class PasteUV(bpy.types.Operator):
    bl_idname = "uv.custom_paste_uv"        # Unique identifier for buttons and menu items to reference.
    bl_label = "Custom Paste UV"         # Display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}

    def execute(self, context):
        # Finding a correct area type for the operator
        area_type = 'IMAGE_EDITOR'
        areas  = [area for area in bpy.context.window.screen.areas if area.type == area_type]

        if len(areas) <= 0:
            raise Exception(f"Make sure an Area of type {area_type} is open or visible in your screen!")

        # Setting the override context
        with bpy.context.temp_override(
            window=bpy.context.window,
            area=areas[0],
            region=[region for region in areas[0].regions if region.type == 'WINDOW'][0],
            screen=bpy.context.window.screen
        ):
            bpy.ops.uv.select_box(pinned=False, xmin=0, xmax=1920, ymin=0, ymax=1080, wait_for_input=False, mode='SET')
            bpy.ops.uv.paste()

        return {'FINISHED'}


def copy_func(self, context):
    self.layout.operator(CopyUV.bl_idname)

def paste_func(self, context):
    self.layout.operator(PasteUV.bl_idname)

def register():
    bpy.utils.register_class(CopyUV)
    bpy.utils.register_class(PasteUV)
    # Adding operators to the existing menu
    bpy.types.VIEW3D_MT_object.append(copy_func)
    bpy.types.VIEW3D_MT_object.append(paste_func)

def unregister():
    bpy.utils.unregister_class(CopyUV)
    bpy.utils.unregister_class(PasteUV)

# This allows you to run the script directly from Blender's Text editor
# to test the add-on without having to install it.
if __name__ == "__main__":
    register()