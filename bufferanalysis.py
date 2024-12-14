import arcpy
import arcpy.mapping
arcpy.env.workspace=r"C:\Users\Orpa\PycharmProjects\pythonProject1\input"
arcpy.env.overwriteOutput=True
shape_data=arcpy.ListFeatureClasses()

print (shape_data)
point_data=r"C:\Users\Orpa\PycharmProjects\pythonProject1\input\Shahid Mineer.shp"

buffer_distance="100 Meters"

buffer_output=r"C:\Users\Orpa\PycharmProjects\pythonProject1\output\Point_Buffer1.shp"

arcpy.Buffer_analysis(point_data,buffer_output,buffer_distance,dissolve_option='All')

pdf_output=r'C:\Users\Orpa\PycharmProjects\pythonProject1\buffermapoutput\pointmap.pdf'

mxd_path=r'C:\Users\Orpa\PycharmProjects\pythonProject1\map\blankmap.mxd'

mxd=arcpy.mapping.MapDocument(mxd_path)

df=arcpy.mapping.ListDataFrames(mxd)[0]
point_layer=arcpy.mapping.Layer(buffer_output)

arcpy.mapping.AddLayer(df,point_layer,add_position='TOP')

arcpy.mapping.ExportToPDF(mxd,pdf_output)


