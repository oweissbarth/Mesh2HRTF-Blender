#                                Mesh2HRTF
#                Copyright (C) 2015 by Harald Ziegelwanger,
#        Acoustics Research Institute, Austrian Academy of Sciences
#                        mesh2hrtf.sourceforge.net
#
# Mesh2HRTF is licensed under the GNU Lesser General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
# Mesh2HRTF is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details.
# You should have received a copy of the GNU LesserGeneral Public License along with Mesh2HRTF. If not, see <http://www.gnu.org/licenses/lgpl.html>.
#
# If you use Mesh2HRTF:
# - Provide credits:
#   "Mesh2HRTF, H. Ziegelwanger, ARI, OEAW (mesh2hrtf.sourceforge.net)"
# - In your publication, cite both articles:
#   [1] Ziegelwanger, H., Kreuzer, W., and Majdak, P. (2015). "Mesh2HRTF: Open-source software package for the numerical calculation of head-related transfer functions," in Proceedings of the 22nd ICSV, Florence, IT.
#   [2] Ziegelwanger, H., Majdak, P., and Kreuzer, W. (2015). "Numerical calculation of listener-specific head-related transfer functions and sound localization: Microphone model and mesh discretization," The Journal of the Acoustical Society of America, 138, 208-222.


bl_info = {
    "name" : "Mesh2HRTF",
    "author" : "Harald Ziegelwanger, Robert Pelzer, Oliver Weissbarth",
    "description" : "",
    "blender" : (2, 80, 0),
    "version" : (0, 1, 4),
    "location" : "",
    "warning" : "",
    "category" : "Import-Export"
}

from .ExportEvaluationGrid import ExportEvaluationGrid
from .ExportMesh2HRTF import ExportMesh2HRTF
from .MaterialAssignment import MaterialAssignment
from .ModelCheck import ModelCheckOperator

classes = (
    ExportEvaluationGrid,
    ExportMesh2HRTF,
    MaterialAssignment,
    ModelCheckOperator
)

def register():
    from bpy.utils import register_class
    import bpy.types
    for cls in classes:
        register_class(cls)
    
    bpy.types.TOPBAR_MT_file_export.append(menu_func_export)

def unregister():
    import bpy.types
    from bpy.utils import unregister_class
    bpy.types.TOPBAR_MT_file_export.remove(menu_func_export)
    for cls in reversed(classes):
        unregister_class(cls)




def menu_func_export(self, context):
    self.layout.operator(ExportMesh2HRTF.bl_idname, text="Mesh2HRTF")