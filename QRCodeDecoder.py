# this is wriiten by kuldeep
import qrcode, io, qrcode, base64, cv2
import numpy as np


class QRCodeDecoder:
    """A class to handle QR code operations."""

    # Create a static instance of the class
    instance = None

    def __new__(cls):
        """Override the __new__ method to create a singleton instance."""
        if cls.instance is None:
            cls.instance = super(QRCodeDecoder, cls).__new__(cls)
        return cls.instance


    # Step 1: Decode Base64 to Image
    @staticmethod
    def base64_to_image(base64_string: str):
        """Decodes a base64 string into an image.

        :param base64_string: Base64 encoded string of the image.
        :return: Decoded image as a numpy array.
        """
        # Decode the base64 string into binary image data
        image_data = base64.b64decode(base64_string)
        # Convert the binary data to a numpy array for OpenCV
        np_image = np.frombuffer(image_data, np.uint8)
        # Decode the numpy array to an image
        image = cv2.imdecode(np_image, cv2.IMREAD_COLOR)
        return image

    # Step 2: Decode QR Code from Image to Text
    @staticmethod
    def image_to_qr_text(image: np.ndarray) -> str:
        """Extracts text from a QR code present in the image.

        :param image: Image in which to find the QR code.
        :return: Decoded text from the QR code, or a message indicating no QR code was found.
        """
        if image is None:
            raise ValueError("Image is not valid.")

        # Initialize OpenCV QRCodeDetector
        qr_code_detector = cv2.QRCodeDetector()
        # Detect and decode the QR code
        data, _, _ = qr_code_detector.detectAndDecode(image)
        
        if data:
            return data
        else:
            return "No QR code found in the image."

    # Method to save and display the QR code image
    @staticmethod
    def save_and_display_qr_code(base64_string: str, output_image_path: str):
        """Saves and displays the QR code image.

        :param base64_string: Base64 encoded string of the image.
        :param output_image_path: Path where the image will be saved.
        """
        # Decode base64 to image
        image = QRCodeDecoder.base64_to_image(base64_string)

        # Save the decoded image
        if output_image_path:
            cv2.imwrite(output_image_path, image)
            print(f"Image saved to {output_image_path}")

        # Display the QR code image
        if image is not None:
            cv2.imshow("QR Code", image)
            cv2.waitKey(0)  # Wait for a key press to close the window
            cv2.destroyAllWindows()  # Close the window

    # Method to display QR code image without saving
    @staticmethod
    def display_qr_code_only(base64_string: str):
        """Displays the QR code image without saving it.

        :param base64_string: Base64 encoded string of the image.
        """
        # Decode base64 to image
        image = QRCodeDecoder.base64_to_image(base64_string)

        # Display the QR code image
        if image is not None:
            cv2.imshow("QR Code", image)
            cv2.waitKey(0)  # Wait for a key press to close the window
            cv2.destroyAllWindows()  # Close the window

    # Method to convert image file path to base64
    @staticmethod
    def qr_image_to_base64(image_path: str) -> str:
        """Converts an image file at the specified path to a base64 encoded string.

        :param image_path: Path to the image file.
        :return: Base64 encoded string of the image.
        """
        # Read the image from the given path
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError("Image not found or cannot be opened.")

        # Convert image to base64
        _, buffer = cv2.imencode('.png', image)  # Convert image to PNG format
        base64_string = base64.b64encode(buffer).decode('utf-8')  # Encode to base64
        return base64_string

    @staticmethod
    def base64_to_qr_text(base64_string: str) -> str:
        """Decodes base64 string to an image and then extracts QR code text.

        :param base64_string: Base64 encoded string of the image.
        :return: Decoded text from the QR code.
        """
        if len(base64_string) < 50:
            print("Input parameter is Wrong.")
            exit(0)
        image = QRCodeDecoder.base64_to_image(base64_string)
        return QRCodeDecoder.image_to_qr_text(image)

    @staticmethod
    def string_to_qr_base64(text: str) -> str:
        """Generates a QR code from a string and returns it as a base64 encoded string.

        :param text: The string to encode in the QR code.
        :return: Base64 encoded string of the generated QR code image.
        """
        
        # Generate QR code
        qr = qrcode.make(text)

        # Save QR code to a bytes buffer
        buffered = io.BytesIO()
        qr.save(buffered, format="PNG")
        
        # Convert to base64
        qr_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
        return qr_base64

    # @staticmethod
    # def string_to_qr_image(text: str):          # this is very slow but reliable
    #     """Generates a QR code from a string and displays it.

    #     :param text: The string to encode in the QR code.
    #     """
    #     # Generate QR code
    #     qr = qrcode.make(text)

    #     # Display the QR code image
    #     qr.show()  # This will open the default image viewer with the QR code

    @staticmethod
    def string_to_qr_image_save(text: str, output_image_path: str):
        """Generates a QR code from a string and saves it as an image.

        :param text: The string to encode in the QR code.
        :param output_image_path: The path where the image will be saved.
        """
        # Generate QR code
        qr = qrcode.make(text)

        # Save the QR code image to the specified path
        qr.save(output_image_path)
        print(f"QR Code image saved to {output_image_path}.")
    

    @staticmethod
    def string_to_qr_image_display(text: str):

        """Generates a QR code from a string and displays it using OpenCV.

        :param text: The string to encode in the QR code.
        """
        # Generate QR code
        qr = qrcode.make(text)

        # Convert the QR code to a NumPy array
        qr_image = np.array(qr)

        # Check if the image is boolean and convert to uint8
        if qr_image.dtype == bool:
            qr_image = qr_image.astype(np.uint8) * 255  # Convert boolean to uint8

        # Check dimensions and convert as necessary
        if len(qr_image.shape) == 2:  # Grayscale image
            qr_image = cv2.cvtColor(qr_image, cv2.COLOR_GRAY2BGR)
        elif qr_image.shape[2] == 4:  # RGBA image
            qr_image = cv2.cvtColor(qr_image, cv2.COLOR_RGBA2BGR)
        else:  # RGB image
            qr_image = cv2.cvtColor(qr_image, cv2.COLOR_RGB2BGR)

        # Display the QR code image using OpenCV
        cv2.imshow("QR Code", qr_image)
        cv2.waitKey(0)  # Wait for a key press to close the window
        cv2.destroyAllWindows()  # Close the window

    # @staticmethod
    # def string_to_qr_image_save(text: str, output_image_path: str):
    #     """Generates a QR code from a string and saves it as an image.

    #     :param text: The string to encode in the QR code.
    #     :param output_image_path: The path where the image will be saved.
    #     """
    #     # Generate QR code
    #     qr = qrcode.make(text)

    #     # Save the QR code image to the specified path
    #     qr.save(output_image_path)
    #     print(f"QR Code image saved to {output_image_path}.")

    @staticmethod
    def instance_creation_guide():
        """Provides guidance on how to create an instance of QRCodeDecoder."""
        print("You can call methods directly without creating an instance:")
        print("Example: QRCodeDecoder.save_and_display_qr_code(base64_str, output_image_path)")
        print("Example: QRCodeDecoder.display_qr_code_only(base64_str)")
        print("Example: QRCodeDecoder.image_path_to_base64(image_path)")


# Example usage
if __name__ == "__main__":
    # Display guidance for usage
    # QRCodeDecoder.instance_creation_guide()

    # Replace with your actual base64 string
    # base64_string = "iVBORw0KGgoAAAANSUhEUgAA..."  # Your base64 encoded QR code image string
    base64_string = "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"

    # Display the QR code without saving
    # QRCodeDecoder.display_qr_code_only(base64_string)

    # Optionally decode QR text directly from base64
    # decoded_qr_text = QRCodeDecoder.base64_to_qr_text(base64_string)
    # print(f"QR Code Text: {decoded_qr_text}")

    # Convert a QR code image from file to base64 string
    # image_path = "path/to/your/qr_code_image.png"  # Replace with your image path


    # output_image_path = 'ticket_qr.png'
    # base64_converted = QRCodeDecoder.qr_image_to_base64(".png")  # Convert the image to base64
    # print(f"Converted Base64: {base64_converted}")

    # print(QRCodeDecoder.string_to_qr_base64("hi"))          #1
    # QRCodeDecoder.string_to_qr_image_save("hi", "hi.png")

    # QRCodeDecoder.string_to_qr_image_display("hi")
    # QRCodeDecoder.save_and_display_qr_code(base64_string, "ab.png")

    # print(QRCodeDecoder.base64_to_qr_text("base64_string"))
    # QRCodeDecoder().display_qr_code_only(base64_string)
    # QRCodeDecoder.display_qr_code_only(base64_string)
    pass
    clientTransactionId =  "2128007535885"
    # "userId": "zxp",
    # "txnToken": "489b81e0c9c44f4a994c7519dc1607931728558609722",
    paymentAmount =  "74.50"
    payment_text = f"upi://pay?pa=paytm-67793009@ptybl&pn=IRCTC Chatbot&mc=4112&tr={clientTransactionId}&am={paymentAmount}&cu=INR"
    # payment_text = f"upi://pay?pa=paytm-6779300dskgfub;orwtiyhcu=INR"
    print(payment_text)

    QRCodeDecoder.string_to_qr_image_display(payment_text)
    QRCodeDecoder.string_to_qr_image_save(payment_text, "Pay_QR.png")

    print("-----------")
