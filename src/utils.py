#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Collection of different utility tools"""

import sys
import argparse
import matplotlib.pyplot as plt
import pandas as pd


def _check_input_arguments():
    """Some error-handling and interaction for the optional input values: number of steps, walkers, whether user wants to save the plot locally, which movement pattern and how many runs are desired"""
    # Initialize argparse and specify the optional arguments
    help_msg = "Simulate a random walk with n walkers for n steps. You can use the following options to change the simulation to your needs. Have fun!"
    parser = argparse.ArgumentParser(description=help_msg, prefix_chars="-")
    parser.add_argument(
        "-s",
        metavar="Steps",
        dest="total_steps",
        help="Integer | Number of total steps every walker shall take. Default value: 1000",
        default=1000,
    )
    parser.add_argument(
        "-w",
        metavar="Walkers",
        dest="n_walkers",
        help="Integer | Number of total walkers to be created. Default value: 1",
        default=1,
    )
    parser.add_argument(
        "-m",
        metavar="Movepattern",
        dest="movepattern",
        help="Boolean | Choose neighborhood movement pattern between Neumann (4 directions, false) or Moore (8 directions, true, default)",
        default="true",
    )
    parser.add_argument(
        "-xy",
        metavar="Startpoint",
        dest="random_start",
        help="Boolean | Do you want different (random) start points for each walker (true, default) or let all plots start at 0,0 (false)?",
        default="true",
    )
    parser.add_argument(
        "-p",
        metavar="Save plot",
        dest="want_plot_saved",
        help="Boolean | Do you want to automatically save the plot locally (./data/)? Use true/false. Default: false",
        default="false",
    )
    parser.add_argument(
        "-csv",
        metavar="Save csv",
        dest="want_csv_saved",
        help="Boolean | Do you want to automatically save the results as csv-file locally (./data/)? Use true/false. Default: false",
        default="false",
    )
    parser.add_argument(
        "-r",
        metavar="Runs",
        dest="total_runs",
        help="Integer | Total runs of the script (generate multiple plots if wished). Default value: 1",
        default=1,
    )
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        print("\nYou can run the program with the default values.")
        default_run = input("Want to run it now? Use y/n: ")
        if default_run in ["y", "yes", "yup", "ye", "Y", "YES", "YUP", "YE"]:
            args = parser.parse_args()
        else:
            print(
                "Exiting program, call again to run. Use -h or --help to show the help again."
            )
            sys.exit(1)
    else:
        args = parser.parse_args()

    # Assign arguments to variables and do some checks for error-handling
    total_steps = abs(int(args.total_steps))
    n_walkers = int(args.n_walkers)
    movepattern = args.movepattern.lower()
    random_start = args.random_start.lower()
    want_plot_saved = args.want_plot_saved.lower()
    want_csv_saved = args.want_csv_saved.lower()
    total_runs = int(args.total_runs)
    if total_steps == 0:
        total_steps = 1000
        print("Changed quantity of steps to 1000 to be able to plot something.")
    if total_runs < 1:
        total_runs = 1
    elif total_runs > 10:
        total_runs = 10
        print(
            "Changed quantity of runs/plots to 10. Trust me, you don't want to generate more that that."
        )
    if n_walkers < 1:
        n_walkers = 1
        print("Changed quantity of walkers to 1 to be able to plot something.")
    if movepattern not in ["true", "false"]:
        movepattern = "true"
        print(
            "Changed movement pattern to default value 'Moore' due to wrong input from user."
        )
    if random_start not in ["true", "false"]:
        random_start = "true"
        print(
            "Changed starting point to default value 'random start' due to wrong input from user."
        )

    return (
        total_steps,
        n_walkers,
        movepattern,
        random_start,
        want_plot_saved,
        want_csv_saved,
        total_runs,
    )


def plot_walker_path(n_walkers, new_walker, random_start):
    """Plot the coords of every step"""
    ax = plt.gca()  # get current axes
    next_col = next(ax._get_lines.prop_cycler)["color"]  # iterate through colors
    plt.plot(
        new_walker.x,
        new_walker.y,
        alpha=0.33,
        lw=2,
        color=next_col,
        label="{}, speed: {}".format(new_walker.walker_type(), new_walker.walker_speed),
    )
    plt.scatter(new_walker.x, new_walker.y, color=next_col, alpha=1, s=2)
    if n_walkers <= 15:
        plt.legend()
    else:
        pass
    if random_start == "true":
        plt.scatter(
            new_walker.x[0],
            new_walker.y[0],
            marker="P",
            s=100,
            color=next_col,
            edgecolors="black",
        )
    else:
        plt.scatter(
            0,
            0,
            marker="P",
            s=100,
            color="white",
            edgecolors="black",
        )
    plt.scatter(
        new_walker.x[-1],
        new_walker.y[-1],
        marker="X",
        s=100,
        color=next_col,
        edgecolors="black",
    )


def plot_all_walkers(steps, n_walkers, want_plot_saved):
    """Generate plot with precalculated paths and show them together in a plot"""
    if n_walkers == 1:
        plt.title(
            "Random Walk Simulation with {} walker and {} steps".format(
                n_walkers, steps
            )
        )
    else:
        plt.title(
            "Random Walk Simulation with {} walkers and {} steps".format(
                n_walkers, steps
            )
        )
    # checks if the user wants to locally save the figure as well
    while want_plot_saved not in ["true", "false"]:
        want_plot_saved = input(
            "Do you want to save the plot as figure? Use y/n: "
        ).lower()
        if want_plot_saved in [
            "y",
            "yes",
            "yup",
            "ye",
        ] or want_plot_saved in ["n", "no", "nope"]:
            break
        print("Please provide a valid input.")
    if want_plot_saved in [
        "y",
        "yes",
        "yup",
        "ye",
        "true",
        1,
    ]:
        plt.savefig("../data/random_walkers_{}w_{}s.png".format(n_walkers, steps))
    else:
        pass
    plt.tight_layout()
    plt.show()


def write_to_dataframe(walkers, steps, n_walkers, want_csv_saved):
    """Save in dataframe and write to csv file"""
    # checks if the user wants to locally save the results as csv-file as well
    while want_csv_saved not in ["true", "false"]:
        want_csv_saved = input(
            "Do you want to save the results as csv-file? Use y/n: "
        ).lower()
        if want_csv_saved in [
            "y",
            "yes",
            "yup",
            "ye",
        ] or want_csv_saved in ["n", "no", "nope"]:
            break
        print("Please provide a valid input.")
    if want_csv_saved in [
        "y",
        "yes",
        "yup",
        "ye",
        "true",
        1,
    ]:
        walkers_df = pd.DataFrame().from_dict(walkers, orient="index")
        walkers_df.to_csv("../data/walkers_{}w_{}s.csv".format(n_walkers, steps))
    else:
        pass
