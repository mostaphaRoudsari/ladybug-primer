## ![](../../images/icons/Photovoltaics_Performance_Metrics.png) Photovoltaics Performance Metrics - [[source code]](https://github.com/ladybug-tools/ladybug-legacy/tree/master/src/Ladybug_Photovoltaics%20Performance%20Metrics.py)

![](../../images/components/Photovoltaics_Performance_Metrics.png)

Use this component to calculate various Photovoltaics performance metrics - 

#### Inputs
* ##### PVsurface [Required]
- Input planar Grasshopper/Rhino Surface (not a polysurface) on which the PV modules will be applied. If you have a polysurface, explode it (using "Deconstruct Brep" component) and then feed its Faces(F) output to _PVsurface. Surface normal should be faced towards the sun. - Or create the Surface based on initial PV system size by using "PV SWH system size" component.
* ##### PVsurfacePercent [Optional]
The percentage of surface which will be used for PV modules (range 0-100). - Some countries and states, have local codes which limit the portion of the roof, which can be covered by crystalline silicon modules. For example, this may include having setbacks(distances) of approximatelly 90cm from side and top edges of a roof, as a fire safety regulation. - If not supplied, default value of 100 percent (all surface area will be covered in PV modules) is used. - In percent.
* ##### PVmoduleSettings [Optional]
A list of PV module settings. Use the "Simplified Photovoltaics Module" or "Import Sandia Photovoltaics Module" or "Import CEC Photovoltaics Module" components to generate them. - If not supplied, the following PV module settings will be used by default: - module material: crystalline silicon (c-Si) - moduleType: Close (flush) roof mount - moduleEfficiency: 15 % - temperatureCoefficient: -0.5 %/C - moduleActiveAreaPercent: 90 %
* ##### ACenergyPerHour [Required]
Import "ACenergyPerYear" output data from "Photovoltaics surface" component. - In kWh.
* ##### totalRadiationPerHour [Required]
Import "totalRadiationPerHour" output data from "Photovoltaics surface" component. - In kWh/m2.
* ##### cellTemperaturePerHour [Required]
Import "cellTemperaturePerHour" output data from "Photovoltaics surface" component. - In C.
* ##### ACenergyDemandPerHour [Optional]
Required electrical energy used for any kind of load: heating, cooling, electric lights, solar water heating circulation pump etc. For example, any of the Honeybee's "Read EP Result" outputs can be inputted in here. Either separately or summed. - If nothing inputted, this input will be neglected (there is no required electrical energy). - In kWh.
* ##### energyCostPerKWh [Optional]
The cost of one kilowatt hour in any currency unit (dollar, euro, yuan...) - If not supplied, 0.15 $/kWh will be used as default value.
* ##### embodiedEnergyPerM2 [Optional]
Energy necessary for an entire product life-cycle of PV module per square meter. - If not supplied default value of 4410 (MJ/m2) will be used. - In MJ/m2 (megajoules per square meter).
* ##### embodiedCO2PerM2 [Optional]
Carbon emissions produced during PV module's life-cycle per square meter. - If not supplied default value of 225 (kg CO2/m2) will be used. - In kg CO2/m2 (kilogram of CO2 per square meter).
* ##### lifetime [Optional]
Life expectancy of a PV module. - If not supplied default value of 30 (years) will be used. - In years.
* ##### gridEfficiency [Optional]
An average primary energy to electricity conversion efficiency. - If not supplied default value of 29 (perc.) will be used. - In percent.
* ##### optimal [Optional]
Set to "True" to calculate optimal PVsurface area. An optimal PVsurface area will cover 100% of the of the annual electricity load ("ACenergyDemandPerHour_").
* ##### runIt [Required]
...

#### Outputs
* ##### readMe!
...
* ##### optimalSystemSize
Optimal PV system size (optimal total size of the PV array) for a given PVsurface's tilt, array and "ACenergyDemandPerHour_". Minimum system size is 0.01 kW. Input it to "systemSize_" input of "PV SWH system size" component to see how much area it would require. - To calculate it, set the "optimal_" input to "True". - In thermal kiloWatts (kWt).
* ##### CUFperYear
Capacity Utilization Factor (or Capacity Factor or sometimes evan called Plant Load Factor (PLF)) - ratio of the annual AC power output and maximum possible output under ideal conditions if the sun shone throughout the day and throughout the year. It is sometimes used by investors or developers for Financial and Maintenance analysis of the PV systems, instead of "basicPRperYear". - In percent (%).
* ##### basicPRperYear
Basic Performance Ratio - ratio of the actual and theoretically possible annual energy output. It is worldwide accepted standard metric for measuring the performance of the PV system, therefor it is used for Maintenance analysis of PV systems. Used for Maintenance analysis of PV systems. - basicPR is more precise than upper "CUF" and should be used instead of it, unless "CUF" is specifically required. - In percent(%).
* ##### temperatureCorrectedPRperMonth
Temperature corrected Performance Ratio - ratio of the actual and theoretically possible energy output for each month during a year, corrected for PV module's Cell temperature. Mid-day hours (solarRadiation > 0.6 kWh/m2) only taken into account. Used for Maintenance analysis of PV systems. - In percent(%).
* ##### temperatureCorrectedPRperYear
Temperature corrected Performance Ratio - ratio of the actual and theoretically possible annual energy output, corrected for PV module's Cell temperature. Mid-day hours (solarRadiation > 0.6 kWh/m2) only taken into account. Used for Maintenance analysis of PV systems. - It is more precise than upper "basicPR" and should be used instead of it, unless "basicPR" is specifically required. - In percent(%).
* ##### energyOffsetPerMonth
Percentage of the electricity demand covered by Photovoltaics system for each month during a year. - It is used for Financial and Maintenance analysis of the PV system. - In percent(%).
* ##### energyOffsetPerYear
Percentage of the total annual electricity demand covered by Photovoltaics system for a whole year. - It is used for Financial and Maintenance analysis of the PV system. - In percent(%).
* ##### energyValue
Total Energy value for the whole year in currency unit (dollars, euros, yuans...) - It is used for Financial analysis of the PV system.
* ##### Yield
Ratio of annual AC power output and nameplate DC power rating. It is used for Financial analysis of the PV systems. - In hours (h).
* ##### EROI
Energy Return On Investment - a comparison of the generated electricity to the amount of primary energy used throughout the PV module's product life-cycle. - It is used for Financial analysis of the PV system. - Unitless.
* ##### embodiedEnergy
Total energy necessary for an entire product life-cycle of PV modules. - It used for the Life Cycle analysis of the PV system. - In GJ (gigajoules).
* ##### embodiedCO2
Total carbon emissions produced during PV module's life-cycle. - It used for the Life Cycle analysis of the PV system. - In tCO2 (tons of CO2).
* ##### CO2emissionRate
An index which shows how effective a PV system is in terms of global warming. It is used in comparison with other fuels and technologies (Hydroelectricity(15), Wind(21), Nuclear(60), Geothermal power(91), Natural gas(577), Oil(893), Coal(955) ...) - It is part of the Life Cycle analysis of the PV system. - In gCO2/kWh.
* ##### EPBT
Energy PayBack Time - time it takes for PV modules to produce all the energy used through-out its product life-cycle. After that period, they start producing zero-emissions energy. - It is used for Life Cycle analysis of the PV system. - In years.


[Check Hydra Example Files for Photovoltaics Performance Metrics](https://hydrashare.github.io/hydra/index.html?keywords=Ladybug_Photovoltaics Performance Metrics)