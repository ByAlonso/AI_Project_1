COLORS = {'red': color(255,0,0), 'blue': color(0,0,255), 'green': color(0,255,0), 'yellow': color(255,255,0)}

def is_integer(a, rel_tol=1e-9, abs_tol=0.0):
    b = round(a)
    return abs(a - b) <= rel_tol #max(rel_tol * max(abs(a), abs(b)), abs_tol)


class Robot:
    def __init__(self,x_pos, y_pos, w, clr):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.w = w
        self.name = clr
        self.clr = color(COLORS[clr])
        
        # Animation
        self.i = x_pos
        self.j = y_pos
    
    def move_robot(self, grid, dir, step=1):
        if dir == 'right':
            move = step if (grid[self.y_pos][self.x_pos].has_right_wall) == False else 0
            self.i += move
        elif dir == 'left':
            move = step if (grid[self.y_pos][self.x_pos].has_left_wall) == False else 0
            self.i -= move
        elif dir == 'up':
            move = step if (grid[self.y_pos][self.x_pos].has_up_wall) == False else 0
            self.j -= move
        elif dir == 'down':
            move = step if (grid[self.y_pos][self.x_pos].has_down_wall) == False else 0
            self.j += move
        
        
        # print(self.y_pos, self.j, is_integer(self.j))
        self.x_pos = int(round(self.i)) if is_integer(self.i) else self.x_pos
        self.y_pos = int(round(self.j)) if is_integer(self.j) else self.y_pos
        
        if move == 0:
            return False
        else:
            return True        
            
    def print_robot(self):
        w = self.w
        x = self.i * w + w/2
        y = self.j * w + w/2
        
        fill(self.clr)
        noStroke()
        ellipse(x, y, w/2.8, w/1.2)
        ellipse(x, y+w/10, w/2, w/2)
        ellipse(x, y+w/3, w/2.5, w/5)
    
        stroke(153)
        fill(255)    
    