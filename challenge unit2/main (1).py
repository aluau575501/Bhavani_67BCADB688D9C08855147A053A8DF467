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


    