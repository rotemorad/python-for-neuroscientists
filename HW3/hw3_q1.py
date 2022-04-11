from pathlib import Path


class FolderIterator:
    """.Iterates through the supplied folder, finding duplicates.

    Call the iter_folder() method to parse the directory.

    Attributes
    ----------
    foldername : path-like
        Name of base folder to iterate on.
    uniques : list
        A list of unique files in the folder and their content.
    duplicates : dict
        The keys are the parent files and the values are a list of filenames
        with the same content.
    """

    def __init__(self, foldername='base'):
        self.foldername = Path(str(foldername))  # pathlib.Path instance
        self.uniques = []  # list instance
        self.duplicates = {}  # dict instance

    def _get_readable_files(self):
        """Function checks if the folder is a directory and returns only the files that are readable"""
        sub_files = self.foldername.rglob('*') if self.foldername.is_dir() else self.foldername
        return [file_path for file_path in sub_files if file_path.suffix != '']

    def _get_content(self):
        """Function reads files content and stores them in a dict{file_name: content}"""
        return {file.name: file.read_text() for file in self._get_readable_files()}

    def iter_folder(self):
        """Main function to find duplicate and unique files in the filesystem."""
        files = self._get_content()
        for content in set(files.values()):
            for file in files.items():
                if file[1] == content:
                    self.uniques.append(file)
                    break

            dups_names = [filename for filename, file_content in files.items() if file_content == content]
            if len(dups_names) > 1:
                self.duplicates[dups_names[0]] = dups_names[1:]

        return self.duplicates, self.uniques
