from royal_game.dao.memberDAO import MemberDAO


class MemberService:

    def addMemberService(self, dto):
        db = MemberDAO()
        return db.addMember(dto)
