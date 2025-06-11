from enum import Enum

class UserType(str, Enum):
    anonymous = "anonymous"
    primary = "primary"

class UserStatus(str, Enum):
    online = "online"
    disabled = "disabled"
    invisible = "invisible"

class RelationshipLevel(int, Enum):
    stranger = 0
    acquaintance = 1
    familiar = 2
    trust = 3