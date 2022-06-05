#version 330 core

// Variable d'entrée, ici la position
layout (location = 0) in vec3 position;

//Un Vertex Shader minimaliste
uniform vec4 translation;
uniform mat4 rotation;
uniform mat4 projection
void main (void)
{
  //Coordonnees du sommet
  
  //gl_Position = vec4(position,1.0);
  vec4 p=rotation *vec4(position, 1.0);
  //p.x=p.x*0.3;
  //p+=vec4(-0.7,-0.8,0.0,0.0);
  gl_Position = p+translation;
  gl_Position = projection*gl_Position;

}
