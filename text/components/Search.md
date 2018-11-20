## ![](../../images/icons/Search.png) Search - [[source code]](https://github.com/mostaphaRoudsari/ladybug/tree/master/src/Ladybug_Search.py)

![](../../images/components/Search.png)

Use this to look for the components in the Ladybug suite of tools that are most relevant to your query.

#### Inputs
* ##### keyword [Required]
A word. This only accepts text inputs. Example is ("drybulb Temperature" or "tunnel") without quotation marks.
* ##### occurrences [Default]
An integer. This number determines the search resolution. The default value is set to 3. 
* ##### open [Optional]
A boolean. If boolean of True value is provided, primer pages for the components that appear in the result

#### Outputs
* ##### log
Run time messages
* ##### result
The list of components across all Lasybug Tools plugins in which the keyword appears at least the number of times set in


[Check Hydra Example Files for Search](https://hydrashare.github.io/hydra/index.html?keywords=Ladybug_Search)