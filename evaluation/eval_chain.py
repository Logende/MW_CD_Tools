from evaluation import scenario, simulation_launcher,evaluation_tribe_comparison
from multiprocessing import Process


def main():
    scenarios = [
        scenario.Scenario("all_tribes_random"),
        scenario.Scenario("all_tribes_aggressive")
    ]

    evaluate(scenarios)

    for s in scenarios:
        evaluation_tribe_comparison.evaluate(s)


def evaluate(scenarios):
    proc = []
    for s in scenarios:
        p = Process(target=simulation_launcher.launch_scenario, args=(s,))
        p.start()
        proc.append(p)
    for p in proc:
        p.join()


if __name__ == "__main__":
    main()
