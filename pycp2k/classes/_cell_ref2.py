from pycp2k.inputsection import InputSection


class _cell_ref2(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.A = None
        self.B = None
        self.C = None
        self.Abc = None
        self.Alpha_beta_gamma = None
        self.Cell_file_name = None
        self.Cell_file_format = None
        self.Periodic = None
        self.Multiple_unit_cell = None
        self.Symmetry = None
        self._name = "CELL_REF"
        self._keywords = {'Cell_file_format': 'CELL_FILE_FORMAT', 'B': 'B', 'Cell_file_name': 'CELL_FILE_NAME', 'Abc': 'ABC', 'A': 'A', 'Periodic': 'PERIODIC', 'Alpha_beta_gamma': 'ALPHA_BETA_GAMMA', 'Symmetry': 'SYMMETRY', 'C': 'C', 'Multiple_unit_cell': 'MULTIPLE_UNIT_CELL'}
        self._aliases = {'Angles': 'Alpha_beta_gamma'}


    @property
    def Angles(self):
        """
        See documentation for Alpha_beta_gamma
        """
        return self.Alpha_beta_gamma

    @Angles.setter
    def Angles(self, value):
        self.Alpha_beta_gamma = value
