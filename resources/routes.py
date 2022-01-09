from resources.admin import CreateAdmin, CreateCoach
from resources.auth import Register, Login, LoginCoach, LoginAdmin
from resources.training import ListCreateTraining

routes = (
    (Register, "/register"),
    (Login, "/login"),
    (LoginCoach, "/coaches/login"),
    (ListCreateTraining, "/students/trainings"),
    (CreateAdmin, "/admins/create-admin"),
    (LoginAdmin, "/admins/login"),
    (CreateCoach, "/admins/create-coach"),
)
