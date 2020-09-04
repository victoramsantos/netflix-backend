from src.repository.ReminderRepository import ReminderRepository
from src.repository.WatchedRepository import WatchedRepository
from src.service.ReminderService import ReminderService
from src.service.WatchedService import WatchedService

reminder_service = ReminderService(
    reminder_repository=ReminderRepository()
)

watched_service = WatchedService(
    watched_repository=WatchedRepository()
)