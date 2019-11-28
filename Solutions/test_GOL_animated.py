import numpy as np
import GOL_animated

def test_step():
    """
    Testing function for GOL step using 'Toad' from:
    https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life
    """
    
    cells1 = np.array([[0,0,0,0,0,0],
                  [0,0,0,0,0,0],
                  [0,0,1,1,1,0],
                  [0,1,1,1,0,0],
                  [0,0,0,0,0,0],
                  [0,0,0,0,0,0]])
    
    cells2 = np.array([[0,0,0,0,0,0],
                  [0,0,0,1,0,0],
                  [0,1,0,0,1,0],
                  [0,1,0,0,1,0],
                  [0,0,1,0,0,0],
                  [0,0,0,0,0,0]])
    
    test = GOL_animated.step(cells1)
    assert(np.array_equal(test,cells2))