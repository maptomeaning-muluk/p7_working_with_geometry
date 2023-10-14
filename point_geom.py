import arcpy
import os

x_pune = 73.84613708248342
y_pune = 18.520175562604294

point_obj = arcpy.Point(x_pune,y_pune)

spatial_ref = arcpy.SpatialReference("WGS 1984")

point_geom = arcpy.PointGeometry(point_obj,spatial_ref)

gdb_path = r"D:\SEM_III\Programming_3\p7_working_with_geometry\Practical_7_ProProject\07_Working_with_Geometry_Objects.gdb"
fc_name =   "Samphaji_Udyan_Bus_Stop_Pune"
fc_path = os.path.join(gdb_path,fc_name)

arcpy.CopyFeatures_management(point_geom,fc_path)

print("process complete")