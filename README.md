# coding-test
Api para gerenciar a agenda de salas de reuniões da empresa feito em Django

Rodar a API:

python manage.py runserver

superuser: admin pass: admin@secret

End Points:

Salas:

Listagem de Salas: GET  : /api/v1/salas/

Cadastro de Salas: POST : /api/v1/salas/  
{
    "nome": "Py",
    "descricao": "Sala de Reuniçao mezanino | Recursos: Computador + Projetor",
    "quantidade_pessoas": 5
}

Edição de Salas: PUT : /api/v1/salas/5

{
    "nome": "Py",
    "descricao": "Sala de Reuniçao mezanino | Recursos: Computador + Projetor",
    "quantidade_pessoas": 5
}

Exclusão de Salas: DELETE: /api/v1/salas/5

Agenda:

Listagem de Agenda: GET  : /api/v1/agenda/

Cadastro de Agenda: POST : /api/v1/agenda/  
{
	"sala": 4,
	"data": "2018-09-10",
	"hora_inicial": "16:00:00",
	"hora_final": "17:00:00"
}

Edição de Agenda: PUT : /api/v1/salas/10

{
	"sala": 4,
	"data": "2018-09-10",
	"hora_inicial": "16:00:00",
	"hora_final": "17:00:00"
}

Exclusão de Agenda: DELETE: /api/v1/salas/10

Filtros:

Por Data: /api/v1/agenda/?data=2018-09-10
[{"id":9,"sala":1,"data":"2018-09-11","hora_inicial":"08:00:00","hora_final":"10:00:00"}]

Por Sala: /api/v1/agenda/?sala=4
[{"id":7,"sala":4,"data":"2018-09-10","hora_inicial":"16:00:00","hora_final":"17:00:00"},{"id":8,"sala":4,"data":"2018-09-10","hora_inicial":"18:00:00","hora_final":"19:00:00"}]

                  

