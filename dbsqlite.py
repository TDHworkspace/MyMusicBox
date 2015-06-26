# -*- coding: utf-8 -*-
'''
sqllite3 操作
用于记录播放列表
'''
__author__ = 'Louie.v (louie.vv@gmail.com)'
import sqlite3


dbName='./plist.db'

class DbSqlite():
    def __init__(self):
            '''
            创建数据库，如果库存在，不创建。
            '''
            creat_db_sql='''
                CREATE TABLE if not exists "plist" (
                "id"  INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                "songid"  INTEGER NOT NULL,
                "songname"  TEXT(20) NOT NULL,
                "mp3url"  TEXT(200) NOT NULL,
                "artist"  TEXT(40),
                "album_name"  TEXT(40),
                "album_picurl"  TEXT(200),
                CONSTRAINT "listid" UNIQUE ("id" ASC),
                CONSTRAINT "songid" UNIQUE ("songid" ASC)
                );'''
            try:
                conn=sqlite3.connect(dbName)
                cr=conn.cursor()
                cr.execute(creat_db_sql)
                fe=cr.fetchall()
                cr.close()
                conn.close()
            except sqlite3.Error,e:
                print "On Create Table Error: ",e


    def select_db(self,sid):
            '''
            执行查询
            '''
            conn=sqlite3.connect(dbName)
            cr=conn.cursor()
            cr.execute("select songid from plist where songid=" + str(sid) +";")
            fe=cr.fetchall()
            cr.close()
            conn.close()
            return  fe

    def count_db(self):
            '''
            执行查询
            '''
            conn=sqlite3.connect(dbName)
            cr=conn.cursor()
            cr.execute("select count(*) from plist;")
            fe=cr.fetchall()
            cr.close()
            conn.close()
            return  fe
    def insert_db(self,dataDic):
            '''
            插入数据
            '''
            sqlDate=(dataDic["song_id"],dataDic["song_name"],dataDic["mp3_url"],dataDic["artist"],dataDic["album_name"],dataDic["album_picurl"])
            try:
                conn=sqlite3.connect(dbName)
                cr=conn.cursor()
                cr.execute('''insert into plist ("songid","songname","mp3url","artist","album_name","album_picurl") values (?,?,?,?,?,?)''',sqlDate)
                conn.commit()
                fe=cr.fetchall()
                cr.close()
                conn.close()
                return True
            except sqlite3.Error,e:
                print "On Insert Error: ",e
                return "insert db error"

    def delete_db(self,sid):
            '''
            删除数据
            '''
            try:
                conn=sqlite3.connect(dbName)
                cr=conn.cursor()
                cr.execute("delete from plist where songid="+ sid +";")
                conn.commit()
                fe=cr.fetchall()
                cr.close()
                conn.close()
                return True
            except sqlite3.Error,e:
                print "On Delete Error: ",e
                return "delete db error"
    def delete_all(self):
        '''
        删除所有
        '''
        try:
            conn=sqlite3.connect(dbName)
            cr=conn.cursor()
            cr.execute("delete from plist;")
            conn.commit()
            fe=cr.fetchall()
            cr.execute('update sqlite_sequence set seq=1 where name="plist";')
            conn.commit()
            fe=cr.fetchall()
            cr.close()
            conn.close()
            return  True
        except sqlite3,e:
            print "On Delete All Error:",e
            return False

    def select_all(self):
            '''
            查询所有结果
            '''
            conn=sqlite3.connect(dbName)
            cr=conn.cursor()
            cr.execute("select songid,songname,artist from plist;")
            fe=cr.fetchall()
            cr.close()
            conn.close()
            return  fe
            print "====================================select start================================"
            for row in fe:
                print row
            print "=====================================select end================================"
            return fe


if __name__ == "__main__":
    db=DbSqlite()
    db.insert_db({
        'song_id':32358694,
        'song_name':"Brave Shine",
        'mp3_url':"""http://m1.music.126.net/NEl-rP7FHqjScMRA9HchfQ==/7886796906996700.mp3""",
        'artist':"Aimer",
        'album_name':"Brave Shine",
        'album_picurl':"http://p4.music.126.net/EnZBXon5cZWLPHEn2cHMFQ==/2940094094533735.jpg"
    })
    db.select_all()
    db.select_db(str(2222))

