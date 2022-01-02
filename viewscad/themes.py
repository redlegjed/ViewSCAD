'''
Themes for ViewScad
================================================================
Defines a class to define the theme plus these predefined themes:
* 'light' - same as original version of ViewScad
* 'dark' - Dark background and grid lines changed
'''
 
 
#================================================================
#%% Imports
#================================================================
 
#================================================================
#%% Constants
#================================================================
 
#================================================================
#%% Functions
#================================================================

def col_from_hex(c):
    return [int(c[1:3], 16) / 256, int(c[3:5], 16) / 256, int(c[5:7], 16) / 256]

#================================================================
#%% Classes
#================================================================
 
class Theme():
    """
    Theme class for ViewScad Renderer

    The class defines properties for all the colors used in  
    Viewscad

    Example usage
    -----------------
    Create default theme
    >>> my_theme = Theme('my_theme_name')

    Customise theme by entering color labels when creating the
    theme object.
    >>> custom_theme = Theme('custom_theme',AXIS_X_COLOR='#090909')

    Display theme name an colors
    >>> my_theme
        ViewScad theme [dark]
        ------------------------------
        AXIS_X_COLOR : #ff00ff
        AXIS_Y_COLOR : #ffff00
        AXIS_Z_COLOR : #00ffff
        BACKGROUND_COLOR : #3D3D3D
        OBJ_COLOR : #f7d62c
        SELECTED_EDGE_COLOR : #6666ff
        SELECTED_FACE_COLOR : #ff0000
        SELECTED_VERTEX_COLOR : #00ff00

    """

    def __init__(self,name,**kwargs) -> None:

        self.name = name
        
        self.OBJ_COLOR = kwargs.get('OBJ_COLOR', '#f7d62c')
        self.SELECTED_FACE_COLOR = kwargs.get('SELECTED_FACE_COLOR', '#ff0000')
        self.SELECTED_EDGE_COLOR = kwargs.get('SELECTED_EDGE_COLOR', '#6666ff')
        self.SELECTED_VERTEX_COLOR = kwargs.get('SELECTED_VERTEX_COLOR', '#00ff00')
        self.BACKGROUND_COLOR = kwargs.get('BACKGROUND_COLOR', '#ffffff')
        self.AXIS_X_COLOR = kwargs.get('AXIS_X_COLOR', '#ff0000')
        self.AXIS_Y_COLOR = kwargs.get('AXIS_Y_COLOR', '#00ff00')
        self.AXIS_Z_COLOR = kwargs.get('AXIS_Z_COLOR', '#0000ff')
        self.TEXT_COLOR = kwargs.get('TEXT_COLOR', '#0f0f0f')

    def __repr__(self) -> str:
        """
        Display theme name and colors

        Returns
        -------
        str
            Theme name and list of all the colors
        """
        txt = [
            f'ViewScad theme [{self.name}]',
            '-'*30,
        ]
        txt += [f'{k} : {getattr(self,k)}' for k in dir(self) if k.endswith('_COLOR')]

        return '\n'.join(txt)

    @property
    def OBJ_RGB(self):
        return col_from_hex(self.OBJ_COLOR)

    @property
    def SELECTED_FACE_RGB(self):
        return col_from_hex(self.SELECTED_FACE_COLOR)

    @property
    def SELECTED_EDGE_COLOR_INT(self):
        return col_from_hex(self.SELECTED_EDGE_COLOR)

    @property
    def SELECTED_VERTEX_RGB(self):
        return col_from_hex(self.SELECTED_VERTEX_COLOR)

    @property
    def axis_cols(self):
        return [self.AXIS_X_COLOR,self.AXIS_Y_COLOR,self.AXIS_Z_COLOR]

#================================================================
#%% Themes
#================================================================
# Create some predefined themes

# Light theme - default
theme_light = Theme('light')

# Dark theme - grid colors are secondary colors
theme_dark = Theme('dark',
    BACKGROUND_COLOR='#3D3D3D',
    AXIS_X_COLOR='#ff00ff',
    AXIS_Y_COLOR='#ffff00',
    AXIS_Z_COLOR='#00ffff',
    TEXT_COLOR='#ffffff',
)

