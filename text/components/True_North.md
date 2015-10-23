## True_North [![IMAGE](images/icons/True_North.png)]

![IMAGE](images/components/True_North.png)

Use this component to calculate Earth's true north from magnetic north.

#### Inputs
* _location <Required>: Input data from Ladybug's "Import epw" "location" output, or create your own location data with Ladybug's "Construct Location" component.
* magneticNorth_ <Optional>: Input a vector to be used as a magnetic North direction, or a number between 0 and 360 that represents the clockwise degrees off from the Y-axis.
* date_ <Optional>: Date for which magnetic north should be calculated. Input a date in the following order: month, day, year.
* COFfile_ <Optional>: By default "Magnetic north" component already has 2015-2020 integrated WMM coefficients data.

#### Outputs
* readMe!: ...
* trueNorth: Geographic north (direction towards the North Pole) - magnetic north corrected for the value of magnetic declination. Ranges from 0-360.
* trueNorthVec: Vector representation of the upper "trueNorth".
* magneticDeclination: An angle between magnetic north and true north. It is positive east of true north and negative west of true north.
* magneticFieldVec: Earth's magnetic field vector at chosen location.


[Check Hydra Example Files for True_North](https://hydrashare.github.io/hydra/index.html?keywords=True_North)