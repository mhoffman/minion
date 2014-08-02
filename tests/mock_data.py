''' Data structures used for unit testing. '''
from datetime import date, datetime
import brain_of_minion as brain

from ConfigParser import SafeConfigParser

TEST_DATA_DIRECTORY = '/tmp/test_minion'

def mock_settings():
    ''' Always return the default settings. '''
    return brain._settings_parser(TEST_DATA_DIRECTORY)

EXPECTED_DATE = datetime(2014, 04, 14, 0, 0)

TEST_FILE_TEMPLATE_CONTENT = \
'''Weekend Plan for 2014-04-14
==============================
:date: 2014-04-14

The topic is: {topic}

Goals
------
Wow. Such goals. So accomplish.'''

TEST_FILE_CONTENT = \
'''Weekend Plan for 2014-04-14
==============================
:date: 2014-04-14

The topic is: This is a great topic.

Goals
------
Wow. Such goals. So accomplish.'''

TEST_FILE_CONTENT_WITH_TAGS = \
'''Weekend Plan for 2014-04-14
==============================
:date: 2014-04-14

The topic is: This is a great topic.

Goals
------
Wow. Such goals. So accomplish.
:tags: bar foo ninja'''

TEST_FILE_TITLE = '''Weekend Plan for 2014-04-14'''

# This 'tag' should not appear in file content for testing.
TEST_GIBBERISH = 'Slartibarfast'

# This 'tag' should appear in various file content for testing.
TEST_TAG = 'Ninja'
TEST_TAGS = ['foo', 'BAR', 'Ninja']
TEST_TAG_LINE = ':tags: bar foo ninja'
