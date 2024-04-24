from define import DEFAULT_ENM
from define import DEFAULT_EMG
class baseError(object):
    def __init__(self,eid=-1,enm=DEFAULT_ENM,emg=DEFAULT_EMG):
        self.eid = eid
        self.enm = enm
        self.emg = emg
    def as_string(self):
        string =  f'Return Error({self.enm},{self.eid}) type:{self}:\n'
        string += f'    {self.emg}'
        return string
    def __repr__(self):
        return f'<Error id={self.eid}>'
