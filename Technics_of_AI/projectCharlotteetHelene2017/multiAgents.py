# multiAgents.py
# --------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

from util import manhattanDistance,get_nearest
from game import Directions,Actions
import random, util
from NeuralNet import *
from config import *
from game import Mode

from game import Agent

class ReflexAgent(Agent):
  """
    A reflex agent chooses an action at each choice point by examining
    its alternatives via a state evaluation function.

    The code below is provided as a guide.  You are welcome to change
    it in any way you see fit, so long as you don't touch our method
    headers.
  """


  def getAction(self, gameState):
    """
    You do not need to change this method, but you're welcome to.

    getAction chooses among the best options according to the evaluation function.

    Just like in the previous project, getAction takes a GameState and returns
    some Directions.X for some X in the set {North, South, West, East, Stop}
    """
    # Collect legal moves and successor states
    legalMoves = gameState.getLegalActions()

    # Choose one of the best actions
    scores = [self.evaluationFunction(gameState, action) for action in legalMoves]
    bestScore = max(scores)
    bestIndices = [index for index in range(len(scores)) if scores[index] == bestScore]
    chosenIndex = random.choice(bestIndices) # Pick randomly among the best

    "Add more of your code here if you want to"

    return legalMoves[chosenIndex]

  def evaluationFunction(self, currentGameState, action):
    """
    Design a better evaluation function here.

    The evaluation function takes in the current and proposed successor
    GameStates (pacman.py) and returns a number, where higher numbers are better.

    The code below extracts some useful information from the state, like the
    remaining food (newFood) and Pacman position after moving (newPos).
    newScaredTimes holds the number of moves that each ghost will remain
    scared because of Pacman having eaten a power pellet.

    Print out these variables to see what you're getting, then combine them
    to create a masterful evaluation function.
    """
    # Useful information you can extract from a GameState (pacman.py)
    successorGameState = currentGameState.generatePacmanSuccessor(action, self)
    newPos = successorGameState.getPacmanPosition()
    newFood = successorGameState.getFood()
    newGhostStates = successorGameState.getGhostStates()
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]

    "*** YOUR CODE HERE ***"
    return successorGameState.getScore()

def scoreEvaluationFunction(currentGameState):
  """
    This default evaluation function just returns the score of the state.
    The score is the same one displayed in the Pacman GUI.

    This evaluation function is meant for use with adversarial search agents
    (not reflex agents).
  """
  return currentGameState.getScore()

class MultiAgentSearchAgent(Agent):
  """
    This class provides some common elements to all of your
    multi-agent searchers.  Any methods defined here will be available
    to the MinimaxPacmanAgent, AlphaBetaPacmanAgent & ExpectimaxPacmanAgent.

    You *do not* need to make any changes here, but you can if you want to
    add functionality to all your adversarial search agents.  Please do not
    remove anything, however.

    Note: this is an abstract class: one that should not be instantiated.  It's
    only partially specified, and designed to be extended.  Agent (game.py)
    is another abstract class.
  """

  def __init__(self, evalFn = 'scoreEvaluationFunction', depth = '2'):
    self.index = 0 # Pacman is always agent index 0
    self.evaluationFunction = util.lookup(evalFn, globals())
    self.depth = int(depth)


class AINeuralAgent(Agent):

# Args = ["-l", "mediumClassic", "-p", "AINeuralAgent", "-g", "DirectionalGhost", "-q",
# "-a","dim1=1,dim2=2,dim3=3,dim4=4,neural_file=filename"]
# pour le training de PacMan Decoder
# import pacman
# args_training = readCommand( Args ) # Get game components based on input
# score = runGames( **args_training )

  def __init__(self,neural_file):
    self.index = 0
    self.mode = 0
    #create NeuralNet object
    self.neural = NeuralNet(l_nodes)
    self.neural.load(neural_file)
    

  def getNeural(self):
    #Pour ajouter les poids dans PacMan decoder
    return self.neural

  def getAction(self, gameState):
    """
    You do not need to change this method, but you're welcome to.

    getAction chooses among the best options according to the output of the neural network
    """
    #def food_pos(foodGrid):
      #for x in foodGrid:


    # Collect legal moves and successor states
    legalMoves = gameState.getLegalActions()
    PacState = gameState.getPacmanState()
    position = PacState.getPosition()
    direction = PacState.getDirection()
    GhostStates = gameState.getGhostStates()
    #print("ghost =",GhostStates)
    #print(GhostStates)
    inputs = []
    
    food_list = gameState.getFood().asList()
    capsules_list = gameState.getCapsules()
    #print("capsules =",capsules_list)
    if len(capsules_list) == 0 :
      capsules_list = food_list

    #closest food and energizer
    closest_food = get_nearest(food_list,position)
    #print("closest_food = ",closest_food)
    closest_capsule = get_nearest(capsules_list,position)

    width = gameState.data.layout.width
    height = gameState.data.layout.height
    #print width
    #print height

    distance_food = manhattanDistance(position,closest_food)
    distance_cap = manhattanDistance(position,closest_capsule)


    surface = width*height

    inputs.append(float(distance_food)/surface)
    inputs.append(float(distance_cap)/surface)

    for i in range(len(GhostStates)):
      GhostState = gameState.getGhostState( i+1 )
      mode = GhostState.mode
      pos = gameState.getGhostPosition( i+1 )
      distance = manhattanDistance(position,pos)

      

      inputs.append(float(distance/surface))
      inputs.append(Mode._order[mode]/5.0)

    outputs = self.neural.execute(len(self.neural.layersList)-1,inputs)
    best = direction
    opposite = Actions.reverseDirection(direction)
    fitness = 0.0
    fitness_opp = -1

    #print direction
    #print "len outputs = " + str(len(outputs))
    #print "inputs = " + str(inputs)
    #print( outputs)

    possible_direction = ['North','South','East','West']

    for i in range(len(outputs)):
      other = possible_direction[i]
      LegalMove = other in legalMoves
      #print "other=" + other
      #print "direction=" + direction
      #print str(LegalMove)
      
      if LegalMove and (other != opposite) and (outputs[i] > fitness):
        best = other
        fitness = outputs[i]
      elif other == opposite:
        fitness_opp = outputs[i]

      if (best == direction) and (fitness_opp > fitness) and (direction not in legalMoves) and len(legalMoves) <= 2 and opposite in legalMoves:
        best = opposite

    return best
