"""" Shooter model for representing a shooter in the competition. """
from pydantic import BaseModel, Field


class Shooter(BaseModel):
    """ Model representing a shooter with its result in the competition and the corresponding league/event. """

    name: str = Field(..., description="Name of the shooter")
    team_id: str = Field(...,examples="Wappersdorf 1", description="Identifier for the team the shooter belongs to")
    score: int = Field(..., description="Score of the shooter")
    discipline: str = Field(..., description="Discipline of the shooter")
    league: str = Field(..., description="League of the shooter")

    def __str__(self):
        return f"[{self.league}] - {self.name} - {self.team_id} - {self.score} - {self.discipline}"
