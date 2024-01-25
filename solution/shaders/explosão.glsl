#version 150 core

layout(points) in;
layout(points, max_vertices = 100) out;

in vec3 vColor[];
out vec3 fColor;

const int numParticles = 100;
const float spread = 1.0; // Quão longe as partículas podem ir
const float PI = 3.1415926535897932384626433832795;

void main() {
    fColor = vColor[0]; // Cor baseada na entrada do vertex shader

    for (int i = 0; i < numParticles; ++i) {
        float angle = 2.0 * PI * float(i) / float(numParticles);
        float distance = spread * fract(sin(float(i) * 12.9898 + 4.1414) * 43758.5453);
        vec4 offset = vec4(distance * cos(angle), distance * sin(angle), 0.0, 0.0);
        gl_Position = gl_in[0].gl_Position + offset;
        gl_PointSize = 100.0; // Ajuste conforme necessário para aumentar o tamanho do ponto
        EmitVertex();
        EndPrimitive();
    }
}
