from royal_game.db.jdbcUtils import JDBCUtils
import cx_Oracle


class MemberDAO:

    def addMember(self, dto):
        try:
            userpwd = "1234"  # Obtain password string from a user prompt or environment variable
            conn = cx_Oracle.connect("test", userpwd, "192.168.0.9/orcl", encoding="UTF-8")
            #conn = JDBCUtils.connection(self)
            cursor = conn.cursor()
            sql = "insert into member values(:1,:2,:3)"
            cursor.execute(sql, (dto.user_id, dto.user_pass, dto.user_pass))
            conn.commit()
            return True
        except cx_Oracle.Error as e:
            print(e)
            return False
