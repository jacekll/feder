#!/bin/python2.7
# -*- coding: utf-8 -*-
"""
A tool to insert institutions from CSV files.

Requirements:
 - requests
 - gusregon
 - unicodecsv
 - jmespath

Example usage:

To run help text use:
$ python insert_institution_csv.py -h
"""
from __future__ import print_function, unicode_literals

import argparse
import sys

import itertools
from Queue import Queue

import jmespath
import requests
import tqdm
import unicodecsv as csv
import requests_cache

try:
    from urlparse import urljoin
except ImportError:
    from urllib.parse import urljoin


class Client(object):

    def __init__(self, start, s=None):
        self.start = start
        self.s = s or requests.Session()

    def get_page_iter(self):
        q = Queue()
        q.put(self.start)
        while not q.empty():
            resp = self.s.get(url=q.get())
            if resp.status_code != 200:
                return
            data = resp.json()
            if data.get('next'):
                q.put(data['next'])
            for row in data['results']:
                yield row

JMES_DEFAULT = "{name: name, url:url, pk:pk, email:email, tags:join(',',tags), jst:jst, regon:regon}"


class Command(object):

    def __init__(self, argv):
        self.argv = argv
        self.args = self.get_build_args(argv[1:])
        self.s = requests.Session() if not self.args.cache else requests_cache.CachedSession()

    def get_build_args(self, argv):
        parser = argparse.ArgumentParser()
        parser.add_argument('--output',
                            required=True,
                            type=argparse.FileType('w'),
                            help="Output CSV-file")
        parser.add_argument('--start',
                            required=True,
                            help="Start URL")
        parser.add_argument('--jmes', type=jmespath.compile,
                            required=False,
                            help='JMESPath to convert values (default: "{}")'.format(JMES_DEFAULT),
                            default=jmespath.compile(JMES_DEFAULT))
        parser.add_argument('--cache', action='store_true', help="Enable cache")
        return parser.parse_args(argv)

    def run(self):

        client = Client(start=self.args.start, s=self.s)
        data = client.get_page_iter()
        first = next(data)

        fieldnames = self.args.jmes.search(first).keys()

        print("Identified fields: {}".format(", ".join(fieldnames)))

        writer = csv.DictWriter(self.args.output, fieldnames=fieldnames)
        writer.writeheader()
        for item in tqdm.tqdm(itertools.chain([first], data)):
            writer.writerow(self.args.jmes.search(item))

if __name__ == "__main__":
    sys.exit(Command(sys.argv).run())
