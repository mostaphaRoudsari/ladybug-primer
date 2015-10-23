## Comfort_Mannequin [![IMAGE](images/icons/Comfort_Mannequin.png)]

![IMAGE](images/components/Comfort_Mannequin.png)

Use this component to color a mannequin based on their relation to a comfort temperature. - 

#### Inputs
* _ambientTemperature <Required>: The temperture around the mannequin, which can be either UTCI (outdoor comfort), Standard Effective Temperature (PMV comfort), or Operative Temperature (Adaptive Comfort).
* targetTemperature_ <Optional>: The target comfort temperature that the mannequin wants to be at.  The default is set to 20C
* comfortRange_ <Optional>: The number of degrees above and below the target temperture that the subject will still find comfortable.  The default is set to 3C, which is pretty common for many comfort metrics.
* ------------------------- <>: ...
* bodyPosture_ <Optional>: An interger to set the posture of the comfort mannequin, which can have a large effect on the radiation striking the mannequin.  0 = Standing, 1 = Sitting, and 2 = Lying Down.  The default is set to 1 for sitting.
* rotationAngle_ <Optional>: An optional rotation angle in degrees.  Use this number to adjust the angle of the comfort mannequin in space.  The angle of the mannequin in relation to the sun can have a large effect on the amount of radiation that falls on it and thus largely affect the resulting mean radiant temperature.
* bodyLocation_ <Optional>: An optional point that sets the position of the comfort mannequin in space.  Use this to move the comfort mannequin around in relation to contextShading_ connected below. The default is set to the Rhino origin.
* legendPar_ <Optional>: Optional legend parameters from the Ladybug Legend Parameters component.

#### Outputs
* mannequinMesh: A colored mesh of a comfort mannequin showing the amount of radiation falling over the mannequin's body.
* legend: A legend that corresponds to the colors on the mannequinMesh and shows the relative W/m2.
* legendBasePt: The legend base point, which can be used to move the legend in relation to the chart with the grasshopper "move" component.


[Check Hydra Example Files for Comfort_Mannequin](https://hydrashare.github.io/hydra/index.html?keywords=Comfort_Mannequin)