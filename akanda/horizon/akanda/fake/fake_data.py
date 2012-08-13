port_aliases_fake_data = {
# Fake data for Port Aliases
# .. attribute:: id
#         Fake implementation detail
#
# .. attribute:: alias_name
#         type: free text??
#
# .. attribute:: protocol
#         type: integer??
#
#         PROTOCOL_CHOICES = (
#             (0, 'TCP'),
#             (1, 'UDP'),
#             (2, 'TCP+UDP'),
#        )
#
# .. attribute:: ports
#         type: list of integers??
#
# Note(rods): we need to define data types in order to write forms' validation

    'df698e967f554e4284583c10ba326c5b': {
        'id': 'df698e967f554e4284583c10ba326c5b',
        'alias_name': 'FTP',
        'protocol': 0,
        'ports': [21, 22],
    },
    '6269ee9f6dcd4a099b9551fb8ad27a3a': {
        'id': '6269ee9f6dcd4a099b9551fb8ad27a3a',
        'alias_name': 'SSH',
        'protocol': 0,
        'ports': [22]
    },
    'd50abcd19dd04f788ae9ebed3865460e': {
        'id': 'd50abcd19dd04f788ae9ebed3865460e',
        'alias_name': 'SMTP',
        'protocol': 0,
        'ports': [25],
    },
    '13bbcf90c97f4cbdac446ecf8e6b893b': {
        'id': '13bbcf90c97f4cbdac446ecf8e6b893b',
        'alias_name': 'MySQL',
        'protocol': 2,
        'ports': [3306],
    }
}

instances_fake_data = {
# Fake instances
    '015eff2961d8430ba0c7c483fcb2da7a': {
        'id': '015eff2961d8430ba0c7c483fcb2da7a',
        'name': 'Instance 1',
    },
    '7f256428dbfe4bec91e643fac513778e': {
        'id': '7f256428dbfe4bec91e643fac513778e',
        'name': 'Instance 2',
    },
    '7f96521d5e8345878f6924f6d75c2884': {
        'id': '7f96521d5e8345878f6924f6d75c2884',
        'name': 'Instance 3',
    },
    'a5456395a9e3476d96af4aafb6880a3d': {
        'id': 'a5456395a9e3476d96af4aafb6880a3d',
        'name': 'Instance 4',
    }
}


host_aliases_fake_data = {
#  Fake data for Host Aliases
# .. attribute:: id
#         Fake implementation detail
#
# .. attribute:: alias_name
#         type: free text??
#
# .. attribute:: instances
#         type: list of instances id??
#
# Note(rods): we need to define data types in order to write forms' validation

    '8b26e7e8cedd4bdf86e2a8f433bbc0f8': {
        'id': '8b26e7e8cedd4bdf86e2a8f433bbc0f8',
        'alias_name': 'New Host Alias',
        'instances': ['015eff2961d8430ba0c7c483fcb2da7a',
                      '7f256428dbfe4bec91e643fac513778e',
                      '7f96521d5e8345878f6924f6d75c2884']
    },
}
