import os

import streamlit as st
import weaviate
from PIL import Image

from indexer import encode_image


def get_client():
    client = weaviate.connect_to_local()
    return client


def query_similar(client, query_image_path, top_k=3):
    images_collection = client.collections.get("Images")

    response = images_collection.query.near_image(
        near_image=encode_image(query_image_path),
        limit=top_k,
        return_properties=["filename"],
        return_metadata=["distance", "certainty"],
    )

    results = []
    for obj in response.objects:
        results.append(
            {
                "filename": obj.properties["filename"],
                "distance": obj.metadata.distance,
                "certainty": obj.metadata.certainty,
            }
        )
    return results


def main():
    st.set_page_config(page_title="Personal Image Search", layout="wide")
    st.title("🖼️ Personal Image Search Demo")
    st.markdown(
        "Upload an image and see the **top-3 most similar images** from your collection."
    )
    st.write("---")

    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Display uploaded image
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Uploaded image", width=400)

        # Save uploaded image temporarily
        temp_path = "./temp_query.jpg"
        image.save(temp_path, "JPEG")

        # Connect to Weaviate and query
        client = get_client()
        try:
            results = query_similar(client, temp_path, top_k=3)

            st.write("### 🔍 Top 3 similar images")
            cols = st.columns(3)  # 3 images side by side

            for idx, (col, res) in enumerate(zip(cols, results), 1):
                col.write(f"**{idx}. {res['filename']}**")
                col.write(f"Distance: {res['distance']:.4f}")
                col.write(f"Certainty: {res['certainty']:.4f}")

                img_path = f"./images_jpg/{res['filename']}"
                if os.path.exists(img_path):
                    res_img = Image.open(img_path)
                    col.image(res_img, width=200)

        finally:
            client.close()


if __name__ == "__main__":
    main()
