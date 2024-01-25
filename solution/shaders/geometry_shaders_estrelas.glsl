#version 330 core
layout(points) in;
layout(line_strip, max_vertices = 22) out;

in vec3 vColor[]; // Recebe a cor do Vertex Shader
out vec3 fColor;  // Passa a cor ao Fragment Shader

const float PI = 3.1415926;
const int numPoints = 10; // Número de pontas da estrela
const float outerRadius = 0.2; // Raio externo
const float innerRadius = 0.1; // Raio interno

void main() {
    fColor = vColor[0]; // Define a cor da estrela

    for(int i = 0; i <= numPoints * 2; i++) {
        float angle = 2.0 * PI * float(i) / float(numPoints);
        float radius = i % 2 == 0 ? outerRadius : innerRadius;

        vec4 offset = vec4(radius * cos(angle), radius * sin(angle), 0.0, 0.0);
        gl_Position = gl_in[0].gl_Position + offset;
        EmitVertex();
    }

    EndPrimitive(); // Finaliza a primitiva atual
}