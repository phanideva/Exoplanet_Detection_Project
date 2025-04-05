
from src import data_processing, transit_detection, ml_model, bayesian_composition, report_generator

def main():
    print("Starting Exoplanet Detection Pipeline...")
    data_processing.run()
    transit_detection.run()
    ml_model.run()
    bayesian_composition.run()
    report_generator.run()

if __name__ == "__main__":
    main()
