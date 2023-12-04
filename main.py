from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel

from dbmodel import Base, Ammo, Armor, AshesOfWar, Boss, Class, Creature, Incantation, Item, Location, NPC, Shield, Sorcery, Spirit, Talisman, Weapon, AmmoCreate, ArmorCreate, AshesOfWarCreate, BossCreate, ClassCreate, CreatureCreate, IncantationCreate, ItemCreate, LocationCreate, NPCCreate, ShieldCreate, SorceryCreate, SpiritCreate, TalismanCreate, WeaponCreate, AmmoRead, ArmorRead, AshesOfWarRead, BossRead, ClassRead, CreatureRead, IncantationRead, ItemRead, LocationRead, NPCRead, ShieldRead, SorceryRead, SpiritRead, TalismanRead, WeaponRead

app = FastAPI()

app.add_middleware(
	CORSMiddleware,
	allow_origins=["*"], # set to * here to allow all origins because Blazor does not have a set origin port for all users. 
						 # Ideally, you would set this to the port that Blazor is running on (e.g. http://localhost:7134 for me)
	allow_credentials=True,
	allow_methods=["*"],
	allow_headers=["*"],
)

SQLALCHEMY_DATABASE_URL = "sqlite:///./eldenring.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_all_items(db: Session, model):
    return db.query(model).all()

def get_item_by_id(db: Session, model, item_id: int):
    return db.query(model).filter(model.id == item_id).first()

def create_item(db: Session, model, item_create):
    db_item = model(**item_create.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

def update_item(db: Session, model, item_id: int, item_update):
    db_item = db.query(model).filter(model.id == item_id).first()
    if db_item:
        for key, value in item_update.dict().items():
            setattr(db_item, key, value)
        db.commit()
        db.refresh(db_item)
    return db_item

def delete_item(db: Session, model, item_id: int):
    db_item = db.query(model).filter(model.id == item_id).first()
    if db_item:
        db.delete(db_item)
        db.commit()
    return db_item

# Ammo routes
@app.get("/ammo")
async def get_ammo(db: Session = Depends(get_db)):
    return get_all_items(db, Ammo)

@app.get("/ammo/{id}")
async def get_ammo_by_id(id: int, db: Session = Depends(get_db)):
    return get_item_by_id(db, Ammo, id)

@app.post("/ammo")
async def create_ammo(ammo: AmmoCreate, db: Session = Depends(get_db)):
    return create_item(db, Ammo, ammo)

@app.put("/ammo/{id}")
async def update_ammo(id: int, ammo: AmmoCreate, db: Session = Depends(get_db)):
    return update_item(db, Ammo, id, ammo)

@app.delete("/ammo/{id}")
async def delete_ammo(id: int, db: Session = Depends(get_db)):
    return delete_item(db, Ammo, id)

# Armor routes
@app.get("/armor")
async def get_armor(db: Session = Depends(get_db)):
    return get_all_items(db, Armor)

@app.get("/armor/{id}")
async def get_armor_by_id(id: int, db: Session = Depends(get_db)):
    return get_item_by_id(db, Armor, id)

@app.post("/armor")
async def create_armor(armor: ArmorCreate, db: Session = Depends(get_db)):
    return create_item(db, Armor, armor)

@app.put("/armor/{id}")
async def update_armor(id: int, armor: ArmorCreate, db: Session = Depends(get_db)):
    return update_item(db, Armor, id, armor)

@app.delete("/armor/{id}")
async def delete_armor(id: int, db: Session = Depends(get_db)):
    return delete_item(db, Armor, id)

# Ashes of War routes
@app.get("/ashesofwar")
async def get_ashesofwar(db: Session = Depends(get_db)):
    return get_all_items(db, AshesOfWar)

@app.get("/ashesofwar/{id}")
async def get_ashesofwar_by_id(id: int, db: Session = Depends(get_db)):
    return get_item_by_id(db, AshesOfWar, id)

@app.post("/ashesofwar")
async def create_ashesofwar(ashesofwar: AshesOfWarCreate, db: Session = Depends(get_db)):
    return create_item(db, AshesOfWar, ashesofwar)

@app.put("/ashesofwar/{id}")
async def update_ashesofwar(id: int, ashesofwar: AshesOfWarCreate, db: Session = Depends(get_db)):
    return update_item(db, AshesOfWar, id, ashesofwar)

@app.delete("/ashesofwar/{id}")
async def delete_ashesofwar(id: int, db: Session = Depends(get_db)):
    return delete_item(db, AshesOfWar, id)

# Boss routes
@app.get("/boss")
async def get_boss(db: Session = Depends(get_db)):
    return get_all_items(db, Boss)

@app.get("/boss/{id}")
async def get_boss_by_id(id: int, db: Session = Depends(get_db)):
    return get_item_by_id(db, Boss, id)

@app.post("/boss")
async def create_boss(boss: BossCreate, db: Session = Depends(get_db)):
    return create_item(db, Boss, boss)

@app.put("/boss/{id}")
async def update_boss(id: int, boss: BossCreate, db: Session = Depends(get_db)):
    return update_item(db, Boss, id, boss)

@app.delete("/boss/{id}")
async def delete_boss(id: int, db: Session = Depends(get_db)):
    return delete_item(db, Boss, id)

# Elden Ring Class routes
@app.get("/eldenringclass")
async def get_eldenringclass(db: Session = Depends(get_db)):
    return get_all_items(db, Class)

@app.get("/eldenringclass/{id}")
async def get_eldenringclass_by_id(id: int, db: Session = Depends(get_db)):
    return get_item_by_id(db, Class, id)

@app.post("/eldenringclass")
async def create_eldenringclass(eldenringclass: ClassCreate, db: Session = Depends(get_db)):
    return create_item(db, Class, eldenringclass)

@app.put("/eldenringclass/{id}")
async def update_eldenringclass(id: int, eldenringclass: ClassCreate, db: Session = Depends(get_db)):
    return update_item(db, Class, id, eldenringclass)

@app.delete("/eldenringclass/{id}")
async def delete_eldenringclass(id: int, db: Session = Depends(get_db)):
    return delete_item(db, Class, id)

# Creature routes
@app.get("/creature")
async def get_creature(db: Session = Depends(get_db)):
    return get_all_items(db, Creature)

@app.get("/creature/{id}")
async def get_creature_by_id(id: int, db: Session = Depends(get_db)):
    return get_item_by_id(db, Creature, id)

@app.post("/creature")
async def create_creature(creature: CreatureCreate, db: Session = Depends(get_db)):
    return create_item(db, Creature, creature)

@app.put("/creature/{id}")
async def update_creature(id: int, creature: CreatureCreate, db: Session = Depends(get_db)):
    return update_item(db, Creature, id, creature)

@app.delete("/creature/{id}")
async def delete_creature(id: int, db: Session = Depends(get_db)):
    return delete_item(db, Creature, id)

# Incantation routes
@app.get("/incantation")
async def get_incantation(db: Session = Depends(get_db)):
    return get_all_items(db, Incantation)

@app.get("/incantation/{id}")
async def get_incantation_by_id(id: int, db: Session = Depends(get_db)):
    return get_item_by_id(db, Incantation, id)

@app.post("/incantation")
async def create_incantation(incantation: IncantationCreate, db: Session = Depends(get_db)):
    return create_item(db, Incantation, incantation)

@app.put("/incantation/{id}")
async def update_incantation(id: int, incantation: IncantationCreate, db: Session = Depends(get_db)):
    return update_item(db, Incantation, id, incantation)

@app.delete("/incantation/{id}")
async def delete_incantation(id: int, db: Session = Depends(get_db)):
    return delete_item(db, Incantation, id)

# Elden Ring Item routes
@app.get("/eldenringitem")
async def get_eldenringitem(db: Session = Depends(get_db)):
    return get_all_items(db, Item)

@app.get("/eldenringitem/{id}")
async def get_eldenringitem_by_id(id: int, db: Session = Depends(get_db)):
    return get_item_by_id(db, Item, id)

@app.post("/eldenringitem")
async def create_eldenringitem(eldenringitem: ItemCreate, db: Session = Depends(get_db)):
    return create_item(db, Item, eldenringitem)

@app.put("/eldenringitem/{id}")
async def update_eldenringitem(id: int, eldenringitem: ItemCreate, db: Session = Depends(get_db)):
    return update_item(db, Item, id, eldenringitem)

@app.delete("/eldenringitem/{id}")
async def delete_eldenringitem(id: int, db: Session = Depends(get_db)):
    return delete_item(db, Item, id)

# Elden Ring Location routes
@app.get("/eldenringlocation")
async def get_eldenringlocation(db: Session = Depends(get_db)):
    return get_all_items(db, Location)

@app.get("/eldenringlocation/{id}")
async def get_eldenringlocation_by_id(id: int, db: Session = Depends(get_db)):
    return get_item_by_id(db, Location, id)

@app.post("/eldenringlocation")
async def create_eldenringlocation(eldenringlocation: LocationCreate, db: Session = Depends(get_db)):
    return create_item(db, Location, eldenringlocation)

@app.put("/eldenringlocation/{id}")
async def update_eldenringlocation(id: int, eldenringlocation: LocationCreate, db: Session = Depends(get_db)):
    return update_item(db, Location, id, eldenringlocation)

@app.delete("/eldenringlocation/{id}")
async def delete_eldenringlocation(id: int, db: Session = Depends(get_db)):
    return delete_item(db, Location, id)

# NPC routes
@app.get("/npc")
async def get_npc(db: Session = Depends(get_db)):
    return get_all_items(db, NPC)

@app.get("/npc/{id}")
async def get_npc_by_id(id: int, db: Session = Depends(get_db)):
    return get_item_by_id(db, NPC, id)

@app.post("/npc")
async def create_npc(npc: NPCCreate, db: Session = Depends(get_db)):
    return create_item(db, NPC, npc)

@app.put("/npc/{id}")
async def update_npc(id: int, npc: NPCCreate, db: Session = Depends(get_db)):
    return update_item(db, NPC, id, npc)

@app.delete("/npc/{id}")
async def delete_npc(id: int, db: Session = Depends(get_db)):
    return delete_item(db, NPC, id)

# Shield routes
@app.get("/shield")
async def get_shield(db: Session = Depends(get_db)):
    return get_all_items(db, Shield)

@app.get("/shield/{id}")
async def get_shield_by_id(id: int, db: Session = Depends(get_db)):
    return get_item_by_id(db, Shield, id)

@app.post("/shield")
async def create_shield(shield: ShieldCreate, db: Session = Depends(get_db)):
    return create_item(db, Shield, shield)

@app.put("/shield/{id}")
async def update_shield(id: int, shield: ShieldCreate, db: Session = Depends(get_db)):
    return update_item(db, Shield, id, shield)

@app.delete("/shield/{id}")
async def delete_shield(id: int, db: Session = Depends(get_db)):
    return delete_item(db, Shield, id)

# Sorcery routes
@app.get("/sorcery")
async def get_sorcery(db: Session = Depends(get_db)):
    return get_all_items(db, Sorcery)

@app.get("/sorcery/{id}")
async def get_sorcery_by_id(id: int, db: Session = Depends(get_db)):
    return get_item_by_id(db, Sorcery, id)

@app.post("/sorcery")
async def create_sorcery(sorcery: SorceryCreate, db: Session = Depends(get_db)):
    return create_item(db, Sorcery, sorcery)

@app.put("/sorcery/{id}")
async def update_sorcery(id: int, sorcery: SorceryCreate, db: Session = Depends(get_db)):
    return update_item(db, Sorcery, id, sorcery)

@app.delete("/sorcery/{id}")
async def delete_sorcery(id: int, db: Session = Depends(get_db)):
    return delete_item(db, Sorcery, id)

# Spirit routes
@app.get("/spirit")
async def get_spirit(db: Session = Depends(get_db)):
    return get_all_items(db, Spirit)

@app.get("/spirit/{id}")
async def get_spirit_by_id(id: int, db: Session = Depends(get_db)):
    return get_item_by_id(db, Spirit, id)

@app.post("/spirit")
async def create_spirit(spirit: SpiritCreate, db: Session = Depends(get_db)):
    return create_item(db, Spirit, spirit)

@app.put("/spirit/{id}")
async def update_spirit(id: int, spirit: SpiritCreate, db: Session = Depends(get_db)):
    return update_item(db, Spirit, id, spirit)

@app.delete("/spirit/{id}")
async def delete_spirit(id: int, db: Session = Depends(get_db)):
    return delete_item(db, Spirit, id)

# Talisman routes
@app.get("/talisman")
async def get_talisman(db: Session = Depends(get_db)):
    return get_all_items(db, Talisman)

@app.get("/talisman/{id}")
async def get_talisman_by_id(id: int, db: Session = Depends(get_db)):
    return get_item_by_id(db, Talisman, id)

@app.post("/talisman")
async def create_talisman(talisman: TalismanCreate, db: Session = Depends(get_db)):
    return create_item(db, Talisman, talisman)

@app.put("/talisman/{id}")
async def update_talisman(id: int, talisman: TalismanCreate, db: Session = Depends(get_db)):
    return update_item(db, Talisman, id, talisman)

@app.delete("/talisman/{id}")
async def delete_talisman(id: int, db: Session = Depends(get_db)):
    return delete_item(db, Talisman, id)

# Weapon routes
@app.get("/weapon")
async def get_weapon(db: Session = Depends(get_db)):
    return get_all_items(db, Weapon)

@app.get("/weapon/{id}")
async def get_weapon_by_id(id: int, db: Session = Depends(get_db)):
    return get_item_by_id(db, Weapon, id)

@app.post("/weapon")
async def create_weapon(weapon: WeaponCreate, db: Session = Depends(get_db)):
    return create_item(db, Weapon, weapon)

@app.put("/weapon/{id}")
async def update_weapon(id: int, weapon: WeaponCreate, db: Session = Depends(get_db)):
    return update_item(db, Weapon, id, weapon)

@app.delete("/weapon/{id}")
async def delete_weapon(id: int, db: Session = Depends(get_db)):
    return delete_item(db, Weapon, id)