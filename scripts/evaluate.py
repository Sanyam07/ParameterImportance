from importance.importance.importance import Importance
from importance.utils.io.cmd_reader import CMDs
import logging

if __name__ == '__main__':
    cmd_reader = CMDs()
    args, misc_ = cmd_reader.read_cmd()  # read cmd args
    logging.basicConfig(level=args.verbose_level)
    importance = Importance(args.scenario_file, args.history, args.modus)  # create importance object
    importance_value_dict = importance.evaluate_scenario()
    print(importance.evaluator)
    # TODO plotting
