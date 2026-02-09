import os
import weaviate
import base64
from weaviate.classes.config import Configure, DataType, Property


def encode_image(image_path):
    with open(image_path, "rb") as file:
        return base64.b64encode(file.read()).decode('utf-8')

def main():
    client = weaviate.connect_to_local()
    
    try:
        if client.collections.exists("Images"):
            client.collections.delete("Images")
        
        client.collections.create(
            name="Images",
            properties=[
                Property(name="filename", data_type=DataType.TEXT),
                Property(name="image", data_type=DataType.BLOB),
            ],
            vector_config=Configure.Vectors.img2vec_neural(image_fields=["image"])
        )
        
        images_collection = client.collections.get("Images")
        images_folder = "./images_jpg"
        
        for filename in os.listdir(images_folder):
            image_path = os.path.join(images_folder, filename)
            images_collection.data.insert(
                {"filename": filename, "image": encode_image(image_path)}
            )
        
        print(
            f"Indexed {images_collection.aggregate.over_all(total_count=True).total_count} images"
        )
    
    finally:
        client.close()
    

if __name__ == "__main__":
    main()