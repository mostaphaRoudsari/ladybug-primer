## Photovoltaics Surface [![](../../images/icons/Photovoltaics_Surface.png)]

![](../../images/components/Photovoltaics_Surface.png)

Use this component to calculate amount of electrical energy that can be produced by a surface if a certain percentage of it is covered with Photovoltaics. Component based on NREL PVWatts v1 fixed tilt calculator for crystalline silicon (c-Si) photovoltaics. Sources: http://www.nrel.gov/docs/fy14osti/60272.pdf https://pvpmc.sandia.gov - 

#### Inputs
* ##### _PVsurface [Required]
- Input planar Surface (not a polysurface) on which the PV modules will be applied. If you have a polysurface, explode it (using "Deconstruct Brep" component) and then feed its Faces(F) output to _PVsurface. Surface normal should be faced towards the sun. - Or input surface Area, in square meters (example: "100"). - Or input PV system size (nameplate DC power rating), in kiloWatts at standard test conditions (example: "4 kw").
* ##### _epwFile [Required]
Input .epw file path by using grasshopper's "File Path" component.
* ##### PVsurfacePercent_ [Optional]
The percentage of surface which will be used for PV modules (range 0-100). - If not supplied, default value of 100 (all surface area will be covered in PV modules) is used.
* ##### PVsurfaceTiltAngle_ [Optional]
The angle from horizontal of the inclination of the PVsurface. Example: 0 = horizontal, 90 = vertical. (range 0-180) - If not supplied, but surface inputted into "_PVsurface", PVsurfaceTiltAngle will be calculated from an angle PVsurface closes with XY plane. If not supplied, but surface NOT inputted into "_PVsurface" (instead, a surface area or system size inputed), location's latitude will be used as default value.
* ##### PVsurfaceAzimuthAngle_ [Optional]
The orientation angle (clockwise from the true north) of the PVsurface normal vector. (range 0-360) - If not supplied, but surface inputted into "_PVsurface", PVsurfaceAzimuthAngle will be calculated from an angle PVsurface closes with its north. If not supplied, but surface NOT inputted into "_PVsurface" (instead, a surface area or system size inputed), default value of 180° (south-facing) for locations in the northern hemisphere or 0° (north-facing) for locations in the southern hemisphere, will be used.
* ##### ____________________ [Default]
Script variable PhotovoltaicsSurface
* ##### DCtoACderateFactor_ [Optional]
Factor which accounts for various locations and instances in a PV system where power is lost from DC system nameplate to AC power. It ranges from 0 to 1. It can be calculated with Ladybug's "DC to AC derate factor" component. - If not supplied, default value of 0.85 will be used.
* ##### moduleActiveAreaPercent_ [Optional]
Percentage of the module's area excluding module framing and gaps between cells.  - If not supplied, default value of 90(%) will be used.
* ##### moduleType_ [Optional]
Module type and mounting configuration: - 0 = Glass/cell/glass, Close (flush) roof mount (pv array mounted parallel and relatively close to the plane of the roof (between two and six inches)) 1 = Glass/cell/polymer sheet, Insulated back (pv curtain wall, pv skylights) 2 = Glass/cell/polymer sheet, Open rack (ground mount array, flat/sloped roof array that is tilted, pole-mount solar panels, solar carports, solar canopies) 3 = Glass/cell/glass, Open rack (the same as upper "2" type, just with a glass on the back part of the module). - If not supplied, default type: "Glass/cell/glass, Close (flush) roof mount" (0) is used.
* ##### moduleEfficiency_ [Optional]
The ratio of energy output from the PV module to input energy from the sun. It ranges from 0 to 100 (%). Current typical module efficiencies for crystalline silicon modules range from 14-20% - If not defined, default value of 15(%) will be used.
* ##### north_ [Optional]
Input a vector to be used as a true North direction, or a number between 0 and 360 that represents the clockwise degrees off from the Y-axis. - If not supplied, default North direction will be set to the Y-axis (0 degrees).
* ##### albedo_ [Optional]
Average reflection coefficient of the area surrounding the PV surface. It ranges from 0 for very dark to 1 for bright white or metallic surface. Here are some specific values: - Dry asphalt  0.12 Wet Asphalt  0.18 Bare soil  0.17 Grass  0.20 Concrete  0.30 Granite  0.32 Dry sand  0.35 Copper  0.74 Wet snow  0.65 Fresh snow  0.82 Aluminum  0.85 - If not supplied default value of 0.20 (Grass) will be used.
* ##### ____________________ [Default]
Script variable PhotovoltaicsSurface
* ##### annualHourlyData_ [Optional]
An optional list of hourly data from Ladybug's "Import epw" component (e.g. dryBulbTemperature), which will be used for "conditionalStatement_".
* ##### conditionalStatement_ [Optional]
This input allows users to calculate the Photovoltaics surface component results only for those annualHourlyData_ values which fit specific conditions or criteria. To use this input correctly, hourly data, such as dryBulbTemperature or windSpeed, must be plugged into the "annualHourlyData_" input. The conditional statement input here should be a valid condition statement in Python, such as "a>25" or "b<3" (without the quotation marks). conditionalStatement_ accepts "and" and "or" operators. To visualize the hourly data, English letters should be used as variables, and each letter alphabetically corresponds to each of the lists (in their respective order): "a" always represents the 1st list, "b" always represents the 2nd list, etc. For example, if you have an hourly dryBulbTemperature connected as the first list, and windSpeed connected as the second list (both to the annualHourlyData_ input), and you want to plot the data for the time period when temperature is between 18°C and 23°C, and windSpeed is larger than 3m/s, the conditionalStatement_ should be written as "18<a<23 and b>3" (without the quotation marks).
* ##### ____________________ [Default]
Script input ______________________.
* ##### _runIt [Required]
...

#### Outputs
* ##### readMe!
...
* ##### ________________________
Script variable Python
* ##### ACenergyPerHour
AC power output for each hour during a year, in kWh
* ##### ACenergyPerMonth
Total AC power output for each month, in kWh
* ##### ACenergyPerYear
Total AC power output for a whole year, in kWh
* ##### averageDailyACenergyPerMonth
An average AC power output per day in each month, in kWh/day
* ##### averageDailyACenergyPerYear
An average AC power output per day in a whole year, in kWh/day
* ##### ________________________
Script variable Python
* ##### totalRadiationPerHour
Total Incident POA (Plane of array) irradiance for each hour during a year, in kWh/m2
* ##### moduleTemperaturePerHour
Module temperature for each hour during year, in °C
* ##### cellTemperaturePerHour
Cell temperature for each hour during year, in °C
* ##### ________________________
Script variable PhotovoltaicsSurface
* ##### nameplateDCpowerRating
DC rating or system size of the PV system. In kW
* ##### PVcoverArea
An area of the inputted _PVsurface which will be covered with Photovoltaics. In m2
* ##### PVcoverActiveArea
coverArea with excluded module framing and gaps between cells. In m2


[Check Hydra Example Files for Photovoltaics Surface](https://hydrashare.github.io/hydra/index.html?keywords=Ladybug_Photovoltaics Surface)