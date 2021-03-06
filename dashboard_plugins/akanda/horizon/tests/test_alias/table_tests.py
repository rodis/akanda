# -*- encoding: utf-8 -*-
#
# Copyright © 2012 New Dream Network, LLC (DreamHost)
#
# Author: Rosario Di Somma <rosario.disomma@dreamhost.com>
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import mock

from horizon import test

from akanda.horizon.alias.tables import PortAliasTable
from akanda.horizon.api.quantum_extensions_client import (Port)

PORT_TEST_DATA = (
    Port('SSH', 'tcp', 22, '1'),
    Port('IRC', 'tcp', 33, '2'),
    Port('MySQL', 'udp', 44, '3'),
)


class PortAliasTableTests(test.TestCase):
    def test_table_instantiation(self):
        """ Tests everything that happens when the table is instantiated. """
        self.table = PortAliasTable(self.request, PORT_TEST_DATA)
        # Properties defined on the table
        self.assertEqual(self.table.data, PORT_TEST_DATA)
        self.assertEqual(self.table.name, "ports")
        # Verify calculated options that weren't specified explicitly
        self.assertTrue(self.table._meta.actions_column)
        self.assertTrue(self.table._meta.multi_select)
        # Test for verbose_name
        self.assertEqual(unicode(self.table), u"Port Aliases")
        # Column ordering and exclusion.
        # This should include auto-columns for multi_select and actions,
        # but should not contain the excluded column.
        # Additionally, auto-generated columns should use the custom
        # column class specified on the table.
        self.assertQuerysetEqual(self.table.columns.values(),
                                 ['<Column: multi_select>',
                                  '<Column: alias_name>',
                                  '<Column: protocol>',
                                  '<Column: ports>',
                                  '<Column: actions>'])
        # Actions (these also test ordering)
        self.assertQuerysetEqual(self.table.base_actions.values(),
                                 ['<Create: create>',
                                  '<Delete: delete>',
                                  '<Edit: edit>'])
        self.assertQuerysetEqual(self.table.get_table_actions(),
                                 ['<Create: create>',
                                  '<Delete: delete>'])
        self.assertQuerysetEqual(self.table.get_row_actions(PORT_TEST_DATA[0]),
                                 ['<Edit: edit>'])
        # Auto-generated columns
        multi_select = self.table.columns['multi_select']
        self.assertEqual(multi_select.auto, "multi_select")
        self.assertEqual(multi_select.get_final_attrs().get('class', ""),
                         "multi_select_column")
        actions = self.table.columns['actions']
        self.assertEqual(actions.auto, "actions")
        self.assertEqual(actions.get_final_attrs().get('class', ""),
                         "actions_column")

    def test_table_construction(self):
        self.table = PortAliasTable(self.request, PORT_TEST_DATA)
        # Verify we retrieve the right columns for headers
        columns = self.table.get_columns()
        self.assertQuerysetEqual(columns, ['<Column: multi_select>',
                                           '<Column: alias_name>',
                                           '<Column: protocol>',
                                           '<Column: ports>',
                                           '<Column: actions>'])
        # Verify we retrieve the right rows from our data
        rows = self.table.get_rows()
        self.assertQuerysetEqual(rows, ['<Row: ports__row__1>',
                                        '<Row: ports__row__2>',
                                        '<Row: ports__row__3>'])
        # Verify each row contains the right cells
        self.assertQuerysetEqual(rows[0].get_cells(),
                                 ['<Cell: multi_select, ports__row__1>',
                                  '<Cell: alias_name, ports__row__1>',
                                  '<Cell: protocol, ports__row__1>',
                                  '<Cell: ports, ports__row__1>',
                                  '<Cell: actions, ports__row__1>'])

    def test_table_actions_verbose_name(self):
        req = self.factory.post('/my_url/')
        self.table = PortAliasTable(req, PORT_TEST_DATA)

        table_actions = self.table.get_table_actions()
        create_action = table_actions[0]
        delete_action = table_actions[1]

        row_actions = self.table.get_row_actions(PORT_TEST_DATA[0])
        edit_action = row_actions[0]

        # Create
        self.assertEqual(unicode(create_action.verbose_name), 'Create Alias')

        # Delete
        self.assertEqual(unicode(delete_action.verbose_name),
                         'Delete Port Alias')
        self.assertEqual(unicode(delete_action.verbose_name_plural),
                         'Delete Port Aliases')
        self.assertEqual(unicode(delete_action.action_present), 'Delete')
        self.assertEqual(unicode(delete_action.action_past), 'Deleted')

        # Edit
        self.assertEqual(unicode(edit_action.verbose_name), 'Edit Alias')

    def test_table_actions_post(self):
        #Delete
        action_string = "ports__delete"
        req = self.factory.post('/my_url/', {'action': action_string,
                                             'object_ids': [1, 2]})
        self.table = PortAliasTable(req, PORT_TEST_DATA)
        table_actions = self.table.get_table_actions()
        delete_action = table_actions[1]

        with mock.patch.object(delete_action, 'delete') as mock_delete:
            mock_delete.return_value = None
            with mock.patch.object(
                    delete_action, 'success_url') as mock_success:
                mock_success.return_value = ''
                handled = self.table.maybe_handle()
                self.assertEqual(handled.status_code, 302)
                self.assertEqual(list(req._messages)[0].message,
                                 u"Deleted Port Aliases: SSH, IRC")
