import bpy, math

angle = math.radians(137.5)
for i in range (400):
    r = math.sqrt(i)
    x = r * math.cos(i * angle)
    y = r * math.sin(i * angle)
    bpy.ops.mesh.primitive_ico_sphere_add(radius=1, enter_editmode=False, align='WORLD', location=(x, y, 0), scale=(1, 1, 1))