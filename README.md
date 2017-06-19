## Grail The Card Game

### Concepts
THis project is an attempt to create a digital version of one of my favorite card games called "The legend of the Grail". Also would be a great learning experience writing a game ground up with python. 

### The Game
Basically it's a PvP card game with two teams combatting each other. The very innovative part of this game is that it invented a new philoshpy that incoprates the idea of hand management with the ideology of a team game so seamlessly.

[Rules and Intro (In Chinese, would follow up with translation when I have the time)](http://baike.baidu.com/item/星杯传说)

### Architecture
As the full game is really complicated, the following breakdown is based on a simplified version.

#### Basic Cards

There are a total of 150 cards for the core gameplay, can be generally classified into 2 categories:

- Attack

  There are 6 different kinds of attacks:

  - Wind
  - Water
  - Fire
  - Earth
  - Thunder
  - Darkness (Special)

- Magic

  There 5 kinds of magic cards:

  - Poison
  - Invincible
  - Exhaust
  - Shield
  - boom

So a pesudo class of a basic card type would be something like follows:

```java
public class Cards {
  public int cardID 
  public String cardType //Type of the card Magic
  public String elementType //which element the card is
}

public class AttackCards extends Cards {
  private final int damage = 2
  public ArrayList<String> exSpell //2 special spells associated with this card
}

public class MagicCards extends Cards {
  public String magicType //Type of magic
}
```

#### Team

The team class is a model class that contains critical info of a team:

- teamColor
- teamMorale (HP)
- teamGemPool
- teamGrails

#### Player

The player class is a model class that contains critical info of a player

#### Round

#### GameController

