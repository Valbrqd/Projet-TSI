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
    o.transformation.translation.y = 1
    viewer.add_object(o)

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

#===================== Création du batiment du musée ===================================
    program = glutils.create_program_from_file('shadermusee.vert','shadermusee.frag')
    GL.glUseProgram(program)
    sommetsmusee = np.array(((-1.0,-1.0,-1.0),(-1.0,-1.0, 1.0),(-1.0, 1.0, 1.0), 
    (1.0, 1.0,-1.0),(-1.0,-1.0,-1.0),(-1.0, 1.0,-1.0), 
    (1.0,-1.0, 1.0),(-1.0,-1.0,-1.0),(1.0,-1.0,-1.0),
    (1.0, 1.0,-1.0),(1.0,-1.0,-1.0),(-1.0,-1.0,-1.0),
    (-1.0,-1.0,-1.0),(-1.0, 1.0, 1.0),(-1.0, 1.0,-1.0),
    (1.0,-1.0, 1.0),(-1.0,-1.0, 1.0),(-1.0,-1.0,-1.0),
    (-1.0, 1.0, 1.0),(-1.0,-1.0, 1.0),(1.0,-1.0, 1.0),
    (1.0, 1.0, 1.0),(1.0,-1.0,-1.0),(1.0, 1.0,-1.0),
    (1.0,-1.0,-1.0),(1.0, 1.0, 1.0),(1.0,-1.0, 1.0),
    (1.0, 1.0, 1.0),(1.0, 1.0,-1.0),(-1.0, 1.0,-1.0),
    (1.0, 1.0, 1.0),(-1.0, 1.0,-1.0),(-1.0, 1.0, 1.0),
    (1.0, 1.0, 1.0),(-1.0, 1.0, 1.0),(1.0,-1.0, 1.0)),np.float32)

    # attribution d'une liste d'etat (1 indique la création d'une seule liste) ´
    vao = GL.glGenVertexArrays(1)
    # affectation de la liste d'etat courante ´
    GL.glBindVertexArray(vao)
    # attribution d’un buffer de donnees (1 indique la création d’un seul buffer) ´
    vbo = GL.glGenBuffers(1)
    # affectation du buffer courant
    GL.glBindBuffer(GL.GL_ARRAY_BUFFER, vbo)

    GL.glBufferData(GL.GL_ARRAY_BUFFER, sommetsmusee, GL.GL_STATIC_DRAW)

    # Les deux commandes suivantes sont stockees dans l' ´ etat du vao courant ´
    # Active l'utilisation des donnees de positions ´
    # (le 0 correspond a la location dans le vertex shader) `
    GL.glEnableVertexAttribArray(0)
    # Indique comment le buffer courant (dernier vbo "binde") ´
    # est utilise pour les positions des sommets ´
    GL.glVertexAttribPointer(0, 3, GL.GL_FLOAT, GL.GL_FALSE, 0, None)

    GL.glDrawArrays(GL.GL_TRIANGLES, 0, 12*3)


    vao = Text.initalize_geometry()
    texture = glutils.load_texture('fontB.jpg')
    o = Text('', np.array([-0.8, 0.3], np.float32), np.array([0.8, 0.8], np.float32), vao, 2, programGUI_id, texture)
    viewer.add_object(o)
    o = Text('', np.array([-0.5, -0.2], np.float32), np.array([0.5, 0.3], np.float32), vao, 2, programGUI_id, texture)
    viewer.add_object(o)

    viewer.run()


if __name__ == '__main__':
    main()