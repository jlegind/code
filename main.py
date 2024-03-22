# import time module, Observer, FileSystemEventHandler
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import pandas as pd
import csv # for the delimiter sniffer
import cchardet as chardet # for file encoding sniffer
import numpy as np
import os

class OnMyWatch:
    # Set the directory on watch
    # watchDirectory = ""

    def __init__(self, watchDirectory = r"C:\csv_processing\Data"):
        self.watchDirectory = watchDirectory
        self.observer = Observer()
        print(f"Monitoring {self.watchDirectory} ")
        import os


    def run(self):
        event_handler = Handler(path = self.watchDirectory)
        self.observer.schedule(event_handler, self.watchDirectory)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Observer Stopped")

        self.observer.join()


class Handler(FileSystemEventHandler):

    def __init__(self, path=''):
        self.path_to_watch = path

    def fileNameGetDate(self, filename):
        # A very specific function for extracting the date string as ISO date (yyyy-MM-dd) from the file name itself. Example: NHMD_Herba_20230913_15_55_RL.csv
        tokens = None
        if '-' in filename:
            tokens = filename.split('-')
        else:
            tokens = filename.split('_')

        fileDate = f"{tokens[2]}"
        year = fileDate[0:4]
        month = fileDate[4:6]
        day = fileDate[6:8]
        isoDate = f"{year}-{month}-{day}"
        return isoDate

    def backslashFilepathSanitizer(self, filePath):
        #Utility function that might come in handy later.
        tokenPath = filePath.split('\\')
        sanPath = '/'.join(tokenPath)
        return sanPath

    def getDelimiter(self, filePath):
        '''
        The file delimiter might not always be the same so a delimiter sniffer is useful.
        :param filePath: Must be the absolute path
        :return: the *sv delimiter
        '''

        # filePath = self.backslashFilepathSanitizer(filePath)
        # print(f"The filepath is: -{filePath}-")
        with open(filePath, 'r') as f1:
            dialect = csv.Sniffer().sniff(f1.read())  #### detect delimiters
            f1.seek(0)

            match dialect.delimiter:
                case '\t':
                    print("Delimiter is TAB")
                    return "\t"
                case ';':
                    return ";"
                case ',':
                    return ','
                case '|':
                    return '|'
                case _:  # This is the default case
                    return dialect.delimiter
                    print("Error, no recognized delimiter found!")

    def encodingSniffer(self, fileName):
        '''
         Made to check the file encoding. Will mainly be utf-8 or windows-1252 (ANSI)
        :param fileName: Absolute file path
        :return: the encoding as a string
        '''
        with open(f"{fileName}", "rb") as f:
            msg = f.read()
            result = chardet.detect(msg)
            enc = result['encoding']
            match enc:
                case 'ASCII':
                    return 'Windows-1252'
                case 'UTF-8':
                    return 'UTF-8'
                case 'UTF-8-SIG':
                    return 'UTF-8'
                case _:
                    print('unknown encoding')
                    return 'Windows-1252'

    def extractFilename(self, name, separator='\\'):
        #Picks out the file name from a full file path.
        tokens = name.split(separator)
        print('TOKENSSSS AH!', tokens)
        nameCandidate = tokens[-1] #Get last item in tokens which is the filename and the extension.
        realName = nameCandidate[0:-4] # Pick out the name and no extension.
        return realName

    def addColumnsToDf(self, myDf, filename):
        ''' Adds three specific columns see https://github.com/NHMDenmark/Mass-Digitizer/issues/461#issuecomment-1953535744
        myDf is generated in the exe part of the code and comes from the file added to the monitored directory
        :returns the df with the three added columns
        '''
        header = myDf.columns.to_list()
        print(myDf.head(2).to_string())
        dateString = self.fileNameGetDate(filename)

        remarks = 'notes'
        # CONDITION IN HERE
        myDf['datefile_date'] = np.where(~myDf[remarks].notnull(), myDf[remarks], dateString)  # if remarks are not empty the date string is added to the 'datefile_date column.
        myDf['datefile_date'] = np.where(~myDf[remarks].notnull(), myDf[remarks], dateString)
        # Columns added to satisfy the tabular remarks requirements

        myDf['datafile_remark'] = filename
        myDf['datafile_source'] = 'DaSSCo data file'

        return myDf

    def dfToFile(self, myDf, filename, name_extension=''):  # name_extension can be 'original'...
        # Write the *SV processed file in place of the original. This file will be ready to transfer into the 'PostProcessed' directory
        outputPath = f"{self.path_to_watch}/{filename}"

        if name_extension:
            tokenPath = outputPath.split('.')
            print(tokenPath)
        delimiter = self.getDelimiter(outputPath)
        coda = self.encodingSniffer(outputPath)

        myDf.to_csv(outputPath, sep=delimiter, index=False, header=True, encoding=coda)
        return "TSV saved :)"

    def fileNameAppend(myString, fileName):
        """
        For adding a string value to the end of a filename prior to the extension.
        :param myString: Could be 'original' or 'processed' or ...
        :param fileName:  The file name that should be operated on.
        :return: The tweaked filename
        """
        tokenized = fileName.split('.')
        namePart = tokenized[0]
        extension = tokenized[-1]
        updatedName = f"{namePart}{myString}.{extension}"
        return updatedName


    def on_any_event(self, event):

        # df = self.addColumnsToDf(df, )
        # except PermissionError as e:  # A silly error that does not affect the desired result, i.e. the end output file. Likely an issue with the directory being on the N drive.
        #     pass
        if event.is_directory:
            return None

        elif event.event_type == 'created':
            # Event is created, you can process it now
            fileFullPath = event.src_path
            print(f"Watchdog received created event - {fileFullPath}")

            time.sleep(3)
            delimiter = self.getDelimiter(filePath=fileFullPath)
            fileEncoding = self.encodingSniffer(fileFullPath)
            fileName = self.extractFilename(fileFullPath)
            df = pd.read_csv(fileFullPath, sep=delimiter, encoding=fileEncoding, converters={'agentlastname': lambda x: x.replace('/r', '')})
            print(f"The delimiter is -{delimiter}- and the filie encoding is: [{fileEncoding}]")
            df = self.addColumnsToDf(df, fileName)
            print(f'file path preior to dfto file! !{fileFullPath}!')
            ###
            # SET destination directory
            destinationFolder = r"C:\csv_processing\Data"
            destinationFileName = fileName
            dest = f"{destinationFolder}\{fileName}.csv"
            print(f"DESTINATION:::{dest}")
            # res = self.dfToFile(df, fileFullPath, name_extension='_original')
            # print(res)



if __name__ == '__main__':
    watch = OnMyWatch()
    watch.run()