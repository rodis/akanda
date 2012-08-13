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
