#version 330

layout (points) in;
layout (triangle_strip, max_vertices = 6) out;

// Use arcade's global projection UBO
uniform Projection {
    uniform mat4 matrix;
} proj;

in vec2 vertex_pos[];
in vec4 vertex_color[];
in float vertex_radius[];

out vec2 g_uv;
out vec3 g_color;

void main() {
    vec2 center = vertex_pos[0];
    vec2 hsize = vec2(vertex_radius[0]);

    g_color = vertex_color[0].rgb;

    gl_Position = proj.matrix * vec4(vec2(-hsize.x, hsize.y) + center, 0.0, 1.0);
    g_uv = vec2(0, 1);
    EmitVertex();

    gl_Position = proj.matrix * vec4(vec2(-hsize.x, -hsize.y) + center, 0.0, 1.0);
    g_uv = vec2(0, 0);
    EmitVertex();

    gl_Position = proj.matrix * vec4(vec2(hsize.x, hsize.y) + center, 0.0, 1.0);
    g_uv = vec2(1, 1);
    EmitVertex();

    gl_Position = proj.matrix * vec4(vec2(hsize.x, -hsize.y) + center, 0.0, 1.0);
    g_uv = vec2(1, 0);
    EmitVertex();

    EndPrimitive();
}