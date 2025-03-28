import numpy as np
import png
import os

class Image:
    def __init__(self, x_pixels=0, y_pixels=0, num_channels=0, filename=''):
        # you need to input either filename OR x_pixels, y_pixels, and num_channels
        self.input_path = 'input/'
        self.output_path = 'output/'

        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)

        if x_pixels and y_pixels and num_channels:
            self.x_pixels = x_pixels
            self.y_pixels = y_pixels
            self.num_channels = num_channels
            self.array = np.zeros((y_pixels, x_pixels, num_channels))  # Corrected shape (height, width, channels)
        elif filename:
            self.array = self.read_image(filename)
            self.y_pixels, self.x_pixels, self.num_channels = self.array.shape
        else:
            raise ValueError("You need to input either a filename OR specify the dimensions of the image")

    def read_image(self, filename, gamma=2.2):
        """
        Read PNG RGB image, return 3D numpy array (Y, X, channel)
        Values are floats, gamma is decoded
        """
        file_path = os.path.join(self.input_path, filename)
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File '{file_path}' not found.")

        reader = png.Reader(file_path)
        w, h, pixels, metadata = reader.asRGB8()

        image_2d = np.vstack(list(pixels)).astype(np.float32) / 255.0  # Normalize to 0-1 range
        image_3d = image_2d.reshape(h, w, 3) ** gamma  # Apply gamma correction

        return image_3d

    def write_image(self, output_file_name, gamma=2.2):
        """
        Write a 3D numpy array (Y, X, channel) of values between 0 and 1 to a PNG file
        """
        im = np.clip(self.array, 0, 1)
        y, x = im.shape[0], im.shape[1]
        im = (255 * (im ** (1 / gamma))).astype(np.uint8)  # Apply inverse gamma correction
        im_reshaped = im.reshape(y, x * 3)

        writer = png.Writer(x, y)
        with open(os.path.join(self.output_path, output_file_name), 'wb') as f:
            writer.write(f, im_reshaped)

if __name__ == '__main__':
    try:
        im = Image(filename='images.png')  # Make sure the file exists in the 'input/' folder
        im.write_image('images.png')
    except Exception as e:
        print(f"Error: {e}")
