import kpi


class accessKpis(kpi):
    
    def __init__(self,kpis_config_filepath,period,logfilepath):
        super(accessKpis, self).__init(kpis_config_filepath,period,logfilepath)
        config=self.getConfig()
        dest_filename=config['accessOutput']
        headers=config['accessHeaders']
        self.entry=None
    
    def setEntry(loglines):
        '''
        Calculate kpi entry
        '''
    
        entry = [0] * 3
        entry[0]=loglines[0].split()[0].strip()
        starting_time=loglines[0].split()[1].strip()
        finishing_time=loglines[-1].split()[1].strip()
        entry[1]=starting_time+"-"+finishing_time
        for line in self.considered_logs:
            if "GET" in line:
                entry[2]=entry[2]+1

        self.entry=entry
    # END setEntry


