# -*- coding: utf-8 -*-
"""
Created on Fri Jun 19 22:54:15 2020

@author: msmsa
"""
from PySide6 import QtCore
from time import time
import warnings
import os
import traceback
from  ..MCResults import MCResults


class Worker_MC(QtCore.QThread):
    """
    This class instantiates a new QThread that handle the MC.\n
    """
    UpdatePBr_Opt = QtCore.Signal(int)
    Report = QtCore.Signal(dict)
    Error = QtCore.Signal(str)

    def __init__(self, parent, project, InputFlow_object, n, seed=None, TypeOfPFAS='All'):
        super().__init__(parent)
        self.project = project
        self.n = n
        self.seed = seed
        self.TypeOfPFAS = TypeOfPFAS
        self.InputFlow_object = InputFlow_object
        warnings.filterwarnings("ignore", category=RuntimeWarning)

    def run(self):
        try:
            self.UpdatePBr_Opt.emit(0)
            Time_start = time()
            self.project.setup_MC(self.InputFlow_object, seed=self.seed)
            MC_results_raw = self.project.MC_Run(n=self.n, TypeOfPFAS=self.TypeOfPFAS, signal=self.UpdatePBr_Opt)
            MC_results = MCResults(MC_results_raw)
            MC_results.to_df()
            Time_finish = time()
            self.UpdatePBr_Opt.emit(100)
            self.Report.emit({'time': round(Time_finish - Time_start), 'results': MC_results})
        except Exception as e:
            err_msg = f"Monte Carlo error:\n{traceback.format_exc()}"
            print(err_msg)
            self.Error.emit(err_msg)


class Worker_Plot(QtCore.QThread):
    """
    This class instantiates a new QThread that plot sankey.\n
    """
    Plot = QtCore.Signal()
    Error = QtCore.Signal(str)

    def __init__(self, parent, project):
        super().__init__(parent)
        self.Project = project

    def run(self):
        try:
            filename = os.path.join(os.getcwd(), 'sankey')
            print(f"[Worker_Plot] Generating sankey: {filename}.html")
            self.Project.plot_sankey(view=False, filename=filename)
            print(f"[Worker_Plot] Sankey generated, emitting Plot signal")
            self.Plot.emit()
        except Exception as e:
            err_msg = f"Plot error:\n{traceback.format_exc()}"
            print(err_msg)
            self.Error.emit(err_msg)
