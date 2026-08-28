from PIL import Image
from caption_generator import ImageCaptionGenerator


def main():
    image_path = "assets/test_image.jpg"

    print("\nStarting Image Captioning AI...")
    print("-" * 50)

    generator = ImageCaptionGenerator()

    image = Image.open(image_path)

    print("\nGenerating caption...")
    caption = generator.generate_caption(image)

    print("\n" + "=" * 50)
    print("GENERATED CAPTION")
    print("=" * 50)
    print(caption)
    print("=" * 50)


if __name__ == "__main__":
    main()