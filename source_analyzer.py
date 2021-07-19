import os
class Source_Analyzer:
    def __init__(self, source):
        self.source = source
        self.is_end = False
        self.current = ''
        self.counter = 0
        self.extension_list = []
        self.ordanzahl = 0
        self.fileanzahl = 0
        self.len_list = 0
        self.fulllist = []
        self.scanlist = os.listdir(source)
        self.filesize = 0.0
        self.ordsize = 0.0

    def scan(self):
#        print(self.scanlist)
        for self.current in self.scanlist:
            self.fulllist.append(os.path.join(self.source, self.current))
        self.len_list = len(self.fulllist)
#        print(self.fulllist)
#        print(self.lenlist)
        while self.is_end == False:
            for current in self.fulllist:
                self.current=str(current)
#                print(self.current)
                if os.path.isdir(self.current):
                    self.counter = self.counter+1
#                    print(f'if ' + str(self.counter))
#                    self.is_end = False
                    self.scanlist = os.listdir(self.current)
                    self.merged = os.path.join(self.source, current)
                    for current in self.scanlist:
                        self.fulllist.append(os.path.join(self.merged, current))
                    self.len_list=len(self.fulllist)
                else:
                    self.counter = self.counter+1
#                    print(f'else ' + str(self.counter))
                    if self.len_list == self.counter:
                        self.is_end = True
#                print(self.fulllist)

    def getFilesize(self):
        for current in self.fulllist:
            if os.path.isfile(current) == True:
                self.filesize = self.filesize + os.stat(current).st_size
        return self.filesize

    def getOrdsize(self):
        for current in self.fulllist:
            if os.path.isdir(current) == True:
                self.ordsize = self.ordsize + os.stat(current).st_size
        return self.ordsize

    def getOrdanzahl(self):
        for current in self.fulllist:
            if os.path.isdir(current) == True:
                self.ordanzahl += 1
        return self.ordanzahl

    def getFileanzahl(self):
        for current in self.fulllist:
            if os.path.isfile(current) == True:
                self.fileanzahl += 1
        return self.fileanzahl

    def split_path(self, path):
        return

    def getExtensions(self):
        #fullfilelist = [full_file_path for full_file_path in self.fulllist if os.path.isfile(full_file_path)]
        fullfilelist = filter(os.path.isfile, self.fulllist)

        all_extensions = list(map(lambda path: path.split(".")[-1], fullfilelist))
        unique_extensions_list = dict.fromkeys(all_extensions).keys()

        extension_count_dict = {}
        for unique_extension in unique_extensions_list:
            extension_count_dict[unique_extension] = all_extensions.count(unique_extension)
        return extension_count_dict

    
    def showListe(self):
        print("Dein analysierter Ordner hat Folgendes ergeben:")
        print("Das ist der Inhalt deines Ordners inklusive Unterordnern:")
        for each in self.fulllist:
            print(each)