## ![](../../images/icons/Draft_Discomfort.png) Draft Discomfort

![](../../images/components/Draft_Discomfort.png)

Use this component to calculate discomfort from cold drafts on the back of the neck (arguably the most sensitive part of the human body to cold drafts).  This model was derived from empircal tests that involved blowing cold air on the back of subjects's necks who were otherwise at thermally neutral conditions by the pmv standard.   _ This model used to be the standard endorsed by ASHRAE 55 and EN-12521 for all draft cases but has since been replaced with a model that more accurately targets draft discomfort at foot level. The paper in which this model was published can be found here: _ Fanger, P.O., Melikov, A.K., Hanzawa, H., Ring, J. “Air Turbulence and Sensation of Draught.” Energy and Buildings 12, no. 1 (1988): 21–39. - 

#### Inputs
* ##### draftAirTemp [Required]
The air temperature of the draft in degrees Celcius.
* ##### draftAirVeloc [Required]
The velocity of the draft in m/s.

#### Outputs
* ##### PPD
Script variable Python


[Check Hydra Example Files for Draft Discomfort](https://hydrashare.github.io/hydra/index.html?keywords=Ladybug_Draft Discomfort)