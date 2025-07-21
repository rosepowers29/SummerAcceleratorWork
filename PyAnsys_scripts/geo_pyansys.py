import numpy as np
from ansys.geometry.core.math import Plane, Point2D, Point3D, Vector2D, Vector3D, UnitVector3D
from ansys.geometry.core.misc import UNITS as units
from ansys.geometry.core.misc import DEFAULT_UNITS as default_units
from pint import Quantity
from ansys.geometry.core.misc import Angle, Distance
from ansys.geometry.core.sketch import Sketch



#creating 2D and 3D points and vectors
#-------------------------------------
origin = Point3D([0,0,0])
unit_x = Vector3D([1,0,0])
unit_y = Vector3D([0,1,0])
unit_z = Vector3D([0,0,1])
#just a basic Cartesian coordinate system
#vector operations: sum (+), dot (*), cross (%)

#creating a vector from points
#-------------------------------------
p1 = origin
p2 = Point3D([4,8,0]) #random point on the xy plane
xyvec1 = Vector3D.from_points(p1, p2)

#two ways of turning a vector to a unit vector
#--------------------------------------
# one is to use the normalize command:
xyvec1_norm = xyvec1.normalize()
# the other is to use the UnitVector class when creating
# the vector in the first place:
xyvec2 = UnitVector3D([4,8,0])

#booleans to check if vecs are perpendicular, parallel, 
#opposite, etc
#-----------------------------------
perp_bool = unit_x.is_perpendicular_to(unit_y) #true
par_bool = unit_x.is_parallel_to(unit_y) #false
opp_bool = unit_x.is_opposite(unit_y) #false
#find the angle between two vectors
xy_angle = unit_x.get_angle_between(unit_y) #pi/2

#---------------------------------------------

#CREATING PLANES

#----------------------------------------------
#define with an origin and xy axes
#let's define the three basic Cartesian planes
xyplane = Plane(origin, unit_x, unit_y)
yzplane = Plane(origin, unit_y, unit_z)
zxplane = Plane(origin, unit_z, unit_x)
#can use a boolean to see if a point is in the plane
# useful for checking geometry constraints
testpoint = Point3D([4,8,0])
xy_bool = xyplane.is_point_contained(testpoint) #true
yz_bool = yzplane.is_point_contained(testpoint) #false

#Quantity objects
# class with two elements: number and unit
#------------------------------------------
#example just use length and width
length = Quantity(10, units.mm)
width = 1.2 * units.mm # an alternate construction method 
#we can also put units into a Point object
#for instance, we could make the endpoint of our height at
top = Point3D([0,10,0], unit=units.mm)
#we can also set default units (as we would in the DM gui, e.g.)
default_units.LENGTH = units.mm
# we also have distance and angle objects
# likely can be used like the dimensions in DM
# distance is like quantity, except there is an
# "active check" on the units, i.e. if we try to pass
# a non-length unit to a distance like degrees or Newtons it will throw
# an error. Same for a non-angle unit to the Angle object
#--------------------------------------------------
