# Grip structural screening — not an FEA result

## Result status
Fusion Simulation workspace activation succeeded, but adsk.sim.Simulations.get(activeDocument) returned null before and after activation. No finite-element study was created, meshed, or solved. No safety factor or flight approval has been established. The original CAD files have not been changed.

The accompanying CSV is a calculated centrifugal-load parameter sweep, not a simulated stress contour. All blade masses and center-of-mass radii in it are hypothetical scenarios.

## Confirmed inputs
Maximum speed 4000 RPM; total flying mass 200 g; intended PETG grip; metal bearings, spacers and other hardware.

## Method and units
Angular speed omega = 2*pi*RPM/60 = 418.879 radians/second.
Blade centrifugal force F = blade mass (kg) * blade COM radius from rotor axis (m) * omega^2.
The radius must be measured from the main rotor axis, not from the grip bolt.
At fixed mass and radius, force varies with RPM squared.

Screening areas taken from the provisional CAD:
- Two cheeks, each 3 mm thick and 10 mm wide, with a 2.2 mm bolt hole.
- Net tensile area = 2*3*(10-2.2) = 46.8 mm^2.
- Projected bolt-bearing area = 2*3*2.2 = 13.2 mm^2.
- Illustrative shoulder contact area = pi/4*(6^2-4.8^2) = 10.179 mm^2.

Stress/pressure = force / area, with N/mm^2 equivalent to MPa. Both cheeks are assumed to share force equally. The shoulder pressure assumes a flat 6 mm OD metal ring contacting a 4.8 mm ID shoulder. Actual bearing race contact, thrust load path and stack alignment have not been established; the shoulder calculation is only a sensitivity estimate.

## Example
For a 5 g blade with its center of mass 100 mm from the main axis:
- Outward force: 87.73 N per blade.
- Nominal cheek net tension: 1.88 MPa.
- Nominal projected bolt-bearing pressure: 6.65 MPa.
- Illustrative shoulder contact pressure: 8.62 MPa.
These are different stress measures in different regions; they must not be added or read as peak von Mises stress.

The helicopter weight is about 1.96 N. That is the total thrust required for steady hover, not the blade retention load. The rotor blade centrifugal forces largely balance at the hub but each grip still carries its own blade load.

## Exclusions
No local stress concentrations, cheek bending, bolt preload, contact/separation, shoulder bending/shear, grip self centrifugal load, thrust/lift bending, pitch-link loads, vibration, fatigue, creep, temperature or layer-direction effects are included. These simplified stresses can understate critical stresses. No printed PETG strength or elastic modulus was assumed; no pass/fail decision or deflection is calculated.

## Required for a meaningful structural simulation
1. Blade mass and center-of-mass radius from the main rotor axis.
2. Measured blade root and bolt dimensions, hub/shaft dimensions, and bearing/washer/spacer stack with retention details.
3. Printed PETG directional test data, print orientation, material brand, process settings, operating temperature, and design life/load spectrum.
4. Verified metal/plastic contact areas and a defensible representation of shaft support and pitch loads.
5. A mesh-refinement check on the finalized geometry, followed by physical validation.

The current sharp cheek-to-housing transitions and unverified bearing shoulder deserve particular attention in the next design revision. Material selection alone does not establish adequate strength.

Do not spin the fit prototype based on this screening calculation.

References:
- Autodesk static stress assumptions: https://help.autodesk.com/cloudhelp/ENU/Fusion-Simulate/files/SIM-STATIC-STRESS-ANALYSIS.htm
- Autodesk simulation material limitation: https://www.autodesk.com/support/technical/article/caas/sfdcarticles/sfdcarticles/Some-components-are-using-a-material-with-invalid-properties-in-simulation-precheck-in-Fusion-360.html

