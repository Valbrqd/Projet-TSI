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

    program3d_id = glutils.create_program_from_file('shader.vert', 'shader.frag')
    programGUI_id = glutils.create_program_from_file('gui.vert', 'gui.frag')

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
    
    
#================================== SINGE Suzanne ===============================
    m21 = Mesh.load_obj('ressources/objets/singe.obj')
    m21.normalize()
    m21.apply_matrix(pyrr.matrix44.create_from_scale([0.5,0.5,0.5,1]))
    tr21 = Transformation3D()
    tr21.translation.y = -np.amin(m.vertices, axis=0)[1]
    tr21.translation.z = -10
    tr21.rotation_center.z = 0.2
    texture = glutils.load_texture('ressources/textures/blanc.jpg')
    o21 = Object3D(m21.load_to_gpu(), m21.get_nb_triangles(), program3d_id, texture ,tr21)
    o21.transformation.translation.y = 2
    viewer.add_object(o21)
#================================= Textes ========================================
    m = Mesh()
    p0, p1, p2, p3 = [-50, 0, -50], [50, 0, -50], [50, 0, 50], [-50, 0, 50]
    n, c = [0, 1, 0], [1, 1, 1]
    t0, t1, t2, t3 = [0, 0], [1, 0], [1, 1], [0, 1]
    m.vertices = np.array([[p0 + n + c + t0], [p1 + n + c + t1], [p2 + n + c + t2], [p3 + n + c + t3]], np.float32)
    m.faces = np.array([[0, 1, 2], [0, 2, 3]], np.uint32)
    texture = glutils.load_texture('ressources/textures/blanc.jpg')
    VAO = m.load_to_gpu()
    tr6 = Transformation3D()
    tr6.translation.y = 28
    o1 = Object3D(VAO, m.get_nb_triangles(), program3d_id, texture, tr6)
    viewer.add_object(o1)
    
    m5 = Mesh()
    p05, p15, p25, p35 = [-50, 0, -50], [50, 0, -50], [50, 0, 50], [-50, 0, 50]
    n5, c5 = [0, 1, 0], [1, 1, 1]
    t05, t15, t25, t35 = [0, 0], [1, 0], [1, 1], [0, 1]
    m5.vertices = np.array([[p05 + n5 + c5 + t05], [p15 + n5 + c5 + t15], [p25 + n5 + c5 + t25], [p35 + n5 + c5 + t35]], np.float32)
    m5.faces = np.array([[0, 1, 2], [0, 2, 3]], np.uint32)
    texture = glutils.load_texture('ressources/textures/grass.jpg')
    VAO = m5.load_to_gpu()
    o1 = Object3D(VAO, m.get_nb_triangles(), program3d_id, texture, Transformation3D())
    viewer.add_object(o1)

    vao = Text.initalize_geometry()
    texture = glutils.load_texture('ressources/textures/fontB.jpg')
    o = Text('', np.array([-0.8, 0.3], np.float32), np.array([0.8, 0.8], np.float32), vao, 2, programGUI_id, texture)
    viewer.add_object(o)
    o = Text('', np.array([-0.5, -0.2], np.float32), np.array([0.5, 0.3], np.float32), vao, 2, programGUI_id, texture)
    viewer.add_object(o)
#================================ Cube mur ========================================

    m2 = Mesh.load_obj('ressources/objets/cube.obj')
    m2.normalize()
    m2.apply_matrix(pyrr.matrix44.create_from_scale([1, 1, 1, 1]))
    texture2 = glutils.load_texture('ressources/textures/mur.jpg')
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
    
    m3 = Mesh.load_obj('ressources/objets/cube.obj')
    m3.normalize()
    m3.apply_matrix(pyrr.matrix44.create_from_scale([0.9, 30, 30, 1]))
    texture = glutils.load_texture('ressources/textures/blanc.jpg')
    vao3 = m3.load_to_gpu()
    tr6 = Transformation3D()
    tr6.translation.x = -30
    tr6.translation.y = +1
    o6 = Object3D(vao3, m3.get_nb_triangles(), program3d_id, texture, tr6)
    viewer.add_object(o6)
    
    m4 = Mesh.load_obj('ressources/objets/cube.obj')
    m4.normalize()
    m4.apply_matrix(pyrr.matrix44.create_from_scale([0.9, 30, 30, 1]))
    texture = glutils.load_texture('ressources/textures/blanc.jpg')
    vao4 = m4.load_to_gpu()
    tr7 = Transformation3D()
    tr7.translation.x = 30
    tr7.translation.y = +1
    o7 = Object3D(vao4, m4.get_nb_triangles(), program3d_id, texture, tr7)
    viewer.add_object(o7)
    
    
    m5 = Mesh.load_obj('ressources/objets/cube.obj')
    m5.normalize()
    m5.apply_matrix(pyrr.matrix44.create_from_scale([30, 30,0.9, 1]))
    texture = glutils.load_texture('ressources/textures/blanc.jpg')
    vao5 = m5.load_to_gpu()
    tr8 = Transformation3D()
    tr8.translation.z = -30
    tr8.translation.y = +1
    o8 = Object3D(vao5, m5.get_nb_triangles(), program3d_id, texture, tr8)
    viewer.add_object(o8)
    
    m6 = Mesh.load_obj('ressources/objets/cube.obj')
    m6.normalize()
    m6.apply_matrix(pyrr.matrix44.create_from_scale([30, 30, 0.9, 1]))
    texture = glutils.load_texture('ressources/textures/blanc.jpg')
    vao6 = m6.load_to_gpu()
    tr9 = Transformation3D()
    tr9.translation.z= 30
    tr9.translation.y = +1
    o9 = Object3D(vao6, m6.get_nb_triangles(), program3d_id, texture, tr9)
    viewer.add_object(o9)
    
#==================================================================================
    
    
    
    
    
    
    
    #création mur
    # mur2 = Mesh()
    # p01, p11, p21, p31 = [-25, 0, -25], [25, 0, -25], [-25, 25, -25], [25, 25, -25]
    # n1, c1 = [0, 0, 1], [1, 1, 1]
    # t01, t11, t21, t31 = [0, 0], [1, 0], [1, 1], [0, 1]
    # mur2.vertices = np.array([[p01 + n1 + c1 + t01], [p11 + n1 + c1 + t11], [p21 + n1 + c1 + t21], [p31 + n1 + c1 + t31]], np.float32)
    # mur2.faces = np.array([[0, 1, 2], [1, 2, 3]], np.uint32)
    # texture = glutils.load_texture('grass.jpg')
    # o2 = Object3D(mur2.load_to_gpu(), mur2.get_nb_triangles(), program3d_id, texture, Transformation3D())
    # viewer.add_object(o2)
    
    # mur3 = Mesh()
    # p02, p12, p22, p32 = [25, 0, -25], [25, 0, -5], [25, 25, -25], [25, 25, 25]
    # n2, c2 = [1, 0, 0], [1, 1, 1]
    # t02, t12, t22, t32 = [0, 0], [1, 0], [1, 1], [0, 1]
    # mur3.vertices = np.array([[p02 + n2 + c2 + t02], [p12 + n2 + c2 + t12], [p22 + n2 + c2 + t22], [p32 + n2 + c2 + t32]], np.float32)
    # mur3.faces = np.array([[0, 1, 2], [1, 2, 3]], np.uint32)
    # texture = glutils.load_texture('grass.jpg')
    # o3 = Object3D(mur3.load_to_gpu(), mur3.get_nb_triangles(), program3d_id, texture, Transformation3D())
    # viewer.add_object(o3)
    

#===================== Création du batiment du musée ===================================

    
#=======================================================================================

    

    viewer.run()


if __name__ == '__main__':

    main()