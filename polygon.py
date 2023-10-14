import arcpy
import os

gdb_path = r"D:\SEM_III\Programming_3\p7_working_with_geometry\Practical_7_ProProject\07_Working_with_Geometry_Objects.gdb"
Output_fc_name = "Pune_Nashik_Ahemadnagar"
Output_fc_path = os.path.join(gdb_path,Output_fc_name)

x_pune = 73.84613708248342
y_pune = 18.520175562604294

x_chakan =73.85933954976838
y_chakan =18.756245401004094

x_sangamner =74.20799732463209
y_sangamner = 19.566631485430126

x_nashik = 73.79643390932937
y_nashik = 20.006160390279028

x_ang = 74.73549780752666
y_ang = 19.121971237541523

point_obj_pune = arcpy.Point(x_pune,y_pune)
point_obj_chakan = arcpy.Point(x_chakan,y_chakan)
point_obj_sangamner = arcpy.Point(x_sangamner,y_sangamner)
point_obj_nashik = arcpy.Point(x_nashik,y_nashik)
point_obj_ang = arcpy.Point(x_ang,y_ang)


spatial_ref = arcpy.SpatialReference("WGS 1984")

polygon_array = arcpy.Array()

polygon_array.add(point_obj_pune)
polygon_array.add(point_obj_chakan)
polygon_array.add(point_obj_sangamner)
polygon_array.add(point_obj_nashik)
polygon_array.add(point_obj_ang)

polygon_geom = arcpy.Polygon(polygon_array,spatial_ref)

arcpy.CopyFeatures_management(polygon_geom, Output_fc_path)

print("Process Complete")