class MyFile:
    def __init__(self, name, size):
        self.name = name
        self.size = size

class MyDir:
    def __init__(self, name, parent):
        self.name = name
        self.content = {}
        self.parent = parent

    def mkdir(self, name):
        self.content[name] = MyDir(name, self)

    def create_file(self, name, size):
        self.content[name] = MyFile(name, size)

class FileSystem:
    root = MyDir('root', None)
    clean_max = 100000
    clean_sums = []
    disk_size = 0
    free_space = 70000000

    def __init__(self, puzzle):
        self.current_dir = self.root
        self.puzzle = puzzle.split("\n")
        self.create()

    def cd(self, dir):
        if dir == '/':
            self.current_dir = self.root
        elif dir == "..":
            self.current_dir = self.current_dir.parent
        else:
            self.current_dir = self.current_dir.content[dir]

    def dir(self, name):
        self.current_dir.mkdir(name)

    def create_file(self, vals):
        size = int(vals[0])
        name = vals[1]
        self.disk_size += size
        self.free_space -= size
        self.current_dir.create_file(name, size)

    def create(self):
        for command in self.puzzle:
            command_vals = command.split()

            if command.startswith('$ cd'):
                self.cd(command_vals[2])
            elif command.startswith('dir'):
                self.dir(command_vals[1])
            elif not command.startswith("$ ls"):
                self.create_file(command_vals)

        self.current_dir = self.root

    def print_system(self, dir = None, tab = ""):
        dir = self.current_dir if dir == None else dir

        for element in dir.content.values():
            if isinstance(element, MyDir):
                print(tab, '-', element.name, '(dir)')
                self.print_system(element, tab + "\t")
            else:
                print(tab,'-', element.name, '(size=',element.size,')')

        print('Disk size:',self.disk_size)

    def addto_clean(self, name, size, option):
        if option == 1 and size <= self.clean_max:
            print('Adding to clean, dir',name,' with size:',size)
            self.clean_sums.append(size)
        else:
            sumto_limit = self.free_space + size
            if sumto_limit >= 30000000:
                print('Adding to clean, dir',name,' with size:',size,'that increase free space to', sumto_limit)
                self.clean_sums.append(size)

    def dir_size(self, dir, option):
        total_size = 0

        for element in dir.content.values():
            if isinstance(element, MyDir):
                sizedir = self.dir_size(element, option)
                self.addto_clean(element.name, sizedir, option)
                total_size += sizedir
            else:
                total_size += element.size

        return total_size

    def clean(self, option):
        dir = self.root
        self.clean_sums = []

        for element in dir.content.values():
            if isinstance(element, MyDir):
                sizedir = self.dir_size(element, option)
                self.addto_clean(element.name, sizedir, option)

        if option == 1:
            return sum(self.clean_sums)
        else:
            return min(self.clean_sums)
