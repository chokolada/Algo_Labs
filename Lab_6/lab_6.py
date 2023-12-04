class FiniteStateMachine:
    def __init__(self, pattern):
        self.pattern = pattern
        self.states = {f"state {i}" for i in range(len(pattern))}
        self.transitions = self.initialize_transitions()

    def initialize_transitions(self):
        transitions = {}
        first_symbol = self.pattern[0]

        for i in range(len(self.pattern)):
            current_state = "state " + str(i)
            next_state = "state " + str(i + 1)

            transitions[current_state] = {self.pattern[i]: next_state}

            if first_symbol is not None and first_symbol is not self.pattern[i]:
                transitions[current_state][first_symbol] = "state " + str(i)
                first_symbol = None

        transitions["state" + str(len(self.pattern))] = {}
        return transitions

    def process_input(self, input_string):
        all_needle_starts = []
        starting_state = "state 0"
        current_state = starting_state

        for symbol_index, symbol in enumerate(input_string):
            try:
                current_state = self.transitions[current_state][symbol]
            except KeyError:
                try:
                    current_state = self.transitions[starting_state][symbol]
                except KeyError:
                    current_state = starting_state

            if current_state == f"state {len(self.states)}":
                current_state = starting_state
                all_needle_starts.append(symbol_index - len(self.states) + 1)

        return all_needle_starts


if __name__ == "__main__":
    haystack = "ababcdeabcabcabc"
    needle = "abc"

    fsm = FiniteStateMachine(needle)

    print(fsm.transitions)

    result = fsm.process_input(haystack)
    print(result)
