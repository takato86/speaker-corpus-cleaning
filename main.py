import os
from src.entity.sentence import SentenceManager
from src.logic.cleaner import Cleaner
from logging import getLogger
import glob


def main():
    file_path_pattern = os.path.join("data", "input", "text", "*.xlsx")
    file_pathes = [file_path for file_path in glob.glob(file_path_pattern)]
    output_dir = os.path.join("data", "output", "text")

    for file_path in file_pathes:
        sentence_manager = SentenceManager(file_path)
        cleaner = Cleaner(sentence_manager)
        cleaner.clean()
        output_file_path = os.path.join(output_dir, file_path)
        sentence_manager.export(output_file_path)


if __name__ == '__main__':
    logger = getLogger("__main__")
    main()
