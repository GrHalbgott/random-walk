#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A Random Walk Simulation"""

from walkers import Walker
import utils
import sys
import os
import time

# change path to where this file is located (important for relative paths)
try:
    os.chdir(sys.path[0])
except Exception:
    print(
        "Please check if your path is correct. You can comment out the command above if not needed."
    )
    sys.exit()


def main():
    """
    Generates random walkers, calculates their path, saves them in a dataframe and plots them into a plot
    :return: csv-file with walkers and their attributes and a plot with all walkers
    """
    (
        total_steps,
        n_walkers,
        move_pattern,
        random_start,
        want_plot_saved,
        total_runs,
    ) = utils._check_input_arguments()

    starttime = time.time()

    # enabling the script to run multiple times
    for run_num in range(total_runs):
        run_num += 1
        walkers = {}
        # creating multiple instances of walkers
        for walker_num in range(n_walkers):
            new_walker = Walker(total_steps=total_steps)
            new_walker.random_walk(move_pattern, random_start)

            # add to list of walkers (csv-file)
            walkers[walker_num] = {"geometry": new_walker}

            utils.plot_walker_path(n_walkers, new_walker, random_start)

        # write information about walkers to dataframe
        utils.write_to_dataframe(walkers)

        stoptime = time.time()

        # Print out the information to user
        if n_walkers == 1:
            print(
                "Finished computing the Random Walk Simulation with {} walker & {} steps.\n The script took {:0.2f} seconds to run.".format(
                    n_walkers, total_steps, stoptime - starttime
                )
            )
        else:
            print(
                "Finished computing the Random Walk Simulation with {} walkers & {} steps.\n The script took {:0.2f} seconds to run.".format(
                    n_walkers, total_steps, stoptime - starttime
                )
            )

        utils.plot_all_walkers(total_steps, n_walkers, want_plot_saved)


if __name__ == "__main__":
    main()
