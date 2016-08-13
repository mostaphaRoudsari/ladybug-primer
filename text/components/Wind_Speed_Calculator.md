## ![](../../images/icons/Wind_Speed_Calculator.png) Wind Speed Calculator

![](../../images/components/Wind_Speed_Calculator.png)

Use this component to calculate wind speed at a specific height for a given terrain type.  By default, the component will calculate ground wind speed, which is useful for comfrt calculations.  Also, by hooking up wind data from an epw file, you can use the resulting data to create a wind rose at any height. - 

#### Inputs
* ##### north [Optional]
Input a vector to be used as a true North direction for the sun path or a number between 0 and 360 that represents the degrees off from the y-axis to make North.  The default North direction is set to the Y-axis (0 degrees).
* ##### windSpeed_tenMeters [Required]
The wind speed from the import EPW component or a number representing the wind speed at 10 meters off the ground in agricultural or airport terrian.  This input also accepts lists of numbers representing different speeds at 10 meters.
* ##### windDirection [Optional]
The wind direction from the import EPW component or a number in degrees represeting the wind direction from north,  This input also accepts lists of numbers representing different directions.
* ##### terrainType [Optional]
An interger or text string that sets the terrain class associated with the output windSpeedAtHeight. Interger values represent the following terrain classes: 0 = City: large city centres, 50% of buildings above 21m over a distance of at least 2000m upwind. 1 = Suburban: suburbs, wooded areas. 2 = Country: open, with scattered objects generally less than 10m high. 3 = Water: Flat, unobstructed areas exposed to wind flowing over a large water body (no more than 500m inland).
* ##### epwTerrain [Optional]
An interger or text string that sets the terrain class associated with the output windSpeedAtHeight. The default is set to 2 for flat clear land, which is typical for most EPW files that are recorded at airports.  Interger values represent the following terrain classes: 0 = City: large city centres, 50% of buildings above 21m over a distance of at least 2000m upwind. 1 = Suburban: suburbs, wooded areas. 2 = Country: open, with scattered objects generally less than 10m high. 3 = Water: Flat, unobstructed areas exposed to wind flowing over a large water body (no more than 500m inland).
* ##### heightAboveGround [Optional]
Optional. This is the height above ground for which you would like to measure wind speed. Providing more than one value will generate a list of speeds at each given height. Default height is 2 m above ground, which is what a person standing on the ground would feel.
* ##### epwHeight [Optional]
An optional number to set the height at which the _windSpeed_tenMeters was recorded if the wind was not recorded at 10 meters above the ground.  The default is set to 10 meters as this is the height at which all wind in EPW files is recorded.
* ##### powerOrLog [Optional]
Set to "True" to use a power law to translate the wind speed to that at a given height and set to "False" to use a log law to translate the wind speed.  The default is set to "True" for a power law as this is the function that is used by EnergyPlus.
* ##### analysisPeriod [Optional]
If you have connected data from an EPW component, plug in an analysis period from the Ladybug_Analysis Period component to calculate data for just a portion of the year. The default is Jan 1st 00:00 - Dec 31st 24:00, the entire year.

#### Outputs
* ##### readMe!
...
* ##### windSpeedAtHeight
The wind speed at the connected height above the ground.
* ##### windVectorAtHeight
Returns a list of vectors representing wind speed and direction at every hour within the analysis period, at each height provided.


[Check Hydra Example Files for Wind Speed Calculator](https://hydrashare.github.io/hydra/index.html?keywords=Ladybug_Wind Speed Calculator)