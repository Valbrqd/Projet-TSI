from pickle import FALSE, TRUE
import OpenGL.GL as GL
import glfw
import pyrr
import numpy as np
import cpe3d as txt
class ViewerGL:
    def __init__(self):
        # initialisation de la librairie GLFW
        glfw.init()
        # paramétrage du context OpenGL
        glfw.window_hint(glfw.CONTEXT_VERSION_MAJOR, 3)
        glfw.window_hint(glfw.CONTEXT_VERSION_MINOR, 3)
        glfw.window_hint(glfw.OPENGL_FORWARD_COMPAT, GL.GL_TRUE)
        glfw.window_hint(glfw.OPENGL_PROFILE, glfw.OPENGL_CORE_PROFILE)
        # création et paramétrage de la fenêtre
        glfw.window_hint(glfw.RESIZABLE, False)
        self.window = glfw.create_window(1920, 1080, 'OpenGL', None, None)
        # paramétrage de la fonction de gestion des évènements
        glfw.set_key_callback(self.window, self.key_callback)
        # activation du context OpenGL pour la fenêtre
        glfw.make_context_current(self.window)
        glfw.swap_interval(1)
        # activation de la gestion de la profondeur
        GL.glEnable(GL.GL_DEPTH_TEST)
        # choix de la couleur de fond
        GL.glClearColor(0.556, 0.867, 1, 1.0)
        print(f"OpenGL: {GL.glGetString(GL.GL_VERSION).decode('ascii')}")

        self.objs = []
        self.touch = {}

    def run(self):
        # boucle d'affichage
        while not glfw.window_should_close(self.window):
            #=================== Inclinaison des objets si besoin =====================
            self.objs[4].transformation.rotation_euler[pyrr.euler.index().roll] = 0.7
            self.objs[4].transformation.rotation_euler[pyrr.euler.index().pitch] = 0.2
            self.objs[5].transformation.rotation_euler[pyrr.euler.index().yaw] = -3.2
            self.objs[6].transformation.rotation_euler[pyrr.euler.index().pitch] = -3.2
            self.objs[6].transformation.rotation_euler[pyrr.euler.index().roll] = 1.6
            GL.glClear(GL.GL_COLOR_BUFFER_BIT | GL.GL_DEPTH_BUFFER_BIT)
            # nettoyage de la fenêtre : fond et profondeur
            self.update_key()

            for obj in self.objs:
                GL.glUseProgram(obj.program)
                if isinstance(obj, txt.Object3D):
                    self.update_camera(obj.program)
                obj.draw()

            # print(np.linalg.norm(self.objs[0].transformation.translation - self.objs[1].transformation.translation))         

            # changement de buffer d'affichage pour éviter un effet de scintillement
            glfw.swap_buffers(self.window)
            # gestion des évènements
            glfw.poll_events()
        
    def key_callback(self, win, key, scancode, action, mods):
        # sortie du programme si appui sur la touche 'échappement'
        if key == glfw.KEY_ESCAPE and action == glfw.PRESS:
            glfw.set_window_should_close(win, glfw.TRUE)
        self.touch[key] = action
    
    def add_object(self, obj):
        self.objs.append(obj)

    def set_camera(self, cam):
        self.cam = cam

    def update_camera(self, prog):
        GL.glUseProgram(prog)
        # Récupère l'identifiant de la variable pour le programme courant
        loc = GL.glGetUniformLocation(prog, "translation_view")
        # Vérifie que la variable existe
        if (loc == -1) :
            print("Pas de variable uniforme : translation_view")
        # Modifie la variable pour le programme courant
        translation = -self.cam.transformation.translation
        GL.glUniform4f(loc, translation.x, translation.y, translation.z, 0)

        # Récupère l'identifiant de la variable pour le programme courant
        loc = GL.glGetUniformLocation(prog, "rotation_center_view")
        # Vérifie que la variable existe
        if (loc == -1) :
            print("Pas de variable uniforme : rotation_center_view")
        # Modifie la variable pour le programme courant
        rotation_center = self.cam.transformation.rotation_center
        GL.glUniform4f(loc, rotation_center.x, rotation_center.y, rotation_center.z, 0)

        rot = pyrr.matrix44.create_from_eulers(-self.cam.transformation.rotation_euler)
        loc = GL.glGetUniformLocation(prog, "rotation_view")
        if (loc == -1) :
            print("Pas de variable uniforme : rotation_view")
        GL.glUniformMatrix4fv(loc, 1, GL.GL_FALSE, rot)
    
        loc = GL.glGetUniformLocation(prog, "projection")
        if (loc == -1) :
            print("Pas de variable uniforme : projection")
        GL.glUniformMatrix4fv(loc, 1, GL.GL_FALSE, self.cam.projection)

    def update_key(self):
        if glfw.KEY_UP in self.touch and self.touch[glfw.KEY_UP] > 0:
#===================================== Gestion collision et affichge texte ========================================
            d = pyrr.matrix33.apply_to_vector(pyrr.matrix33.create_from_eulers(self.objs[0].transformation.rotation_euler), pyrr.Vector3([0, 0, 0.3]))
            bol = True
            for i in range(5,len(self.objs)-7):
                if abs(self.objs[0].transformation.translation.x + d[0] -self.objs[i].transformation.translation.x)<1.8 and abs(self.objs[0].transformation.translation.z + d[2] -self.objs[i].transformation.translation.z)<1.8 :
                    bol = False
            if bol :
                self.objs[0].transformation.translation += d
#================================ Affichage Suzanne ==============================================
            if abs(self.objs[0].transformation.translation.x + d[0] - self.objs[1].transformation.translation.x)<3 and abs(self.objs[0].transformation.translation.z + d[2] -self.objs[1].transformation.translation.z)<3 :
                self.objs[-1].value = "Le singe suzanne"
                self.objs[-1].visible = True
            else :
                self.objs[-1].visible = False
#================================ Affichage Stegosaurus ==========================================
            if abs(self.objs[0].transformation.translation.x + d[0] - self.objs[2].transformation.translation.x)<3 and abs(self.objs[0].transformation.translation.z + d[2] -self.objs[2].transformation.translation.z)<3 :
                self.objs[-2].value = "Stegosaurus"
                self.objs[-2].visible = True
            else :
                self.objs[-2].visible = False
#================================ Affichage Voiture ==============================================
            if abs(self.objs[0].transformation.translation.x + d[0] - self.objs[3].transformation.translation.x)<3 and abs(self.objs[0].transformation.translation.z + d[2] -self.objs[3].transformation.translation.z)<3 :
                self.objs[-3].value = "Voiture multiverse"
                self.objs[-3].visible = True
            else :
                self.objs[-3].visible = False
#================================ Affichage Donut ==============================================
            if abs(self.objs[0].transformation.translation.x + d[0] - self.objs[4].transformation.translation.x)<3 and abs(self.objs[0].transformation.translation.z + d[2] -self.objs[4].transformation.translation.z)<3 :
                self.objs[-4].value = "Donut de Rodolphe"
                self.objs[-4].visible = True
            else :
                self.objs[-4].visible = False
#================================ Affichage Loup ==============================================
            if abs(self.objs[0].transformation.translation.x + d[0] - self.objs[5].transformation.translation.x)<3 and abs(self.objs[0].transformation.translation.z + d[2] -self.objs[5].transformation.translation.z)<3 :
                self.objs[-5].value = "Golden Wolf"
                self.objs[-5].visible = True
            else :
                self.objs[-5].visible = False
#================================ Affichage Dracaufeu ==============================================
            if abs(self.objs[0].transformation.translation.x + d[0] - self.objs[6].transformation.translation.x)<3 and abs(self.objs[0].transformation.translation.z + d[2] -self.objs[6].transformation.translation.z)<3 :
                self.objs[-6].value = "Naruto"
                self.objs[-6].visible = True
            else :
                self.objs[-6].visible = False
#================================ Affichage Central ==============================================
            if abs(self.objs[0].transformation.translation.x + d[0] - self.objs[7].transformation.translation.x)<3 and abs(self.objs[0].transformation.translation.z + d[2] -self.objs[7].transformation.translation.z)<3 :
                self.objs[-7].value = "Central"
                self.objs[-7].visible = True
            else :
                self.objs[-7].visible = False
#=================================================================================================
        if glfw.KEY_DOWN in self.touch and self.touch[glfw.KEY_DOWN] > 0:
            d2= pyrr.matrix33.apply_to_vector(pyrr.matrix33.create_from_eulers(self.objs[0].transformation.rotation_euler), pyrr.Vector3([0, 0, 0.1]))
            self.objs[0].transformation.translation -= d2

            if abs(self.objs[0].transformation.translation.x + d2[0] - self.objs[1].transformation.translation.x)<3 and abs(self.objs[0].transformation.translation.z + d2[2] -self.objs[1].transformation.translation.z)<3 :
                self.objs[-1].value = "Le singe suzanne"
                self.objs[-1].visible = True
            else :
                self.objs[-1].visible = False

            if abs(self.objs[0].transformation.translation.x + d2[0] - self.objs[2].transformation.translation.x)<3 and abs(self.objs[0].transformation.translation.z + d2[2] -self.objs[2].transformation.translation.z)<3 :
                self.objs[-2].value = "Stegosaurus"
                self.objs[-2].visible = True
            else :
                self.objs[-2].visible = False

            if abs(self.objs[0].transformation.translation.x + d2[0] - self.objs[3].transformation.translation.x)<3 and abs(self.objs[0].transformation.translation.z + d2[2] -self.objs[3].transformation.translation.z)<3 :
                self.objs[-3].value = "Voiture multiverse"
                self.objs[-3].visible = True
            else :
                self.objs[-3].visible = False
            
            if abs(self.objs[0].transformation.translation.x + d2[0] - self.objs[4].transformation.translation.x)<3 and abs(self.objs[0].transformation.translation.z + d2[2] -self.objs[4].transformation.translation.z)<3 :
                self.objs[-4].value = "Donut de Rodolphe"
                self.objs[-4].visible = True
            else :
                self.objs[-4].visible = False

            if abs(self.objs[0].transformation.translation.x + d2[0] - self.objs[5].transformation.translation.x)<3 and abs(self.objs[0].transformation.translation.z + d2[2] -self.objs[5].transformation.translation.z)<3 :
                self.objs[-5].value = "Golden Wolf"
                self.objs[-5].visible = True
            else :
                self.objs[-5].visible = False

            if abs(self.objs[0].transformation.translation.x + d2[0] - self.objs[6].transformation.translation.x)<3 and abs(self.objs[0].transformation.translation.z + d2[2] -self.objs[6].transformation.translation.z)<3 :
                self.objs[-6].value = "Dracaufeu 120PV"
                self.objs[-6].visible = True
            else :
                self.objs[-6].visible = False
            
            if abs(self.objs[0].transformation.translation.x + d2[0] - self.objs[7].transformation.translation.x)<3 and abs(self.objs[0].transformation.translation.z + d2[2] -self.objs[7].transformation.translation.z)<3 :
                self.objs[-7].value = "Central"
                self.objs[-7].visible = True
            else :
                self.objs[-7].visible = False
#====================================================================================================================================
        if glfw.KEY_LEFT in self.touch and self.touch[glfw.KEY_LEFT] > 0:
            self.objs[0].transformation.rotation_euler[pyrr.euler.index().yaw] -= 0.1
        if glfw.KEY_RIGHT in self.touch and self.touch[glfw.KEY_RIGHT] > 0:
            self.objs[0].transformation.rotation_euler[pyrr.euler.index().yaw] += 0.1

        if glfw.KEY_I in self.touch and self.touch[glfw.KEY_I] > 0:
            self.cam.transformation.rotation_euler[pyrr.euler.index().roll] -= 0.1
        if glfw.KEY_K in self.touch and self.touch[glfw.KEY_K] > 0:
            self.cam.transformation.rotation_euler[pyrr.euler.index().roll] += 0.1
        if glfw.KEY_J in self.touch and self.touch[glfw.KEY_J] > 0:
            self.cam.transformation.rotation_euler[pyrr.euler.index().yaw] -= 0.1
        if glfw.KEY_L in self.touch and self.touch[glfw.KEY_L] > 0:
            self.cam.transformation.rotation_euler[pyrr.euler.index().yaw] += 0.1

        if glfw.KEY_SPACE in self.touch and self.touch[glfw.KEY_SPACE] == 0:
            self.cam.transformation.rotation_euler = self.objs[0].transformation.rotation_euler.copy() 
            self.cam.transformation.rotation_euler[pyrr.euler.index().yaw] += np.pi
            self.cam.transformation.rotation_center = self.objs[0].transformation.translation + self.objs[0].transformation.rotation_center
            self.cam.transformation.translation = self.objs[0].transformation.translation + pyrr.Vector3([0, 2, 5])
