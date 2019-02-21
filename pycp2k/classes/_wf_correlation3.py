from pycp2k.inputsection import InputSection
from ._mp2_info3 import _mp2_info3
from ._direct_canonical3 import _direct_canonical3
from ._wfc_gpw3 import _wfc_gpw3
from ._ri_mp23 import _ri_mp23
from ._opt_ri_basis3 import _opt_ri_basis3
from ._ri_rpa3 import _ri_rpa3
from ._ri_laplace3 import _ri_laplace3
from ._cphf3 import _cphf3
from ._interaction_potential9 import _interaction_potential9
from ._eri_mme4 import _eri_mme4


class _wf_correlation3(InputSection):
    def __init__(self):
        InputSection.__init__(self)
        self.Method = None
        self.Memory = None
        self.Scale_s = None
        self.Scale_t = None
        self.Group_size = None
        self.Row_block = None
        self.Col_block = None
        self.Calc_cond_num = None
        self.Ri_metric = None
        self.Eri_method = None
        self.Minimal_gap = None
        self.MP2_INFO = _mp2_info3()
        self.DIRECT_CANONICAL = _direct_canonical3()
        self.WFC_GPW = _wfc_gpw3()
        self.RI_MP2 = _ri_mp23()
        self.OPT_RI_BASIS = _opt_ri_basis3()
        self.RI_RPA = _ri_rpa3()
        self.RI_LAPLACE = _ri_laplace3()
        self.CPHF = _cphf3()
        self.INTERACTION_POTENTIAL = _interaction_potential9()
        self.ERI_MME = _eri_mme4()
        self._name = "WF_CORRELATION"
        self._keywords = {'Scale_t': 'SCALE_T', 'Method': 'METHOD', 'Scale_s': 'SCALE_S', 'Calc_cond_num': 'CALC_COND_NUM', 'Eri_method': 'ERI_METHOD', 'Row_block': 'ROW_BLOCK', 'Memory': 'MEMORY', 'Ri_metric': 'RI_METRIC', 'Group_size': 'GROUP_SIZE', 'Col_block': 'COL_BLOCK', 'Minimal_gap': 'MINIMAL_GAP'}
        self._subsections = {'DIRECT_CANONICAL': 'DIRECT_CANONICAL', 'RI_MP2': 'RI_MP2', 'MP2_INFO': 'MP2_INFO', 'CPHF': 'CPHF', 'OPT_RI_BASIS': 'OPT_RI_BASIS', 'RI_LAPLACE': 'RI_LAPLACE', 'WFC_GPW': 'WFC_GPW', 'ERI_MME': 'ERI_MME', 'INTERACTION_POTENTIAL': 'INTERACTION_POTENTIAL', 'RI_RPA': 'RI_RPA'}
        self._aliases = {'Ri': 'Ri_metric', 'Row_block_size': 'Row_block', 'Col_block_size': 'Col_block', 'Number_proc': 'Group_size', 'Calc_condition_number': 'Calc_cond_num'}


    @property
    def Number_proc(self):
        """
        See documentation for Group_size
        """
        return self.Group_size

    @property
    def Row_block_size(self):
        """
        See documentation for Row_block
        """
        return self.Row_block

    @property
    def Col_block_size(self):
        """
        See documentation for Col_block
        """
        return self.Col_block

    @property
    def Calc_condition_number(self):
        """
        See documentation for Calc_cond_num
        """
        return self.Calc_cond_num

    @property
    def Ri(self):
        """
        See documentation for Ri_metric
        """
        return self.Ri_metric

    @Number_proc.setter
    def Number_proc(self, value):
        self.Group_size = value

    @Row_block_size.setter
    def Row_block_size(self, value):
        self.Row_block = value

    @Col_block_size.setter
    def Col_block_size(self, value):
        self.Col_block = value

    @Calc_condition_number.setter
    def Calc_condition_number(self, value):
        self.Calc_cond_num = value

    @Ri.setter
    def Ri(self, value):
        self.Ri_metric = value
