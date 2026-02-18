# 2018 scan_3d
 
# 3D Reconstruction from Fringe Pattern Projection

with a very strict NDA 

Development time 15 months (aprox)

## 1. Introduction

3D surface measurement is essential in:

    * Industrial inspection
    * Reverse engineering
    * Medical imaging
    * Cultural heritage preservation
    * Non-contact optical methods are widely used
    * Fringe Projection Profilometry (FPP) is a high-precision structured light technique

## 2. What is Fringe Projection?

    * A structured light method
    * A projector casts sinusoidal fringe patterns onto an object
    * A camera captures the deformed fringe image
    * Deformation encodes surface height information

Basic Idea:
    Flat surface → straight fringes
    Object surface → distorted fringes

|   |  |
|---|--|
|graphical explanation |![database sample ](/source/imagens/patron1.png)| 
||![comparative sample ](/source/imagens/patron2.png)| 
||![comparative sample ](/source/imagens/patron3.png)| 



## 3. Complete Reconstruction Pipeline

   * Project fringe patterns
   * Capture deformed images
   * Compute wrapped phase
   * Perform phase unwrapping
   * Convert phase to depth
   * Generate 3D point cloud
   * Mesh reconstruction

## 4. Advantages

   * High accuracy (micron-level possible)
   * Non-contact
   * Fast measurement
   * Suitable for complex surfaces

## 5. Limitations

   * Sensitive to ambient light
   * Reflective surfaces cause errors
   * Shadows and occlusions
   * Phase unwrapping errors

## 6. Applications

   * Industrial quality inspection
   * Reverse engineering
   * Biomedical surface measurement
   * 3D scanning systems
   * Microstructure analysis


