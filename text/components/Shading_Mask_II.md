## Shading_Mask_II [![IMAGE](images/icons/Shading_Mask_II.png)]

![IMAGE](images/components/Shading_Mask_II.png)

Use this component to see the portion of the sky dome that is masked by context geometry around a given viewpoint.

#### Inputs
* _testPt <Required>: A view point for which one wants to see the portion of the sky masked by the context geometry surrounding this point.
* _context <Required>: Context geometry surrounding the _testPt that could block the view to the sky.  Geometry must be a Brep or list of Breps.
* radius_ <Optional>: Scale of the sky dome
* merge_ <Optional>: Script variable shadingMask

#### Outputs
* maskedSrfOnGound: Script variable Python
* maskedCrvsOnSky: Script variable shadingMask
* maskedSkyDome: Script variable shadingMaskII
* unmaskedSkyDome: Script variable shadingMaskII


[Check Hydra Example Files for Shading_Mask_II](https://hydrashare.github.io/hydra/index.html?keywords=Shading_Mask_II)