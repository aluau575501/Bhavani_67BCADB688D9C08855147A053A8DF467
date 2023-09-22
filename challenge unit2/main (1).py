'''Implement a class called Player that represents a cricket player. The Player class should have a
method called play() which prints "The player is playing cricket. Derive two classes, Batsman and
Bowler, from the Player class. Override the play() method in each derived class to print "The batsman
is batting" and "The bowler is bowling", respectively. Write a program to create objects of both the
Batsman and Bowler classes and call the play() method for each object.'''
#define the basss class player
class player:
  def play(self):
    print("the playeris playing cricket.")
    # define the derived class batsman
class batsman(player):
  def play(self):
    print("the batsman is batting.")
    #define the derived class bowler
class bowler(player):
  def play(self):
    print("the bowler is boeling.")
    #create objects of batsman and bowle classes
Batsman =batsman()
Bowler=bowler()
#call the play()mathod for each object
Batsman.play()
Bowler.play()


    
