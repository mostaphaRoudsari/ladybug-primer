## ![](../../images/icons/Shading_Mask.png) Shading Mask

![](../../images/components/Shading_Mask.png)

Use this component to see the portion of the sky dome that is masked by context geometry around a given viewpoint. The component will generate separate meshs for the portions of the sky dome that are masked and visible. The component will also calculate the percentage of the sky that is masked by the context geometry and the percentage that is visible (the sky view factor). - 

#### Inputs
* ##### testPt [Required]
A view point for which one wants to see the portion of the sky masked by the context geometry surrounding this point.
* ##### context [Required]
Context geometry surrounding the _testPt that could block the view to the sky.  Geometry must be a Brep or list of Breps.
* ##### skyDensity [Default]
An integer that is greater than or equal to 0, which to sets the number of times that the Tergenza sky patches are split.  Set to 0 to view a sky mask with the typical Tregenza sky, which will divide up the sky with a coarse density of 145 sky patches.  Set to 1 to view a sky mask of a Reinhart sky, which will divide up each of these Tergenza patches into 4 patches to make a sky with a total of 580 sky patches. Higher numbers input here will ensure a greater accuracy but will also take longer. The default is set to 3 to give you a high accuracy.
* ##### scale [Optional]
Scale of the sky dome

#### Outputs
* ##### masked
A mesh of the portion of the sky dome masked by the _context geometry.
* ##### visible
A mesh of the portion of the sky dome visible by the _testPt through the _context geometry.
* ##### percMasked
The percentage of the sky masked by the _context geometry at the _testPt.
* ##### skyView
The percentage of the sky visible by the _testPt through the _context geometry.


[Check Hydra Example Files for Shading Mask](https://hydrashare.github.io/hydra/index.html?keywords=Ladybug_Shading Mask)