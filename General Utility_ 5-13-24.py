from PIL import Image #Imports package that allows for image format conversion
import os             #Imports package that allows for operating system file navigation
import subprocess     #Imports package that allows for the ExifTool to be ran

def file_names():                                                               #Asks user to input file path, checks if file path exists, creates output file path that is a jpg
    loop1 = 0
    while loop1 == 0:
        input_path = input("Enter the path of the image file: ")                #Asks for user to input file path: Example input: C:\Users\dvitale\Documents\Exif_Testing.bmp
        if os.path.isfile(input_path):                                          #Checks to see if file path exists. If file path exists, the loop is broken
            print("File path is valid")
            loop1 = 1
        else:                                                                   #Handles invalid user input by looping back to the beginning of the function.
            print("File path is not valid or it only points to a directory")
    output_path = os.path.splitext(input_path)[0] + '.jpg'                      #takes input file path and changes file format to .jpg
    return input_path, output_path                                              #returns variable to the main function so that other functions can use them


def convert_to_jpg(input_path, output_path):                          #converts image to jpg
    try:
        image = Image.open(input_path)                                #tries to open image file

        if image.mode =='RGBA':                                       #if image is RGBA it is converted to RGB. This is a necessary step for .png and .tiff
            image = image.convert('RGB')

        image.save(output_path, format='JPEG', quality=100)           #saves image as jpg
        print(f"Conversion successful: {input_path} ->{output_path}") #prints confirmation message

    except Exception as e:                                            #handles error - I have not received this error in any of my testing.
        print(f"Conversion failed {e}")

def add_comment_to_jpg(output_path,):                       #uses ExifTool to add comment to metadata
    exifTool = "/Users/dvitale/exiftool.exe"                #Defines location of ExifTool
    comment = input("Enter comment: ")                      #Asks user to input the comment they want to add
    command = [exifTool, "-comment="+comment, output_path]  #Calls ExifTool and specifies comment that will be added to the image
    subprocess.run(command)                                 #Runs command



def main(): #calls all previously defined functions with their necessary inputs and returned outputs
    
    input_path, output_path = file_names()
    convert_to_jpg(input_path, output_path)
    add_comment_to_jpg(output_path)

main()
