import gradio as gr

from caption_generator import ImageCaptionGenerator


# ============================================================
# AI IMAGE CAPTIONING SYSTEM
# ============================================================

print("=" * 60)
print("AI IMAGE CAPTIONING SYSTEM")
print("=" * 60)

# Load the BLIP model once when the application starts.
caption_generator = ImageCaptionGenerator()


# ============================================================
# CAPTION GENERATION
# ============================================================

def generate_caption(image):
    """Generate an AI caption for the uploaded image."""

    if image is None:
        return "⚠️ Please upload an image first."

    try:
        caption = caption_generator.generate_caption(image)

        if not caption:
            return "⚠️ No caption could be generated."

        return caption

    except Exception as error:
        print(f"Caption generation error: {error}")
        return "❌ An error occurred while generating the caption."


# ============================================================
# CLEAR FUNCTION
# ============================================================

def clear_all():
    """Clear the image and generated caption."""

    return None, ""


# ============================================================
# CUSTOM CSS
# ============================================================

custom_css = """
.gradio-container {
    max-width: 1150px !important;
    margin: auto !important;
}

#main-title {
    text-align: center;
    margin-bottom: 5px;
}

#subtitle {
    text-align: center;
    opacity: 0.8;
    margin-bottom: 25px;
}

#caption-box textarea {
    font-size: 18px !important;
    line-height: 1.6 !important;
}

#generate-btn {
    width: 100%;
    font-size: 17px;
    font-weight: bold;
}

#clear-btn {
    width: 100%;
    font-size: 17px;
}

.info-card {
    padding: 15px;
    border-radius: 12px;
    margin-top: 10px;
}
"""


# ============================================================
# GRADIO APPLICATION
# ============================================================

with gr.Blocks(
    title="AI Image Captioning System"
) as app:

    # --------------------------------------------------------
    # HEADER
    # --------------------------------------------------------

    gr.Markdown(
        """
        <div id="main-title">

        # 🖼️ AI Image Captioning System

        </div>

        <div id="subtitle">

        ### Generate natural-language descriptions from images using Artificial Intelligence

        Upload an image and let the AI analyze its visual content.

        </div>
        """
    )

    # --------------------------------------------------------
    # MAIN WORKSPACE
    # --------------------------------------------------------

    with gr.Row(equal_height=True):

        # ----------------------------------------------------
        # IMAGE INPUT
        # ----------------------------------------------------

        with gr.Column():

            gr.Markdown("### 📤 Upload Image")

            image_input = gr.Image(
                type="pil",
                label="Input Image",
                height=400
            )

            gr.Markdown(
                """
                **Supported formats:** JPG, JPEG, PNG, WEBP

                Upload a clear image for better caption quality.
                """
            )

        # ----------------------------------------------------
        # CAPTION OUTPUT
        # ----------------------------------------------------

        with gr.Column():

            gr.Markdown("### 🤖 AI Generated Caption")

            caption_output = gr.Textbox(
                label="Generated Caption",
                placeholder="Your AI-generated description will appear here...",
                lines=8,
                buttons=["copy"],
                elem_id="caption-box"
            )

            gr.Markdown(
                """
                <div class="info-card">

                **AI Model:** Salesforce BLIP

                **Deep Learning Framework:** PyTorch

                **NLP/Vision Framework:** Hugging Face Transformers

                **Image Processing:** Pillow

                </div>
                """
            )

    # --------------------------------------------------------
    # ACTION BUTTONS
    # --------------------------------------------------------

    with gr.Row():

        generate_button = gr.Button(
            "✨ Generate Caption",
            variant="primary",
            elem_id="generate-btn"
        )

        clear_button = gr.Button(
            "🗑️ Clear",
            variant="secondary",
            elem_id="clear-btn"
        )

    # --------------------------------------------------------
    # HOW IT WORKS
    # --------------------------------------------------------

    gr.Markdown("---")

    gr.Markdown(
        """
        ## 🔍 How It Works

        **1. Upload Image**  
        The user selects an image from their computer.

        **2. Image Preprocessing**  
        The image is converted into a format suitable for the AI model.

        **3. Visual Analysis**  
        Salesforce BLIP analyzes the visual information contained in the image.

        **4. Caption Generation**  
        The model generates a natural-language description.

        **5. Result Display**  
        The generated caption is displayed to the user.

        ---

        ## 🧠 Technology Stack

        | Technology | Purpose |
        |------------|---------|
        | Python | Application development |
        | PyTorch | Deep learning framework |
        | Hugging Face Transformers | Pretrained AI model |
        | Salesforce BLIP | Image captioning |
        | Pillow | Image processing |
        | Gradio | Web interface |

        ---

        ### 🤖 AI Model

        **Salesforce BLIP — `Salesforce/blip-image-captioning-base`**

        The application uses a pretrained vision-language model to understand
        images and generate meaningful natural-language descriptions.

        > **Note:** The application runs locally and performs inference using the
        pretrained BLIP model.
        """
    )

    # --------------------------------------------------------
    # FOOTER
    # --------------------------------------------------------

    gr.Markdown(
        """
        ---

        <div style="text-align:center; opacity:0.7;">

        **CodSoft Artificial Intelligence Internship — Task 3**

        **AI-Based Image Captioning System**

        </div>
        """
    )

    # --------------------------------------------------------
    # EVENT HANDLERS
    # --------------------------------------------------------

    generate_button.click(
        fn=generate_caption,
        inputs=image_input,
        outputs=caption_output
    )

    clear_button.click(
        fn=clear_all,
        inputs=[],
        outputs=[image_input, caption_output]
    )


# ============================================================
# START APPLICATION
# ============================================================

if __name__ == "__main__":

    app.launch(
        theme=gr.themes.Soft(),
        css=custom_css
    )