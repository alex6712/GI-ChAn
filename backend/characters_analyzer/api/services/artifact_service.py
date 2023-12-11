from uuid import UUID

from sqlalchemy.ext.asyncio import AsyncSession

from characters_analyzer.database.tables.entities import Artifact
from characters_analyzer.schemas import ArtifactData


async def add_artifact(
    session: AsyncSession, user_id: UUID, artifact_data: ArtifactData
):
    """Adds an artifact record to the database.

    Parameters
    ----------
    session : AsyncSession
        Request session object.
    user_id : UUID
        ID of the user that holds this artifact.
    artifact_data : ArtifactData
        Artifact data.
    """
    session.add(Artifact(user_id=user_id, **artifact_data.model_dump()))
    await session.commit()
