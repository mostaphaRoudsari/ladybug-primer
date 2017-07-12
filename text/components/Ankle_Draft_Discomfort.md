## ![](../../images/icons/Ankle_Draft_Discomfort.png) Ankle Draft Discomfort

![](../../images/components/Ankle_Draft_Discomfort.png)

Use this component to calculate discomfort from cold drafts at ankle-level.  The original tests used to create the model involved blowing cold air on subject's ankles at a height of 10 cm off of the ground.

#### Inputs
* ##### fullBodyPMV [Required]
The predicted mean vote (PMV) of the subject.  This can be calculated using the "Ladybug_PMV Comfort Calculator" component.  The reason for why PMV is incorporated into this draft discomfort model is that people are likely to feel more uncomfortable from downdraft when their whole body is already feeling cold.
* ##### draftAirVeloc [Required]
The velocity of the draft in m/s.

#### Outputs
* ##### PPD
Script variable Python


[Check Hydra Example Files for Ankle Draft Discomfort](https://hydrashare.github.io/hydra/index.html?keywords=Ladybug_Ankle Draft Discomfort)