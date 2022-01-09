from resources.admin import CreateAdmin
from resources.auth import Register, Login, LoginCoach
from resources.training import ListCreateTraining

routes = (
    (Register, "/register"),
    (Login, "/login"),
    (LoginCoach, "/coaches/login"),
    (ListCreateTraining, "/students/trainings"),
    (CreateAdmin, "/admins/create-admin"),
)
