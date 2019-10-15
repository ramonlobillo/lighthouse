import re, string, os, datetime,yaml


class kpi:

    kpis_config=None
    period=None
    now=None
    limit=None
    outputfilepath=None
    logfilepath=None
    considered_log=None
    dest_filename=None
    headers=None
    entry=None

    def __init__(self,kpis_config_filepath,period,logfilepath):
        '''
        Constructor of KPI class.
        '''
        self.period=period
        self.logfilepath=logfilepath

        self.kpis_config=yaml.load(open(kpis_config_filepath))

        #now=datetime.datetime.now()
        self.now = datetime.datetime.strptime("2019-10-15 23:49:59,999","%Y-%m-%d %H:%M:%S,%f")
        self.limit = self.now - datetime.timedelta(seconds=int(period))

        self.considered_log=self.getLogs()
    # END constructor

    def setEntry(self):
        pass

    def getConfig(self):
        return self.kpis_config

    def getConsideredLog(self):
        return self.considered_log

    def getLimit(self):
        return self.limit

    def getNow(self):
        return self.now

    def getLogs(self):
        '''
        Get logfile and filter the entries from limit timestamp until now.
        Return the filtered logs in a list of strings.
        '''
        timestamp_format=re.compile(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}')
        loglines=[]
        with open(self.logfilepath, 'rt') as log:
            for line in reversed(log.readlines()):
                if timestamp_format.search(" ".join(line.split()[0:2])):
                    timestamp=datetime.datetime.strptime( \
                            (" ".join(line.split()[0:2])), "%Y-%m-%d %H:%M:%S,%f")
                    if timestamp > self.limit:
                        loglines.append(line)
                    else:
                        break
        return loglines
    # END getlogs

    def addHeader(self):
        '''
        Check if file exists and if not, created it and add the headers.
        '''
        if not os.path.exists(self.dest_filename):
            output=open(self.dest_filename,'w')
            output.write(";".join(self.headers)+'\n')
            output.close()
    # END addHeader

    def dumpEntry(self):
        '''
        dump entry in the destination file.
        '''
        self.addHeader()
        output=open(self.dest_filename,'a+')
        output.write(";".join(str(v) for v in self.entry))
        output.write('\n')
        output.close()
    # END dumpEntry

