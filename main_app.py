from main_create import main as main_create
from auto_compare import compare_files_in_directories as main_compare

def main():
    main_directory = input("Where's all ur data?")
    main_create(main_directory)
    main_compare(main_directory)



if __name__ == "__main__":
    main()