from .templates import BasicTemplate

from multiprocessing import Pipe


class Basic(BasicTemplate):
    def __init__(self, ctrl_pipe: Pipe, conf : dict = {}):
        super().__init__(ctrl_pipe=ctrl_pipe, conf=conf)
        