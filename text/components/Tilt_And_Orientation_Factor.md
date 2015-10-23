## Tilt_And_Orientation_Factor [![IMAGE](images/icons/Tilt_And_Orientation_Factor.png)]

![IMAGE](images/components/Tilt_And_Orientation_Factor.png)

This component calculates the Tilt and Orientation Factor (TOF) for PV modules/Solar hot watter collectors.

#### Inputs
* _PVsurface <Required>: - Input planar Surface (not a polysurface) on which the PV modules will be applied. If you have a polysurface, explode it (using "Deconstruct Brep" component) and then feed its Faces(F) output to _PVsurface. Surface normal should be faced towards the sun.
* _epwFile <Required>: Input .epw file path by using grasshopper's "File Path" component.
* PVsurfaceTiltAngle_ <Optional>: The angle from horizontal of the inclination of the PVsurface. Example: 0 = horizontal, 90 = vertical. (range 0-180)
* PVsurfaceAzimuthAngle_ <Optional>: The orientation angle (clockwise from the true north) of the PVsurface normal vector. (range 0-360)
* annualShading_ <Optional>: Losses due to buildings, structures, trees, mountains or other objects that prevent solar radiation from reaching the PV module/Solar hot water collector.
* north_ <Optional>: Input a vector to be used as a true North direction, or a number between 0 and 360 that represents the clockwise degrees off from the Y-axis.
* albedo_ <Optional>: Average reflection coefficient of the area surrounding the PV surface. It ranges from 0 for very dark to 1 for bright white or metallic surface. Here are some specific values:
* ______________________ <Default>: Script variable PhotovoltaicsSurface
* precision_ <Optional>: Represents the square root number of analysis field for the output "geometry" mesh. Ranges from 1-100.
* scale_ <Optional>: Scale of the overall geometry.
* origin_ <Optional>: Origin for the final "geometry" output.
* legendPar_ <Optional>: Optional legend parameters from the Ladybug "Legend Parameters" component.
* ______________________ <Default>: Script input ______________________.
* bakeIt_ <Optional>: Set to "True" to bake the Tilt and orientation factor results into the Rhino scene.
* _runIt <Required>: ...

#### Outputs
* readMe!: ...
* ____________________________: Script variable PhotovoltaicsSurface
* TOF: Tilt and Orientation Factor - solar radiation at the actual tilt and azimuth divided by the solar radiation at the optimum tilt and azimuth.
* TSRF: Total Solar Resource Fraction - the ratio of solar radiation available accounting for both annual shading and TOF, compared to the solar radiation available at a given location at the optimum tilt and azimuth and with no shading.
* PVsurfaceTilt: Tilt angle of the inputted PVsurface.
* PVsurfaceAzimuth: Orientation angle of the inputted PVsurface.
* optimalTilt: Optimal tilt of the PVsurface for a given location. Optimal tilt being the one that receives the most annual solar radiation.
* optimalAzimuth: Optimal orientation of the PVsurface for a given location. Optimal azimuth being the one that receives the most annual solar radiation.
* optimalRoofPitch: Optimal steepness of the PVsurface for a given location. Optimal steepness being the one that receives the most annual solar radiation.
* optimalRadiation: Total solar radiation per square meter for a whole year received on a PVsurface of optimal tilt and azimuth, at given location.
* ____________________________: Script variable PhotovoltaicsSurface
* geometry: Geometry of the whole TOF mesh chart.
* originPt: The origin point of the "geometry" output.
* analysisPt: A point indicating inputted PVsurface's Tilt/Azimuth position on the solar radiation table.
* legend: A legend for the annual total solar radiation (in kWh/m2). Connect this output to a Grasshopper's "Geo" parameter in order to preview the legend separately in the Rhino scene.  
* legendBasePt: Legend base point, which can be used to move the "legend" geometry with grasshopper's "Move" component.


[Check Hydra Example Files for Tilt_And_Orientation_Factor](https://hydrashare.github.io/hydra/index.html?keywords=Tilt_And_Orientation_Factor)