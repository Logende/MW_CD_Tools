import subprocess
from evaluation import scenario


def main():
    print("Starting Simulation Process.")
    scenario_instance = scenario.Scenario("all_tribes_aggressive")
    launch_scenario(scenario_instance)
    print("Finished Simulation Process.")


def launch_scenario(scenario_instance):
    subprocess.call(['java', '-jar',
                     scenario_instance.simulation_jar_path,
                     "whatever",
                     scenario_instance.eval_config_path,
                     scenario_instance.eval_results_path])


if __name__ == "__main__":
    main()
