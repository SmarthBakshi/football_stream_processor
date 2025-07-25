import os
import mlflow
from football_stream_processor.utils.eda_utils import PassDataEDA, add_engineered_features
import pandas as pd

def main():
    mlflow.set_experiment("football-pass-eda")
    with mlflow.start_run(run_name="eda-run"):
        df = pd.read_pickle(".pickle/pass_data.pkl")
        df = add_engineered_features(df)

        eda = PassDataEDA(df)
        eda.missing_values()
        eda.class_distribution()
        eda.data_types()

        df_clean = eda.remove_duplicates()
        eda.eda_visualizations()

        # Log the DataFrame
        if os.path.exists(".pickle/pass_data.pkl"):
            mlflow.log_artifact(".pickle/pass_data.pkl", artifact_path="data")
        else:
            print("Warning: .pickle/pass_data.pkl does not exist and cannot be logged.")
        
        # Log plots manually if saved to disk
        plot_dir = "resources/plots"
        for plot_file in os.listdir(plot_dir):
            full_path = os.path.join(plot_dir, plot_file)
            mlflow.log_artifact(full_path)

        print("EDA completed and logged to MLflow.")

if __name__ == "__main__":
    main()