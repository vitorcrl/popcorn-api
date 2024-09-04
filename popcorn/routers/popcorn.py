from fastapi import APIRouter, Depends, HTTPException
from typing import List
from sqlalchemy.orm import Session
# from ..database import SessionLocal, engine
from popcorn.logger import logger

# models.Base.metadata.create_all(bind=engine)

router = APIRouter()

# Dependência para obter a sessão do banco de dados
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# @router.post("/popcorns/", response_model=schemas.popcorn)
# def create_popcorn(popcorn: schemas.popcornCreate, db: Session = Depends(get_db)):
#     logger.info("Rota para criação de um novo popcorn")
#     return crud.create_popcorn(db=db, popcorn=popcorn)

@router.get("/popcorns/")
def read_popcorns(skip: int = 0, limit: int = 10):
    logger.info("Rota para leitura de todos os itens")
    return {"details": "popcorns"}
# @router.get("/popcorns/", response_model=List[schemas.popcorn])
# def read_popcorns(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
#     logger.info("Rota para leitura de todos os itens")
#     popcorns = crud.get_popcorns(db, skip=skip, limit=limit)
#     return popcorns
# @router.get("/popcorns/{popcorn_id}", response_model=schemas.popcorn)
# def read_popcorn(popcorn_id: int, db: Session = Depends(get_db)):
#     logger.info("Rota para leitura de um popcorn específico")
#     db_popcorn = crud.get_popcorn(db, popcorn_id=popcorn_id)
#     if db_popcorn is None:
#         raise HTTPException(status_code=404, detail="popcorn not found")
#     return db_popcorn

# @router.put("/popcorns/{popcorn_id}", response_model=schemas.popcorn)
# def update_popcorn(popcorn_id: int, popcorn: schemas.popcornCreate, db: Session = Depends(get_db)):
#     logger.info("Rota para atualização de um popcorn")
#     db_popcorn = crud.update_popcorn(db, popcorn_id=popcorn_id, updated_popcorn=popcorn)
#     if db_popcorn is None:
#         raise HTTPException(status_code=404, detail="popcorn not found")
#     return db_popcorn

# @router.delete("/popcorns/{popcorn_id}")
# def delete_popcorn(popcorn_id: int, db: Session = Depends(get_db)):
#     logger.info("Rota para exclusão de um popcorn")
#     db_popcorn = crud.delete_popcorn(db, popcorn_id=popcorn_id)
#     if db_popcorn is None:
#         raise HTTPException(status_code=404, detail="popcorn not found")
#     return {"detail": "popcorn deleted"}
