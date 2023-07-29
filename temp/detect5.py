from PIL import Image
import os
import shutil
from skimage.metrics import structural_similarity as ssim

# Function to calculate SSIM between two images
def calculate_ssim(image1, image2):
    return ssim(image1, image2, multichannel=True)

# Function to group similar images in a folder
def group_similar_images(input_folder, output_folder, threshold=0.95):
    image_files = [f for f in os.listdir(input_folder) if f.endswith(".jpg") or f.endswith(".png")]
    
    # Create output folders if they don't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    # Iterate through each image in the folder
    for i, image_file in enumerate(image_files):
        image1_path = os.path.join(input_folder, image_file)
        
        # Compare this image with other images in the folder
        for j, other_image_file in enumerate(image_files[i+1:], start=i+1):
            image2_path = os.path.join(input_folder, other_image_file)
            
            # Open and resize the images for SSIM calculation
            image1 = Image.open(image1_path).resize((100, 100))
            image2 = Image.open(image2_path).resize((100, 100))
            
            # Calculate SSIM score between the two images
            similarity_score = calculate_ssim(image1, image2)
            
            if similarity_score >= threshold:
                # If images are similar, move or copy to the same group folder
                group_folder = os.path.join(output_folder, f"group_{i+1}")
                if not os.path.exists(group_folder):
                    os.makedirs(group_folder)
                shutil.copy(image1_path, group_folder)
                shutil.copy(image2_path, group_folder)

if __name__ == "__main__":
    input_folder = "D:/Media"
    output_folder = "D:/Media_new"
    similarity_threshold = 0.95  # Adjust this threshold as needed
    
    group_similar_images(input_folder, output_folder, similarity_threshold)
