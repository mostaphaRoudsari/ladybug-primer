## ![](../../images/icons/Radiation_Calla_Lily.png) Radiation Calla Lily

![](../../images/components/Radiation_Calla_Lily.png)

Use this component to draw Radiation Calla Lily or Dome, which shows you how radiation would fall on an object from all directions for a given sky. _ It is useful for finding the best direction with which to orient solar panels and gives a sense of the consequences of deviating from such an orientation. _ The Calla Lily/Dome can be understood in three different ways: _ 1) The Calla Lily/Dome a 3D representation of all possible radiation roses for a given sky since it includes all vertical angles from 0 to 90. 2) The Calla Lily/Dome is the reciprocal of the Tergenza Sky Dome since the Cala Dome essentially shows you how the radiation from the sky will fall onto a hemispherical object. 3) The Calla Lily/Dome is a smart radiation analysis of a hemisphere.  Your results would effectively be the same if you made a hemisphere in Rhino and ran it through the "Radiation Analysis" component but, with this component, you will get a smoother color gradient and the component will automatically output the point (or vector) with the most radiation. - 

#### Inputs
* ##### selectedSkyMtx [Required]
The output from the selectSkyMtx component.
* ##### horAngleStep [Default]
An angle in degrees between 0 and 360 that represents the step for horizontal rotation. Smaller numbers will yeild a finer and smoother mesh with smoother colors.  The number input here should be smaller than 360 and divisible by 360.  The default is set to 10 degrees.
* ##### verAngleStep [Default]
Angle in degrees step between 0 and 90 that represents the step for vertical rotation. Smaller numbers will yeild a finer and smoother mesh with smoother colors.  The number input here should be smaller than 90 and divisible by 90.  The default is set to 10 degrees.
* ##### centerPoint [Default]
Input a point to locate the center point of the Calla Lily Graph
* ##### horScale [Default]
Input a number here to change horizontal (XY) scale of the graph. The default value is set to 1.  Note that, for the dome representation, this input will change the scale of the entire dome (both horizontal and vertical).
* ##### verScale [Default]
Input a number here to change vertical (Z) scale of the graph. The default value is set to 1. Note that, for the dome representation, this input will have no effect.
* ##### domeOrLily [Optional]
Set to "True" to have the component create a radiation dome and set to "False" to have it generate a Lily.  The default is set to "False" for a Lily. _ The difference between the Dome and the Lily is that, for the Lily, the Z scale is essentially the same as the color scale, which is redundant but also beautiful and potentially useful if you have to present data with a Black/White printer or to someone who is color blind. _ For the Dome, the vertical angles of rotation serve to define the Z scale.  In this sense, the normal to the dome at any given point is the angle at which the radiation study is being run.  This gives a geometric intuitive sense of how you should orient panels to capture or avoid the most sun.
* ##### legendPar [Optional]
Optional legend parameters from the Ladybug Legend Parameters component.
* ##### runIt [Required]
Set to "True" to run the component and generate a radiation Calla Lily.
* ##### bakeIt [Optional]
Set to "True" to bake the Calla Lily into the Rhino scene.

#### Outputs
* ##### readMe!
...
* ##### radiationLilyMesh
A colored mesh representing radiation of the Calla Lily or Dome.
* ##### baseCrvs
A set of guide curves for the Calla Lily.
* ##### legend
A legend of the radiation on the Calla Lily. Connect this output to a grasshopper "Geo" component in order to preview the legend in the Rhino scene.  
* ##### testPts
The vertices of the Calla Lily mesh.  These are hidden by default.
* ##### testPtsInfo
Information for each test point of the Calla Lily mesh.  "HRA" stands for "Horizontal Rotation Angle" while "VRA" stand for "Vertical Rotation Angle."  HRA varies from 0 to 360 while VRA varies from 0 to 90.
* ##### values
The radiation values for each test points (or mesh faces) of the Calla Lily in kWh/m2.
* ##### maxRadPt
The point on the Cala Lilly with the greatest amount of solar radiation.  This is useful for understanding the best direction to orient solar panels.
* ##### maxRadVector
The vector that should be used to orient solar panels such that they recieve the greatest possible solar radiation.
* ##### maxRadInfo
Information about the test point with the greates amount of radiation in the Calla Lily.  "HRA" stands for "Horizontal Rotation Angle" while "VRA" stand for "Vertical Rotation Angle."  HRA varies from 0 to 360 while VRA varies from 0 to 90.


[Check Hydra Example Files for Radiation Calla Lily](https://hydrashare.github.io/hydra/index.html?keywords=Ladybug_Radiation Calla Lily)