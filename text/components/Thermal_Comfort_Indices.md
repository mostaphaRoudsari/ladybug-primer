## Thermal Comfort Indices [![](../../images/icons/Thermal_Comfort_Indices.png)]

![](../../images/components/Thermal_Comfort_Indices.png)

Use this component to calculate different thermal comfort indices 

#### Inputs
* ##### _comfortIndex [Required]
Choose one of the comfort indices: 0 - HI (Heat Index) 1 - humidex (humidity index) 2 - DI (Discomfort Index) 3 - WCI (Wind Chill Index) 4 - WCT (Wind Chill Temperature) 5 - WBGT (Wet-Bulb Globe Temperature) indoors 6 - WBGT (Wet-Bulb Globe Temperature) outdoors 7 - TE (Effective Temperature) 8 - AT (Apparent Temperature) 9 - TS (Thermal Sensation) 10 - ASV (Actual Sensation Vote) 11 - MRT (Mean Radiant Temperature) 12 - Iclp (Predicted Insulation Index Of Clothing) 13 - HR (Heart Rate) 14 - DhRa (Dehydration Risk)
* ##### _____________________ [Default]
Script variable ThermalComfortIndices
* ##### _location [Required]
Input data from Ladybug's "Import epw" "location" output, or create your own location data with Ladybug's "Construct Location" component
* ##### _dryBulbTemperature [Required]
Hourly Dry Bulb Temperature (air temperature), in Celsius
* ##### dewPointTemperature_ [Optional]
Hourly Dew Point Temperature, in Celsius If not supplied, it will be calculated from dryBulbTemperature and relativeHumidity
* ##### _relativeHumidity [Required]
Hourly Relative Humidity, in percent (from 0% to 110%)
* ##### windSpeed_ [Optional]
Hourly Wind Speed, in meters/second If not supplied, default value of 0.3 m/s is used.
* ##### globalHorizontalRadiation_ [Optional]
Total amount of direct and diffuse solar radiation received on a horizontal surface, in Wh/m2. If not supplied, default value of 0 Wh/m2 is used.
* ##### totalSkyCover_ [Optional]
Amount of sky dome in tenths covered by clouds or obscuring phenomena, in tenths of coverage (from 1 to 10). For example: 1 is 1/10 covered. 10 is total coverage (10/10). If not supplied, dfault value of 8 (8/10) is used.
* ##### metabolicRate_ [Optional]
Input metabolic rate in mets. If not supplied 2.32 will be used as default value Here are some of the examples of metabolic rates mets based on activity: Activity - met ------------------- Reclining  - 0.8 Seating - 1.0 Car driving - 1.2 Sedentary activity (office, dwelling, school, laboratory) - 1.2 Standing - 1.2 Standing (light activity: shopping, laboratory, light industry) - 1.6 Standing (medium activity: shop assistant, domestic work) - 2.0 Walking (5 km/h) - 3.4 ... Washing dishes standing - 2.5 Domestic work (raking leaves on the lawn) - 2.9 Domestic work (washing by hand and ironing) - 2.9 Iron and steel (ramming the mould with a pneumatic hammer) - 3.0 Building industry (brick laying) - 2.2 Building industry (forming the mould) - 3.1 Building industry (loading a wheelbarrow with stones and mortar) - 4.7 Forestry (cutting with chainsaw) - 3.5 Forestry (working with an axe) - 8.5 Agriculture (digging with a spade) - 6.5 ... Volleyball - 4.0 Golf - 5.0 Softball - 5.0 Gymnastics - 5.5 Aerobic Dancing - 6.0 Swimming - 6.0 Ice skating - 6.2 Bicycling (15 km/h) - 4.0 Bicycling (20km/h) - 6.2 Skiing (9 km/h) - 7.0 Backpacking - 7.0 Basketball - 7.0 Handball - 8.0 Hockey - 8.0 Racquetball - 8.0 Soccer - 8.0 Running (8 km/h) - 8.5 Running (15km/h) - 9.5
* ##### age_ [Optional]
An age of the person. This input is only important for HR (Heart Rate) index. If not supplied, default value of 30 will be used.
* ##### gender_ [Optional]
Input 0 or "male"  or  1 or "female". This input is only important for HR (Heart Rate) index. If not supplied, "male" will be used as a default value.
* ##### acclimated_ [Optional]
Input True if person in subject is acclimatized, or False if it's not. This input is only important for DhRa (Dehydration risk). If no value is supplied, False (unacclimated) will be used by default.
* ##### _____________________ [Default]
Script variable thermalComfortIndices
* ##### HOY_ [Optional]
An hour of the year for which you would like to calculate thermal indices.  This must be a value between 1 and 8760. This input will override the analysisPeriod_ input below.
* ##### analysisPeriod_ [Optional]
An optional analysis period from the Analysis Period component. 
* ##### _runIt [Required]
...

#### Outputs
* ##### readMe!
...
* ##### comfortIndexValue
Humidex (°C) - the human-perceived increase in air temperature due to Dew point temperature increase. Used by Canadian Meteorologist service.
* ##### comfortIndexCategory
Each number (from 0 to 5) represents a certain humidex thermal sensation category. With categories being the following:     - category 0 (<30°C): Little or no discomfort     - category 1 (30-35°C): Noticeable discomfort     - category 2 (35-40°C): Evident discomfort     - category 3 (40-45°C): Intense discomfort; avoid exertion     - category 4 (45-54°C): Dangerous discomfort     - category 5 (>54°C): Heat stroke probable
* ##### comfortableOrNot
Outputs 0 or 1. 0 indicates that a person is not comfortable, 1 that he/she is comfortable at that hour (meaning humidex is < 30°C)
* ##### percentComfortable
Percentage of time chosen for analysis period, during which humidex is < 26.6°C
* ##### percentHotExtreme
Percentage of time chosen for analysis period, during which humidex is > 54.4°C
* ##### percentColdExtreme
 


[Check Hydra Example Files for Thermal Comfort Indices](https://hydrashare.github.io/hydra/index.html?keywords=Ladybug_Thermal Comfort Indices)