# Generate CLI script boilerplate
#
# This script has command:
#   $ python3 -m service.pseudodevice.spawn --name <name> --id <id>
#
# This script has option:
#   --name <name>  Name of device
#   --id <id>      ID of device
#

import argparse
import json
import logging
import random
import sys
import time

LOG_LEVEL = logging.INFO
LOG_FORMAT = '%(asctime)s %(levelname)s: %(message)s'


def spawn(name, _id):
    # Create or update file here
    with open(f'{name}{_id}', 'w') as f:
        paylaod = json.dumps({
            'current': random.randint(0, 100),
            'voltage': random.randint(0, 100),
        })
        f.write(paylaod)
        logging.info(f'Write to file: {paylaod}')


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', type=str, help='Name of device', default='pseudodevice')
    parser.add_argument('--id', type=str, help='ID of device', default='1')
    return parser.parse_args()


def main():
    args = parse_args()
    logging.basicConfig(level=LOG_LEVEL, format=LOG_FORMAT)

    logging.info('Starting pseudodevice')
    while 1:
        try:
            spawn(args.name, args.id)
            time.sleep(1)
        except KeyboardInterrupt:
            logging.info('Stopping pseudodevice')
            sys.exit(0)


if __name__ == '__main__':
    sys.exit(main())

