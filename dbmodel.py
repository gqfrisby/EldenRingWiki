from sqlalchemy import Column, Integer, String, Numeric
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel

Base = declarative_base()

class Ammo(Base):
    __tablename__ = 'ammos'

    id = Column(String, primary_key=True)
    name = Column(String)
    image = Column(String)
    description = Column(String)
    type = Column(String)
    passive = Column(String)
    #attackPower = Column(String)  # Assuming attackPower is stored as a JSON string

    def __repr__(self):
        return f"<Ammo(id={self.id}, name='{self.name}', image='{self.image}', " \
               f"description='{self.description}', type='{self.type}', " \
               f"passive='{self.passive}')>"
    
class AmmoCreate(BaseModel):
    id: str
    name: str
    image: str
    description: str
    type: str
    passive: str

class AmmoRead(AmmoCreate):
    class Config:
        orm_mode = True
    
class Armor(Base):
    __tablename__ = 'armors'

    id = Column(String, primary_key=True)
    name = Column(String)
    image = Column(String)
    description = Column(String)
    category = Column(String)
    weight = Column(Numeric)
    #dmgNegation = Column(String)  # Assuming dmgNegation is stored as a JSON string
    #resistance = Column(String)  # Assuming resistance is stored as a JSON string

    def __repr__(self):
        return f"<Armor(id={self.id}, name='{self.name}', image='{self.image}', " \
               f"description='{self.description}', category='{self.category}', " \
               f"weight={self.weight})>"
    
class ArmorCreate(BaseModel):
    id: str
    name: str
    image: str
    description: str
    category: str
    weight: float
    #dmgNegation: dict
    #resistance: dict

class ArmorRead(ArmorCreate):
    class Config:
        orm_mode = True

class AshesOfWar(Base):
    __tablename__ = 'ashes_of_war'

    id = Column(String, primary_key=True)
    name = Column(String)
    image = Column(String)
    description = Column(String)
    affinity = Column(String)
    skill = Column(String)

    def __repr__(self):
        return f"<AshesOfWar(id={self.id}, name='{self.name}', image='{self.image}', " \
               f"description='{self.description}', affinity='{self.affinity}', " \
               f"skill='{self.skill}')>"
    
class AshesOfWarCreate(BaseModel):
    id: str
    name: str
    image: str
    description: str
    affinity: str
    skill: str

class AshesOfWarRead(AshesOfWarCreate):
    class Config:
        orm_mode = True
    
class Boss(Base):
    __tablename__ = 'bosses'

    id = Column(String, primary_key=True)
    name = Column(String)
    image = Column(String)
    description = Column(String)
    location = Column(String)
    drops = Column(String)  # Assuming drops is stored as a JSON string or serialized list
    healthPoints = Column(String)

    def __repr__(self):
        return f"<Boss(id={self.id}, name='{self.name}', image='{self.image}', " \
               f"description='{self.description}', location='{self.location}', " \
               f"drops='{self.drops}', healthPoints='{self.healthPoints}')>"
    
class BossCreate(BaseModel):
    id: str
    name: str
    image: str
    description: str
    location: str
    #drops: list
    healthPoints: str

class BossRead(BossCreate):
    class Config:
        orm_mode = True
    
class Class(Base):
    __tablename__ = 'classes'

    id = Column(String, primary_key=True)
    name = Column(String)
    image = Column(String)
    description = Column(String)
    level = Column(String)
    vigor = Column(String)
    mind = Column(String)
    endurance = Column(String)
    strength = Column(String)
    dexterity = Column(String)
    intelligence = Column(String)
    faith = Column(String)
    arcane = Column(String)

    def __repr__(self):
        return f"<Class(id={self.id}, name='{self.name}', image='{self.image}', " \
               f"description='{self.description}', level='{self.level}', " \
               f"vigor='{self.vigor}', mind='{self.mind}', " \
               f"endurance='{self.endurance}', strength='{self.strength}', " \
               f"dexterity='{self.dexterity}', intelligence='{self.intelligence}', " \
               f"faith='{self.faith}', arcane='{self.arcane}')>"
    
class ClassCreate(BaseModel):
    id: str
    name: str
    image: str
    description: str
    level: str
    vigor: str
    mind: str
    endurance: str
    strength: str
    dexterity: str
    intelligence: str
    faith: str
    arcane: str

class ClassRead(ClassCreate):
    class Config:
        orm_mode = True
    
class Creature(Base):
    __tablename__ = 'creatures'

    id = Column(String, primary_key=True)
    name = Column(String)
    image = Column(String)
    description = Column(String)
    location = Column(String)
    # Drops excluded as per the request

    def __repr__(self):
        return f"<Creature(id={self.id}, name='{self.name}', image='{self.image}', " \
               f"description='{self.description}', location='{self.location}')>"
    
class CreatureCreate(BaseModel):
    id: str
    name: str
    image: str
    description: str
    location: str
    #drops: list

class CreatureRead(CreatureCreate):
    class Config:
        orm_mode = True
    
class Incantation(Base):
    __tablename__ = 'incantations'

    id = Column(String, primary_key=True)
    name = Column(String)
    image = Column(String)
    description = Column(String)
    type = Column(String)
    cost = Column(Numeric)
    slots = Column(Numeric)
    effects = Column(String)
    # Requirements excluded as per the request

    def __repr__(self):
        return f"<Incantation(id={self.id}, name='{self.name}', image='{self.image}', " \
               f"description='{self.description}', type='{self.type}', " \
               f"cost={self.cost}, slots={self.slots}, effects='{self.effects}')>"
    
class IncantationCreate(BaseModel):
    id: str
    name: str
    image: str
    description: str
    type: str
    cost: float
    slots: float
    effects: str

class IncantationRead(IncantationCreate):
    class Config:
        orm_mode = True
    
class Item(Base):
    __tablename__ = 'items'

    id = Column(String, primary_key=True)
    name = Column(String)
    image = Column(String)
    description = Column(String)
    type = Column(String)
    effect = Column(String)

    def __repr__(self):
        return f"<Item(id={self.id}, name='{self.name}', image='{self.image}', " \
               f"description='{self.description}', type='{self.type}', " \
               f"effect='{self.effect}')>"
    
class ItemCreate(BaseModel):
    id: str
    name: str
    image: str
    description: str
    type: str
    effect: str

class ItemRead(ItemCreate):
    class Config:
        orm_mode = True

class Location(Base):
    __tablename__ = 'locations'

    id = Column(String, primary_key=True)
    name = Column(String)
    image = Column(String)
    description = Column(String)

    def __repr__(self):
        return f"<Location(id={self.id}, name='{self.name}', image='{self.image}', " \
               f"description='{self.description}')>"
    
class LocationCreate(BaseModel):
    id: str
    name: str
    image: str
    description: str

class LocationRead(LocationCreate):
    class Config:
        orm_mode = True
    
class NPC(Base):
    __tablename__ = 'npcs'

    id = Column(String, primary_key=True)
    name = Column(String)
    image = Column(String)
    description = Column(String)
    location = Column(String)
    quote = Column(String)

    def __repr__(self):
        return f"<NPC(id={self.id}, name='{self.name}', image='{self.image}', " \
               f"description='{self.description}', location='{self.location}', " \
               f"quote='{self.quote}')>"
    
class NPCCreate(BaseModel):
    id: str
    name: str
    image: str
    description: str
    location: str
    quote: str

class NPCRead(NPCCreate):
    class Config:
        orm_mode = True
    
class Shield(Base):
    __tablename__ = 'shields'

    id = Column(String, primary_key=True)
    name = Column(String)
    image = Column(String)
    description = Column(String)
    category = Column(String)
    weight = Column(Numeric)
    #attack = Column(String)  # Assuming attack is stored as a JSON string
    #defence = Column(String)  # Assuming defence is stored as a JSON string
    # The last four attributes (requiredAttributes, scalesWith) have been excluded

    def __repr__(self):
        return f"<Shield(id={self.id}, name='{self.name}', image='{self.image}', " \
               f"description='{self.description}', category='{self.category}', " \
               f"weight={self.weight}, attack='{self.attack}', " \
               f"defence='{self.defence}')>"
    
class ShieldCreate(BaseModel):
    id: str
    name: str
    image: str
    description: str
    category: str
    weight: float
    #attack: dict
    #defence: dict

class ShieldRead(ShieldCreate):
    class Config:
        orm_mode = True
    
class Sorcery(Base):
    __tablename__ = 'sorceries'

    id = Column(String, primary_key=True)
    name = Column(String)
    image = Column(String)
    description = Column(String)
    type = Column(String)
    cost = Column(Numeric)
    slots = Column(Numeric)
    effects = Column(String)
    # 'requires' attribute excluded as per the request

    def __repr__(self):
        return f"<Sorcery(id={self.id}, name='{self.name}', image='{self.image}', " \
               f"description='{self.description}', type='{self.type}', " \
               f"cost={self.cost}, slots={self.slots}, effects='{self.effects}')>"
    
class SorceryCreate(BaseModel):
    id: str
    name: str
    image: str
    description: str
    type: str
    cost: float
    slots: float
    effects: str

class SorceryRead(SorceryCreate):
    class Config:
        orm_mode = True
    
class Spirit(Base):
    __tablename__ = 'spirits'

    id = Column(String, primary_key=True)
    name = Column(String)
    image = Column(String)
    description = Column(String)
    fpCost = Column(Numeric)
    hpCost = Column(Numeric)
    effects = Column(String)

    def __repr__(self):
        return f"<Spirit(id={self.id}, name='{self.name}', image='{self.image}', " \
               f"description='{self.description}', fpCost={self.fpCost}, " \
               f"hpCost={self.hpCost}, effects='{self.effects}')>"
    
class SpiritCreate(BaseModel):
    id: str
    name: str
    image: str
    description: str
    fpCost: float
    hpCost: float
    effects: str

class SpiritRead(SpiritCreate):
    class Config:
        orm_mode = True
    
class Talisman(Base):
    __tablename__ = 'talismans'

    id = Column(String, primary_key=True)
    name = Column(String)
    image = Column(String)
    description = Column(String)
    effects = Column(String)

    def __repr__(self):
        return f"<Talisman(id={self.id}, name='{self.name}', image='{self.image}', " \
               f"description='{self.description}', effects='{self.effects}')>"
    
class TalismanCreate(BaseModel):
    id: str
    name: str
    image: str
    description: str
    effects: str

class TalismanRead(TalismanCreate):
    class Config:
        orm_mode = True
    
class Weapon(Base):
    __tablename__ = 'weapons'

    id = Column(String, primary_key=True)
    name = Column(String)
    image = Column(String)
    description = Column(String)
    category = Column(String)
    weight = Column(Numeric)
    #attack = Column(String)  # Assuming attack is stored as a JSON string
    #defence = Column(String)  # Assuming defence is stored as a JSON string
    #requiredAttributes = Column(String)  # Assuming requiredAttributes is stored as a JSON string
    #scalesWith = Column(String)  # Assuming scalesWith is stored as a JSON string

    def __repr__(self):
        return f"<Weapon(id={self.id}, name='{self.name}', image='{self.image}', " \
               f"description='{self.description}', category='{self.category}', " \
               f"weight={self.weight})>"
    
class WeaponCreate(BaseModel):
    id: str
    name: str
    image: str
    description: str
    category: str
    weight: float
    #attack: dict
    #defence: dict
    #requiredAttributes: dict
    #scalesWith: dict

class WeaponRead(WeaponCreate):
    class Config:
        orm_mode = True
    
