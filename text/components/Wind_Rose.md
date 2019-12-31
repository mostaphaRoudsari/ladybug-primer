## ![](../../images/icons/Wind_Rose.png) Wind Rose - [[source code]](https://github.com/ladybug-tools/ladybug-legacy/tree/master/src/Ladybug_Wind%20Rose.py)

![](../../images/components/Wind_Rose.png)

Use this component to make a windRose in the Rhino scene. In this wind rose diagram, each wedge represents the percentage of time the wind came from that direction during the analysis period you choose. You will note that each wedge is also colored. These colors relate directly with the legend displayed on the right. The colors in a wedge conveys the relative percentage of time the wind coming from that direction was within that speed range. - 

#### Inputs
* ##### north [Default]
Input a vector to be used as a true North direction for the wind rose or a number between 0 and 360 that represents the degrees off from the y-axis to make North.  The default North direction is set to the Y-axis (0 degrees).
* ##### hourlyWindDirection [Required]
The list of hourly wind direction data from the Import epw component.
* ##### hourlyWindSpeed [Required]
The list of hourly wind speed data from the Import epw component.
* ##### annualHourlyData [Optional]
An optional list of hourly data from the Import epw component, which will be overlaid on wind rose (e.g. dryBulbTemperature)
* ##### analysisPeriod [Default]
An optional analysis period from the Analysis Period component.
* ##### conditionalStatement [Optional]
This input allows users to remove data that does not fit specific conditions or criteria from the wind rose. To use this input correctly, hourly data, such as temperature or humidity, must be plugged into the annualHourlyData_ input. The conditional statement input here should be a valid condition statement in Python, such as "a>25" or "b<80" (without quotation marks). The current version of this component accepts "and" and "or" operators. To visualize the hourly data, only lowercase English letters should be used as variables, and each letter alphabetically corresponds to each of the lists (in their respective order): "a" always represents the 1st list, "b" always represents the 2nd list, etc. For the WindBoundaryProfile component, the variable "a" always represents windSpeed. For example, if you have hourly dry bulb temperature connected as the second list, and relative humidity connected as the third list (both to the annualHourlyData_ input), and you want to plot the data for the time period when temperature is between 18C and 23C, and humidity is less than 80%, the conditional statement should be written as “18<b<23 and c<80” (without quotation marks). This also accepts output from Ladybug_Beaufort Ranges component.
* ##### numOfDirections [Default]
A number of cardinal directions with which to divide up the data in wind rose. Values must be greater than 4 since you can have no fewer than 4 cardinal directions.
* ##### centerPoint [Default]
Input a point here to change the location of the wind rose in the Rhino scene.  The default is set to the Rhino model origin (0,0,0).
* ##### maxFrequency [Optional]
An optional number between 1 and 100 that represents the maximum percentage of hours that the outer-most ring of the wind rose represents.  By default, this value is set by the wind direction with the largest number of hours (the highest frequency) but you may want to change this if you have several wind roses that you want to compare to each other.  For example, if you have wind roses for different months or seasons, which each have different maximum frequencies.
* ##### showFrequency [Optional]
Connect boolean and set it to True to display frequency of wind coming from each direction. By default, these values will be displayed in gray color. 
* ##### showAverageVelocity [Optional]
Connect boolean and set it to True to display average wind velocity in m/s for wind coming from each direction. If a conditional statement is connected to the conditionalStatement_ input, a beaufort number is plotted(in square brackets) along with the average velocities. This number indicates the effect caused by wind of average velocity coming from that partcular direction. By default, these values will be displayed in black color.
* ##### scale [Default]
Input a number here to change the scale of the wind rose.  The default is set to 1.
* ##### legendPar [Optional]
Optional legend parameters from the Ladybug Legend Parameters component.
* ##### bakeIt [Optional]
An integer that tells the component if/how to bake the bojects in the Rhino scene.  The default is set to 0.  Choose from the following options: 0 (or False) - No geometry will be baked into the Rhino scene (this is the default). 1 (or True) - The geometry will be baked into the Rhino scene as a colored hatch and Rhino text objects, which facilitates easy export to PDF or vector-editing programs. 2 - The geometry will be baked into the Rhino scene as colored meshes, which is useful for recording the results of paramteric runs as light Rhino geometry.
* ##### runIt [Required]
Set this value to "True" to run the component and generate a wind rose in the Rhino scene.

#### Outputs
* ##### readMe!
...
* ##### calmRoseMesh
A mesh in the center of the wind rose representing the relative number of hours where the wind speed is around 0 m/s.
* ##### windRoseMesh
A mesh representing the wind speed from different directions for all hours analyzed.
* ##### windRoseCrvs
A set of guide curves that mark the number of hours corresponding to the windRoseMesh.
* ##### windRoseCenPts
The center point(s) of wind rose(s).  Use this to move the wind roses in relation to one another using the grasshopper "move" component.
* ##### legend
A legend of the wind rose. Connect this output to a grasshopper "Geo" component in order to preview the legend separately in the Rhino scene.
* ##### legendBasePts
The legend base point(s), which can be used to move the legend in relation to the rose with the grasshopper "move" component.
* ##### title
The title for the wind rose. Connect this output to a grasshopper "Geo" component in order to preview the legend separately in the Rhino scene.
* ##### averageVelocityMesh
Mesh output for average wind velocities displayed on WindRose. This will only output meshes if boolean value of True is provided to showAverageVelocity_. By default, these meshes are displayed in black color.
* ##### frequencyMesh
Mesh output for frequencies displayed on WindRose. This will only output meshes if boolean value of True is provided to showFrequency_. By default, these meshes are displayed in gray color.
* ##### windSpeeds
Wind speed data for the wind rose displayed in the Rhino scene.
* ##### windDirections
Wind direction data for the wind rose displayed in the Rhino scene.
* ##### averageVelocities
A list containing average wind velocity for all wind rose directions.
* ##### frequencies
A list containing frequency of time the wind is coming from a particular direction for all wind rose directions.


[Check Hydra Example Files for Wind Rose](https://hydrashare.github.io/hydra/index.html?keywords=Ladybug_Wind Rose)