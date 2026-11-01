# Helicopter blade grip design inputs

Status: preliminary; grip geometry and flight strength not validated.

Confirmed inputs
- Total flying mass: 200 g
- Maximum rotor speed: 4000 RPM
- Printed material: PETG
- Radial bearing: 3 mm ID x 6 mm OD x 2.5 mm width
- Shape reference: user-supplied blade grip photograph

Previously supplied, pending confirmation
- Thrust bearing: 3 mm ID x 6 mm OD x 2.8 mm width

Required before sizing the grip
- Blade-root thickness and width
- Blade mounting hole diameter and hole location relative to root end
- Blade length, mass per blade, and center-of-mass location
- Feathering shaft geometry and bearing/washer/spacer retention stack
- Pitch-link attachment location or compatible rotor system
- Printer model and calibrated bearing-fit allowance
- Scope: blade grip only or complete rotor head

Nominal bearing OD is not automatically the finished printed pocket diameter.
Determine the pocket allowance with a calibration coupon on the intended printer.
PETG fit prototypes are not approved for powered rotor operation.
CAD and prototype mesh generated; see prototype notes below.

## Prototype generated
Files: grip-fit-prototype.f3d, .step, .stl, grip-preview.png, create-grip.py.
Fusion reports one solid body, 2.1316 cubic centimetres volume.
Overall bounding box: 12 x 23 x 28 mm.
Assumed blade gap: 4 mm; cheeks: 3 mm each; blade bolt hole: 2.2 mm.
Housing: 12 mm OD, 12 mm axial length.
Bearing pocket: 6.15 mm diameter, provisional printer allowance.
Inner radial pocket: z=0 to 2.5 mm.
Shoulder: z=2.5 to 3.9 mm, bore 4.8 mm.
Outer radial/thrust access pocket: z=3.9 to 12 mm.
Bearing shoulder, washer clearance, retention stack, blade root, and pitch-arm position require measured verification.
The source images are not dimensioned manufacturing drawings; this is a simplified reference-based prototype, not an exact replacement.
STL is for unpowered fit checking only. Do not spin this prototype.
Metal bearings and spacers do not remove the loads transmitted through the plastic grip.

