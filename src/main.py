from ui.ui import UI, window
from services.calculator_service import CalculatorService
from services.user_service import UserService
from repositories.history_repository import history_repository
from repositories.user_repository import user_repository

if __name__ == "__main__":
    calculator = CalculatorService()
    user = UserService(user_repository, history_repository)
    ui = UI(window, calculator, user)
    ui.start()
    window.mainloop()
