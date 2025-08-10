from pathlib import Path
import time

import aiofiles
from fastapi import UploadFile
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import ImagePath
from core.schemas.images import ImageCreate


async def upload_movie_image(
    session: AsyncSession,
    image: UploadFile,
    movie_id: int,
):
    # 2. Подготовка директории
    upload_dir = Path("env/static/movie_images")
    upload_dir.mkdir(parents=True, exist_ok=True)

    # 3. Генерация уникального имени файла
    file_ext = Path(image.filename).suffix.lower()
    filename = f"movie_{movie_id}_{int(time.time())}{file_ext}"
    filepath = upload_dir / filename

    # 4. Чтение и сохранение файла
    try:
        contents = await image.read()
        async with aiofiles.open(filepath, "wb") as f:
            await f.write(contents)
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to save image: {str(e)}",
        )

    image_path = ImagePath(path=str(filepath), movie_id=movie_id)
    session.add(image_path)
    await session.commit()
    return image_path
