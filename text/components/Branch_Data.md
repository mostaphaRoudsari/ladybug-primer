## ![](../../images/icons/Branch_Data.png) Branch Data - [[source code]](https://github.com/ladybug-tools/ladybug-legacy/tree/master/src/Ladybug_Branch%20Data.py)

![](../../images/components/Branch_Data.png)

Use this component to convert any list of annual data into a data tree branched by day of the year, month of the year, or hour of the day. If the data is not 8760 value sof each hour, the number of _data items should match number of items in HOY_. - 

#### Inputs
* ##### data [Required]
A list of data to be branched for each month, day and hour.  Note that this can be either a list of 8760 values for each hour of the year, the output of the "Import EPW" component, or a custom list of data that is matched by the data in the HOY_ input.
* ##### HOY [Optional]
A list of numbers between 1 and 8760 that represents an hour of the year.

#### Outputs
* ##### dataEachDayOfYear
The input data that has been branched data for each day of the year. The paths of the branches are in the following format {month ; dayOfMonth}.
* ##### dataEachMonth
The input data that has been branched for each month of the year. Branch paths are from 0 to 11.
* ##### dataEachHourOfDay
The input data that has been branched for each hour of the day. Branches are from 0 to 23.


[Check Hydra Example Files for Branch Data](https://hydrashare.github.io/hydra/index.html?keywords=Ladybug_Branch Data)