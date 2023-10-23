# import error
# def import_module(module_name, abbr="", package_name="", function_name=""):
#     try:
#         if package_name:
#             from module_name import package_name
#         elif abbr:
#             import module_name as abbr
#         elif function_name:
#             from module_name import function_name
#     except ImportError as e:
#         # Check if the error message contains "No module named"
#         if "No module named" in str(e):
#             print(f"Import error: Module '{module_name}' not found.")
#         else:
#             print(f"Import error: {e}")
#
#
# # Call your function with different import options
# import_module("random", abbr = "randint")

def import_module(module_name):
    try:
        import module_name
    except ModuleNotFoundError as e:
        print(f"Import error: {e}")

def from_import(module_name, function_name):
    try:
        from module_name import function_name
    except ModuleNotFoundError as e:
        print(f"Import error: {e}")



# FileNotFound error
def check_file(filepath, filename):
    try:

    except FileNotFoundError as e:
        print(f"{e}, input a correct file name")


# input error



# avoid 2 audios play together
import pygame
while pygame.mixer.music.get_busy():
    pygame.mixer.music.stop()