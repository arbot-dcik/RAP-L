import baseError
from define import DEFAULT_EMG
class SyntaxErr(baseError.baseError):
    def __init__(self,emg=DEFAULT_EMG):
        super().__init__(1,'SyntaxErr',emg)
