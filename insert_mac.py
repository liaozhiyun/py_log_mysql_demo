#!/usr/bin/env python

import lmysql
from mylog import logging as Log

def get_mac_code(file_name):
    mac_code = []
    with open(file_name) as f:
        for line in f:
            print(line)
            line = line[:-2]
            Log.info(line)
            #vec = line.split(',')
            #mac = vec[0]
            #code = vec[1]
            #print("mac:" + mac + "\tcode:" + code)
            #mac_code[mac] = code
            mac_code.append(line)
        return mac_code

def insert_db():
    mac_code = get_mac_code('./mac_code.txt')
    conn = lmysql.MySQLCommand('172.18.253.67', 8005, 'tom', 'tom123', 'kkb_db')
    conn.connect()
    print("mac_code size:" + str(len(mac_code)))
    Log.info("mac_code size:" + str(len(mac_code)))
    insert_success_count = 0
    query_success_count = 0
    update_success_count = 0
    need_update_count = 0
    
    #for key in mac_code:
    for line in mac_code:
        vec = line.split(',')
        mac = vec[0]
        code = vec[1]

        query_sql = 'select * from t_machine where mac = \'{}\' or code = \'{}\';'.format(mac, code)
        print("query_sql:" + query_sql)
        Log.info("query_sql:" + query_sql)
        
        rows = conn.select(query_sql)
        if rows == None:
            continue
        else:
            query_success_count = query_success_count + 1

        if len(rows) == 0:
            insert_sql = 'insert into t_machine (mac, code, type, colorType, bstate, createTime, modifyTime) values (\'{}\', \'{}\', 1, 0, 1, NOW(), NOW());'.format(mac, code)
            print("insert_sql:" + insert_sql)
            Log.info("insert_sql:" + insert_sql)
            #'''
            ret = conn.insert(insert_sql)
            if ret == 0:
                insert_success_count = insert_success_count + 1
            #'''
        else:
            for row in rows:
                val = "\t\t\t" + str(row[0]) + "\t" + str(row[1]) + "\t" + str(row[2]) + \
                "\t" + str(row[3]) + "\t" + str(row[4]) + "\t" + str(row[5]) + \
                "\t" + str(row[6]) + "\t" + str(row[7])
                print("t_machine exist:" + val)
                Log.info("t_machine exist:" + val)
                old_id = row[0]
                old_mac = str(row[1])
                old_mac = old_mac.upper()
                old_code = str(row[2])
                
                new_mac = str(mac)
                new_code = str(code)
                
                update_sql = "";
                if new_mac == old_mac and new_code == old_code:
                    continue
                if new_mac == old_mac and new_code != old_code:
                    update_sql = 'update t_machine set code = \'{}\' where id = {};'.format(new_code, old_id)
                elif mnew_code == old_code and new_mac != old_mac:
                    update_sql = 'update t_machine set mac = \'{}\' where id = {};'.format(new_mac, old_id)
                else:
                    print("occur error")

                print("update_sql:" + update_sql)
                Log.info("update_sql:" + update_sql)
                need_update_count = need_update_count + 1
                ret = conn.update(update_sql)
                if ret == 0:
                    update_success_count = update_success_count + 1
    print("insert_success_count:" + str(insert_success_count))
    Log.info("insert_success_count:" + str(insert_success_count))
    print("query_success_count:" + str(query_success_count))
    Log.info("query_success_count:" + str(query_success_count))
    print("need_update_count:" + str(need_update_count))
    Log.Info("need_update_count:" + str(need_update_count))
    print("update_success_count:" + str(update_success_count))
    Log.info("update_success_count:" + str(update_success_count))
    conn.Close()

if __name__ == '__main__':
    #get_mac_code('./mac_code.txt')
    insert_db()
