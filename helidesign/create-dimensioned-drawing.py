import json,csv,math,hashlib
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A3,landscape
from reportlab.lib.colors import HexColor,black,white
import pypdfium2 as pdfium
D=Path(r'C:/Users/Sambit Baliarsingh/Documents/Codex/2026-11-01/i-h/outputs/helidesign')
G=json.loads((D/'r7-drawing-geometry.json').read_text())
OUT=D/'grip-r7-dimensioned-reference.pdf'
W,H=landscape(A3); C=canvas.Canvas(str(OUT),pagesize=(W,H))
C.setTitle('Helicad R7 - Dimensioned reference drawing - not for manufacture')
BLUE=HexColor('#163c59');GRAY=HexColor('#647280');RED=HexColor('#a63124')
def text(x,y,s,size=10,color=black,bold=False):
 C.setFillColor(color);C.setFont('Helvetica-Bold' if bold else 'Helvetica',size);C.drawString(x,y,s)
def line(x1,y1,x2,y2,color=black,width=.6):
 C.setStrokeColor(color);C.setLineWidth(width);C.line(x1,y1,x2,y2)
def arrow(x,y,ang):
 C.setFillColor(BLUE);p=C.beginPath();p.moveTo(x,y)
 for a in [ang+.35,ang-.35]:p.lineTo(x+6*math.cos(a),y+6*math.sin(a))
 p.close();C.drawPath(p,fill=1,stroke=0)
def hd(x1,x2,y,ey,label):
 for x in [x1,x2]:line(x,ey,x,y+5,GRAY,.35)
 line(x1,y,x2,y,BLUE);arrow(x1,y,0);arrow(x2,y,math.pi)
 C.setFont('Helvetica',10);tw=C.stringWidth(label,'Helvetica',10);C.setFillColor(white);C.rect((x1+x2-tw)/2-4,y-3,tw+8,13,fill=1,stroke=0)
 text((x1+x2-tw)/2,y,label,10,BLUE)
def vd(y1,y2,x,ex,label):
 for y in [y1,y2]:line(ex,y,x+5,y,GRAY,.35)
 line(x,y1,x,y2,BLUE);arrow(x,y1,math.pi/2);arrow(x,y2,-math.pi/2)
 C.saveState();C.translate(x-6,(y1+y2)/2);C.rotate(90);text(-C.stringWidth(label,'Helvetica',10)/2,0,label,10,BLUE);C.restoreState()
def base(page,title):
 C.setFillColor(white);C.rect(0,0,W,H,fill=1,stroke=0)
 text(34,H-42,'HELICAD / R7',22,BLUE,True);text(34,H-65,title,12,GRAY)
 text(W-380,H-43,'REFERENCE ONLY - NOT FOR MANUFACTURE',12,RED,True)
 line(34,H-80,W-34,H-80,BLUE,1)
 line(34,48,W-34,48,BLUE)
 text(34,29,'Units: mm | CAD revision: R7 | Dimension tolerances: TBD | Do not scale drawing',9,GRAY)
 text(W-195,29,f'2026-11-01 | Sheet {page} of 2',9,GRAY)
def proj(ox,oy,axes,scale=9):
 for edge in G['edges']:
  p=C.beginPath()
  for i,v in enumerate(edge):
   x=ox+v[axes[0]]*scale;y=oy+v[axes[1]]*scale
   if i==0:p.moveTo(x,y)
   else:p.lineTo(x,y)
  C.setStrokeColor(HexColor('#48545d'));C.setLineWidth(.48);C.drawPath(p)
def leader(x,y,tx,ty,label):
 line(x,y,tx-6,ty+3,BLUE,.5);C.setFillColor(BLUE);C.circle(x,y,1.8,fill=1,stroke=0);text(tx,ty,label,10,BLUE)
base(1,'Actual CAD wireframe projections with nominal dimensions')
# Side: horizontal Z, vertical Y. Pitch arm is included in the projection.
ox,oy,s=110,480,10
proj(ox,oy,(2,1),s)
text(ox,720,'VIEW ALONG X / Z horizontal, Y vertical',11,BLUE,True)
hd(ox,ox+29.5*s,395,oy-60,'29.50 overall Z')
vd(oy-6*s,oy+16*s,65,ox,'22.00 overall Y')
hd(ox,ox+25*s,680,oy+45,'25.00 blade-bolt axis from z=0')
leader(ox+25*s,oy,410,470,'2.20 DIA through both cheeks')
leader(ox+15.8*s,oy+3.4*s,410,550,'Oval: 6.80 wide x 8.40 long')
text(110,365,'Cheek end R4.50; cheek width 9.00; oval ends z=11.60 and 20.00.',10)
# Along Y: horizontal Z vertical X
ox2,oy2=110,200
proj(ox2,oy2,(2,0),10)
text(110,315,'VIEW ALONG Y / Z horizontal, X vertical',11,BLUE,True)
vd(oy2-60,oy2+60,65,110,'12.00 overall X')
vd(oy2-20,oy2+20,445,405,'4.00 blade gap')
leader(ox2+22*10,oy2+35,490,255,'3.00 cheek thickness, each side')
text(110,90,'Top/blade end: z=29.50. Bottom/bearing opening: z=0.',10,GRAY)
# end-on + preview right column
text(675,720,'END VIEW / looking along Z',11,BLUE,True)
proj(790,530,(0,1),8)
hd(790-6*8,790+6*8,450,530-48,'12.00 housing DIA')
leader(790+4*8,530+14*8,880,655,'Pitch hole 1.80 DIA')
text(675,422,'Pitch-hole axis: x=4.00, y=14.00; parallel to Z.',10)
C.drawImage(str(D/'grip-r7-preview.png'),660,110,width=450,height=337.5,preserveAspectRatio=True,mask='auto')
text(680,91,'Isometric view: not to scale.',9,GRAY)
text(34,H-105,'Projections include visible and hidden CAD edges without hidden-line classification. STEP remains authoritative.',10,GRAY)
C.showPage()
base(2,'Dimension schedule, axial stack and tolerance status')
rows=[
('Overall envelope','X=12.00; Y=22.00; Z=29.50','Measured CAD bounds'),
('Round outer housing','DIA 12.00; z=0 to 8.00','Nominal / provisional'),
('Housing-to-fork loft','z=8.00 to 12.00','Exact surface in STEP'),
('Loft end envelope','X=10.00; Y=9.00 at z=12.00','Nominal / provisional'),
('Fork cheeks','3.00 thick each; 4.00 clear gap','Nominal / provisional'),
('Fork cheeks X locations','-5.00 to -2.00; +2.00 to +5.00','Nominal / provisional'),
('Fork end / bolt axis','R4.50; axis at y=0, z=25.00','Nominal / provisional'),
('Blade bolt holes','DIA 2.20 through X, both cheeks','Sleeve fit unverified'),
('Oval access','6.80 wide in Y; 8.40 long in Z','Nominal'),
('Oval access location','z=11.60 to 20.00; center y=0','Through both cheeks / X'),
('Bottom bearing pocket','DIA 6.15; z=0 to 9.30','Print allowance only'),
('Terminal shoulder','z=9.30 to 10.70; thickness 1.40','Retention unverified'),
('Shoulder center bore','DIA 4.80','Washer passage restricted'),
('Upper relief cut','DIA 6.15; z=10.70 to 17.60','Interrupted by access slot'),
('Pitch arm thickness','4.00; z=2.00 to 6.00','Nominal / provisional'),
('Pitch hole','DIA 1.80; axis at x=4.00, y=14.00','Parallel to Z; no thread'),
('Pitch arm nose','R2.00; center x=4.00, y=14.00','Exact outline in STEP'),
]
x,y=34,H-112; widths=[185,330,255];rh=25
for i,label in enumerate(['FEATURE','NOMINAL CAD DIMENSION (mm)','STATUS']):
 xx=x+sum(widths[:i]);C.setFillColor(BLUE);C.rect(xx,y-rh,widths[i],rh,fill=1,stroke=0);text(xx+8,y-17,label,9,white,True)
y-=rh
for idx,row in enumerate(rows):
 for i,val in enumerate(row):
  xx=x+sum(widths[:i]);C.setFillColor(HexColor('#eff3f6') if idx%2==0 else white);C.rect(xx,y-rh,widths[i],rh,fill=1,stroke=0);text(xx+8,y-17,val,9)
 y-=rh
# right axial stack section diagram: z upwards
sx,sy,sc=990,195,28
text(855,710,'AXIAL STACK / schematic',11,BLUE,True)
text(855,691,'z=0 at bottom opening; not to scale',9,GRAY)
parts=[('Inner radial',0,2.5,6),('Spacer',2.5,3.9,4.4),('Outer radial',3.9,6.4,6),('Washer',6.4,6.5,4.5),('Thrust assembly',6.5,9.3,6)]
for k,(name,z0,z1,od) in enumerate(parts):
 C.setFillColor(HexColor(['#ccd9e5','#e9d8a7','#ccd9e5','#b89651','#c3d7c8'][k]));C.setStrokeColor(GRAY);C.setLineWidth(.5)
 C.rect(sx-od*8,sy+z0*sc,od*16,max((z1-z0)*sc,1),fill=1,stroke=1)
 # nominal shaft opening
 C.setFillColor(white);C.rect(sx-12,sy+z0*sc,24,max((z1-z0)*sc,1),fill=1,stroke=0)
 text(855,sy+(z0+z1)*sc/2,name,9)
for z in [0,2.5,3.9,6.4,6.5,9.3,10.7]:
 yy=sy+z*sc;line(sx+55,yy,sx+65,yy,GRAY)
 # closely spaced washer levels are listed separately in schedule
 if z not in [6.4,6.5]:text(sx+70,yy-3,f'{z:.2f}',9)
C.setFillColor(HexColor('#d3d5d7'));C.rect(sx-49.2,sy+9.3*sc,98.4,1.4*sc,fill=1,stroke=0)
C.setFillColor(white);C.rect(sx-38.4,sy+9.3*sc,76.8,1.4*sc,fill=1,stroke=0)
text(855,510,'Shoulder: 9.30 to 10.70',9)
text(855,171,'Washer: z=6.40 to 6.50',9)
text(855,151,'Insert from bottom, deepest first:',9,BLUE,True)
for i,t in enumerate(['Thrust > washer > outer radial', '> spacer > inner radial']):text(855,134-i*15,t,9)
# notes under table
ny=y-24
notes=[
'TOLERANCES: Not specified. No general +/- tolerance, bearing fit class, coaxiality, finish or mould shrinkage is released.',
'DIA 6.15 includes an uncalibrated 0.15 diametral allowance over DIA 6 bearings. Do not transfer this fit to aluminium.',
'All dimensions describe the existing prototype; they are not validated OEM interface requirements.',
'Material: intended PETG was discussed; CAD last inspected as default Steel. Material/process selection is unresolved.',
'No structural FEA, fatigue test or flight validation. Shaft retention, preload and thrust-race contact require redesign/review.',
'For complete pitch-arm/loft geometry use the STEP. This PDF is a dimension reference, not a fully toleranced production drawing.'
]
for t in notes:text(34,ny,t,9,RED if t.startswith('TOLERANCES') else GRAY);ny-=17
C.save()
# dimension schedule is machine-readable alongside PDF
with (D/'grip-r7-dimensions.csv').open('w',newline='',encoding='utf-8') as f:
 w=csv.writer(f);w.writerow(['feature','nominal_dimension_mm','status','manufacturing_tolerance']);w.writerows([list(r)+['TBD - not released'] for r in rows])
# render for visual QA
p=pdfium.PdfDocument(str(OUT))
QA=Path(r'C:/Users/Sambit Baliarsingh/Documents/Codex/2026-11-01/i-h/work/pdf-qa');QA.mkdir(exist_ok=True)
for i in range(len(p)):p[i].render(scale=1.25).to_pil().save(str(QA/f'r7-drawing-{i+1}.png'))
print('Created PDF with',len(p),'pages and dimension CSV')
