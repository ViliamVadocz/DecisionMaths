const TAPE_LEN: usize = 20;

enum Direction {
    Left,
    Right
}

struct Action {
    write: bool,
    motion: Direction,
    next_state: usize
}

impl Action {
    fn new (write: bool, motion: Direction, next_state: usize) -> Action {
        Action {
            write,
            motion,
            next_state
        }
    }
}

enum Outcome {
    Do(Action),
    Halt
}

struct State {
    if_true: Outcome,
    if_false: Outcome
}

impl State {
    fn new(if_true: Outcome, if_false: Outcome) -> State {
        State {
            if_true,
            if_false
        }
    }
}

struct TuringMachine {
    is_running: bool,
    states: Vec<State>,
    current_state: usize,
    tape: [bool; TAPE_LEN],
    pointer_pos: usize
}

impl TuringMachine {
    fn execute(&mut self) {
        println!("current state: {}", self.current_state);

        // look at tape
        let pointer_value = self.tape.get(self.pointer_pos).unwrap();
        println!("pointer at index {} reading: {}", self.pointer_pos, *pointer_value);

        // get correct outcome
        let outcome: &Outcome;
        if *pointer_value {
            outcome = &self.states.get(self.current_state).unwrap().if_true;
        } else {
            outcome = &self.states.get(self.current_state).unwrap().if_false;
        }

        // see outcome of state
        match outcome {
            Outcome::Halt => self.is_running = false,
            // execute action
            Outcome::Do(action) => {
                // write to tape at pointer_pos
                println!("writing: {}", action.write);
                self.tape[self.pointer_pos] = action.write;
                // move pointer
                match action.motion {
                    Direction::Left => {
                        println!("moving: left");
                        self.pointer_pos -= 1;
                    },
                    Direction::Right => {
                        println!("moving: right");
                        self.pointer_pos += 1;
                    }
                }
                // transition state
                self.current_state = action.next_state;
            }
        }
    }

    fn print_tape(&self) {
        let mut tape: Vec<u8> = vec![];
        for &element in self.tape.iter() {
            if element {
                tape.push(1);
            } else {
                tape.push(0);
            }
        }
        println!{"tape: {:?}", tape};
    }
}

// TODO Implement Turing Machine
// TODO Example Turing Machine test

// TODO Busy Beaver Problem

// TODO Bring back Alphabet
// States should implement a `on(char: Alphabet) -> Outcome`

pub fn run() {
    type D = Direction;

    // print three ones then halt.
    let simple_test_machine = vec![
        State::new(
            Outcome::Halt,
            Outcome::Do(Action::new(true, D::Right, 1))
        ),
        State::new(
            Outcome::Halt,
            Outcome::Do(Action::new(true, D::Right, 2))
        ),
        State::new(
            Outcome::Halt,
            Outcome::Do(Action::new(true, D::Left, 0))
        )
    ];

    let mut beaver = TuringMachine {
        is_running: true,
        states: simple_test_machine,
        current_state: 0,
        tape: [false; TAPE_LEN],
        pointer_pos: 0
    };

    while beaver.is_running {
        println!("");
        beaver.print_tape();
        beaver.execute();
    }

    println!("The Turing Machine has halted.");
}