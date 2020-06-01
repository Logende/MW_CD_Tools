from evaluation import scenario, evaluation_results
import matplotlib.pyplot as plt
import os.path


class TribeABResults:
    def __init__(self):
        self.wins = 0
        self.losses = 0
        self.ties = 0
        self.totalDuration = 0
        self.matchCount = 0


def main():
    print("Starting Evaluation-Tribe-Comparison Process.")
    scenario_instance = scenario.Scenario("all_tribes_random")
    evaluate(scenario_instance)
    print("Finished Evaluation-Tribe-Comparison Process.")


def evaluate(scenario_instance):
    results = evaluation_results.read_results(scenario_instance)

    # Step 1: Prepare all results in an accessible lookup dict and list all tribe names
    tribes = set()
    lookup = {}
    for result in results:
        tribe_a = result.tribeA
        tribe_b = result.tribeB
        if tribe_a not in lookup:
            lookup[tribe_a] = {}
        a_results = lookup[tribe_a]

        if tribe_b not in a_results:
            a_results[tribe_b] = TribeABResults()

        ab_results = a_results[tribe_b]
        ab_results.matchCount += 1
        ab_results.totalDuration += result.duration
        if result.victoryType == "PLAYER_A":
            ab_results.wins += 1
        elif result.victoryType == "PLAYER_B":
            ab_results.losses += 1
        else:
            ab_results.ties += 1
        tribes.add(tribe_a)
        tribes.add(tribe_b)

    # Step 2: Fill the results from the lookup dict in a matrix
    tribes_sorted = sorted(tribes)
    matrix = []
    header_column = [""]
    header_column.extend(tribes_sorted)
    matrix.append(header_column)
    color_matrix = []
    color_neutral_column = ["w"]
    color_neutral_column.extend("w" for _ in tribes_sorted)
    color_matrix.append(color_neutral_column)
    for tribe_a in tribes_sorted:

        tribe_column = [tribe_a]
        matrix.append(tribe_column)
        color_column = ["w"]
        color_matrix.append(color_column)

        for tribe_b in tribes_sorted:
            matrix_entry = look_up_matrix_entry(lookup, tribe_a, tribe_b)
            tribe_column.append(matrix_entry)
            try:
                value = int(matrix_entry)
                if value > 0:
                    color_column.append("g")
                else:
                    color_column.append("r")
            except ValueError:
                color_column.append("w")

    total_score_column = [""]
    total_score_column.extend(look_up_total_score(lookup, tribe_a, tribes_sorted) for tribe_a in tribes_sorted)
    matrix.append(total_score_column)
    color_matrix.append(color_neutral_column)

    result_folder = os.path.dirname(scenario_instance.eval_results_path)
    plot_file_path = os.path.join(result_folder, "tribe_comparison.png")
    plot_matrix(matrix, color_matrix, plot_file_path)


def look_up_total_score(lookup, tribe_b, tribes):
    result = 0
    for tribe_a in tribes:
        score = look_up_matrix_entry_numerical(lookup, tribe_a, tribe_b)
        result += score
    return result


def look_up_matrix_entry_numerical(lookup, tribe_a, tribe_b):
    matrix_entry = look_up_matrix_entry(lookup, tribe_a, tribe_b)
    try:
        value = int(matrix_entry)
        return value
    except ValueError:
        return 0


def look_up_matrix_entry(lookup, tribe_a, tribe_b):
    if tribe_a in lookup:
        a_results = lookup[tribe_a]
        if tribe_b in a_results:
            ab_results = a_results[tribe_b]
            ab_score = - ab_results.wins + ab_results.losses
            return str(ab_score)

    if tribe_b in lookup:
        b_results = lookup[tribe_b]
        if tribe_a in b_results:
            ba_results = b_results[tribe_a]
            ba_score = ba_results.wins - ba_results.losses
            return str(ba_score)

    return "x"


def plot_matrix(matrix, colors, file_path):
    fig = plt.figure(dpi=150)
    ax = fig.add_subplot(1, 1, 1)
    table_data = matrix
    table = ax.table(cellText=table_data, loc='center', cellColours=colors)
    # table.set_fontsize(14)
    table.scale(1, 1)
    ax.axis('off')
    plt.savefig(file_path)


if __name__ == "__main__":
    main()
