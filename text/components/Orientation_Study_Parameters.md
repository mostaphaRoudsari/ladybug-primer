## Orientation_Study_Parameters [![IMAGE](images/icons/Orientation_Study_Parameters.png)]

![IMAGE](images/components/Orientation_Study_Parameters.png)

Use this component with the Ladybug "Radiation Analysis", "Sunlight Hours Analysis", or "View Analysis" component to set up the parameters for an Orientation Study.

#### Inputs
* _divisionAngle <Required>: A number between 0 and 180 that represents the degrees to rotate the geometry for each step of the Orientation Study.
* _totalAngle <Required>: A number between 0 and 360 that represents the degrees of the total rotation that the geometry will undergo over the course of the Orientation Study. This _totalAngle should be larger than the _divisionAngle and divisible by the _divisionAngle.
* basePoint_ <Optional>: Input a point here to change the center about which the Orientation Study will rotate the geometry. If no point is connected, the default point of rotation will be the center of the test geometry.
* rotateContext_ <Optional>: Input either a Boolean value or a set of context Breps that should be rotated along with the test geometry. If set this input to "True", all context Breps will be rotated with the test geometry.  The default is set to "False" to only rotate the test geometry.
* _runTheStudy <Required>: [Boolean or GeometryBase] Since orientation study may take a long time, this is an extra

#### Outputs
* orientationStudyPar: A list of Orientation Study parameters that can be plugged into the Ladybug "Radiation Analysis", "Sunlight Hours Analysis", or "View Analysis" component.


[Check Hydra Example Files for Orientation_Study_Parameters](https://hydrashare.github.io/hydra/index.html?keywords=Orientation_Study_Parameters)