from modules.kpi import kpi


class accessKpi(kpi):

    def __init__(self, kpis_config_filepath, period, logfilepath):
        super(accessKpi, self).__init__(kpis_config_filepath, \
                                        period, logfilepath)
        config = self.getConfig()
        self.dest_filename = config['accessOutput']
        self.headers = config['accessHeaders']
        self.entry = []

    def setEntry(self):
        '''
        Calculate kpi entry
        '''
        loglines = self.considered_log
        entry = [0] * 3
        entry[0] = loglines[0].split()[0].strip()
        starting_time = loglines[0].split()[1].strip()
        finishing_time = loglines[-1].split()[1].strip()
        entry[1] = starting_time+"-"+finishing_time
        for line in loglines:
            if "GET" in line:
                entry[2] = entry[2]+1
        self.entry = entry
        
    # END setEntry
