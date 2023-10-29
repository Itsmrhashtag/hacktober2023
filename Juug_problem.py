class JugState:
    def __init__(self, jug1, jug2):
        self.jug1 = jug1
        self.jug2 = jug2

    def __str__(self):
        return f'<{self.jug1},{self.jug2}>'

    def __eq__(self, other):
        return self.jug1 == other.jug1 and self.jug2 == other.jug2

    def is_valid(self, max_jug1, max_jug2):
        return 0 <= self.jug1 <= max_jug1 and 0 <= self.jug2 <= max_jug2

    def successors(self, max_jug1, max_jug2):
        successors = []

        # Fill jug1
        successors.append(JugState(max_jug1, self.jug2))

        # Fill jug2
        successors.append(JugState(self.jug1, max_jug2))

        # Empty jug1
        successors.append(JugState(0, self.jug2))

        # Empty jug2
        successors.append(JugState(self.jug1, 0))

        # Pour from jug1 to jug2
        amount_to_pour = min(self.jug1, max_jug2 - self.jug2)
        successors.append(JugState(self.jug1 - amount_to_pour, self.jug2 + amount_to_pour))

        # Pour from jug2 to jug1
        amount_to_pour = min(self.jug2, max_jug1 - self.jug1)
        successors.append(JugState(self.jug1 + amount_to_pour, self.jug2 - amount_to_pour))

        return [state for state in successors if state.is_valid(max_jug1, max_jug2)]

def dfs(jug1_max, jug2_max, initial_state, goal_state):
    open_states = [initial_state]
    closed_states = []

    while open_states:
        current_state = open_states.pop()
        closed_states.append(current_state)

        print("*"*90)
        print(f"Current State: {current_state}")
        
        if current_state == goal_state:
            print("Solution Found:")
            print(" -> ".join(map(str, closed_states)))
            print("\nEnd DFS")
            return

        print("Successors:")
        successors = current_state.successors(jug1_max, jug2_max)

        for successor in successors:
            if successor not in open_states and successor not in closed_states:
                open_states.append(successor)
                print(f"Open State: {successor}")
        print("Closed State:", current_state)

    print("No solution found.")

if __name__ == "__main__":
    jug1_max = 4
    jug2_max = 3
    initial_state = JugState(0, 0)
    goal_state = JugState(0, 2)

    print("Initial State:", initial_state)
    print("Goal State:", goal_state)

    print("Start DFS:")
    dfs(jug1_max, jug2_max, initial_state, goal_state)
