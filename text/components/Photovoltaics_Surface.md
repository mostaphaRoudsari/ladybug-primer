## Photovoltaics_Surface [![IMAGE](images/icons/Photovoltaics_Surface.png)]

![IMAGE](images/components/Photovoltaics_Surface.png)

Use this component to calculate amount of electrical energy that can be produced by a surface

#### Inputs
* _PVsurface <Required>: - Input planar Surface (not a polysurface) on which the PV modules will be applied. If you have a polysurface, explode it (using "Deconstruct Brep" component) and then feed its Faces(F) output to _PVsurface. Surface normal should be faced towards the sun.
* _epwFile <Required>: Input .epw file path by using grasshopper's "File Path" component.
* PVsurfacePercent_ <Optional>: The percentage of surface which will be used for PV modules (range 0-100).
* PVsurfaceTiltAngle_ <Optional>: The angle from horizontal of the inclination of the PVsurface. Example: 0 = horizontal, 90 = vertical. (range 0-180)
* PVsurfaceAzimuthAngle_ <Optional>: The orientation angle (clockwise from the true north) of the PVsurface normal vector. (range 0-360)
* ____________________ <Default>: Script variable PhotovoltaicsSurface
* DCtoACderateFactor_ <Optional>: Factor which accounts for various locations and instances in a PV system where power is lost from DC system nameplate to AC power. It ranges from 0 to 1.
* moduleActiveAreaPercent_ <Optional>: Percentage of the module's area excluding module framing and gaps between cells. 
* moduleType_ <Optional>: Module type and mounting configuration:
* moduleEfficiency_ <Optional>: The ratio of energy output from the PV module to input energy from the sun. It ranges from 0 to 100 (%).
* north_ <Optional>: Input a vector to be used as a true North direction, or a number between 0 and 360 that represents the clockwise degrees off from the Y-axis.
* albedo_ <Optional>: Average reflection coefficient of the area surrounding the PV surface. It ranges from 0 for very dark to 1 for bright white or metallic surface. Here are some specific values:
* ____________________ <Default>: Script variable PhotovoltaicsSurface
* annualHourlyData_ <Optional>: An optional list of hourly data from Ladybug's "Import epw" component (e.g. dryBulbTemperature), which will be used for "conditionalStatement_".
* conditionalStatement_ <Optional>: This input allows users to calculate the Photovoltaics surface component results only for those annualHourlyData_ values which fit specific conditions or criteria. To use this input correctly, hourly data, such as dryBulbTemperature or windSpeed, must be plugged into the "annualHourlyData_" input. The conditional statement input here should be a valid condition statement in Python, such as "a>25" or "b<3" (without the quotation marks).
* ____________________ <Default>: Script input ______________________.
* _runIt <Required>: ...

#### Outputs
* readMe!: ...
* ________________________: Script variable Python
* ACenergyPerHour: AC power output for each hour during a year, in kWh
* ACenergyPerMonth: Total AC power output for each month, in kWh
* ACenergyPerYear: Total AC power output for a whole year, in kWh
* averageDailyACenergyPerMonth: An average AC power output per day in each month, in kWh/day
* averageDailyACenergyPerYear: An average AC power output per day in a whole year, in kWh/day
* ________________________: Script variable Python
* totalRadiationPerHour: Total Incident POA (Plane of array) irradiance for each hour during a year, in kWh/m2
* moduleTemperaturePerHour: Module temperature for each hour during year, in °C
* cellTemperaturePerHour: Cell temperature for each hour during year, in °C
* ________________________: Script variable PhotovoltaicsSurface
* nameplateDCpowerRating: DC rating or system size of the PV system. In kW
* PVcoverArea: An area of the inputted _PVsurface which will be covered with Photovoltaics. In m2
* PVcoverActiveArea: coverArea with excluded module framing and gaps between cells. In m2


[Check Hydra Example Files for Photovoltaics_Surface](https://hydrashare.github.io/hydra/index.html?keywords=Photovoltaics_Surface)