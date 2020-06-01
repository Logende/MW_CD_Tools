import json


def read_results(scenario):
    results = []
    with open(scenario.eval_results_path, 'r') as stream:
        try:
            config = json.load(stream)
            for section_name in config:
                result = EvaluationResult(config[section_name])
                results.append(result)

        except IOError:
            print("Unable to read results file " + scenario.eval_results_path)
    return results


class EvaluationResult:
    def __init__(self, config):
        self.tribeA = config["tribeA"]
        self.tribeB = config["tribeB"]
        self.controllerA = config["controllerA"]
        self.controllerB = config["controllerB"]
        self.duration = config["duration"]
        self.victoryType = config["victoryType"]
        self.events = config["events"]
