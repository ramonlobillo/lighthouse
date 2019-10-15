#!/bin/python
import datetime,gzip,argparse,time, yaml
from modules.accessKpi import accessKpi

'''
*****************
* runKpis.py *
*****************
crontask that gather server.log and generates kpis entry in defined output.
    @param input_file:Input file should not be gzipped. Example: server.log.
    @param period:Time to consider since now backwards. In seconds.
'''

def main(logfile, period):
    '''
    Process access.log to generate KPI entry on file
    '''

    access_kpis= accessKpi("kpis_config.yml",period,logfile)
    if len(access_kpis.getConsideredLog()) == 0:
        print("No log lines found from %s to %s"                     \
           %(access_kpis.getLimit().strftime("%Y-%m-%d %H:%M:%S.%f"),\
             access_kpis.getNow().strftime("%Y-%m-%d %H:%M:%S.%f")))
        exit(1)
    else:
        print("%s lines to process from %s. Interval: %s <-> %s "\
            %(len(access_kpis.getConsideredLog()),logfile,       \
            access_kpis.getLimit().strftime("%Y-%m-%d %H:%M:%S"),\
            access_kpis.getNow().strftime("%Y-%m-%d %H:%M:%S")))


    access_kpis.setEntry()
    access_kpis.dumpEntry()
    del(access_kpis)

# END main()


if __name__ == '__main__':

    start_time = time.time()
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file', help='Input file should not be gzipped. Example: server.log')
    parser.add_argument('period', help='Time to consider since now backwards. In seconds.')
    args = parser.parse_args()
    print('Loading kpis_config.yml configuration')
    main(args.input_file, args.period)
    print('FINISHED: Created in %.2f seconds.' % (time.time() - start_time))
    # END main
