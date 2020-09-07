from src.repository.SupportRepository import SupportRepository
from src.service.SupportService import SupportService

support_service = SupportService(
    support_repository=SupportRepository()
)