import pygame as pg
from OpenGL.GL import *
import OpenGL.GL.shaders as shaders
from numpy import array

# settings
SCR_WIDTH = 800
SCR_HEIGHT = 600

code_vertex_shader = """
#version 150 core
in vec2 pos;

void main()
{
    gl_Position = vec4(pos, 0.0, 1.0);
}
"""

code_fragment_shader = """
#version 150 core
out vec4 outColor;

void main()
{
    outColor = vec4(1.0, 0.0, 0.0, 1.0);
}
"""

code_geometry_shader = """
#version 150 core

layout(points) in;
layout(line_strip, max_vertices = 2) out;

void main()
{
    gl_Position = gl_in[0].gl_Position + vec4(-0.1, 0.0, 0.0, 0.0);
    EmitVertex();

    gl_Position = gl_in[0].gl_Position + vec4(0.1, 0.0, 0.0, 0.0);
    EmitVertex();

    EndPrimitive();
}
"""


#
#
# vertex_shader = open("shaders/vertex_shader.glsl", "r").read()
# fragment_shader = open("shaders/fragment_shader.glsl", "r").read()
# geometry_shader = open("shaders/geometry_shader.glsl", "r").read()
#

class VCHelper:

    def __init__(self):
        self.vbo = None
        self.vao = None
        self.points = None
        self.shader = None
        self.clock = pg.time.Clock()
        self.windowSize = (SCR_WIDTH, SCR_HEIGHT)

        self.vertex_shader = code_vertex_shader
        self.fragment_shader = code_fragment_shader
        self.geometry_shader = code_geometry_shader

    def initShaders(self):
        """
        This method contains the definition and compilation instructions for the
            vertex, fragment, and geometry shaders.
        """
        # build and compile our shader program
        # ------------------------------------
        # vertex shader
        vertexShader = shaders.compileShader(self.vertex_shader, GL_VERTEX_SHADER)
        # fragment shader
        fragmentShader = shaders.compileShader(self.fragment_shader, GL_FRAGMENT_SHADER)
        # geometry shader
        geometryShader = shaders.compileShader(self.geometry_shader, GL_GEOMETRY_SHADER)
        # link shaders
        self.shader = shaders.compileProgram(vertexShader, fragmentShader, geometryShader)
        result = glGetProgramiv(self.shader, GL_LINK_STATUS)

        if not result:
            raise RuntimeError(glGetProgramInfoLog(self.shader))

        glUseProgram(self.shader)

    def initVertexBuffer(self):
        """ This method  initializes the vertex buffer objects (VBOs) containing the
            vertex data for the different geometries to be drawn """

        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)

        # set up vertex data (and buffer(s)) and configure vertex attributes
        # ------------------------------------------------------------------
        self.points = array([
            -0.5, 0.5, 1.0, 0.0, 0.0,  # top-left    (red)
            0.5, 0.5, 0.0, 1.0, 0.0,  # top-right  (green)
            0.5, -0.5, 0.0, 0.0, 1.0,  # bottom-right (blue)
            -0.5, -0.5, 1.0, 1.0, 0.0,  # bottom-left (yellow)
        ])
        self.vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, (GLfloat * len(self.points))(*self.points), GL_STATIC_DRAW)

        # position attribute
        glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 5 * sizeof(GLfloat), None)
        glEnableVertexAttribArray(0)

        # color attribute
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 5 * sizeof(GLfloat), ctypes.c_void_p(2 * sizeof(GLfloat)))
        glEnableVertexAttribArray(1)

        # size attribute
        glVertexAttribPointer(2, 1, GL_FLOAT, GL_FALSE, 5 * sizeof(GLfloat), ctypes.c_void_p(4 * sizeof(GLfloat)))
        glEnableVertexAttribArray(2)

        glBindBuffer(GL_ARRAY_BUFFER, 0)
        glBindVertexArray(0)

    def initWindow(self, width=SCR_WIDTH, height=SCR_HEIGHT):
        """ This method initializes a pygame window to serve as OpenGL context """
        pg.init()
        self.windowSize = (width, height)
        pg.display.set_mode(self.windowSize, pg.DOUBLEBUF | pg.OPENGL | pg.RESIZABLE)
        pg.display.set_caption("Visual Computing")

        # initialize OpenGL
        glClearColor(0.0, 0.0, 0.2, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

    def render(self):
        """ This method contains the instructions for rendering the scene. """
        # render
        # ------
        glClearColor(0.0, 0.0, 0.0, 1.0)
        glClear(GL_COLOR_BUFFER_BIT)

        # Render frame
        glUseProgram(self.shader)
        glBindVertexArray(self.vao)
        glDrawArrays(GL_POINTS, 0, 4)

        # Swap buffers
        pg.display.flip()

    def processEvents(self):
        """ This method contains the instructions for processing events. """

        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        self.initShaders()


# initialize the helper class
myWindow = VCHelper()
myWindow.initWindow()

# initialize the vertex buffer objects
myWindow.initVertexBuffer()

# initialize the shaders
myWindow.initShaders()

# render loop
while True:
    myWindow.processEvents()
    myWindow.render()
    myWindow.clock.tick(60)
