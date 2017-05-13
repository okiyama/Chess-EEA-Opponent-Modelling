# Chess-EEA-Opponent-Modelling
Modelling opponents in Chess using the Estimation Exploration Algorithm

A rewrite of my [Senior Thesis work](https://github.com/okiyama/EEA-Opponent-Modeling), this time built to model opponents in Chess rather than Konane.

Hopefully the code and results will be better with the knowledge I gained working on my thesis.

The end result is a webpage frontend where users can be presented with a chess puzzle where an EEA backend will learn to model what move they will make and show them the predictions before they make their moves. Before that though, need to make the EEA backend.

The basic idea is to present a real opponent with a chess puzzle and see what move they come up with for it. Given that move, we will evolve a set of models (in our case, represented by chess engines, varying them either by search depth, time to search or an ELO variable if the engine provides it) which come up with that move and all previous moves the player has shown us. Then we find a new puzzle which maximizes the disagreement among the existing models and present that to the real opponent. Rinse and repeat from there. This makes it so that inaccurate models are culled quickly and we get maximum information out of the opponent for each puzzle. 

The entire process is predicated on the assumption that evolving models is cheap and getting moves from an opponent is expensive. This should be true in terms of keeping a user interested in this experiment.


# TODO:  
 * It would be cool and smart if things like number of opponents, time for evolution and what not were in a config file
 * Get random move from random game in RandomTestGetter