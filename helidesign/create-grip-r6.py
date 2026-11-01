import adsk.core, adsk.fusion, json, os

def run(_context: str):
    app=adsk.core.Application.get()
    doc=app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)
    doc.name='Helidesign R6 - reference style grip - FIT ONLY'
    d=adsk.fusion.Design.cast(app.activeProduct)
    r=d.rootComponent

    out=r'C:/Users/Sambit Baliarsingh/Documents/Codex/2026-11-01/i-h/outputs/helidesign'
    P=adsk.core.Point3D.create
    V=adsk.core.ValueInput.createByReal
    F=adsk.fusion.FeatureOperations
    def plane(z):
        q=r.constructionPlanes.createInput(); q.setByOffset(r.xYConstructionPlane,V(z/10)); return r.constructionPlanes.add(q)
    def circle(z,diam,name,depth,op):
        s=r.sketches.add(plane(z)); s.name=name
        s.sketchCurves.sketchCircles.addByCenterRadius(P(0,0,0),diam/20)
        e=r.features.extrudeFeatures.addSimple(s.profiles.item(0),V(depth/10),op); e.name=name; s.isVisible=False
        return e
    def rect(z,x1,y1,x2,y2,depth,name,op):
        s=r.sketches.add(plane(z)); s.name=name
        s.sketchCurves.sketchLines.addTwoPointRectangle(P(x1/10,y1/10,0),P(x2/10,y2/10,0))
        e=r.features.extrudeFeatures.addSimple(s.profiles.item(0),V(depth/10),op);e.name=name;s.isVisible=False
        return e
    circle(0,12,'Compact round bearing housing',8,F.NewBodyFeatureOperation)
    a=r.sketches.add(plane(8));a.name='Round transition start'
    a.sketchCurves.sketchCircles.addByCenterRadius(P(0,0,0),.6)
    c=r.sketches.add(plane(12));c.name='Slim fork transition end'
    c.sketchCurves.sketchLines.addTwoPointRectangle(P(-.5,-.45,0),P(.5,.45,0))
    li=r.features.loftFeatures.createInput(F.JoinFeatureOperation)
    li.loftSections.add(a.profiles.item(0));li.loftSections.add(c.profiles.item(0))
    lf=r.features.loftFeatures.add(li);lf.name='Continuous housing to fork transition'
    a.isVisible=False;c.isVisible=False
    def cheek(x,name):
        q=r.constructionPlanes.createInput();q.setByOffset(r.yZConstructionPlane,V(x/10))
        sk=r.sketches.add(r.constructionPlanes.add(q));sk.name=name
        def p(y,z):return sk.modelToSketchSpace(P(x/10,y/10,z/10))
        ls=sk.sketchCurves.sketchLines
        ls.addByTwoPoints(p(-4.5,12),p(4.5,12))
        ls.addByTwoPoints(p(4.5,12),p(4.5,25))
        sk.sketchCurves.sketchArcs.addByThreePoints(p(4.5,25),p(0,29.5),p(-4.5,25))
        ls.addByTwoPoints(p(-4.5,25),p(-4.5,12))
        ef=r.features.extrudeFeatures.addSimple(sk.profiles.item(0),V(.3),F.JoinFeatureOperation)
        ef.name=name;sk.isVisible=False
    cheek(-5,'Rounded slim fork A - provisional blade fit')
    cheek(2,'Rounded slim fork B - provisional blade fit')
    sk=r.sketches.add(plane(2));sk.name='Angled pitch control arm'
    def p(x,y):return P(x/10,y/10,0)
    ls=sk.sketchCurves.sketchLines
    pts=[(-2,4),(2,4),(2,9),(5.41421356,12.58578644)]
    for aa,bb in zip(pts,pts[1:]):ls.addByTwoPoints(p(*aa),p(*bb))
    sk.sketchCurves.sketchArcs.addByThreePoints(p(*pts[-1]),p(5.41421356,15.41421356),p(2.58578644,15.41421356))
    ls.addByTwoPoints(p(2.58578644,15.41421356),p(-2,10));ls.addByTwoPoints(p(-2,10),p(-2,4))
    ef=r.features.extrudeFeatures.addSimple(sk.profiles.item(0),V(.4),F.JoinFeatureOperation)
    ef.name='Integral angled pitch arm';sk.isVisible=False
    circle(0,4.8,'Internal shoulder relief assumed',12,F.CutFeatureOperation)
    circle(0,6.15,'Inner radial pocket 6.15 assumed allowance',2.5,F.CutFeatureOperation)
    circle(3.9,6.15,'Outer bearing stack and assembly passage',13.7,F.CutFeatureOperation)
    # Oval transverse assembly window, resembling the reference relief opening.
    sk=r.sketches.add(r.yZConstructionPlane);sk.name='Oval bearing assembly access'
    def wp(y,z):return sk.modelToSketchSpace(P(0,y/10,z/10))
    ls=sk.sketchCurves.sketchLines
    ls.addByTwoPoints(wp(3.4,15),wp(3.4,16.6))
    sk.sketchCurves.sketchArcs.addByThreePoints(wp(3.4,16.6),wp(0,20),wp(-3.4,16.6))
    ls.addByTwoPoints(wp(-3.4,16.6),wp(-3.4,15))
    sk.sketchCurves.sketchArcs.addByThreePoints(wp(-3.4,15),wp(0,11.6),wp(3.4,15))
    q=r.features.extrudeFeatures.createInput(sk.profiles.item(0),F.CutFeatureOperation)
    q.setDistanceExtent(True,V(2));ef=r.features.extrudeFeatures.add(q)
    ef.name='Oval assembly access through both cheeks';sk.isVisible=False
    # Cross bolt axis is global X; assumed 2.2 mm clearance.
    s=r.sketches.add(r.yZConstructionPlane);s.name='Blade bolt 2.2 mm assumed'
    s.sketchCurves.sketchCircles.addByCenterRadius(s.modelToSketchSpace(P(0,0,2.5)),0.11)
    q=r.features.extrudeFeatures.createInput(s.profiles.item(0),F.CutFeatureOperation)
    q.setDistanceExtent(True,V(2));r.features.extrudeFeatures.add(q);s.isVisible=False
    s=r.sketches.add(plane(2));s.name='Pitch ball mounting 1.8 mm assumed'
    s.sketchCurves.sketchCircles.addByCenterRadius(P(.4,1.4,0),0.09)
    r.features.extrudeFeatures.addSimple(s.profiles.item(0),V(.4),F.CutFeatureOperation);s.isVisible=False
    b=r.bRepBodies.item(0);b.name='PETG grip - fit prototype only'
    for i in range(r.constructionPlanes.count):r.constructionPlanes.item(i).isLightBulbOn=False
    cam=app.activeViewport.camera
    cam.eye=P(7,8,6);cam.target=P(0,.4,1.4)
    cam.upVector=adsk.core.Vector3D.create(1,0,0)
    cam.isFitView=True;app.activeViewport.camera=cam
    app.activeViewport.fit()
    ex=d.exportManager
    ex.execute(ex.createFusionArchiveExportOptions(out+'/grip-r6-fit-only.f3d'))
    st=ex.createSTLExportOptions(b,out+'/grip-r6-fit-only.stl');st.meshRefinement=adsk.fusion.MeshRefinementSettings.MeshRefinementHigh
    ex.execute(st)
    ex.execute(ex.createSTEPExportOptions(out+'/grip-r6-fit-only.step'))
    app.activeViewport.saveAsImageFile(out+'/grip-r6-preview.png',1200,900)
    print(json.dumps({'bodies':r.bRepBodies.count,'solid':b.isSolid,'volume_cm3':b.volume,'bounds_cm':[[b.boundingBox.minPoint.x,b.boundingBox.minPoint.y,b.boundingBox.minPoint.z],[b.boundingBox.maxPoint.x,b.boundingBox.maxPoint.y,b.boundingBox.maxPoint.z]],'features':r.features.count,'files':os.listdir(out)}))







