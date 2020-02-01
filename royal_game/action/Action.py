from royal_game.view.consoleUtils import ConsoleUtils
from royal_game.service.memberService import *

class Action:

    def execute(self):
        pass


class AddMemberAction(Action):

    def execute(self):
        cu = ConsoleUtils()
        dto = cu.getNewMemberInfo()
        ams = MemberService()
        print(ams.addMemberService(dto))

