## Clothing_Function [![IMAGE](images/icons/Clothing_Function.png)]

![IMAGE](images/components/Clothing_Function.png)

Use this component to generate a list of values representing a clothing schedule based on outdoor air temperature.  This schedule can be plugged into the clothingLevel_ input of the PMV Comfort Calculator component.

#### Inputs
* _outdoorAirTemperature <Required>: A number or list of numbers representing the dry bulb temperature of the air in degrees Celcius.  This input can also accept the direct output of dryBulbTemperature from the Import EPW component and this is recommended for hourly comfort analysis.
* analysisPeriod_ <Optional>: If you have hooked up annual temperatures from the importEPW component, use this input to 
* maxClo_ <Optional>: An optional number representing the maximum clo value that someone will wear on the coldest days of the outdoorAirTemperature input.  The default is set to 1 clo, which corresponds to a 3-piece suit.
* maxCloTemp_ <Optional>: An optional number representing the temperature at which the maxClo_ value will be applied.  The default is set to -5C, which means that any lower temperature will get the maxClo_ value.
* minClo_ <Optional>: An optional number representing the minimum clo value that someone will wear on the hotest days of the outdoorAirTemperature input.  The default is set to 0.46 clo, which corresponds to shorts and a T-shirt.
* minCloTemp_ <Optional>: An optional number representing the temperature at which the minClo_ value will be applied.  The default is set to 26C, which means that any higher temperature will get the minClo_ value.

#### Outputs
* readMe!: ...
* cloValues: A list of numbers representing the clothing that would be worn at each hour of the _outdoorAirTemperature.  Note that, if the component senses that you have hooked up a stream of hourly data, the clothing levels will alternate on a 12-hour basis.


[Check Hydra Example Files for Clothing_Function](https://hydrashare.github.io/hydra/index.html?keywords=Clothing_Function)