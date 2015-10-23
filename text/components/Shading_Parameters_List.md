## ![](../../images/icons/Shading Parameters List.png) Shading_Parameters_List

![](../../images/components/Shading_Parameters_List.png)

Use this component to generate shading depths, numbers of shades, horizontal or vertical boolean values, and shade angles for different cardinal directions to be plugged into the "Ladybug_Shading Designer" component or the "Honeybee_EnergyPlus Window Shade Generator". - 

#### Inputs
* ##### northShdParam [Default]
Shading parameter for north-facing glazing.
* ##### westShdParam [Default]
Shading parameter for west-facing glazing.
* ##### southShdParam [Default]
Shading parameter for south-facing glazing.
* ##### eastShdParam [Default]
Shading parameter for east-facing glazing.

#### Outputs
* ##### shdParamList
A list of shading parameters for different cardinal directions to be plugged into either the input of the "ShadingDesigner" component or the "Honeybee_EnergyPlus Window Shade Generator".  Depending on the type of values that you input, these can go into either of these inputs: _depth, _numOfShds, _distBetween, _horOrVertical_, _shdAngle_.


[Check Hydra Example Files for Shading Parameters List](https://hydrashare.github.io/hydra/index.html?keywords=Ladybug_Shading Parameters List)