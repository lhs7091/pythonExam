from royal_game.vo.memberDTO import MemberDTO


class ConsoleUtils:
    user_id = None
    user_pass = None
    user_name = None

    def getNewMemberInfo(self):
        user_id = input('User ID:')
        user_pass = input('password: ')
        user_name = input('name: ')

        dto = MemberDTO(user_id, user_pass, user_name)

        return dto
