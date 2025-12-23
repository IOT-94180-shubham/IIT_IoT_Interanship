from Q1_utils.dbConnection import getBDConnection

def  excutequery(query):
    connection = getBDConnection()
    
    cursor = connection.cursor()
    
    cursor.excute.query()
    
    connection.commit()
    
    cursor.close()
    
    connection.close()
    