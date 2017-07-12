## ![](../../images/icons/Cone_Of_Vision.png) Cone Of Vision

![](../../images/components/Cone_Of_Vision.png)

Use this component to generate and visualize cones of vision.

#### Inputs
* ##### type [Optional]
This input sets the cone of vision, the cone is defined by four values that are vertical angle+, vertical angle-, horizontal angle+, horizontal angle-, distance limits.
* ##### viewPoint [Default]
The point of vision in which to generate the cone of vision.
* ##### viewDirection [Default]
A vector that represents the view direction.
* ##### distanceLimit [Optional]
Set the limit of the view.
* ##### vAngleUp [Optional]
The vertical angle of the upper visual field. A number from 0.0 to 90.0.
* ##### vAngleDown [Optional]
The vertical angle of the lower visual field. A number from 0.0 to 90.0.
* ##### hAngle [Optional]
The horizontal angle from the standard line of sight. A number from 0.0 to 180.0.

#### Outputs
* ##### readMe!
...
* ##### coneOfVision
Brep that represent the cone of vision.
* ##### parameters
Connect this list to Ladybug_View Analysis for customizing the view analysis.


[Check Hydra Example Files for Cone Of Vision](https://hydrashare.github.io/hydra/index.html?keywords=Ladybug_Cone Of Vision)