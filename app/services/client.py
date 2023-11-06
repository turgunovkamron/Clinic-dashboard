from contextlib import closing

from django.db import connection
from django.shortcuts import render
from methodism import dictfetchall

from app.models import Service


def client_doc(request, service: int = None):
    sql = f"""

SELECT a.id ass_id, a.name ass_name, u.id, u.name fname, u.familya l_name, u.img, u.phone, u.gender,u.info,
       p.name prof, pos.name "prosition_id"
FROM app_service a
INNER JOIN app_servicedocs asd ON asd.service_id = a.id
INNER JOIN app_user u ON asd.doc_id = u.id 
LEFT JOIN app_position pos ON pos.id = u.prosition_id 
LEFT JOIN app_professions p ON p.id = u.prof_id 


    
    where a.id={service}
        
    
    """

    with closing(connection.cursor()) as cursor:
        cursor.execute(sql)
        result = dictfetchall(cursor)

    ctx = {
        "roots": result

    }

    return render(request, "page/client/client_docs.html", ctx)
