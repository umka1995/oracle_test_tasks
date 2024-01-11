
def check_relation(connections, first_name, second_name):
    user_friends = {}

    for user, friends in connections:
        user_friends[user] = set(friends)

    # Проверяем наличие общих друзей между заданными пользователями
    if first_name in user_friends and second_name in user_friends:
        common_friends = user_friends[first_name].intersection(user_friends[second_name])
        return bool(common_friends)

    return False

if __name__ == '__main__':

    connections = [
        ('user1', ['friend1', 'friend2']),
        ('user2', ['friend2', 'friend3']),
    
    ]

    first_name = 'user1'
    second_name = 'user2'
    result = check_relation(connections, first_name, second_name)
    print(result)














