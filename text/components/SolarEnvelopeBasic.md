## SolarEnvelopeBasic [![IMAGE](images/icons/SolarEnvelopeBasic.png)]

![IMAGE](images/components/SolarEnvelopeBasic.png)

Use this component to generate a solar envelope for a closed boundary curve with minimum inputs. This component predefines monthly and hourly ranges in order to simplify the creation of useful envelope geometry.  

#### Inputs
* _boundary <Required>: A closed boundary curve representing a piece of land (such as a property to be developed) for which solar access of the surrounding land is desired.
* _location <Required>: The output from the importEPW or constructLocation component.  This is essentially a list of text summarizing a location on the earth.
* _requiredHours <Required>: The number of hours of direct solar access that the property surrounding the boundary curve should receive during the _monthRange. For example an input of 4 will define the hour range roughly between 10AM and 2PM. The component will compute the hour range that will maximize the envelope volume.        
* north_ <Optional>: Input a vector to be used as a true North direction or a number between 0 and 360 that represents the degrees off from the y-axis to make North.  The default North direction is set to the Y-axis (0 degrees).
* _monthRange <Required>: An optional interger value to change the month range for which solar access is being considered. The default month range is Jun 21 - Dec 21.

#### Outputs
* readMe!: ...
* solarEnvelope: A Brep representing a solar envelope.  This volume should be built within in order to ensure that the surrounding property is not shaded for the given number of hours.


[Check Hydra Example Files for SolarEnvelopeBasic](https://hydrashare.github.io/hydra/index.html?keywords=SolarEnvelopeBasic)