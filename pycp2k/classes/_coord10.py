from pycp2k.inputsection import InputSection


class _coord10(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Unit = None
        self.Scaled = None
        self.Default_keyword = []
        self._name = "COORD"
        self._keywords = {'Scaled': 'SCALED', 'Unit': 'UNIT'}
        self._repeated_default_keywords = {'Default_keyword': 'DEFAULT_KEYWORD'}
        self._attributes = ['Default_keyword']

