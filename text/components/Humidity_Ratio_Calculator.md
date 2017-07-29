## ![](../../images/icons/Humidity_Ratio_Calculator.png) Humidity Ratio Calculator - [[source code]](https://github.com/mostaphaRoudsari/ladybug/tree/master/src/Ladybug_Humidity%20Ratio%20Calculator.py)

![](../../images/components/Humidity_Ratio_Calculator.png)

Calculates the humidity ratio from the ladybug weather file import parameters Conversion formulas are taken from the following publications: Vaisala. (2013) Humidity Conversion Formulas: Calculation Formulas for Humidity. www.vaisala.com/Vaisala%20Documents/Application%20notes/Humidity_Conversion_Formulas_B210973EN-F.pdf W. Wagner and A. Pruß:" The IAPWS Formulation 1995 for the Thermodynamic Properties of Ordinary Water Substance for General and Scientific Use ", Journal of Physical and Chemical Reference Data, June 2002 ,Volume 31, Issue 2, pp. 387535 - 

#### Inputs
* ##### dryBulbTemperature [Required]
The dry bulb temperature from the Import epw component.
* ##### relativeHumidity [Required]
The relative humidity from the Import epw component.
* ##### barometricPressure [Optional]
The barometric pressure from the Import epw component.

#### Outputs
* ##### readMe!
...
* ##### humidityRatio
The hourly humidity ratio (kg water / kg air).
* ##### enthalpy
The hourly enthalpy of the air (kJ / kg).
* ##### partialPressure
The hourly partial pressure of water vapor in the atmosphere (Pa).
* ##### saturationPressure
The saturation pressure of water vapor in the atmosphere (Pa).


[Check Hydra Example Files for Humidity Ratio Calculator](https://hydrashare.github.io/hydra/index.html?keywords=Ladybug_Humidity Ratio Calculator)