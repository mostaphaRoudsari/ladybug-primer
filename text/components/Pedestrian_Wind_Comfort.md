## ![](../../images/icons/Pedestrian_Wind_Comfort.png) Pedestrian Wind Comfort

![](../../images/components/Pedestrian_Wind_Comfort.png)

Use this component to analyse pedestrian wind comfort and safety for the present and potential (newly built) urban environments.

#### Inputs
* ##### epwFile [Required]
Input an .epw file path by using the "File Path" parameter, or Ladybug's "Open EPW And STAT Weather Files" component.
* ##### windFactor [Required]
Division of cfd simulation's wind speed values, and annual average wind speed value from the weather data (.epw file) at 10 meters height.
* ##### analysisGeometry [Required]
Input a mesh for whose face centroids the cfd simulation has been performed.
* ##### pedestrianType [Optional]
Choose the pedestrian type used at the analysis location:
* ##### northCfd [Optional]
Input a vector to be used as a Cfd simulation's true North direction, or a number between 0 and 360 that represents the clockwise degrees off from the Y-axis.
* ##### north [Optional]
Input a vector to be used as Rhino's true North direction, or a number between 0 and 360 that represents the clockwise degrees off from the Y-axis.
* ##### legendPar [Optional]
Optional legend parameters from the Ladybug "Legend Parameters" component.
* ##### resultGradient [Optional]
Choose whether or not the resulting geometry-values will be created as a gradient-float or not.
* ##### analysisPeriod [Optional]
An optional analysis period from the "Analysis Period" component.
* ##### annualHourlyData [Optional]
An optional list of hourly data from Ladybug's "Import epw" component (e.g. windSpeed), which will be used for "conditionalStatement_".
* ##### conditionalStatement [Optional]
This input allows users to calculate the Pedestrian wind comfort component results only for those annualHourlyData_ values which fit specific conditions or criteria. To use this input correctly, hourly data, such as windSpeed or windDirection, must be plugged into the "annualHourlyData_" input. The conditional statement input here should be a valid condition statement in Python, such as "a>4" or "b<90" (without the quotation marks).
* ##### bakeIt [Optional]
Set to "True" to bake the pedestrianComfortMesh, pedestrianSafetyMesh, legend, legend2 into the Rhino scene.
* ##### runIt [Required]
...

#### Outputs
* ##### readMe!
...
* ##### pedestrianComfortCategory
Pedestrian wind comfort categories for each face centroid of the _analysisGeometry mesh.
* ##### pedestrianSafetyCategory
Pedestrian wind safety categories for each face centroid of the _analysisGeometry mesh.
* ##### thresholdWindSpeed
Wind speed that for 95% of the chosen analysis period is below the outputted value, for each _analysisGeometry face centroid.
* ##### strongestLocationWindSpeed
The strongest wind speed for the chosen analysis period, for each _analysisGeometry face centroid.
* ##### pedestrianComfortMesh
Colored _analysisGeometry mesh in accordance with disposition of the pedestrian wind comfort categories.
* ##### pedestrianSafetyMesh
Colored _analysisGeometry mesh. Coloring performed on the basis of whether the pedestrian safety criteria for the chosen location is fulfilled or not.
* ##### legend
Legend for the pedestrianComfortMesh and its title.
* ##### legend2
Legend for the pedestrianSafetyMesh and its title.
* ##### legendBasePt
Legend base point, which can be used to move the "legend" geometry with grasshopper's "Move" component.
* ##### legendBasePt2
Legend2 base point, which can be used to move the "legend2" geometry with grasshopper's "Move" component.


[Check Hydra Example Files for Pedestrian Wind Comfort](https://hydrashare.github.io/hydra/index.html?keywords=Ladybug_Pedestrian Wind Comfort)