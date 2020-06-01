import os.path


class Scenario:

    def __init__(self, name):
        # evaluation_dir_path = os.path.dirname(os.path.realpath(__file__))
        # root_dir_path = "os.path.dirname(evaluation_dir_path)"
        root_dir_path = "../"
        files_dir_path = os.path.join(root_dir_path, "files")
        self.simulation_jar_path = os.path.join(files_dir_path, "mw_cd.jar")
        self.eval_config_path = os.path.join(files_dir_path, "scenarios", name, "eval_config.yml")
        self.eval_results_path = os.path.join(files_dir_path, "scenarios", name, "eval_results.json")
        # todo: Add support for a third file: The ML Model
