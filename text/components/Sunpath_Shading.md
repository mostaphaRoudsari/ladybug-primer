## ![](../../images/icons/Sunpath Shading.png) Sunpath_Shading

![](../../images/components/Sunpath_Shading.png)

This component calculates the amount of annual shading of sun window due to location's surroundings. Sun (or solar) window being an area of the the sky dome between winter and summer solstice sun paths. Obstruction from buildings, structures, trees, mountains or other objects are considered. It can be used to calculate annual shading for Photovoltaic arrays, Solar hot water collectors or any other purpose. - Use "annualShading" or "beamIndexPerHour" output for Photovoltaic arrays and "beamIndexPerHour" output for Solar hot water collectors shading analysis. - Based on "Using sun path charts to estimate the effects of shading on PV arrays", University of Oregon, Frank Vignola: http://solardat.uoregon.edu/download/Papers/UsingSunPathChartstoEstimatetheEffectofShadingonPVArrays.pdf - 

#### Inputs
* ##### PVsurface [Required]
Input planar Surface (not polysurface) on which the PV modules/Solar hot water collectors will be applied. If you have a polysurface, explode it (using "Deconstruct Brep" component) and then feed its Faces(F) output to _PVsurface. Surface normal should be faced towards the sun. Number inputs (example: "100") and kiloWatt (example: "4 kw"). are not supported.
* ##### epwFile [Required]
Input .epw file path by using grasshopper's "File Path" component.
* ##### ACenergyPerHour [Optional]
Input the "ACenergyPerHour" output data from "Photovoltaics surface" component. If you are calculating shading analysis for "Solar hot water surface" component (instead of "Photovoltaics surface" component), leave this input empty. In kWh. If you are calculating shading analysis for any other purpose, input annual solar radiation per hour data.
* ##### context [Optional]
Buildings, structures, mountains and other permanent obstructions. Input polysurfaces, surfaces, or meshes.
* ##### coniferousTrees [Optional]
This input allows for partial shading from coniferous(evergreen) context trees. Input polysurfaces, surfaces, or meshes.
* ##### deciduousTrees [Optional]
This input allows for partial shading during in-leaf and leaf-less periods from deciduous context trees. In-leaf being a period from 21st March to 21st September in the northern hemisphere, and from 21st September to 21st March in the southern hemisphere. Leaf-less being a period from 21st September to 21st March in the northern hemisphere, and from 21st March to 21st September in the in the southern hemisphere. Input polysurfaces, surfaces, or meshes.
* ##### coniferousAllyearIndex [Optional]
All year round transmission index for coniferous(evergreen) context trees. It ranges from 0 to 1.0. 0 represents deciduous trees which do not allow solar radiation to pass through them (100% shading). 1 represents all solar radiation passing through deciduous trees, like the trees do not exist (0% shading). - If not supplied default value of 0.30 (equals 70% shading) will be used.
* ##### deciduousInleafIndex [Optional]
Deciduous context trees transmission index for in-leaf period. In-leaf being a period from 21st March to 21st September in the northern hemisphere, and from 21st September to 21st March in the southern hemisphere. It ranges from 0 to 1.0. 0 represents deciduous trees which do not allow solar radiation to pass through them (100% shading). 1 represents all solar radiation passing through deciduous trees, like the trees do not exist (0% shading). - If not supplied default value of 0.23 (equals 77% shading) will be used.
* ##### deciduousLeaflessIndex [Optional]
Deciduous context trees transmission index for leaf-less period. Leaf-less being a period from 21st September to 21st March in the northern hemisphere, and from 21st March to 21st September in the in the southern hemisphere. It ranges from 0 to 1.0. 0 represents deciduous trees which do not allow solar radiation to pass through them (100% shading). 1 represents all solar radiation passing through deciduous trees, like the trees do not exist (0% shading). - If not supplied default value of 0.64 (equals 36% shading) will be used.
* ##### leaflessPeriod [Optional]
Define the leafless period for deciduous trees using Ladybug's "Analysis Period" component. IMPORTANT! This input affects only the "beamIndexPerHour" output. Due to limitations of the used sunpath diagram, it does not affect all the other shading outputs, where default leafless periods (see the line bellow) will always be used. - If not supplied the following default periods will be used: from 21st September to 21st March in the northern hemisphere, and from 21st March to 21st September in the in the southern hemisphere.
* ##### north [Optional]
Input a vector to be used as a true North direction, or a number between 0 and 360 that represents the clockwise degrees off from the Y-axis. - If not supplied, default North direction will be set to the Y-axis (0 degrees).
* ##### scale [Optional]
Scale of the overall geometry (sunPath curves, sunWindow mesh). Use the scale number which enables encompassing all of your context_, coniferousTrees_, deciduousTrees_ objects. - If not supplied, default value of 1 will be used.
* ##### hoursPositionScale [Optional]
Scale factor for positioning of solar time hour points (that's "hoursPositions" output). - If not supplied, default value of 1 will be used.
* ##### precision [Optional]
Overall shading precision. Ranges from 1-100. It represents the square root number of shading analysis points per sun window quadrant. Example - precision of 20 would be 400 shading analysis points per single sun window quadrant. CAUTION!!! Higher precision numbers (50 >) require stronger performance PCs. If your "_context" contains only straight shape buildings/objects, and you have just a couple of trees supplied to the "coniferousTrees_" and "deciduousTrees_" inputs, the precision of < 50 will be just fine. - If not supplied, default value of 2 will be used.
* ##### legendPar [Optional]
Optional legend parameters from the Ladybug "Legend Parameters" component.
* ##### bakeIt [Optional]
Set to "True" to bake the Sunpath shading results into the Rhino scene. - If not supplied default value "False" will be used.
* ##### runIt [Required]
...

#### Outputs
* ##### readMe!
...
* ##### beamIndexPerHour
Transmission index of beam (direct) irradiance for each hour during a year. Transmission index of 0 means 100% shading. Transmission index of 1 means 0% shading. It is calculated for each PVsurface vertex and then averaged. It ranges from 0-1. Unitless.
* ##### sunWindowShadedAreaPer
Percent of the overall sun window shaded area. It is calculated for PVsurface area centroid. It ranges from 0-100(%). In percent(%).
* ##### unweightedAnnualShading
Annual unweighted shading of the active sun window quadrants. Active sun window quadrants are only those which produce AC energy (or solar radiation in case you are using this component for other purposes than Photovoltaics) Unweighted means that each active sun window quadrant produces the same percentage of AC power. It is calculated for each PVsurface vertex and then averaged. It ranges from 0-100(%). In percent(%).
* ##### Sep21toMar21Shading
Weighted shading of the active sun window quadrants, for period between 21st September to 21st March. Active sun window quadrants are only those which produce AC energy (or solar radiation in case you are using this component for other purposes than Photovoltaics) It is calculated for each PVsurface vertex and then averaged. It ranges from 0-100(%). In percent(%).
* ##### Mar21toSep21Shading
Weighted shading of the active sun window quadrants, for period between 21st March to 21st September. Active sun window quadrants are only those which produce AC energy (or solar radiation in case you are using this component for other purposes than Photovoltaics) It is calculated for each PVsurface vertex and then averaged. It ranges from 0-100(%). In percent(%).
* ##### annualShading
Annual weighted shading of the active sun window quadrants. To calculate it, input data to "ACenergyPerHour_" input. Active sun window quadrants are only those which produce AC energy (or solar radiation in case you are using this component for other purposes than Photovoltaics) It is calculated for each PVsurface vertex and then averaged. It ranges from 0-100(%). In percent(%).
* ##### annalysisPts
Each vertex of the inputted _PVsurface for which a separate shading analysis was conducted.
* ##### sunWindowCenPt
The center point of the "sunWindowCrvs" and "sunWindowMesh" geometry. It is calculated for PVsurface area centroid. Use this point to move "sunWindowCrvs" and "sunWindowMesh" geometry around in the Rhino scene with the grasshopper's "Move" component.
* ##### sunWindowCrvs
Geometry of the sun window based on 3D polar sun path diagram. Perpendical curves represent solar time hours. Horizontal arc curves represent sun paths for: 21st December, 21st November/January, 21st October/February, 21st September/March, 21st August/April, 21st July/May, 21st June. The whole sunWindowCrvs geometry output is calculated for PVsurface area centroid. Connect this output to a Grasshopper's "Geo" parameter in order to preview the "sunWindowCrvs" geometry separately in the Rhino scene.
* ##### sunWindowMesh
Sun window mesh based on 3D polar sun path diagram. It is calculated for PVsurface area centroid. Black areas represent 100% shaded portions of the sun window (of both active and inactive quadrants). Darker green and green areas represent partially shaded portions from the coniferous and deciduous trees, respectively. Connect this output to a Grasshopper's "Mesh" parameter in order to preview the "sunWindowMesh" geometry separately in the Rhino scene.
* ##### legend
A legend of the sunWindowMesh. Connect this output to a Grasshopper's "Geo" parameter in order to preview the legend separately in the Rhino scene.  
* ##### legendBasePt
Legend base point, which can be used to move the "legend" geometry with grasshopper's "Move" component.
* ##### quadrantCentroids
Centroid for each sun window active quadrant above the horizon. Use grasshopper's "Text tag" component to visualize them.
* ##### quadrantShadingPercents
Shadinging percent per each sun window active quadrant above the horizon. Active quadrants with less than 0.01% are neglected. Use grasshopper's "Text tag" component to visualize them.
* ##### quadrantACenergyPercents
AC energy percent per each sun window active quadrant above the horizon. Use grasshopper's "Text tag" component to visualize them.
* ##### hoursPositions
Solar time hour point positions. Use grasshopper's "Text tag" component to visualize them.
* ##### hours
Solar time hour strings. Use grasshopper's "Text tag" component to visualize them.


[Check Hydra Example Files for Sunpath Shading](https://hydrashare.github.io/hydra/index.html?keywords=Ladybug_Sunpath Shading)