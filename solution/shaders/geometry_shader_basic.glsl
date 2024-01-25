#version 330 core
layout(points) in;
layout(triangle_strip, max_vertices = 3) out;
void main()
{
    for(int i = 0; i < 3; i++) {
        gl_Position = gl_in[0].gl_Position +
            vec4(i == 0 ? -0.1 : 0.1,
            i == 2 ? -0.1 : 0.1, 0.0, 0.0);
        EmitVertex();
    }
    EndPrimitive();
}