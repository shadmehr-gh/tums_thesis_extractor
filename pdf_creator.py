from pathlib import Path

from PIL import Image

downloads_path = str(Path.home() / "Desktop")
files_path = downloads_path + "/lib.tums.ac.ir"

def pdf_creator(biblioId, multimediaId, page_count):
    #images_path = files_path + "/extracted_pages"
    #only_image_files = [f for f in listdir(images_path) if isfile(join(images_path, f))]
    #print(only_image_files)

    image_files = []
    for i in range(int(page_count)):
        image_files.append("exImageDraw" + str(i + 1) + ".png")
    #print(image_files)

    """
    image_files_pre = []
    image_files_pre.append("exImageDraw.jpg")
    for i in range(200):
        image_files_pre.append("exImageDraw (" + str(i+1) + ").jpg")
    #print(image_files_pre)

    image_files = []
    for j in image_files_pre:
        if isfile(files_path + "/extracted_images/" + j):
            image_files.append(j)
    #print(image_files)
    """

    images = [
        Image.open(files_path + "/extracted_pages/" + f)
        for f in image_files
    ]

    pdf_path = files_path + "/" + biblioId + "_" + multimediaId + ".pdf"

    print(f"Final PDF Will Be Saved in the {files_path} Folder...")

    try:
        images[0].save(pdf_path, "PDF", resolution=100.0, save_all=True, append_images=images[1:])
        print("Finished.")
    except:
        print("An error occurred! The file could not be saved. Please Try Again.")
