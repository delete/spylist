import sys
sys.path.insert(0, '../spymanager')
sys.path.insert(0, '../')

from tests import create_database_collection
from src.spy import SpyManager

# Database settings
DATABASE_NAME = 'spies_database'
COLLECTION_NAME = 'subscriptions'
subscriptions_collection = create_database_collection(DATABASE_NAME, COLLECTION_NAME)

# User to test
USERNAME = 'pinheirofellipe'
CHAT_ID = 123456

# Spy actions
spy_manager = SpyManager(subscriptions_collection)

# Remove if it's exists
spy_manager.remove(USERNAME)

# Adding bot user
spy_manager.add(USERNAME, CHAT_ID)

all_spies = spy_manager.all()

assert len(all_spies) == 1

# Get created spy
spy = spy_manager.get(USERNAME)

assert spy.username == USERNAME

assert spy.exists() is True

# Adding groups
new_group = 'devs'
spy.add_group(new_group)

new_group = 'sports'
spy.add_group(new_group)

assert len(spy.groups) == 2

# Adding user to group
member_mazulo = 'mazulo_'
member_pinheiro = 'pinheirofellipe'
group_to_add = 'devs'

spy.add_members_to_group([member_mazulo, member_pinheiro], group_to_add)

assert len(spy.members_from_group('devs')) == 2

# Remove group
spy.remove_group('sports')

assert len(spy.groups) == 1

# Removing member
spy.remove_member_from_group('mazulo_', 'devs')

assert len(spy.members_from_group('devs')) == 1

print('Well done!')
