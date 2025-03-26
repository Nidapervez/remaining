import os

def bulk_rename(directory, prefix="", suffix="", find_text=None, replace_with=None, lowercase=False, uppercase=False):
    """
    Renames files in the given directory based on provided rules.
    
    :param directory: Directory path containing files.
    :param prefix: Text to prepend to filenames.
    :param suffix: Text to append before file extension.
    :param find_text: Substring to find in filenames.
    :param replace_with: Replacement text for `find_text`.
    :param lowercase: Convert filenames to lowercase.
    :param uppercase: Convert filenames to uppercase.
    """
    if not os.path.isdir(directory):
        print(f"Error: Directory '{directory}' does not exist.")
        return
    
    files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
    if not files:
        print("No files found in the directory.")
        return
    
    print(f"Processing {len(files)} files in '{directory}'...")
    
    for file in files:
        name, ext = os.path.splitext(file)
        
        if find_text and replace_with:
            name = name.replace(find_text, replace_with)
        
        if lowercase:
            name = name.lower()
        elif uppercase:
            name = name.upper()
        
        new_name = f"{prefix}{name}{suffix}{ext}"
        old_path, new_path = os.path.join(directory, file), os.path.join(directory, new_name)
        
        if not os.path.exists(new_path):
            os.rename(old_path, new_path)
            print(f"Renamed: {file} -> {new_name}")
        else:
            print(f"Skipped: {file} (File with new name already exists)")
    
    print("Renaming completed!")

if __name__ == "__main__":
    dir_path = input("Enter directory path: ").strip()
    pre = input("Enter prefix (or leave blank): ").strip()
    suf = input("Enter suffix (or leave blank): ").strip()
    find = input("Find text (or leave blank): ").strip() or None
    replace = input("Replace with (or leave blank): ").strip() or None
    to_lower = input("Convert to lowercase? (y/n): ").strip().lower() == "y"
    to_upper = input("Convert to uppercase? (y/n): ").strip().lower() == "y"
    
    bulk_rename(dir_path, pre, suf, find, replace, to_lower, to_upper)
