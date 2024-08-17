import cv2

def get_color_on_mouse_click(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONUP:
        # Get the color at the clicked point (x, y)
        color = img[y, x]
        
        # Print the BGR values of the color
        print(f"Color at point ({x}, {y}): B={color[0]}, G={color[1]}, R={color[2]}")

# Read the image
img_path = "input_image.jpg"
img = cv2.imread(img_path)

# Create a window and set the callback function
cv2.namedWindow("Image")
cv2.setMouseCallback("Image", get_color_on_mouse_click)

while True:
    # Display the image
    cv2.imshow("Image", img)

    # Break the loop when 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cv2.destroyAllWindows()
