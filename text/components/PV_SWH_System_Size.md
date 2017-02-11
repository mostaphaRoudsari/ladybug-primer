## ![](../../images/icons/PV_SWH_System_Size.png) PV SWH System Size

![](../../images/components/PV_SWH_System_Size.png)

Use this component to generate the PVsurface or SWHsurface for "Photovoltaics surface" or "Solar Water Heating surface" components, based on initial PV or SWH system sizes. - 

#### Inputs
* ##### location [Required]
The output from the "importEPW" or "constructLocation" component.  This is essentially a list of text summarizing a location on the earth.
* ##### PVmoduleSettings [Required]
A list of PV module settings. Use the "Photovoltaics Module" component to generate them.
* ##### SWHsystemSettings [Required]
A list of all SWH system settings. Use the "Solar Water Heating System" or "Solar Water Heating System Detailed" components to generate them.
* ##### systemSize [Optional]
1) In case of PV array: DC (Direct current) power rating of the photovoltaic array in kilowatts (kW) at standard test conditions (STC).  2) In case of SWH array: Capacity of the collectors array in thermal kilowatts (kw) at global or local testing conditions (ISO 9806, EN 12975, ASHRAE 93 ...) - If not supplied, 4 kW will be used as a default. - In kiloWatts (kW) or thermal kiloWatts (kWt).
* ##### arrayTiltAngle [Optional]
An angle from horizontal of the inclination of the PV/SWH array plane. Example: 0 = horizontal, 90 = vertical. (range 0-180) - To get the maximal amount of energy, input the "optimalTilt" output from "Tilt And Orientation Factor"'s component. - If not supplied, location's latitude will be used as default value. - In degrees (°).
* ##### arrayAzimuthAngle [Optional]
The orientation angle (clockwise from the true north) of the PV/SWH array plane's normal vector. (range 0-360) - To get the maximal amount of energy, input the "optimalAzimuth" output from "Tilt And Orientation Factor"'s component. - If not supplied, the following values will be used as default: 180 (due south) for northern hemisphere, 0 (due north) for southern hemisphere. - In degrees(°).
* ##### tiltedArrayHeight [Optional]
The height of the array, measured in the tilted plane. It is depends on the height/width of the PV module/SWH collector. It also depends on the way modules/collectors are positioned in PV/SWH array (vertically or horizontally). It can vary from 1 to 2.3 meters x number of modules/collectors in a single PV/SWH column. - If not supplied, default value of 1.6 meters (with a single PV module/SWH collector per row) will be used. - In meters.
* ##### numberOfRows [Optional]
Number of rows to which PV or SWH array will be divided to. - If not supplied, 1 will be used as a default value (PV/SWH array will have only 1 row).
* ##### skewRowsDistance [Optional]
Distance in meters by which PV/SWH rows will be skewed. Use positive distance to skew the rows to the left. And negative distance to skew the rows to the right. - It requires the "numberOfRows_" to be larger than 1 in order to be able to skew the rows. - If not supplied, 0 will be used as a default (no rows skewing).
* ##### minimalSpacingPeriod [Optional]
Analysis period for which the minimal spacing distance between PV modules/SWH collector rows will derived of. In general this analysis period is taken from 9 to 15 hour on a day at which sun is at its lowest position during a year. That is 21th December in Northern and 21th June in Southern hemisphere (winter and summer solstice). However, this may not be economical for locations with higher latitudes due to low electricity generation during December/June. - So the following "minimalSpacingPeriod_" should be used based on location's latitude: * latitude <= 44: 21. December (northern hemisphere) / 21. June (southern hemisphere). 9-15hours * latitude 44 - 53: 15. November or 15. January (northern hemisphere) / 15. May or 15. July (southern hemisphere). 9-15hours * latitude 53 - 57: 15. October or 15. February (northern hemisphere) / 15. April or 15. August (southern hemisphere). 9-15hours * latitude > 57: 15. September or 15. March (for both northern and southern hemisphere). 9-15hours - It requires the "numberOfRows_" to be larger than 1 in order visualize the minimal spacing between rows. - If not supplied, it will be calculated based on upper mentioned criteria.
* ##### baseSurface [Optional]
Surface on which PV/SWH array will be laid onto. This can be a surface of an angled or flat roof. Or an angled or flat terrain. A facade of a building etc. - If not supplied, a regular horizontal surface in Rhino's XY plane will be used, as a default.
* ##### arrayOriginPt [Optional]
UV coordinate of baseSurface_ at which PV_SWH array will start. It ranges from 0 to 1.0 for both U and V coordinate. Use grasshopper's "Construct Point" or "MD slider" components to input it. - If not supplied, (0.5,0,0) will be used as a default value.
* ##### arrayOriginCorner [Optional]
Corner at which the PV/SWH array begins: - 0 - center bottom 1 - left bottom 2 - right bottom 3 - center top - If not supplied, 0 will be used as a default (bottom center).
* ##### north [Optional]
Input a vector to be used as a true North direction, or a number between 0 and 360 that represents the clockwise degrees off from the Y-axis. - If not supplied, default North direction will be set to the Y-axis (0 degrees).
* ##### energyLoadPerHour [Optional]
A list of energy load values for each hour, during a year. 1) In case of PV array: Electrical energy used for any kind of load: heating, cooling, electric lights, solar water heating circulation pump etc. Use Honeybee "Read EP Result" component or any other one to generate it. - 2) In case of SWH array: Thermal heating energy (or electrical energy) required to heat domestic hot water and/or space heating load and/or space cooling load. Use Ladybug "Residential Hot Water" or "Commercial Public Apartment Hot Water" components to calculate it (simply plugin their "heatingLoadPerHour" outputs). - The purpose of this input is to divide the energy loads to each PV/SWH array rows. - If not inputted, "energyLoadPerRowPerHour" output will not be calculated.

#### Outputs
* ##### readMe!
...
* ##### PV_SWHsurface
Surfaces on which PV modules/SWH collectors will be laid on.
* ##### PV_SWHsurfacesArea
Total area of the PV_SWHsurfaces. - In Rhino documents units (meters, centimeters, feets...).
* ##### minimalSpacing
Minimal distance between fixed (anchor) points of rows. The distance is measured on the ground (or along the base surface if it has been inputted). - In meters.
* ##### minimalSpacingDate
Exact date taken from "minimalSpacingPeriod_" input for which minimal spacing between rows has been calculated.
* ##### arrayOriginPt
Origin point of the PV / SWH array.
* ##### energyLoadPerRowPerHour
"energyLoadPerHour_" input's data divided to rows.


[Check Hydra Example Files for PV SWH System Size](https://hydrashare.github.io/hydra/index.html?keywords=Ladybug_PV SWH System Size)