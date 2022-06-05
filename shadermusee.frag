#version 330 core

// Variable de sortie (sera utilisé comme couleur)
out vec4 color;

//Un Fragment Shader minimaliste
uniform vec4 colorchange;
void main (void)
{
  //Couleur du fragment
  color = colorchange;
}

