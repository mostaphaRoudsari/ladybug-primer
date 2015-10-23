## Orient_to_Camera [![IMAGE](images/icons/Orient_to_Camera.png)]

![IMAGE](images/components/Orient_to_Camera.png)

Use this component to generate a plane that is oriented perpendicular to the active Rhino viewport camera direction and centered at an input _initPosition point.

#### Inputs
* _initPosition <Required>: A point or list of points that will act as the origin9s0 of the plane(s) that will be generated.
* refresh_ <Optional>: Connect either a Grasshopper "button" component that will allow you to refresh the plane orientation upon hitting the button or a Grasshopper "Timer" component to see the plane update in real time as you navigate through the Rhino viewport.

#### Outputs
* orientedToCam: A plane (or list of planes) for each _initPosition connected. All planes are oriented perpendicular to the active Rhino viewport camera direction and are centered at initPosition points.


[Check Hydra Example Files for Orient_to_Camera](https://hydrashare.github.io/hydra/index.html?keywords=Orient_to_Camera)