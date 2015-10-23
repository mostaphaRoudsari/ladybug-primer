## Import Ground Temp [![](../../images/icons/Import_Ground_Temp.png)]

![](../../images/components/Import_Ground_Temp.png)

Use this component to visualise ground temperatures throughout the year at specific depths. Please note that epw files usually only provide ground temperature data at depths 0.5 meters, 2 meters and 4 meters thus data has been interpolated for all other depths. In particular this interpolation assumes that ground temperatures do not vary over the seasons once the depth has reach 9 meters below the ground surface. - 

#### Inputs
* ##### _epwFile [Required]
An .epw file path on your system as a string
* ##### visualisedata_Season []
Set to true to visualise the ground temperature data as an average for every season
* ##### visualisedata_Month []
Set to true to visualise the ground temperature data for every month

#### Outputs
* ##### readMe!
...
* ##### groundtemp1st
In every epw file there are monthly ground temperatures at 3 different depths this is the 1st
* ##### groundtemp2nd
In every epw file there are monthly ground temperatures at 3 different depths this is the 2nd
* ##### groundtemp3rd
In every epw file there are monthly ground temperatures at 3 different depths this is the 3rd
* ##### profileCrvs
This output draws the curves of the temperature curves connect it to G of the Grasshopper component Custom Preview
* ##### crvColors
This output draws the colours of the temperature curves connect it to S of the Grasshopper component Custom Preview
* ##### graphAxes
This output draws the axes of the graph it doesn't need to be connected to anything
* ##### graphtext
This output draws the text of the graph it doesn't need to be connected to anything
* ##### Legend
Script variable Importgroundtemp


[Check Hydra Example Files for Import Ground Temp](https://hydrashare.github.io/hydra/index.html?keywords=Ladybug_Import Ground Temp)