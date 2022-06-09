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

    m = Mesh.load_obj('textured_output.obj')
    m.normalize()
    m.apply_matrix(pyrr.matrix44.create_from_scale([2, 2, 2, 1]))
    tr = Transformation3D()
    tr.translation.y = -np.amin(m.vertices, axis=0)[1]
    tr.translation.z = -5
    tr.rotation_center.z = 0.2
    texture = glutils.load_texture('textured_output.jpg')
    o = Object3D(m.load_to_gpu(), m.get_nb_triangles(), program3d_id, texture, tr)
    o.transformation.translation.y = 2
    viewer.add_object(o)

    m2 = Mesh.load_obj('cube.obj')
    m2.normalize()
    m2.apply_matrix(pyrr.matrix44.create_from_scale([2, 2, 2, 1]))
    tr2 = Transformation3D()
    tr2.translation.y = -np.amin(m.vertices, axis=0)[1]
    tr2.translation.z = -5
    tr2.rotation_center.z = 0.2
    texture2 = glutils.load_texture('cube.jpg')
    o2 = Object3D(m2.load_to_gpu(), m2.get_nb_triangles(), program3d_id, texture2, tr2)
    o2.transformation.translation.y = 2
    viewer.add_object(o2)
    

    
    
    
    m = Mesh()
    p0, p1, p2, p3 = [-25, 0, -25], [25, 0, -25], [25, 0, 25], [-25, 0, 25]
    n, c = [0, 1, 0], [1, 1, 1]
    t0, t1, t2, t3 = [0, 0], [1, 0], [1, 1], [0, 1]
    m.vertices = np.array([[p0 + n + c + t0], [p1 + n + c + t1], [p2 + n + c + t2], [p3 + n + c + t3]], np.float32)
    m.faces = np.array([[0, 1, 2], [0, 2, 3]], np.uint32)
    texture = glutils.load_texture('grass.jpg')
    VAO = m.load_to_gpu()
    o1 = Object3D(VAO, m.get_nb_triangles(), program3d_id, texture, Transformation3D())
    o1.transformation.translation.x = 25
    viewer.add_object(o1)
    o2 = Object3D(VAO, m.get_nb_triangles(), program3d_id, texture, Transformation3D())
    o2.transformation.translation.z = 25
    viewer.add_object(o2)
    o4 = Object3D(VAO, m.get_nb_triangles(), program3d_id, texture, Transformation3D())
    o4.transformation.translation.x = 25
    viewer.add_object(o4)
    o4.transformation.translation.z = 25
    o3 = Object3D(VAO, m.get_nb_triangles(), program3d_id, texture, Transformation3D())
    viewer.add_object(o3)
    
    
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

    vao = Text.initalize_geometry()
    texture = glutils.load_texture('fontB.jpg')
    o = Text('', np.array([-0.8, 0.3], np.float32), np.array([0.8, 0.8], np.float32), vao, 2, programGUI_id, texture)
    viewer.add_object(o)
    o = Text('', np.array([-0.5, -0.2], np.float32), np.array([0.5, 0.3], np.float32), vao, 2, programGUI_id, texture)
    viewer.add_object(o)

    viewer.run()


if __name__ == '__main__':

    main()