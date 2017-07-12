## ![](../../images/icons/Commercial_Public_Apartment_Hot_Water.png) Commercial Public Apartment Hot Water

![](../../images/components/Commercial_Public_Apartment_Hot_Water.png)

Use this component to calculate domestic hot water consumption for each hour during a year, for Commercial, Public and Apartment buildings.

#### Inputs
* ##### epwFile [Required]
Input .epw file path by using grasshopper's "File Path" component.
* ##### buildingType [Required]
Choose the building type for which hot water consumption will be calculated:
* ##### numberOfUnits [Required]
Number of units for upper chosen "_buildingType". Represents the number of:
* ##### litersPerUnitPerDay [Optional]
Number of liters for a single unit and day, based on _buidlingType
* ##### occupancyStartingHour [Optional]
An hour (from 1 to 24) during a day at which the occupancy of the chosen _buildingType starts:
* ##### occupancyDuration [Optional]
Total number of hours in a single day during which the chosen _buildingType will be used.
* ##### firstWeekStartDay [Optional]
Week day on which a year starts (1 - Monday, 2 - Tuesday, 3 - Wednesday...)
* ##### weekendDays [Optional]
Define a list of two weekend (nonworking) days. Through out the World, countries have different days as their weekend days:
* ##### holidayDays [Optional]
List of days (1 to 365) which are holiday (nonworking) days.
* ##### deliveryWaterTemperature [Optional]
Required water temperature. In Celsius
* ##### coldWaterTemperaturePerHour [Optional]
Cold (inlet) water temperature supplied from public water system, for each hour during a year. In Celsius.
* ##### runIt [Required]
...

#### Outputs
* ##### readMe!
...
* ##### heatingLoadPerHour
Thermal energy (or electrical energy) required to heat the domestic hot water consumption for each hour during a year.
* ##### hotWaterPerHour
Domestic hot water consumption for each hour during a year.
* ##### hotWaterPerYear
Domestic hot water consumption for a whole year.
* ##### averageDailyHotWaterPerYear
Average daily hot water consumption for a whole year.
* ##### maximumDailyConsumption
Maximal hot water consumption per day during a year.
* ##### maximumConsumptionDay
Day with maximal hot water consumption.
* ##### minimumDailyConsumption
Minimal hot water consumption per day during a year.
* ##### minimumConsumptionDay
Day with minimal hot water consumption.


[Check Hydra Example Files for Commercial Public Apartment Hot Water](https://hydrashare.github.io/hydra/index.html?keywords=Ladybug_Commercial Public Apartment Hot Water)