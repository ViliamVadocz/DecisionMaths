const TAPE_LEN: usize = 20;

#[derive(Clone)]
#[derive(Copy)]
enum Alphabet {
    Zero,
    One,
}

enum Direction {
    Left,
    Right
}

struct Action {
    write: Alphabet,
    motion: Direction,
    next_state: usize
}

impl Action {
    fn new (write: Alphabet, motion: Direction, next_state: usize) -> Action {
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
    if_one: Outcome,
    if_zero: Outcome
}

impl State {
    fn new(if_one: Outcome, if_zero: Outcome) -> State {
        State {
            if_one,
            if_zero
        }
    }
}

struct TuringMachine {
    is_running: bool,
    states: Vec<State>,
    current_state: usize,
    tape: [Alphabet; TAPE_LEN],
    pointer_pos: usize
}

impl TuringMachine {
    fn execute(&mut self) {
        println!("current state: {}", self.current_state);

        // look at tape
        let pointer_value: Alphabet = self.tape[self.pointer_pos];
        match pointer_value {
            Alphabet::One => println!("pointer at index {} reading: 1", self.pointer_pos),
            Alphabet::Zero => println!("pointer at index {} reading: 0", self.pointer_pos)
        }

        // get correct outcome
        let outcome: &Outcome;
        match pointer_value {
            Alphabet::One => outcome = &self.states[self.current_state].if_one,
            Alphabet::Zero => outcome = &self.states[self.current_state].if_zero,
        }

        // see outcome of state
        match outcome {
            Outcome::Halt => self.is_running = false,
            // execute action
            Outcome::Do(action) => {
                // write to tape at pointer_pos
                match action.write {
                    Alphabet::One => println!("writing: 1"),
                    Alphabet::Zero => println!("writing: 0")
                }
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
        for element in self.tape.iter() {
            match element {
                Alphabet::One => tape.push(1),
                Alphabet::Zero => tape.push(0),
            }
        }
        println!{"tape: {:?}", tape};
    }
}

// Brought back Alphabet
// TODO Make it work with more characters than just 0 and 1

// TODO Busy Beaver Problem

pub fn run() {
    type A = Alphabet;
    type D = Direction;

    // print three ones then halt.
    let simple_test_machine: Vec<State> = vec![
        State::new(
            Outcome::Halt,
            Outcome::Do(Action::new(A::One, D::Right, 1))
        ),
        State::new(
            Outcome::Halt,
            Outcome::Do(Action::new(A::One, D::Right, 2))
        ),
        State::new(
            Outcome::Halt,
            Outcome::Do(Action::new(A::One, D::Left, 0))
        )
    ];

    let mut beaver = TuringMachine {
        is_running: true,
        states: simple_test_machine,
        current_state: 0,
        tape: [A::Zero; TAPE_LEN],
        pointer_pos: 0
    };

    while beaver.is_running {
        println!("");
        beaver.print_tape();
        beaver.execute();
    }

    println!("The Turing Machine has halted.");
}