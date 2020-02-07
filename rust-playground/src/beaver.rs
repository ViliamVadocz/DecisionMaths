use bit_vec::BitVec;

struct enum Direction {
    Left,
    Right
}

struct Action {
    write: bool,
    motion: Direction,
    next_state: usize
}

struct enum Outcome {
    Do(Action),
    Halt
}

struct State {
    if_zero: Outcome,
    if_one: Outcome
}

struct TuringMachine {
    states = [usize]
    current_state: usize,
    tape: BitVec,
    pointer_pos: usize
}

impl TuringMachine {
    fn execute(&self) {
        
    }

    // TODO
    fn extend_tape(&self, direction: Direction) {
        match direction {
            Direction.Right => self.tape.push(false)
            Direction.Left => {
                self.tape = false + self.tape
                self.pointer_pos += 1
            }
        }
        new_tape = self.tape.
    }
}
    
// TODO Implement Turing Machine
// TODO Example Turing Machine test

// TODO Busy Beaver Problem

pub fn run() {
    let states = [
        State {

        },
        State {

        }
    ]

}