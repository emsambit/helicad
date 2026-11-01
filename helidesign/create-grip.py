import adsk.core, adsk.fusion, json, os

def run(_context: str):
    app=adsk.core.Application.get()
    doc=app.documents.add(adsk.core.DocumentTypes.FusionDesignDocumentType)
    doc.name='Helidesign - PETG grip - FIT PROTOTYPE'
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
    # Independent cheeks leave an assumed 4 mm blade-root gap.
    rect(10,-5,-5,-2,5,18,'Cheek A - 3 mm wall assumed',F.JoinFeatureOperation)
    rect(10,2,-5,5,5,18,'Cheek B - 3 mm wall assumed',F.JoinFeatureOperation)
    rect(2,-2,4,2,17,4,'Pitch arm - position assumed',F.JoinFeatureOperation)
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
    ex.execute(ex.createFusionArchiveExportOptions(out+'/grip-fit-prototype.f3d'))
    st=ex.createSTLExportOptions(b,out+'/grip-fit-prototype.stl');st.meshRefinement=adsk.fusion.MeshRefinementSettings.MeshRefinementHigh
    ex.execute(st)
    ex.execute(ex.createSTEPExportOptions(out+'/grip-fit-prototype.step'))
    app.activeViewport.saveAsImageFile(out+'/grip-preview.png',1200,900)
    print(json.dumps({'bodies':r.bRepBodies.count,'solid':b.isSolid,'volume_cm3':b.volume,'bounds_cm':[[b.boundingBox.minPoint.x,b.boundingBox.minPoint.y,b.boundingBox.minPoint.z],[b.boundingBox.maxPoint.x,b.boundingBox.maxPoint.y,b.boundingBox.maxPoint.z]],'features':r.features.count,'files':os.listdir(out)}))


