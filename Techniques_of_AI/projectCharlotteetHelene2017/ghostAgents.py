# ghostAgents.py
# --------------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

from game import Agent
from game import Actions, Mode
from game import Directions
import random
from util import manhattanDistance
import util
from config import *

class GhostAgent( Agent ):
  def __init__( self, index ):
    self.index = index
  

class RandomGhost( GhostAgent ):
  "A ghost that chooses a legal action uniformly at random."
  def getDistribution( self, state ):
    dist = util.Counter()
    for a in state.getLegalActions( self.index ): dist[a] = 1.0
    dist.normalize()
    return dist

class DirectionalGhost( GhostAgent ):
  "A ghost that prefers to rush Pacman, or flee when scared."
  def __init__( self, index, prob_attack=0.8, prob_scaredFlee=0.8 ):
    self.index = index
    self.prob_attack = prob_attack
    self.prob_scaredFlee = prob_scaredFlee
      
  def getDistribution( self, state ):
    # Read variables from state
    ghostState = state.getGhostState( self.index )
    legalActions = state.getLegalActions( self.index )
    pos = state.getGhostPosition( self.index )
    isScared = ghostState.scaredTimer > 0
    
    speed = 1
    if isScared: speed = 0.5
    
    actionVectors = [Actions.directionToVector( a, speed ) for a in legalActions]
    newPositions = [( pos[0]+a[0], pos[1]+a[1] ) for a in actionVectors]
    pacmanPosition = state.getPacmanPosition()

    # Select best actions given the state
    distancesToPacman = [manhattanDistance( pos, pacmanPosition ) for pos in newPositions]
    if isScared:
      bestScore = max( distancesToPacman )
      bestProb = self.prob_scaredFlee
    else:
      bestScore = min( distancesToPacman )
      bestProb = self.prob_attack
    bestActions = [action for action, distance in zip( legalActions, distancesToPacman ) if distance == bestScore]
    
    # Construct distribution
    dist = util.Counter()
    for a in bestActions: dist[a] = bestProb / len(bestActions)
    for a in legalActions: dist[a] += ( 1-bestProb ) / len(legalActions)
    dist.normalize()
    return dist

class FixedGhost(GhostAgent):
  def __init__ (self,index):
    self.mode = Mode.IDLE
    self.index = index
    self.scatter_point = (0,0)
    self.scatterTimer = 0
    self.idleTimer = 0
    self.chaseTimer = 0
    if index == 1: # Blinky
      self.mode = Mode.EXIT

  def initiateTimer(self,state):
    ghostState = state.getGhostState( self.index )
    width = state.data.layout.width
    height = state.data.layout.height
    if self.index == 1:
      ghostState.chaseTimer = 100000
      self.chaseTimer = 100000

    if self.index == 2: # Clyde
      ghostState.idleTimer = 10
      self.idleTimer = 5
      self.scatter_point = (width,height)

    if self.index == 3:
      ghostState.idleTimer = 15
      self.idleTimer = 15
      self.scatter_point = (0,height)

    if self.index == 4:
      ghostState.idleTimer = 20
      self.idleTimer = 20
      self.scatter_point = (width,0)


  def getChaseTarget(self,state):
    PacState = state.getPacmanState()
    pacmanPosition = PacState.getPosition()
    pacmanDirection = PacState.getDirection()
    ghostState = state.getGhostState( self.index )
    position = ghostState.getPosition()
    distance = manhattanDistance(pacmanPosition,position)

    width = state.data.layout.width
    height = state.data.layout.height

    if self.index == 1:
      destination = pacmanPosition
    elif self.index == 2:
      if distance >= 8:
        destination = pacmanPosition
      else:
        destination = self.scatter_point
    elif self.index == 3:
      ghostState_1 = state.getGhostState( 1 )
      pos_1 = ghostState_1.getPosition()
      plusx,plusy = Actions._directions[pacmanDirection]
      dx,dy = pacmanPosition
      pos_2 = (dx + 2*plusx, dy + 2*plusy)
      destination = (pos_1[0] + 2 * (pos_2[0] - pos_1[0]),pos_1[1] - 2* (pos_1[0]-pos_2[1]))
    else:
      plusx,plusy = Actions._directions[pacmanDirection]
      dx,dy = pacmanPosition
      destination = (dx + 4*plusx, dy + 4*plusy)

    return destination


  def getAction(self,state):
    ghostState = state.getGhostState( self.index )
    width = state.data.layout.width
    height = state.data.layout.height
    #print "index = " + str(self.index) + " Mode = " + self.mode
    #print str(ghostState.idleTimer)
    #print str(ghostState.scatterTimer)
    #print self.mode

    self.scatterTimer = max( 0, ghostState.scatterTimer -1)
    self.idleTimer = max(0, ghostState.idleTimer -1)
    self.chaseTimer = max(0, ghostState.chaseTimer -1)

    if self.mode == Mode.CHASE:
      if ghostState.chaseTimer == 0 and self.index !=1:
        self.mode = Mode.SCATTER
        self.scatterTimer = SCATTER_TIME
        return self.getFixedTarget(state,self.scatter_point)
      elif ghostState.getPosition() == START_POSITION:
          self.mode = Mode.EXIT
          return self.getFixedTarget(state,EXIT_POSITION)
      else:
        return self.getFixedTarget(state,self.getChaseTarget(state))

    elif self.mode == Mode.SCATTER:
      if ghostState.scatterTimer == 0:
        self.mode = Mode.CHASE
        self.chaseTimer = CHASE_TIME
        return self.getFixedTarget(state,self.getChaseTarget(state))
      else:
        return self.getFixedTarget(state,self.scatter_point)

    elif ghostState.scaredTimer > 0:
      self.mode = Mode.FRIGHTENED
      return self.getRandomTarget(state)

    elif self.mode == Mode.FRIGHTENED:
      if ghostState.scaredTimer == 0:
        self.mode = Mode.CHASE
        self.chaseTimer = CHASE_TIME
        return self.getFixedTarget(state,self.getChaseTarget(state))
      else:
        return self.getRandomTarget(state)

    elif self.mode == Mode.IDLE:
      if ghostState.idleTimer == 0:
        self.mode = Mode.EXIT
        return self.getFixedTarget(state,EXIT_POSITION)
      else:
        return self.getFixedTarget(state,START_POSITION)

    elif ghostState.getPosition() == START_POSITION and ghostState.idleTimer == 0:
      self.mode = Mode.EXIT
      return self.getFixedTarget(state,EXIT_POSITION)

    elif self.mode == Mode.EXIT:
      if ghostState.getPosition() == EXIT_POSITION:
        self.mode = Mode.CHASE
        self.chaseTimer = CHASE_TIME
        return self.getFixedTarget(state,self.getChaseTarget(state))
      else:
        return self.getFixedTarget(state,EXIT_POSITION)


  def getFixedTarget(self,state,destination):
    ghostState = state.getGhostState( self.index )
    direction = ghostState.getDirection()
    position = ghostState.getPosition()
    dx,dy = position
    legalActions = state.getLegalActions( self.index )

    best = direction
    min_dist = 10000

    for other in legalActions:
      opposite = Actions.reverseDirection(direction)
      plusx,plusy = Actions._directions[other]
      newpos = (dx + plusx,dy + plusy)
      distance = manhattanDistance(newpos,destination)
      if other != opposite and distance < min_dist:
        min_dist = distance
        best = other

    if best not in legalActions:
      best = opposite

    return best

  def getRandomTarget(self,state):
    legalActions = state.getLegalActions( self.index )
    legalActions.sort()
    ghostState = state.getGhostState( self.index )

    pos = state.getGhostPosition( self.index )

    isScared = ghostState.scaredTimer > 0
    
    speed = 1
    if isScared: speed = 0.5
    
    actionVectors = [Actions.directionToVector( a, speed ) for a in legalActions]
    newPositions = [( pos[0]+a[0], pos[1]+a[1] ) for a in actionVectors]
    pacmanPosition = state.getPacmanPosition()

    distancesToPacman = [manhattanDistance( pos, pacmanPosition ) for pos in newPositions]
    bestScore = max( distancesToPacman )
    bestActions = [action for action, distance in zip( legalActions, distancesToPacman ) if distance == bestScore]

    return bestActions[0]

