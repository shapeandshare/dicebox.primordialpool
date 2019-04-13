# Derived from https://github.com/harvitronix/neural-network-genetic-algorithm
# Derived source copyright: Matt Harvey, 2017, Derived source license: The MIT License
# See docs/Matt Harvey.LICENSE

"""Entry point to evolving the neural network. Start here."""
import logging
import os
import errno
from tqdm import tqdm
import dicebox.utils.helpers as helpers
from dicebox.config.dicebox_config import DiceboxConfig
from dicebox.evolutionary_optimizer import EvolutionaryOptimizer

# Config
config_file = './dicebox.config'
CONFIG = DiceboxConfig(config_file)


###############################################################################
# Setup logging.
###############################################################################
helpers.make_sure_path_exists(CONFIG.LOGS_DIR)
logging.basicConfig(
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
    level=logging.INFO,
    filemode='w',
    filename="%s/primordialpool.%s.log" % (CONFIG.LOGS_DIR, os.uname()[1])
)


def train_networks(networks):
    """Train each network.

    Args:
        networks (list): Current population of networks
        dataset (str): Dataset to use for training/evaluating
    """
    pbar = tqdm(total=len(networks))
    for network in networks:
        network.train_v2()
        pbar.update(1)
    pbar.close()


def get_average_accuracy(networks):
    """Get the average accuracy for a group of networks.

    Args:
        networks (list): List of networks

    Returns:
        float: The average accuracy of a population of networks.

    """
    total_accuracy = 0
    for network in networks:
        total_accuracy += network.accuracy_v2

    return total_accuracy / len(networks)


def generate(generations, population):
    logging.info('Generations: %s' % (generations))
    logging.info('Population: %s' % (population))

    """Generate a network with the genetic algorithm.

    Args:
        generations (int): Number of times to evole the population
        population (int): Number of networks in each generation
        nn_param_choices (dict): Parameter choices for networks
        dataset (str): Dataset to use for training/evaluating

    """
    optimizer = EvolutionaryOptimizer(retain=0.4,
                                      random_select=0.1,
                                      mutate_chance=0.2,
                                      config_file='./dicebox.config',
                                      lonestar_model_file='./dicebox.lonestar.json')
    networks = optimizer.create_population(population)

    # Evolve the generation.
    for i in range(generations):
        logging.info("***Doing generation %d of %d***" %
                     (i + 1, generations))
        logging.info('-'*80)
        logging.info('Individuals in current generation')
        print_networks(networks)
        logging.info('-' * 80)

        # Train and get accuracy for networks.
        train_networks(networks)

        # Get the average accuracy for this generation.
        average_accuracy = get_average_accuracy(networks)

        # Print out the average accuracy each generation.
        logging.info("Generation average: %.2f%%" % (average_accuracy * 100))
        logging.info('-'*80)

        logging.info('Top 5 individuals in current generation')

        # Sort our final population.
        current_networks = sorted(networks, key=lambda x: x.accuracy_v2, reverse=True)

        # Print out the top 5 networks.
        print_networks(current_networks[:5])

        # Evolve, except on the last iteration.
        if i != generations - 1:
            # Do the evolution.
            networks = optimizer.evolve(networks)

    # Sort our final population.
    networks = sorted(networks, key=lambda x: x.accuracy_v2, reverse=True)

    # Print out the top 5 networks.
    print_networks(networks[:5])


def print_networks(networks):
    """Print a list of networks.

    Args:
        networks (list): The population of networks

    """
    logging.info('-'*80)
    for network in networks:
        network.print_network_v2()


def main():
    logging.info("***Evolving %d generations with population %d***" % (CONFIG.GENERATIONS, CONFIG.POPULATION))
    generate(CONFIG.GENERATIONS, CONFIG.POPULATION)


if __name__ == '__main__':
    main()
