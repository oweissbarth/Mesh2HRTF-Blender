import bpy
import bmesh
from math import sqrt

class ModelCheckOperator(bpy.types.Operator):
    bl_idname = "object.modelcheck"
    bl_label = "ModelCheck"

    def execute(self, context):
        check_model(bpy.context.active_object)
        return {'FINISHED'}



def check_model(obj):
    #bm = bmesh.new()
    #bm.from_mesh(obj.data)
    bm = bmesh.from_edit_mesh(obj.data)
    dmesh_avg = 0.
    dmesh_eqi = 0.
    dmesh_max = 0
    dmesh_min = 1.0E20

    for f in bm.faces:
        numberOfVerts = len(f.verts)
        f.select_set(False)

        if numberOfVerts != 3 and numberOfVerts != 4:
            print("Face %d is not a quad or triangle" % f.index)
            f.select_set(True)

        dis_ref = sqrt(f.calc_area())

        if numberOfVerts == 3:
            dis_ref *= 1.51967

        for j in range(numberOfVerts):
            k = (j+1)%numberOfVerts

            dist = (f.verts[j].co - f.verts[k].co).length
            dmesh_max = max(dist, dmesh_max)
            dmesh_min = min(dist, dmesh_min)

            dmesh_avg += dist

            if numberOfVerts == 3:
                dmesh_eqi += dist * 0.748
            else:
                dmesh_eqi += dist

            if dist > dis_ref * 10.0 and dist < dis_ref * 100:
                print("Long edge on face %d found"% f.index)

            if dist > dis_ref*100:
                print("Element of very distorted form is found in face %d" % f.index)
                f.select_set(True)



    bmesh.update_edit_mesh(obj.data)

    #bm.to_mesh(obj.data)
    #bm.free()
