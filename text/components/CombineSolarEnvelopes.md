## ![](../../images/icons/CombineSolarEnvelopes.png) CombineSolarEnvelopes - [[source code]](https://github.com/ladybug-tools/ladybug-legacy/tree/master/src/Ladybug_CombineSolarEnvelopes.py)

![](../../images/components/CombineSolarEnvelopes.png)

Use this component to combine two or more solar envelopes from Ladybug_SolarEnvelope component - 

#### Inputs
* ##### baseSrf [Required]
A surface representing the area for which you want to create the solar envelope (could also be a closed planer curve). Must be the same as the _BaseSrf connected to the solar Envelope component.
* ##### envelopePts [Required]
A list of 3d points representing the heights to which the solar envelope reaches. Use the envelopePts output from the solar envelope component.
* ##### HighestEnv [Optional]
if HighestEnv_ is True we'll take the highest points and if it's False we'll take the lowest ones. Default value is True
* ##### gridSize [Required]
A numeric value inidcating the gird size of the analysis in Rhino model units. Muse be the same as the gridSize_ value connected to the solar Envelope component.

#### Outputs
* ##### newEnvPoints
A list of 3d points representing the heights to which the solar envelope reaches.  Plug into a native GH 'Delunay Mesh' component to visualize the full solar envelope.
* ##### envelopeBrep
Brep representing the envelope.


[Check Hydra Example Files for CombineSolarEnvelopes](https://hydrashare.github.io/hydra/index.html?keywords=Ladybug_CombineSolarEnvelopes)