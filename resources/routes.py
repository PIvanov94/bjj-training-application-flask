from resources.admin import CreateAdmin, CreateCoach
from resources.auth import Register, Login, LoginCoach, LoginAdmin
from resources.training import ListCreateTraining, TrainingDetail, BeginnersJoinTraining

routes = (
    (Register, "/register"),
    (Login, "/login"),
    (LoginCoach, "/coaches/login"),
    (ListCreateTraining, "/coaches/trainings"),
    (CreateAdmin, "/admins/create-admin"),
    (LoginAdmin, "/admins/login"),
    (CreateCoach, "/admins/create-coach"),
    (TrainingDetail, "/coaches/trainings/<int:id_>"),
    (BeginnersJoinTraining, "/trainings/beginners/join/<int:id_>")
)
