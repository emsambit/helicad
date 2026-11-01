# R2 research and revision notes

Research date: 2026-11-01.

## Verified sources
Mikado LOGO 200 official manual:
https://www.mikado-heli.de/downloads/anleitungen/200/Logo%20200%20Manual%20V4.pdf
- Identifies VTX 177 blades, part 05406.
- Main blade mounting uses M2x12 bolts, M2 sleeves, M2 nuts and 10x2.1x0.3 mm washers.
- Head hardware: 3x6x2.5 mm radial bearings, 3x6x2.8 mm thrust bearings, 3.1x4.5x0.1 mm washers.
- The spacer is labeled 3x4.4x1.4 mm in the exploded view; the list shows 3x4x1.4 mm. Resolve this discrepancy against actual hardware.

## Search limitations
No verified manufacturer dimensions were found for blade-root thickness or width, sleeve OD, blade mass or balance point. These have NOT been inferred from pictures or substituted from other blade models.
VTX 177 is the official blade designation; it does not establish a precise grip interface or the measurement convention for blade length.

## R2 geometry
Rounded semicircular blade-grip ends, radius 5 mm, centered on the blade bolt.
Rounded pitch arm end, radius 2 mm; arm widens toward housing.
One Fusion solid body, volume 2.08336 cm^3; bounding box 12 x 22.5 x 28 mm.
No metal hardware is included in the exported printable body.

Retained assumptions, NOT verified LOGO 200 interfaces:
- 4 mm blade gap; 3 mm cheeks; 10 mm cheek width.
- 2.2 mm grip bolt clearance, intended for an M2 bolt. Actual sleeve fit is unresolved.
- 6.15 mm bearing pocket diameter, including an uncalibrated 0.15 mm diametral printing allowance.
- Housing OD 12 mm, length 12 mm; internal shoulder bore 4.8 mm, thickness 1.4 mm.
- Radial pocket at z=0..2.5; outer access pocket z=3.9..12 mm.
- Pitch attachment hole 1.8 mm, positioned 14.5 mm from bearing axis; all linkage geometry provisional.

The bearing access pocket is not a verified axial-retention design. The spacer dimensions do not alone locate the housing shoulder or establish thrust-race seating. Round ends improve reference resemblance; no increased structural strength has been demonstrated.

## Verification
Fusion creation returned one solid body and exported F3D, STEP and STL. Preview visually inspected. No structural solve was completed; the earlier load screening is not an R2 simulation. No printed fit, tolerance, fatigue, layer strength or flight validation performed.

R2 is an unpowered fit prototype, not an exact LOGO 200 replacement or flight-ready rotor grip. Print one for measurement only; do not spin it.
