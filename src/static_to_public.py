import os
import shutil

def Static_to_Public(directory=None, full_source=None, full_dest=None, check=False):
    if full_source == None and full_dest == None:
        main_direct = os.getcwd()
        dest = "public"
        dest = os.path.join(main_direct, dest)
        source = "static"
        source = os.path.join(main_direct, source)
    else:
        source = full_source
        dest = full_dest
    if not os.path.exists(source):
        raise Exception("Warning: Static directory unable to be found")
    if os.path.exists(dest) and check == False:
        shutil.rmtree(dest)
        os.makedirs(dest)
    if directory == None:
        direct = os.listdir(source)
    elif directory:
        source = os.path.join(source, directory)
        dest = os.path.join(dest, directory)
        os.makedirs(dest)
        direct = os.listdir(source)
    for item in direct:
        if directory == None:
            new_item = os.path.join(source, item)
            if os.path.isfile(new_item):
                shutil.copy(new_item, dest)
            else:
                Static_to_Public(directory=item, full_source=source, full_dest=dest, check=True)    
        elif directory != None:
            new_item = os.path.join(source, item)
            if os.path.isfile(new_item):
                shutil.copy(new_item, dest)
            else:
                Static_to_Public(directory=item, full_source=source, full_dest=dest, check=True)
def checking():
    return os.getcwd()
    