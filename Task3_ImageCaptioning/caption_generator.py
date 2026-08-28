from PIL import Image
import torch
from transformers import BlipProcessor, BlipForConditionalGeneration


class ImageCaptionGenerator:
    def __init__(self):
        self.model_name = "Salesforce/blip-image-captioning-base"

        print("Loading image captioning model...")
        print("First run may take a few minutes because the model will be downloaded.")

        self.processor = BlipProcessor.from_pretrained(self.model_name)
        self.model = BlipForConditionalGeneration.from_pretrained(
            self.model_name
        )

        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model.to(self.device)

        print(f"Model loaded successfully on: {self.device}")

    def generate_caption(self, image):
        """
        Generate a caption for the supplied image.

        Parameters:
            image: PIL Image

        Returns:
            Generated caption as a string.
        """

        if image is None:
            return "Please provide an image."

        if not isinstance(image, Image.Image):
            image = Image.fromarray(image)

        image = image.convert("RGB")

        inputs = self.processor(
            images=image,
            return_tensors="pt"
        )

        inputs = {
            key: value.to(self.device)
            for key, value in inputs.items()
        }

        with torch.no_grad():
            output = self.model.generate(
                **inputs,
                max_new_tokens=30,
                num_beams=4,
                early_stopping=True
            )

        caption = self.processor.decode(
            output[0],
            skip_special_tokens=True
        )

        return caption.strip()


if __name__ == "__main__":
    print("Image Caption Generator module is ready.")