## Grail The Card Game

### Concepts
THis project is an attempt to create a digital version of one of my favorite card games called "The legend of the Grail". Also would be a great learning experience writing a game ground up with python. 

### The Game
Basically it's a PvP card game with two teams combatting each other. The very innovative part of this game is that it invented a new philoshpy that incoprates the idea of hand management with the ideology of a team game so seamlessly.

[Rules and Intro (In Chinese, would follow up with translation when I have the time)](http://baike.baidu.com/item/星杯传说)

I have not settled on what languages to use. Ideally it should be a multiplayer web app. (probably java/python, I am leaning toward python for simplicity and the fact this project should be pretty small)

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

#### Deck

Should be straightforward enough… A working deck and a discard deck should be fine.. Method to implement might be just shuffle the deck. List should be fine.

#### Character

hmm..This is a tough part to design..

#### Team

The team class is a model class that contains critical info of a team:

- teamColor (Red/Blue)
- teamMorale (HP, max: 15 if 6 // 10 if 4)
- teamGemPool (max: 5)
- teamGrails

#### Player

The player class is a model class that contains critical info of a player

- playerName


- a hand of card object (ArrayList?)

- an associated character obj

- an associated team obj

- max # of cards to hold (default: 6)

- position on the table (ArrayList?)

- energyPool (ArrayList?)

- statusZone (Shield, Heal, etc)

- activation mode (on/off)

- Special tokens

  ```java
  if this.char.hasSpecial == true:
  	this.tokens = new ....
  ```

- powerIndicators (灯)

  ```java
  if this.char.hasPower == true:
  	this.powers = new ....
  ```

#### Round

```java
Start:

//start:
	//choose if activate (qidong)
	if activation:
		switch {
          case attack
          case magic
          case special {
            switch special_acts {
              case buy
              case synthesize
              case extractEnergy
            }
          }
		}
	else:
		switch {
          case attack
          case magic
		}
end
```

#### GameController

##### Flow

1. Gen player objs
2. Randonize player teams
3. Randomnize player orders(positions)
4. for each player: show 3 chars to pick and attach char to player
5. for each player: run his round

##### Also needs to handle:

1. Invoke player for actions out of his turns
2. Adjust team obj for `gemPool`, `teamMorale`
3. Adjust player obj for `statusBar`



### Text GUI Design

This is a big headache. Have no idea yet.

Trying to mock the experience one has playing offline. so one should probably cares about and should display the following at each player's round:

1. The table/order, where he is, his teammates/opponents

2. His hand of cards

3. Everyone's `statusBar`, `char`, `energyPool`, `, anySpecial char's `, `indicators/special_tokens`, `# cards on hand`

   Basically a table displaying everyone else's stats

4. How his team is doing, `teamMorale` and `teamGemPool`

5. His available actions (activate, play cards, use skills, and 3 special moves)

