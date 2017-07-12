## ![](../../images/icons/SunriseSunset.png) SunriseSunset

![](../../images/components/SunriseSunset.png)

Use this component to get information about the sun

#### Inputs
* ##### location [Required]
The output from the importEPW or constructLocation component.  This is essentially a list of text summarizing a location on the earth.
* ##### HOYorAnalysisPeriod [Required]
Connect: 
* ##### isSunUpshift [Optional]
Set the number of hour after the sunrise and before the sunset you intend to exclude from the calculation of isSunUp. If no value is connected, the default value is 0.
* ##### isSunUpAltitude [Optional]
write a conditional statement about solar altitude. Use 'v' as variable.
* ##### year [Optional]
A number between -1000 to 3000. The approximations used in these script are very good for years between 1800 and 2100. Results should still be sufficiently accurate for the range from -1000 to 3000.

#### Outputs
* ##### readMe!
...
* ##### officialSunriseSunset
It is the time between day and night when there is light outside and the Sun is on the horizon (90°50').
* ##### solarNoon
Solar noon is when the sun is at its highest point in the sky each day.
* ##### solarElevationCorrected
Number(s) indicating the sun altitude(s) in degrees for each sun position on the sun path. It consider the atmospheric refraction.
* ##### solarAzimut
Number(s) indicating the sun azimuths in degrees for each sun position on the sun path.
* ##### sunVector
Vector(s) indicating the direction of sunlight for each sun position.
* ##### isSunUp
A list of number. 1 if the sun is up and 0 if the sun is down.
* ##### date
Detailied information for each sun position including date and time.
* ##### sunLightDuration
Duration of sunlight per day expressed in minutes.


[Check Hydra Example Files for SunriseSunset](https://hydrashare.github.io/hydra/index.html?keywords=Ladybug_SunriseSunset)