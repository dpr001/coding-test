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
                  

