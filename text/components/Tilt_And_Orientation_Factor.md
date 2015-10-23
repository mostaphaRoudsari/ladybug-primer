## ![](../../images/icons/Tilt And Orientation Factor.png) Tilt_And_Orientation_Factor

![](../../images/components/Tilt_And_Orientation_Factor.png)

This component calculates the Tilt and Orientation Factor (TOF) for PV modules/Solar hot watter collectors. TOF is a solar radiation at the actual tilt and orientation divided by the solar radiation at the optimum tilt and orientation, expressed in percent.  - 

#### Inputs
* ##### _PVsurface [Required]
- Input planar Surface (not a polysurface) on which the PV modules will be applied. If you have a polysurface, explode it (using "Deconstruct Brep" component) and then feed its Faces(F) output to _PVsurface. Surface normal should be faced towards the sun. - Or input surface Area, in square meters (example: "100").
* ##### _epwFile [Required]
Input .epw file path by using grasshopper's "File Path" component.
* ##### PVsurfaceTiltAngle_ [Optional]
The angle from horizontal of the inclination of the PVsurface. Example: 0 = horizontal, 90 = vertical. (range 0-180) - If not supplied, but surface inputted into "_PVsurface", PVsurfaceTiltAngle will be calculated from an angle PVsurface closes with XY plane. If not supplied, but surface NOT inputted into "_PVsurface" (instead, a surface area inputed), location's latitude will be used as default value.
* ##### PVsurfaceAzimuthAngle_ [Optional]
The orientation angle (clockwise from the true north) of the PVsurface normal vector. (range 0-360) - If not supplied, but surface inputted into "_PVsurface", PVsurfaceAzimuthAngle will be calculated from an angle PVsurface closes with its north. If not supplied, but surface NOT inputted into "_PVsurface" (instead, a surface area inputed), default value of 180° (south-facing) for locations in the northern hemisphere or 0° (north-facing) for locations in the southern hemisphere, will be used.
* ##### annualShading_ [Optional]
Losses due to buildings, structures, trees, mountains or other objects that prevent solar radiation from reaching the PV module/Solar hot water collector. Input range: 0 to 100(%), 0 being unshaded, and 100 being totally shaded PV module/SHW collector. - If not supplied default value of 0(%) will be used.
* ##### north_ [Optional]
Input a vector to be used as a true North direction, or a number between 0 and 360 that represents the clockwise degrees off from the Y-axis. - If not supplied, default North direction will be set to the Y-axis (0 degrees).
* ##### albedo_ [Optional]
Average reflection coefficient of the area surrounding the PV surface. It ranges from 0 for very dark to 1 for bright white or metallic surface. Here are some specific values: - Dry asphalt  0.12 Wet Asphalt  0.18 Bare soil  0.17 Grass  0.20 Concrete  0.30 Granite  0.32 Dry sand  0.35 Copper  0.74 Wet snow  0.65 Fresh snow  0.82 Aluminum  0.85 - If not supplied default value of 0.20 (Grass) will be used.
* ##### precision_ [Optional]
Represents the square root number of analysis field for the output "geometry" mesh. Ranges from 1-100. Example - precision of 4, would mean that 4 fields in X direction (Azimuth) and 4 fields in Y direction (Tilt) = 16 fields, will be used to calculate the final "geometry" mesh. For lower precision numbers (say < 20) even precision numbers are more accurate. - CAUTION!!! Precision numbers (10 >) require stronger performance PCs. If your PC is somewhat "weaker", the precision of < 10 will be just fine. - If not supplied, default value of 2 will be used.
* ##### scale_ [Optional]
Scale of the overall geometry. - If not supplied, default value of 1 will be used.
* ##### origin_ [Optional]
Origin for the final "geometry" output. - If not supplied, default point of (-15,0,0) will be used.
* ##### legendPar_ [Optional]
Optional legend parameters from the Ladybug "Legend Parameters" component.
* ##### bakeIt_ [Optional]
Set to "True" to bake the Tilt and orientation factor results into the Rhino scene. - If not supplied default value "False" will be used.
* ##### _runIt [Required]
...

#### Outputs
* ##### readMe!
...
* ##### TOF
Tilt and Orientation Factor - solar radiation at the actual tilt and azimuth divided by the solar radiation at the optimum tilt and azimuth. In percent(%).
* ##### TSRF
Total Solar Resource Fraction - the ratio of solar radiation available accounting for both annual shading and TOF, compared to the solar radiation available at a given location at the optimum tilt and azimuth and with no shading. Calculated according to the following equation: TSRF = TOF * (100-annualShading)/100 Some USA states, like Oregon and Washington require TSRF to be minimum 75% in order for the PV system to be applicable for incentive programs. - In percent(%).
* ##### PVsurfaceTilt
Tilt angle of the inputted PVsurface. In degrees (°).
* ##### PVsurfaceAzimuth
Orientation angle of the inputted PVsurface. In degrees (°).
* ##### optimalTilt
Optimal tilt of the PVsurface for a given location. Optimal tilt being the one that receives the most annual solar radiation. In degrees (°).
* ##### optimalAzimuth
Optimal orientation of the PVsurface for a given location. Optimal azimuth being the one that receives the most annual solar radiation. In degrees (°).
* ##### optimalRoofPitch
Optimal steepness of the PVsurface for a given location. Optimal steepness being the one that receives the most annual solar radiation. In inches/inches
* ##### optimalRadiation
Total solar radiation per square meter for a whole year received on a PVsurface of optimal tilt and azimuth, at given location. In kWh/m2
* ##### geometry
Geometry of the whole TOF mesh chart. Connect this output to a Grasshopper's "Geo" parameter in order to preview the "geometry" separately in the Rhino scene.
* ##### originPt
The origin point of the "geometry" output. Use this point to move "geometry" output around in the Rhino scene with the grasshopper's "Move" component.
* ##### analysisPt
A point indicating inputted PVsurface's Tilt/Azimuth position on the solar radiation table.
* ##### legend
A legend for the annual total solar radiation (in kWh/m2). Connect this output to a Grasshopper's "Geo" parameter in order to preview the legend separately in the Rhino scene.  
* ##### legendBasePt
Legend base point, which can be used to move the "legend" geometry with grasshopper's "Move" component.


[Check Hydra Example Files for Tilt And Orientation Factor](https://hydrashare.github.io/hydra/index.html?keywords=Ladybug_Tilt And Orientation Factor)