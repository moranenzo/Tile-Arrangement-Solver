from grid import Grid


class Solver():
    """
    A solver class, to be implemented.
    """
    
    def get_solution(self):
        """
        Solves the grid and returns the sequence of swaps at the format 
        [((i1, j1), (i2, j2)), ((i1', j1'), (i2', j2')), ...]. 
        """
        final_list = []
        ind = 1
        m = self.m
        n = self.n

        while ind <= n*m:
            temp_list = []
            init_pos = self.position(ind)
            final_pos = (ind//n, ind % n - 1)

            sens = 1 - 2*(final_pos[1] <= init_pos[1])  # prend la valeur 1 ou -1, permet de déterminer dans quel sens on fait les échanges
            for j in range(final_pos[1], init_pos[1], sens):
                temp_list.append((init_pos[0], j), (init_pos[0], j+1))

            for i in range(final_pos[0], init_pos[0], -1):  #on tri linéairement donc init_pos[1] est nécessairement plus grand que final_pos[1]
                temp_list.append((i, final_pos[1]), (i+1, final_pos[1]))
      
            self.swap_seq(temp_list)

            final_list += temp_list

            ind += 1
        
        return final_list