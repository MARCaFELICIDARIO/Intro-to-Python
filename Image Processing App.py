import os

from PIL import Image, ImageFilter, ImageEnhance

strImageDir = (r"C:\Users\Marcf\Pictures\Camera Roll")

imgFile = None

fileName = (r"C:\Users\Marcf\Pictures\Camera Roll\minecraft.png")

def returnFiles(strDir):
    arTemp = []
    for file in os.listdir(strDir):
        if str(file).find(".") > 0 and len(file)>3:
            name, type = file.split(".")
            if str(type).lower() == "jpg" or str(type).lower() == "png":
                arTemp.append(file)
    return arTemp

def filterOne(imgFile):
    imRed, imGreen, imBlue = imgFile.split()
    imRed = imRed.rotate(3)
    imGreen = imGreen.rotate(358)
    imBlue = imBlue.filter(ImageFilter.GaussianBlur(30))
    enhancer = ImageEnhance.Brightness(imBlue)
    imBlue = enhancer.enhance(1.5)
    imgNew = Image.merge("RGB", (imRed, imGreen, imBlue))
    enhancer = ImageEnhance.Brightness(imgNew)
    imgNew = enhancer.enhance(1.5)
    print("\nThe Filter Has Been Applied.\n")
    imgNew.show()
    return imgNew

def filterTwo(imgFile):
    imRed2, imGreen2, imBlue2 = imgFile.split()
    imRed2 = imRed2.rotate(6)
    imGreen2 = imGreen2.rotate(354)
    imBlue2 = imBlue2.filter(ImageFilter.GaussianBlur(15))
    enhancer = ImageEnhance.Brightness(imBlue2)
    imBlue2 = enhancer.enhance(1.5)
    imgNew2 = Image.merge("RGB", (imRed2, imGreen2, imBlue2))
    enhancer = ImageEnhance.Brightness(imgNew2)
    imgNew2 = enhancer.enhance(1.5)
    print("\nThe Filter Has Been Applied.\n")
    imgNew2.show()
    return imgNew2

def mainMenu():
    print("-"*80)
    print("||", "  InstaPy  ".center(74), "||")
    print("-" * 80)
    if fileName == "":
        print(f"\nFile open: None\n")
    else:
        print(f"\nFile open: {fileName}\n")
    print("What do you want to do?")
    print("1. Open an Image")
    print("2. Apply Filter One")
    print("3. Apply Filter Two")
    print("4. Save Image")
    print("5. Quit")
    strTmp = input("Enter Choice Here:")
    return strTmp

def pressEnter():
    input("\nPress Enter/Return to continue...")
    input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

while True:
    menu = mainMenu()
    if menu == "1":
        arFiles = returnFiles(strImageDir)
        print("Which image file would you like to open?")
        for ind, item in enumerate(arFiles,1):
            print(f"{ind}, {item}")
        indFile = int(input("Enter file number: "))-1
        imgFile = Image.open(strImageDir+"/"+str(arFiles[indFile]))
        strFileName = str(arFiles[indFile])
        imgFile.show()
        print(f"The file {strFileName} has been opened.\n")

    elif menu == "2":
        if imgFile == None:
            print("You need to open an image first.")
        else:
            imgFile = filterOne(imgFile)

    elif menu == "3":
        if imgFile == None:
            print("You need to open an image first.")
        else:
            imgFile = filterTwo(imgFile)

    elif menu == "4":
        imgFile.save("changed.jpg")

    elif menu == "5":
        print("Thanks for trying InstaPy!")
    else:
        print("Invalid Input. Try Again.\n")

    pressEnter()

