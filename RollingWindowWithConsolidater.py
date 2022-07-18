# region imports
from AlgorithmImports import *
# endregion

class consolidate(QCAlgorithm):

    def Initialize(self):
        self.SetStartDate(2021, 1, 17)  # Set Start Date
        self.SetEndDate(2021,1,25)
        self.SetCash(100000)  # Set Strategy Cash
        equity=self.AddEquity("SPY", Resolution.Minute)
        self.equity=equity.Symbol
        self.Consolidate(self.equity, timedelta(minutes=5), self.OnDataconsolidated)
        self.window =RollingWindow[TradeBar](5)
        self.mincount=0
        self.consolcount=0

    def OnDataconsolidated(self,bar):
        self.window.Add(bar)
        if self.consolcount >3:return
        self.Log("Updating 5 Minute Bar") 
        self.Log("Time:{0} >> Open:{1} >> High:{3}>> Low:{4} >>Close: {2}".format(bar.Time,bar.Open,bar.Close,bar.High,bar.Low))
        self.consolcount+=1

    def OnData(self, data: Slice):
        if data[self.equity] is None: return

        if not self.window.IsReady : return

        if self.mincount > 15:return
        self.Log("Data in Rolling window")
        self.Log("Time:{0} >> Open:{1} >> High:{3}>> Low:{4}>> Close: {2} >> High:{3}".format(data.Time,self.window[0].Open,self.window[0].Close,\
        self.window[0].High,self.window[0].Low))
        
        #self.Log("Time:{0} >> Open:{1} >> High:{3}>> Low:{4}>> Close: {2} >> High:{3}".format(data.Time,self.window[1].Open,self.window[1].Close,\
        #self.window[1].High,self.window[1].Low))

        self.mincount+=1
