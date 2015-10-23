## SolarFanBasic [![IMAGE](images/icons/SolarFanBasic.png)]

![IMAGE](images/components/SolarFanBasic.png)

Use this component to generate a solar fan with minimumal input data. This component predefines monthly and hourly ranges in order to simplify the creation of useful fan geometry.    

#### Inputs
* _boundary <Required>: closed boundary curve representing a piece of land (such as a park) or a window for which solar access is desired.
* _location <Required>: The output from the importEPW or constructLocation component.  This is essentially a list of text summarizing a location on the earth.
* _requiredHours <Required>: The number of hours of direct solar access that the property inside the boundary curve should receive during the _monthRange. For example an input of 4 will define the hour range roughly between 10AM and 2PM. The component will compute the hour range that will maximize the fan volume. 
* _height <Required>: The number of Rhino model units that the solar fan should be extended above the boundary curve.
* north_ <Optional>: Input a vector to be used as a true North direction or a number between 0 and 360 that represents the degrees off from the y-axis to make North.  The default North direction is set to the Y-axis (0 degrees).
* _monthRange <Required>: An optional interger value to change the month range for which solar access is being considered. The default month range is Jun 21 - Sep 21.

#### Outputs
* out: ...
* solarFan: Brep representing a solar fan.  This volume should be clear of shading in order to ensure solar access to the area inside the boundary curve for the given number of hours.


[Check Hydra Example Files for SolarFanBasic](https://hydrashare.github.io/hydra/index.html?keywords=SolarFanBasic)