## ![](../../images/icons/Solar_Water_Heating_Surface.png) Solar Water Heating Surface - [[source code]](https://github.com/ladybug-tools/ladybug-legacy/tree/master/src/Ladybug_Solar%20Water%20Heating%20Surface.py)

![](../../images/components/Solar_Water_Heating_Surface.png)

Use this component to calculate amount of thermal energy that can be produced by a surface if a certain percentage of it is covered with Solar water heating liquid collectors. The thermal energy can then be used for domestic hot water, space heating or space cooling. - Component based on: "Solar Engineering of Thermal Processes", John Wiley and Sons, J. Duffie, W. Beckman, 4th ed., 2013. "Technical Manual for the SAM Solar Water Heating Model", NREL, N. DiOrio, C. Christensen, J. Burch, A. Dobos, 2014. "A simplified method for optimal design of solar water heating systems based on life-cycle energy analysis", Renewable Energy journal, Yan, Wang, Ma, Shi, Vol 74, Feb 2015 - http://www.wiley.com/WileyCDA/WileyTitle/productCd-0470873663.html https://sam.nrel.gov/system/tdf/SimpleSolarWaterHeatingModel_SAM_0.pdf?file=1&type=node&id=69521 http://www.sciencedirect.com/science/article/pii/S0960148114004807 - 

#### Inputs
* ##### epwFile [Required]
Input .epw file path by using the "File Path" parameter, or Ladybug's "Open EPW And STAT Weather Files" component.
* ##### heatingLoadPerHour [Required]
Heating load in electrical energy for each hour during a year. In kWh. It represents domestic hot water heating load. With added space heating and/or space cooling heating loads. - To calculate domestic hot water heating load, use Ladybug "Residential Hot Water" or "Commercial Public Apartment Hot Water" components. - Space heating and space cooling loads can be inputted from Honeybee's "Read EP Result" component. Divide each value of space heating load with 0.7, to account for COP(coefficient of performance) of the heating system. Space cooling values do not need to be divided with anything (COP = 1.0).
* ##### SWHsurface [Required]
- Input planar Surface (not polysurface) on which the SWH collectors will be applied. If you have a polysurface, explode it (using "Deconstruct Brep" component) and then feed its Faces(F) output to _SWHsurface. Surface normal should be faced towards the sun. - Or create the Surface based on initial SWH system size by using "PV SWH system size" component.
* ##### SWHsurfacePercent [Optional]
The percentage of surface which will be used for SWH collectors (range 0-100). - There are no general rules or codes which would limit the percentage of the roof(surface) covered with SWH collectors. - If not supplied, default value of 100 (all surface area will be covered with SWH collectors) is used.
* ##### SWHsystemSettings [Optional]
A list of all Solar water heating system settings. Use the "Solar Water Heating System" or "Solar Water Heating System Detailed" components to generate them. - If not supplied, the following swh system settings will be used by default: - glazed flat plate collectors - active - closed loop - pipe length: 20 meters - unshaded
* ##### north [Optional]
Input a vector to be used as a true North direction for the sun path, or a number between 0 and 360 that represents the clockwise degrees off from the Y-axis to make North. - If not supplied, default North direction will be set to the Y-axis (0 degrees).
* ##### albedo [Optional]
A list of 8767 (with header) or 8760 (without the header) albedo values for each hour during a year. Albedo (or Reflection coefficient) is an average ratio of the global incident solar radiation reflected from the area surrounding the PV surface. It ranges from 0 to 1. - It depends on the time of the year/day, surface type, temperature, vegetation, presence of water, ice and snow etc. - If no list supplied, default value of 0.20 will be used, corrected(increased) for the presence of snow (if any). - Unitless.
* ##### annualHourlyData [Optional]
An optional list of hourly data from Ladybug's "Import epw" component (e.g. dryBulbTemperature), which will be used for "conditionalStatement_".
* ##### conditionalStatement [Optional]
This input allows users to calculate the Solar water heating surface component results only for those annualHourlyData_ values which fit specific conditions or criteria. To use this input correctly, hourly data, such as dryBulbTemperature or windSpeed, must be plugged into the "annualHourlyData_" input. The conditional statement input here should be a valid condition statement in Python, such as "a>25" or "b<3" (without the quotation marks). conditionalStatement_ accepts "and" and "or" operators. To visualize the hourly data, English letters should be used as variables, and each letter alphabetically corresponds to each of the lists (in their respective order): "a" always represents the 1st list, "b" always represents the 2nd list, etc. - For example, if you have an hourly dryBulbTemperature connected as the first list, and windSpeed connected as the second list (both to the annualHourlyData_ input), and you want to plot the data for the time period when temperature is between 18°C and 23°C, and windSpeed is larger than 3m/s, the conditionalStatement_ should be written as "18<a<23 and b>3" (without the quotation marks). - This input can also be used for analysis of drainback systems. Input a "dryBulbTemperature" data from "Import epw" component into upper "annualHourlyData_" input. Then input "a>5" to this ("conditionalStatement_") input.
* ##### runIt [Required]
...

#### Outputs
* ##### readMe!
...
* ##### heatFromTankPerHour
Thermal energy provided by the storage tank per each hour during a year. - In kWh.
* ##### heatFromTankPerYear
Total thermal energy provided by the storage tank for a whole year. - In kWh.
* ##### avrDailyheatFromTankPerYear
An average thermal energy provided by the storage tank per day for a whole year. - In kWh/day.
* ##### heatFromAuxiliaryHeaterPerHour
Thermal energy provided and Electrical energy spent by an auxiliary heater per each hour during a year. Electric auxiliary heater used. - In kWh.
* ##### dischargedHeatPerHour
Discharged surplus energy ("heat dump") per each hour during a year. It can be used to heat a pool, hot tub, greenhouse or as snow-melt system (by using radiant floor tubing bellow sidewalks, or radiatior beneath the entrance stairs). - In kWh.
* ##### pumpEnergyPerHour
Electrical energy spent by the circulation pump(s) per hour during a year. - In kWh.
* ##### tankWaterTemperaturePerHour
Tank water temperature per each hour during a year. - In °C.
* ##### SWHsurfaceTiltAngle
The angle from horizontal of the inclination of the SWHsurface. Example: 0 = horizontal, 90 = vertical. It ranges from 0-180. - In degrees.
* ##### SWHsurfaceAzimuthAngle
The orientation angle (clockwise from the true north) of the SWHsurface normal vector. It ranges from 0-360. - In degrees.
* ##### systemSize
Rated SWH system size.  - In kWt.


[Check Hydra Example Files for Solar Water Heating Surface](https://hydrashare.github.io/hydra/index.html?keywords=Ladybug_Solar Water Heating Surface)