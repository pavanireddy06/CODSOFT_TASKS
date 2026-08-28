🖼️ AI-Based Image Captioning System

CodSoft Artificial Intelligence Internship — Task 3

An AI-powered image captioning application that analyzes an uploaded image and generates a natural-language description using a pretrained vision-language model.

✨ Features

Upload JPG, JPEG, PNG, and WEBP images

Image preprocessing with Pillow

Caption generation using Salesforce BLIP

Local inference with PyTorch

Hugging Face Transformers integration

Interactive Gradio web interface

Clear/reset functionality

Model and technology information section

🧠 How It Works

Image Upload → Image Processing → Salesforce BLIP
             → Vision-Language Analysis → Caption Generation

🛠️ Technology Stack

Technology

Purpose

Python

Core programming language

PyTorch

Deep learning and inference

Hugging Face Transformers

Pretrained model integration

Salesforce BLIP

Image captioning

Pillow

Image processing

Gradio

Web interface

📁 Project Structure

Task3_ImageCaptioning/
├── app.py
├── caption_generator.py
├── image_processor.py
├── utils.py
├── test_caption.py
├── requirements.txt
├── README.md
├── .gitignore
├── assets/
├── models/
└── screenshots/

🚀 Run the Project

Create the environment

py -3.12 -m venv venv
.env\Scripts\Activate.ps1

Install dependencies

pip install -r requirements.txt

Start the application

python app.py

Open the local Gradio URL shown in the terminal, typically:

http://127.0.0.1:7860

🧪 Testing

The application was tested with multiple images.

Test 1: a woman standing on a bridge in front of a temple

Test 2: a woman standing in front of a white backdrop

The results demonstrate that the model generates different captions according to the visual content of the supplied images.

🤖 AI Model

Salesforce BLIP — Salesforce/blip-image-captioning-base

The pretrained model is loaded through Hugging Face Transformers and used for local image-caption inference.

🔒 Git Notes

Do not commit the virtual environment, Python cache, downloaded model weights, or Hugging Face cache. These are excluded through .gitignore.

🎯 Internship Outcome

The project successfully demonstrates the core image-captioning objective by combining computer vision and natural-language generation in a working interactive application.

Status: Completed ✅