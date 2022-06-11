from viewerGL import ViewerGL
import glutils
from mesh import Mesh
from cpe3d import Object3D, Camera, Transformation3D, Text
import numpy as np
import OpenGL.GL as GL
import pyrr


def main():
    viewer = ViewerGL()

    viewer.set_camera(Camera())
    viewer.cam.transformation.translation.y = 2
    viewer.cam.transformation.rotation_center = viewer.cam.transformation.translation.copy()

    program3d_id = glutils.create_program_from_file('ressources/shaders/shader.vert', 'ressources/shaders/shader.frag')
    programGUI_id = glutils.create_program_from_file('ressources/shaders/gui.vert', 'ressources/shaders/gui.frag')

    m = Mesh.load_obj('ressources/objets/textured_output.obj')
    m.normalize()
    m.apply_matrix(pyrr.matrix44.create_from_scale([2, 2, 2, 1]))
    tr = Transformation3D()
    tr.translation.y = -np.amin(m.vertices, axis=0)[1]
    tr.translation.z = -5
    tr.rotation_center.z = 0.2
    texture = glutils.load_texture('ressources/textures/textured_output.jpg')
    o = Object3D(m.load_to_gpu(), m.get_nb_triangles(), program3d_id, texture, tr)
    o.transformation.translation.y = 2
    viewer.add_object(o)
    
    
#================================== Singe Suzanne ===============================           /!\ J'ai pas reussi à effectuer une rotation pour qu'elle regarde le centre de la pièce, nécessaire ?
    m21 = Mesh.load_obj('ressources/objets/singe.obj')
    m21.normalize()
    m21.apply_matrix(pyrr.matrix44.create_from_scale([0.5,0.5,0.5,1]))
    tr21 = Transformation3D()
    tr21.translation.y = 2.5
    tr21.translation.z = -22
    tr21.translation.x = 15
    tr21.rotation_center.z = -0.2
    texture = glutils.load_texture('ressources/textures/or.jpg')
    o21 = Object3D(m21.load_to_gpu(), m21.get_nb_triangles(), program3d_id, texture ,tr21)
    #o21.transformation.translation.y = 2
    viewer.add_object(o21)
    
    #================================== Stegosaurus ===============================           /!\ Scanner maxime
    m21 = Mesh.load_obj('ressources/objets/stegosaurus.obj')
    m21.normalize()
    m21.apply_matrix(pyrr.matrix44.create_from_scale([1,1,1,1]))
    tr21 = Transformation3D()
    tr21.translation.y = 2.6
    tr21.translation.z = -22.3
    tr21.translation.x = -15
    tr21.rotation_center.z = -0.2
    texture = glutils.load_texture('ressources/textures/stegosaurus.jpg')
    o21 = Object3D(m21.load_to_gpu(), m21.get_nb_triangles(), program3d_id, texture ,tr21)
    #o21.transformation.translation.y = 2
    viewer.add_object(o21)
    
    
    #================================== Voiture ===============================        
    m21 = Mesh.load_obj('ressources/objets/singe.obj')
    m21.normalize()
    m21.apply_matrix(pyrr.matrix44.create_from_scale([0.5,0.5,0.5,1]))
    tr21 = Transformation3D()
    tr21.translation.y = 2.5
    tr21.translation.z = -22
    tr21.translation.x = 0
    tr21.rotation_center.z = -0.2
    texture = glutils.load_texture('ressources/textures/or.jpg')
    o21 = Object3D(m21.load_to_gpu(), m21.get_nb_triangles(), program3d_id, texture ,tr21)
    #o21.transformation.translation.y = 2
    viewer.add_object(o21)
    
#================================= Toit ========================================
    m = Mesh()
    p0, p1, p2, p3 = [-50, 0, -50], [50, 0, -50], [50, 0, 50], [-50, 0, 50]
    n, c = [0, 1, 0], [1, 1, 1]
    t0, t1, t2, t3 = [0, 0], [1, 0], [1, 1], [0, 1]
    m.vertices = np.array([[p0 + n + c + t0], [p1 + n + c + t1], [p2 + n + c + t2], [p3 + n + c + t3]], np.float32)
    m.faces = np.array([[0, 1, 2], [0, 2, 3]], np.uint32)
    texture = glutils.load_texture('ressources/textures/blanc.jpg')
    VAO = m.load_to_gpu()
    tr6 = Transformation3D()
    tr6.translation.y = 13
    o1 = Object3D(VAO, m.get_nb_triangles(), program3d_id, texture, tr6)
    viewer.add_object(o1)
#================================= Sol ========================================   
    m5 = Mesh()
    p05, p15, p25, p35 = [-50, 0, -50], [50, 0, -50], [50, 0, 50], [-50, 0, 50]
    n5, c5 = [0, 1, 0], [1, 1, 1]
    t05, t15, t25, t35 = [0, 0], [1, 0], [1, 1], [0, 1]
    m5.vertices = np.array([[p05 + n5 + c5 + t05], [p15 + n5 + c5 + t15], [p25 + n5 + c5 + t25], [p35 + n5 + c5 + t35]], np.float32)
    m5.faces = np.array([[0, 1, 2], [0, 2, 3]], np.uint32)
    texture = glutils.load_texture('ressources/textures/sol.jpg')
    VAO = m5.load_to_gpu()
    o1 = Object3D(VAO, m.get_nb_triangles(), program3d_id, texture, Transformation3D())
    viewer.add_object(o1)
    
#===================================== Stands ===================================
    ms = Mesh.load_obj('ressources/objets/pedestal.obj')
    ms.normalize()
    ms.apply_matrix(pyrr.matrix44.create_from_scale([1,1,1,1]))
    vaostand = ms.load_to_gpu()
    texture = glutils.load_texture('ressources/textures/BaseColor.png')

    for bcls in range(3):
        trs = Transformation3D()
        trs.translation.z = -22
        trs.translation.x = -15 + 15*bcls
        trs.rotation_center.z = 0.2
        os = Object3D(vaostand, m21.get_nb_triangles(), program3d_id, texture ,trs)
        os.transformation.translation.y = 1
        viewer.add_object(os)

    for bcls2 in range(3):
        trs = Transformation3D()
        trs.translation.z = 22
        trs.translation.x = -15 + 15*bcls2
        trs.rotation_center.z = 0.2
        os = Object3D(vaostand, m21.get_nb_triangles(), program3d_id, texture ,trs)
        os.transformation.translation.y = 1
        viewer.add_object(os)
    trs = Transformation3D()
    trs.translation.z = 0
    trs.translation.x = 25
    trs.rotation_center.z = 0.2
    os = Object3D(vaostand, m21.get_nb_triangles(), program3d_id, texture ,trs)
    os.transformation.translation.y = 1
    viewer.add_object(os)
#================================ Cube mur ========================================
    #===== contour =====#
    m2 = Mesh.load_obj('ressources/objets/cube.obj')
    m2.normalize()
    m2.apply_matrix(pyrr.matrix44.create_from_scale([1, 1, 1, 1]))
    texture2 = glutils.load_texture('ressources/textures/noir.jpg')
    vao2 = m2.load_to_gpu()
    for val in range(30):
        tr2 = Transformation3D()
        tr2.translation.y = 0
        tr2.translation.z = -30
        tr2.translation.x = -30+2*val
        o2 = Object3D(vao2, m2.get_nb_triangles(), program3d_id, texture2, tr2)
        viewer.add_object(o2)
    
    for val in range(30):
        tr3 = Transformation3D()
        tr3.translation.y =  0
        tr3.translation.x = -30
        tr3.translation.z = -30+2*val
        o3 = Object3D(vao2, m2.get_nb_triangles(), program3d_id, texture2, tr3)
        viewer.add_object(o3)
    
    for val in range(30):
        tr4 = Transformation3D()
        tr4.translation.y =  0
        tr4.translation.z = 30
        tr4.translation.x = -30+2*val
        o4 = Object3D(vao2, m2.get_nb_triangles(), program3d_id, texture2, tr4)
        viewer.add_object(o4)
        
    for val in range (30):   
        tr5 = Transformation3D()
        tr5.translation.y =  0
        tr5.translation.x = 30
        tr5.translation.z = -30+2*val
        o5 = Object3D(vao2, m2.get_nb_triangles(), program3d_id, texture2, tr5)
        viewer.add_object(o5)
    
    #===== Bloc haut mur (donc 4 blocs) =====#
    m3 = Mesh.load_obj('ressources/objets/cube.obj')
    m3.normalize()
    m3.apply_matrix(pyrr.matrix44.create_from_scale([0.9, 15, 30, 1]))
    texture = glutils.load_texture('ressources/textures/blanc.jpg')
    vao3 = m3.load_to_gpu()
    tr6 = Transformation3D()
    tr6.translation.x = -30
    tr6.translation.y = +1
    o6 = Object3D(vao3, m3.get_nb_triangles(), program3d_id, texture, tr6)
    viewer.add_object(o6)
    
    m4 = Mesh.load_obj('ressources/objets/cube.obj')
    m4.normalize()
    m4.apply_matrix(pyrr.matrix44.create_from_scale([0.9, 15, 30, 1]))
    texture = glutils.load_texture('ressources/textures/blanc.jpg')
    vao4 = m4.load_to_gpu()
    tr7 = Transformation3D()
    tr7.translation.x = 30
    tr7.translation.y = +1
    o7 = Object3D(vao4, m4.get_nb_triangles(), program3d_id, texture, tr7)
    viewer.add_object(o7)
    
    m5 = Mesh.load_obj('ressources/objets/cube.obj')
    m5.normalize()
    m5.apply_matrix(pyrr.matrix44.create_from_scale([30, 15,0.9, 1]))
    texture = glutils.load_texture('ressources/textures/blanc.jpg')
    vao5 = m5.load_to_gpu()
    tr8 = Transformation3D()
    tr8.translation.z = -30
    tr8.translation.y = +1
    o8 = Object3D(vao5, m5.get_nb_triangles(), program3d_id, texture, tr8)
    viewer.add_object(o8)
    
    m6 = Mesh.load_obj('ressources/objets/cube.obj')
    m6.normalize()
    m6.apply_matrix(pyrr.matrix44.create_from_scale([30, 15, 0.9, 1]))
    texture = glutils.load_texture('ressources/textures/blanc.jpg')
    vao6 = m6.load_to_gpu()
    tr9 = Transformation3D()
    tr9.translation.z= 30
    tr9.translation.y = +1
    o9 = Object3D(vao6, m6.get_nb_triangles(), program3d_id, texture, tr9)
    viewer.add_object(o9)

#============================= Barrières ========================================
    mbar1 = Mesh.load_obj('ressources/objets/cube.obj')
    mbar1.normalize()
    mbar1.apply_matrix(pyrr.matrix44.create_from_scale([0.1, 1.7, 2, 1]))
    texturebar = glutils.load_texture('ressources/textures/barriere.jpg')
    vaobar = mbar1.load_to_gpu()

    for loop in range(2):
        for val in range(7):
            trbar = Transformation3D()
            trbar.translation.y = 0
            trbar.translation.z = -27+val
            trbar.translation.x = 7.5 - 15*loop
            obar = Object3D(vaobar, mbar1.get_nb_triangles(), program3d_id, texturebar, trbar)
            viewer.add_object(obar)

    for loop in range(2):
        for val in range(7):
            trbar = Transformation3D()
            trbar.translation.y = 0
            trbar.translation.z = 27-val
            trbar.translation.x = 7.5 - 15*loop
            obar = Object3D(vaobar, mbar1.get_nb_triangles(), program3d_id, texturebar, trbar)
            viewer.add_object(obar)

    # for loop in range(2):                    /!\ Pour le stand central faitre un carré autour pour faire comme si c'etait une oeuvre ultra rare
    #     for val in range(7):
    #         trbar = Transformation3D()
    #         trbar.translation.y = 0
    #         trbar.translation.z = 27-val
    #         trbar.translation.x = 7.5 - 15*loop
    #         obar = Object3D(vaobar, mbar1.get_nb_triangles(), program3d_id, texturebar, trbar)
    #         viewer.add_object(obar)
    
    
    
#================================= Textes =========================================
    vao = Text.initalize_geometry()
    texture = glutils.load_texture('ressources/textures/fontB.jpg')
    o = Text('test', np.array([-0.8, 0.3], np.float32), np.array([0.8, 0.8], np.float32), vao, 2, programGUI_id, texture)
    viewer.add_object(o)
    o.visible = False
#===============================================================================
    viewer.run()

if __name__ == '__main__':

    main()
    
    
#commentaire