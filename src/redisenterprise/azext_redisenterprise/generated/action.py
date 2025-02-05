# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------


# pylint: disable=protected-access

# pylint: disable=no-self-use


import argparse
from collections import defaultdict
from knack.util import CLIError


class AddPersistence(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        namespace.persistence = action

    def get_action(self, values, option_string):
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]

            if kl == 'aof-enabled':
                d['aof_enabled'] = v[0]

            elif kl == 'rdb-enabled':
                d['rdb_enabled'] = v[0]

            elif kl == 'aof-frequency':
                d['aof_frequency'] = v[0]

            elif kl == 'rdb-frequency':
                d['rdb_frequency'] = v[0]

            else:
                raise CLIError(
                    'Unsupported Key {} is provided for parameter persistence. All possible keys are: aof-enabled,'
                    ' rdb-enabled, aof-frequency, rdb-frequency'.format(k)
                )

        return d


class AddModules(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddModules, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]

            if kl == 'name':
                d['name'] = v[0]

            elif kl == 'args':
                d['args'] = v[0]

            else:
                raise CLIError(
                    'Unsupported Key {} is provided for parameter modules. All possible keys are: name, args'.format(k)
                )

        return d


class AddLinkedDatabases(argparse._AppendAction):
    def __call__(self, parser, namespace, values, option_string=None):
        action = self.get_action(values, option_string)
        super(AddLinkedDatabases, self).__call__(parser, namespace, action, option_string)

    def get_action(self, values, option_string):
        try:
            properties = defaultdict(list)
            for (k, v) in (x.split('=', 1) for x in values):
                properties[k].append(v)
            properties = dict(properties)
        except ValueError:
            raise CLIError('usage error: {} [KEY=VALUE ...]'.format(option_string))
        d = {}
        for k in properties:
            kl = k.lower()
            v = properties[k]

            if kl == 'id':
                d['id'] = v[0]

            else:
                raise CLIError(
                    'Unsupported Key {} is provided for parameter linked-databases. All possible keys are: id'.format(k)
                )

        return d
