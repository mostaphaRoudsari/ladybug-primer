## ![](../../images/icons/Mesh_Threshold_Selector.png) Mesh Threshold Selector

![](../../images/components/Mesh_Threshold_Selector.png)

Use this component to delete out unwanted areas of a shade after a shade benefit evaluation has been run.  This will help turn your shade evaluation results into an actual shade brep based on a percentage of beneficial shade cells that you decide. - 

#### Inputs
* ##### inputMesh [Required]
The mesh for which you would like to highlight the portion that meets a threshold.
* ##### analysisResult [Required]
A numerical data set whose length corresponds to the number of faces in the _inputMesh.
* ##### percentToKeep [Optional]
A number between 0 and 100 that represents the percentage of the mesh faces that you would like to include in the resulting newColoredMesh.  By default, this is set to 25%.
* ##### levelOfPerform [Optional]
An optional number that represents the threshold above which a given mesh face is included in the newColoredMesh.  An input here will override the percent input above.

#### Outputs
* ##### readMe!
...
* ##### totalValue
The sum of all of the values that meet the criteria multiplied by the mesh face area.  For example, if the _inputMesh is a radiation study mesh, this is equal to the total radiation falling on the newColoredMesh.  For an energy shade benefit mesh, this is the total energy saved by a shade of this size.
* ##### areaMeetsThresh
The area of the newColoredMesh in Rhino model units.
* ##### newColoredMesh
A new colored mesh with the vlues below the threshold deleted out of it.
* ##### newMeshOutline
A set of curves outlining the portion of the mesh that is above the threshold.


[Check Hydra Example Files for Mesh Threshold Selector](https://hydrashare.github.io/hydra/index.html?keywords=Ladybug_Mesh Threshold Selector)