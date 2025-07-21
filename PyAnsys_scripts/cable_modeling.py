import numpy as np
from ansys.geometry.core.math import Plane, Point2D, Point3D, Vector2D, Vector3D, UnitVector3D
from ansys.geometry.core.misc import UNITS as units
from ansys.geometry.core.misc import DEFAULT_UNITS as default_units
from pint import Quantity
from ansys.geometry.core.misc import Angle, Distance
from ansys.geometry.core.sketch import Sketch
from ansys.geometry.core import launch_modeler
import os
from pathlib import Path
from ansys.geometry.core.designer import DesignFileFormat


#------------------------ set units ---------------------#
default_units.LENGTH = units.mm

#------------------------ parameters (make these accessible from cmd line later) ------------#
cable_depth = 1.2 #Distance(1.2, unit=units.mm)
cable_width = 10. #Distance(10, unit=units.mm)
cable_length = 20. #Distance(20, unit=units.mm)
cable_fillet = 0.6 #Distance(0.6, unit=units.mm)

#------------------------ create base sketch on xz plane ------------#
zxplane = Plane(origin = Point3D([0,0,0]), direction_x = Vector3D([0,0,1]), direction_y = Vector3D([1,0,0]))
cable_base = Sketch(zxplane)
#start with a rectangle (box)
#sketch.box(center = Point2D([5,0]), width = cable_depth, height = cable_width)
#construct filleted rectangle from segments and arcs
(
    cable_base.segment(Point2D([cable_fillet, 0]),Point2D([cable_width-2*cable_fillet,0]), tag="TapeEdge")
                   .arc_to_point(Point2D([cable_width-2*cable_fillet, -cable_depth]), Point2D([cable_width-2*cable_fillet, -cable_depth/2]), True, tag="TapeFillet")
                   .segment_to_point(Point2D([cable_fillet, -cable_depth]), tag="LowerEdge")
                   .arc_to_point(Point2D([cable_fillet,0]), Point2D([cable_fillet, -cable_depth/2]), False, tag="OppFillet")
)

#---------------------------- extrude and model --------------------------#
modeler = launch_modeler()
print(modeler)

design = modeler.create_design("RutherfordCable")
cable = design.extrude_sketch(name = "cable", sketch=cable_base, distance=cable_length)


#--------------------------- download design ================================#
file_dir = Path(os.getcwd(), "geo_downloads")
file_dir.mkdir(parents=True, exist_ok=True)
design.download(file_location= Path(file_dir, "bare_cable.scdocx"), format=DesignFileFormat.SCDOCX)
modeler.close()