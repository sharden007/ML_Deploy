import os

# Step 1: Create the main project directory
project_dir = 'ML_Deploy'
os.makedirs(project_dir, exist_ok=True)

# Step 2: Create subdirectories 'app' and 'model' within 'project-dir'
app_dir = os.path.join(project_dir, 'app')
model_dir = os.path.join(project_dir, 'model')

os.makedirs(app_dir, exist_ok=True)
os.makedirs(model_dir, exist_ok=True)

# Step 3: Create the specified files in the appropriate directories
# File paths
init_file = os.path.join(app_dir, '__init__.py')  # Empty file
main_file = os.path.join(app_dir, 'main.py')  # FastAPI code placeholder
model_file = os.path.join(model_dir, 'linear_regression_model.pkl')  # Placeholder for saved model
training_file = os.path.join(project_dir, 'model_training.py')  # Placeholder for training script
requirements_file = os.path.join(project_dir, 'requirements.txt')  # Placeholder for dependencies
dockerfile = os.path.join(project_dir, 'Dockerfile')  # Placeholder for Docker configuration

# Create empty files or add comments where applicable
file_content_map = {
    init_file: "",  # Empty __init__.py file
    main_file: "# FastAPI code for prediction API\n",
    model_file: "# Saved trained model (after running model_training.py)\n",
    training_file: "# Script to train and save the model\n",
    requirements_file: "# Dependencies for the project\n",
    dockerfile: "# Docker configuration\n"
}

for file_path, content in file_content_map.items():
    with open(file_path, 'w') as f:
        f.write(content)

print(f"Project structure created successfully in '{project_dir}'!")
