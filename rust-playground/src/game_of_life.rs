use std::fmt;
use std::{thread, time};
use rand::distributions::{Distribution, Uniform};

const SIZE: usize = 32;

struct Field {
    cells: [[bool; SIZE]; SIZE]
}

impl fmt::Display for Field {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        let mut repr = String::new();
        for &row in self.cells.iter() {
            for &cell in row.iter() {
                if cell {
                    repr.push('O')
                    // repr += "\u{25A1}";
                } else {
                    repr.push('.')
                    // repr += "\u{25A0}";
                }
                repr.push(' ')
            }
            repr.push('\n');
        }
        write!(f, "{}", repr)
    }
}

impl Field {
    fn new(num_living: usize) -> Field {
        if num_living > SIZE * SIZE {
            panic!("requested number of cells is more than are on the field")
        }
        let mut cells = [[false; SIZE]; SIZE];
        let mut rng = rand::thread_rng();
        let range = Uniform::from(0..SIZE);
        let mut i = 0;
        while i < num_living {
            let x = range.sample(&mut rng);
            let y = range.sample(&mut rng);
            if !cells[x][y] {
                cells[x][y] = true;
                i += 1;
            }
        }
        Field {
            cells
        }
    }
    
    fn step(&mut self) {
        let mut neighbours = [[0u8; SIZE]; SIZE];
        for i in 0..SIZE {
            for j in 0..SIZE {
                let mut n = 0;
                // above
                if i > 0 {
                    if j > 0 && self.cells[i - 1][j - 1] {
                        n += 1;
                    }
                    if self.cells[i - 1][j] {
                        n += 1;
                    }
                    if j + 1 < SIZE && self.cells[i - 1][j + 1] {
                        n += 1;
                    }
                }
                // sides
                if j > 0 && self.cells[i][j - 1] {
                    n += 1;
                }
                if j + 1 < SIZE && self.cells[i][j + 1] {
                    n += 1;
                }
                // below
                if i + 1 < SIZE {
                    if j > 0 && self.cells[i + 1][j - 1] {
                        n += 1;
                    }
                    if self.cells[i + 1][j] {
                        n += 1;
                    }
                    if j + 1 < SIZE && self.cells[i + 1][j + 1] {
                        n += 1;
                    }
                }
                neighbours[i][j] = n;
            }
        }
        
        for (i, row) in self.cells.iter_mut().enumerate() {
            for (j, cell) in row.iter_mut().enumerate() {
                let n = neighbours[i][j];
                // living
                if *cell {
                    // overpopulation
                    if n > 3 {
                        *cell = false;
                    // not enough support
                    } else if n < 2 {
                        *cell = false;
                    }
                // dead
                } else {
                    // new life
                    if n == 3 {
                        *cell = true;
                    }
                }
                
            }
        }
    }
}

pub fn run() {
    let time_between_steps = time::Duration::from_millis(500);
    let mut field = Field::new(300);
    for _ in 0..100 {
        // clear the terminal
        print!("\x1B[2J\x1B[1;1H");
        // show field
        println!("{}", field);
        // take step
        field.step();
        // wait
        thread::sleep(time_between_steps);
    }
    println!("Done.")
}