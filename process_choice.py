from image_process import to_greyscale , to_blur_gaussian

def user_choice(choice, image):
    if choice == "gray":
        return to_greyscale(image)
    elif choice == "blur":
        return to_blur_gaussian(image)
    else:
        raise ValueError("Invalid Choice")