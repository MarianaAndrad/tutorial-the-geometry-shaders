#version 330 core

layout(points) in;
layout(line_strip, max_vertices = 4) out;

void main() {
    // Define o deslocamento para as linhas paralelas
    float offset = 0.05;

    // Primeira linha paralela
    gl_Position = gl_in[0].gl_Position + vec4(-offset, offset, 0.0, 0.0);
    EmitVertex();
    gl_Position = gl_in[0].gl_Position + vec4(offset, offset, 0.0, 0.0);
    EmitVertex();

    // Finaliza a primeira linha
    EndPrimitive();

    // Segunda linha paralela
    gl_Position = gl_in[0].gl_Position + vec4(-offset, -offset, 0.0, 0.0);
    EmitVertex();
    gl_Position = gl_in[0].gl_Position + vec4(offset, -offset, 0.0, 0.0);
    EmitVertex();

    // Finaliza a segunda linha
    EndPrimitive();
}
