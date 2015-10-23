## Humidity_Ratio_Calculator [![IMAGE](images/icons/Humidity_Ratio_Calculator.png)]

![IMAGE](images/components/Humidity_Ratio_Calculator.png)

Calculates the humidity ratio from the ladybug weather file import parameters

#### Inputs
* _dryBulbTemperature <Required>: The dry bulb temperature from the Import epw component.
* _relativeHumidity <Required>: The relative humidity from the Import epw component.
* _barometricPressure <Required>: The barometric pressure from the Import epw component.

#### Outputs
* readMe!: ...
* humidityRatio: The hourly humidity ratio (kg water / kg air).
* enthalpy: The hourly enthalpy of the air (kJ / kg).
* partialPressure: The hourly partial pressure of water vapor in the atmosphere (Pa).
* saturationPressure: The saturation pressure of water vapor in the atmosphere (Pa).


[Check Hydra Example Files for Humidity_Ratio_Calculator](https://hydrashare.github.io/hydra/index.html?keywords=Humidity_Ratio_Calculator)