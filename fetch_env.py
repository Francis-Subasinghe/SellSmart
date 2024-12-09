import mlflow

model_uri = "mlruns/0/0/329f09c3c0324af79f00cecbd57f4fc2/artifacts/model"  # Replace with your model URI
env_file_path = "model_env.yml"

# Fetch model dependencies
dependencies = mlflow.pyfunc.get_model_dependencies(model_uri)

# Write the dependencies to the YAML file
with open(env_file_path, "w") as f:
    f.write(dependencies)

print(f"Model dependencies saved to {env_file_path}")
