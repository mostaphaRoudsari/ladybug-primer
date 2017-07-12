## ![](../../images/icons/Solar_Water_Heating_Surface.png) Solar Water Heating Surface

![](../../images/components/Solar_Water_Heating_Surface.png)

Use this component to calculate amount of thermal energy that can be produced by a surface

#### Inputs
* ##### epwFile [Required]
Input .epw file path by using the "File Path" parameter, or Ladybug's "Open EPW And STAT Weather Files" component.
* ##### heatingLoadPerHour [Required]
Heating load in electrical energy for each hour during a year. In kWh.
* ##### SWHsurface [Required]
- Input planar Surface (not polysurface) on which the SWH collectors will be applied. If you have a polysurface, explode it (using "Deconstruct Brep" component) and then feed its Faces(F) output to _SWHsurface. Surface normal should be faced towards the sun.
* ##### SWHsurfacePercent [Optional]
The percentage of surface which will be used for SWH collectors (range 0-100).
* ##### SWHsystemSettings [Optional]
A list of all Solar water heating system settings. Use the "Solar Water Heating System" or "Solar Water Heating System Detailed" components to generate them.
* ##### north [Optional]
Input a vector to be used as a true North direction for the sun path, or a number between 0 and 360 that represents the clockwise degrees off from the Y-axis to make North.
* ##### albedo [Optional]
A list of 8767 (with header) or 8760 (without the header) albedo values for each hour during a year.
* ##### annualHourlyData [Optional]
An optional list of hourly data from Ladybug's "Import epw" component (e.g. dryBulbTemperature), which will be used for "conditionalStatement_".
* ##### conditionalStatement [Optional]
This input allows users to calculate the Solar water heating surface component results only for those annualHourlyData_ values which fit specific conditions or criteria.
* ##### runIt [Required]
...

#### Outputs
* ##### readMe!
...
* ##### heatFromTankPerHour
Thermal energy provided by the storage tank per each hour during a year.
* ##### heatFromTankPerYear
Total thermal energy provided by the storage tank for a whole year.
* ##### avrDailyheatFromTankPerYear
An average thermal energy provided by the storage tank per day for a whole year.
* ##### heatFromAuxiliaryHeaterPerHour
Thermal energy provided and Electrical energy spent by an auxiliary heater per each hour during a year.
* ##### dischargedHeatPerHour
Discharged surplus energy ("heat dump") per each hour during a year.
* ##### pumpEnergyPerHour
Electrical energy spent by the circulation pump(s) per hour during a year.
* ##### tankWaterTemperaturePerHour
Tank water temperature per each hour during a year.
* ##### SWHsurfaceTiltAngle
The angle from horizontal of the inclination of the SWHsurface. Example: 0 = horizontal, 90 = vertical.
* ##### SWHsurfaceAzimuthAngle
The orientation angle (clockwise from the true north) of the SWHsurface normal vector.
* ##### systemSize
Rated SWH system size. 


[Check Hydra Example Files for Solar Water Heating Surface](https://hydrashare.github.io/hydra/index.html?keywords=Ladybug_Solar Water Heating Surface)