## ![](../../images/icons/MRT_Calculator.png) MRT Calculator - [[source code]](https://github.com/mostaphaRoudsari/ladybug/tree/master/src/Ladybug_MRT%20Calculator.py)

![](../../images/components/MRT_Calculator.png)

Use this component calculate Mean Radiant Temperature (MRT) given a set of temperatures and corresponding view factors.  This component will check to be sure view factors add to 1 and will use the following formula: MRT = (V1*T1^4 + V2*T2^4 + ...) ^ (1/4) Where V corresponds to a view factor and T corresponds to a temperature. - 

#### Inputs
* ##### temperatures [Required]
A list of radiant temperatures that correspond to view factors below.
* ##### viewFactors [Required]
A list of viewFactors that correspond to the temperatures above.  These should sum to 1.

#### Outputs
* ##### MRT
The Mean Radiant Temperature that results from the input temperatures and view factors.


[Check Hydra Example Files for MRT Calculator](https://hydrashare.github.io/hydra/index.html?keywords=Ladybug_MRT Calculator)