## ![](../../images/icons/Ankle_Draft_Discomfort.png) Ankle Draft Discomfort - [[source code]](https://github.com/ladybug-tools/ladybug-legacy/tree/master/src/Ladybug_Ankle%20Draft%20Discomfort.py)

![](../../images/components/Ankle_Draft_Discomfort.png)

Use this component to calculate discomfort from cold drafts at ankle-level.  The original tests used to create the model involved blowing cold air on subject's ankles at a height of 10 cm off of the ground. _ The formula has been submitted to be incorporated in the ASHRAE 55 standard with a recommendation that PPD from ankle draft not exceed 20%.  The papers in which this model is published can be found here: _ Schiavon, S., D. Rim, W. Pasut, W. Nazaroff. 2016. Sensation of draft at uncovered ankles for women exposed to displacement ventilation and underfloor air distribution systems. Building and Environment, 96, 228–236. _ Liu, S., S. Schiavon, A. Kabanshi, W. Nazaroff. 2016. Predicted percentage of dissatisfied with ankle draft. Accepted Author Manuscript. Indoor Environmental Quality. http://escholarship.org/uc/item/9076254n - 

#### Inputs
* ##### fullBodyPMV [Required]
The predicted mean vote (PMV) of the subject.  This can be calculated using the "Ladybug_PMV Comfort Calculator" component.  The reason for why PMV is incorporated into this draft discomfort model is that people are likely to feel more uncomfortable from downdraft when their whole body is already feeling cold.
* ##### draftAirVeloc [Required]
The velocity of the draft in m/s.

#### Outputs
* ##### PPD
Script variable Python


[Check Hydra Example Files for Ankle Draft Discomfort](https://hydrashare.github.io/hydra/index.html?keywords=Ladybug_Ankle Draft Discomfort)