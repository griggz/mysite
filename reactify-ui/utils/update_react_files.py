from pathlib import Path
import re
import json
import sys
sys.path.append("..")
try:
    from MySite.settings.local import *
except:
    from MySite.settings.production import *


class Cleaner:
    def __init__(self):
        self.dirs = []
        self.react_paths = []
        self.manifest = self.build_manifest()
        self.files_cleaned = 0

    @staticmethod
    def build_manifest():
        if BUILD_JSON:
            with open(Path(BUILD_JSON), 'r') as f:
                return json.load(f)

    @staticmethod
    def clean(file, pattern, subst):
        with open(Path(file)) as f:
            if not any(re.search(pattern, line) for line in f):
                print('no matches in ' + str(Path(file).name))

        with open(Path(file)) as f:
            out_fname = Path(file).name
            out = open(out_fname, "w")
            for line in f:
                out.write(re.sub(pattern, subst, line))
            out.close()
            os.rename(out_fname, Path(file))

    @staticmethod
    def check_name(pattern, file):
            with open(Path(file)) as f:
                if any(re.search(pattern, line) for line in f):
                    return True

    def get_dirs(self):
        dirs = ['/reactify-ui/build']
        for dirName, subdirList, fileList in os.walk(BASE_DIR):
            for name in dirs:
                if dirName.endswith(name):
                    self.dirs.append(Path(dirName).resolve())

    def get_files(self):
        for path in self.dirs:
            if Path(path).is_dir() is True:
                file_paths = [Path(f) for f in Path(path).glob('**/*') if '/reactify-ui/build/static/' in str(Path(f)) and '.DS_Store' not in str(Path(f)) and f.is_file()]
                for js_path in file_paths:
                    self.react_paths.append(str(Path(js_path).resolve()))
            else:
                raise ValueError

    def process_files(self):
        buildNames = [x for x in self.manifest['files']]
        for file in self.react_paths:
            for name in buildNames:
                check = self.check_name(self.manifest['files'][name]['pattern'], file)
                if check is True:
                    self.clean(file, self.manifest['files'][name]['pattern'], self.manifest['files'][name]['subst'])
                    print(Path(file).name + ' updated!')
                    self.files_cleaned += 1
                else:
                    pass

    def run(self):
        self.get_dirs()
        self.get_files()
        self.process_files()

        print(str(self.files_cleaned) + ' react build files have been successfully updated')


def main():
    Cleaner().run()


if __name__ == '__main__':
    main()
