import argparse
import inspect
import imp
import os
import sys


# Define command line options.
_ARGS = argparse.ArgumentParser("Rewrites CMIP6 vocab definitions to xmind files.")
_ARGS.add_argument(
    "--source",
    help="Path to a directory in which specializations reside.",
    dest="source",
    type=str,
    default=os.path.dirname(__file__)
    )


print os.path.dirname(__file__)


def _main(args):
    """Main entry point.

    """
    # Load specialization modules.
    modules = sorted([i for i in os.listdir(args.source) if not i.startswith('_') and i.endswith('.py')])
    modules = [os.path.join(args.source, m) for m in modules]
    modules = [(m.split("/")[-1].split(".")[0], m) for m in modules]
    modules = [imp.load_source(name, fpath) for name, fpath in modules]

    main = grid = key_properties = None
    sub_processes = []

    for module in modules:
    	if main is None:
    		main = module
    	elif main.__name__.endswith('_grid'):
    		grid = module
    	elif main.__name__.endswith('_key_properties'):
    		key_properties = module
    	else:
    		sub_processes.append(module)





    # modules = [imp.load_module(m.split('.')[0], os.path.join(args.source, m)) for m in modules]





# Entry point.
if __name__ == '__main__':
	pass
    # _main(_ARGS.parse_args())
