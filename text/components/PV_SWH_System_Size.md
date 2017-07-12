## ![](../../images/icons/PV_SWH_System_Size.png) PV SWH System Size

![](../../images/components/PV_SWH_System_Size.png)

Use this component to generate the PVsurface or SWHsurface for "Photovoltaics surface" or "Solar Water Heating surface" components, based on initial PV or SWH system sizes.

#### Inputs
* ##### location [Required]
The output from the "importEPW" or "constructLocation" component.  This is essentially a list of text summarizing a location on the earth.
* ##### PVmoduleSettings [Required]
A list of PV module settings. Use the "Photovoltaics Module" component to generate them.
* ##### SWHsystemSettings [Required]
A list of all SWH system settings. Use the "Solar Water Heating System" or "Solar Water Heating System Detailed" components to generate them.
* ##### systemSize [Optional]
1) In case of PV array: DC (Direct current) power rating of the photovoltaic array in kilowatts (kW) at standard test conditions (STC). 
* ##### arrayTiltAngle [Optional]
An angle from horizontal of the inclination of the PV/SWH array plane. Example: 0 = horizontal, 90 = vertical. (range 0-180)
* ##### arrayAzimuthAngle [Optional]
The orientation angle (clockwise from the true north) of the PV/SWH array plane's normal vector. (range 0-360)
* ##### tiltedArrayHeight [Optional]
The height of the array, measured in the tilted plane.
* ##### numberOfRows [Optional]
Number of rows to which PV or SWH array will be divided to.
* ##### skewRowsDistance [Optional]
Distance in meters by which PV/SWH rows will be skewed.
* ##### minimalSpacingPeriod [Optional]
Analysis period for which the minimal spacing distance between PV modules/SWH collector rows will derived of.
* ##### baseSurface [Optional]
Surface on which PV/SWH array will be laid onto.
* ##### arrayOriginPt [Optional]
UV coordinate of baseSurface_ at which PV_SWH array will start.
* ##### arrayOriginCorner [Optional]
Corner at which the PV/SWH array begins:
* ##### north [Optional]
Input a vector to be used as a true North direction, or a number between 0 and 360 that represents the clockwise degrees off from the Y-axis.
* ##### energyLoadPerHour [Optional]
A list of energy load values for each hour, during a year.

#### Outputs
* ##### readMe!
...
* ##### PV_SWHsurface
Surfaces on which PV modules/SWH collectors will be laid on.
* ##### PV_SWHsurfacesArea
Total area of the PV_SWHsurfaces.
* ##### minimalSpacing
Minimal distance between fixed (anchor) points of rows.
* ##### minimalSpacingDate
Exact date taken from "minimalSpacingPeriod_" input for which minimal spacing between rows has been calculated.
* ##### arrayOriginPt
Origin point of the PV / SWH array.
* ##### energyLoadPerRowPerHour
"energyLoadPerHour_" input's data divided to rows.


[Check Hydra Example Files for PV SWH System Size](https://hydrashare.github.io/hydra/index.html?keywords=Ladybug_PV SWH System Size)