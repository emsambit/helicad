import adsk.core, adsk.fusion, json, os

def run(_context: str):
    app=adsk.core.Application.get()
    doc=app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)
    doc.name='Helidesign R2 - rounded PETG grip - FIT ONLY'
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
    circle(0,12,'Bearing housing OD12 assumed',12,F.NewBodyFeatureOperation)
    # R2: semicircular cheek ends; all blade-root interfaces remain provisional.
    def cheek(x,name):
        q=r.constructionPlanes.createInput()
        q.setByOffset(r.yZConstructionPlane,V(x/10))
        pl=r.constructionPlanes.add(q)
        s=r.sketches.add(pl);s.name=name
        def p(y,z): return s.modelToSketchSpace(P(x/10,y/10,z/10))
        lines=s.sketchCurves.sketchLines
        lines.addByTwoPoints(p(-5,10),p(5,10))
        lines.addByTwoPoints(p(5,10),p(5,23))
        s.sketchCurves.sketchArcs.addByThreePoints(p(5,23),p(0,28),p(-5,23))
        lines.addByTwoPoints(p(-5,23),p(-5,10))
        e=r.features.extrudeFeatures.addSimple(s.profiles.item(0),V(.3),F.JoinFeatureOperation)
        e.name=name;s.isVisible=False
    cheek(-5,'Rounded cheek A - 4 mm gap assumed')
    cheek(2,'Rounded cheek B - 3 mm wall assumed')
    s=r.sketches.add(plane(2));s.name='Rounded pitch arm - geometry assumed'
    def ap(x,y):return P(x/10,y/10,0)
    lines=s.sketchCurves.sketchLines
    lines.addByTwoPoints(ap(-3,4),ap(3,4))
    lines.addByTwoPoints(ap(3,4),ap(2,14.5))
    s.sketchCurves.sketchArcs.addByThreePoints(ap(2,14.5),ap(0,16.5),ap(-2,14.5))
    lines.addByTwoPoints(ap(-2,14.5),ap(-3,4))
    e=r.features.extrudeFeatures.addSimple(s.profiles.item(0),V(.4),F.JoinFeatureOperation)
    e.name=s.name;s.isVisible=False
    circle(0,4.8,'Internal shoulder relief assumed',12,F.CutFeatureOperation)
    circle(0,6.15,'Inner radial pocket 6.15 assumed allowance',2.5,F.CutFeatureOperation)
    circle(3.9,6.15,'Outer radial and thrust access pocket',8.1,F.CutFeatureOperation)
    # Cross bolt axis is global X; assumed 2.2 mm clearance.
    s=r.sketches.add(r.yZConstructionPlane);s.name='Blade bolt 2.2 mm assumed'
    s.sketchCurves.sketchCircles.addByCenterRadius(s.modelToSketchSpace(P(0,0,2.3)),0.11)
    q=r.features.extrudeFeatures.createInput(s.profiles.item(0),F.CutFeatureOperation)
    q.setDistanceExtent(True,V(2));r.features.extrudeFeatures.add(q);s.isVisible=False
    s=r.sketches.add(plane(2));s.name='Pitch ball mounting 1.8 mm assumed'
    s.sketchCurves.sketchCircles.addByCenterRadius(P(0,1.45,0),0.09)
    r.features.extrudeFeatures.addSimple(s.profiles.item(0),V(.4),F.CutFeatureOperation);s.isVisible=False
    b=r.bRepBodies.item(0);b.name='PETG grip - fit prototype only'
    for i in range(r.constructionPlanes.count):r.constructionPlanes.item(i).isLightBulbOn=False
    app.activeViewport.fit()
    ex=d.exportManager
    ex.execute(ex.createFusionArchiveExportOptions(out+'/grip-r2-fit-only.f3d'))
    st=ex.createSTLExportOptions(b,out+'/grip-r2-fit-only.stl');st.meshRefinement=adsk.fusion.MeshRefinementSettings.MeshRefinementHigh
    ex.execute(st)
    ex.execute(ex.createSTEPExportOptions(out+'/grip-r2-fit-only.step'))
    app.activeViewport.saveAsImageFile(out+'/grip-r2-preview.png',1200,900)
    print(json.dumps({'bodies':r.bRepBodies.count,'solid':b.isSolid,'volume_cm3':b.volume,'bounds_cm':[[b.boundingBox.minPoint.x,b.boundingBox.minPoint.y,b.boundingBox.minPoint.z],[b.boundingBox.maxPoint.x,b.boundingBox.maxPoint.y,b.boundingBox.maxPoint.z]],'features':r.features.count,'files':os.listdir(out)}))



