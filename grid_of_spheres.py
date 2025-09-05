import bpy

for i in range(-10,10):
    for j in range (-10,10):
        bpy.ops.mesh.primitive_uv_sphere_add(radius=1, enter_editmode=False, align='WORLD', location=(i * 2, j * 2, 0), scale=(1, 1, 1))