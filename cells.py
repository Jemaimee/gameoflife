
class Game():
    def __init__(self):
        self.alive_cells = {(8.0, 8.0), (8.0, 7.0), (6.0, 7.0), (7.0, 6.0), (8.0, 6.0)}

    def add_cell(self, coordinate:tuple):
        self.alive_cells.add(coordinate)
        
    def remove_cell(self, coordinate:tuple):
        self.alive_cells.discard(coordinate)
    
    def get_neighbors(self, x, y):
        neighobrs = list()
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                neighobrs.append(((x + dx), (y + dy)))
        return neighobrs
    
    def get_cells_to_check(self):
        cells = self.alive_cells.copy()
        cells_to_check = set()
        for cell in cells:
            cells_to_check.add(cell)
            cells_to_check.update(self.get_neighbors(*cell))
        return cells_to_check
        

    def count_alive_neighbors(self, neighbors):
        alive_neighbors = 0
        for cell in neighbors:
            if cell in self.alive_cells:
                alive_neighbors += 1
        return alive_neighbors 

    def should_survive(self, x, y, neighbors):
        alive_neighbors = self.count_alive_neighbors(neighbors)
        if not 2 <= alive_neighbors <= 3:
            self.remove_cell((x, y))

    def get_next_state(self):
        cells_to_check = self.get_cells_to_check()

        next_generation = set()

        for cell in cells_to_check:
            neighors = self.get_neighbors(*cell)
            alive_count = self.count_alive_neighbors(neighors)

            is_alive = cell in self.alive_cells

            if is_alive and alive_count in [2, 3]:
                next_generation.add(cell)
            elif not is_alive and alive_count == 3:
                next_generation.add(cell)

        self.alive_cells = next_generation

