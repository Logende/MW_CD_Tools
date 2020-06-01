from evaluation import scenario, evaluation_results


def main():
    print("Starting Evaluation-Tribe-Comparison Process.")
    scenario_instance = scenario.Scenario("all_tribes_aggressive")
    evaluate(scenario_instance)
    print("Finished Evaluation-Tribe-Comparison Process.")


def evaluate(scenario_instance):
    results = evaluation_results.read_results(scenario_instance)
    print(results)
    # todo: create nice informative table


if __name__ == "__main__":
    main()
