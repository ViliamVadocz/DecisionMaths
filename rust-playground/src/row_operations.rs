#[warn(dead_code)]
use std::fmt;

const DECIMAL_POINTS_IN_PRINT: usize = 2;

#[derive(Debug)]
struct Matrix {
    row: usize,
    col: usize,
    mat: Vec<Vec<f32>>
}

#[derive(Debug)]
struct AugmentedMatrix {
    row: usize,
    col: usize,
    div_col: usize, // separator line
    mat: Vec<Vec<f32>>
}

impl Matrix {
    fn from(mat: Vec<Vec<f32>>) -> Matrix {
        let col: usize = mat.len();
        let row: usize = mat[0].len();
        for test_row in mat.iter() {
            if test_row.len() != row {
                panic!("Row lengths don't match.");
            }
        }
        Matrix {row, col, mat}
    }

    // make identity matrix
    fn identity(size: usize) -> Matrix {
        let mut mat: Vec<Vec<f32>> = vec![];
        for i in 0..size {
            // init row as zeros
            let mut row: Vec<f32> = vec![0.0; size];
            // set element on diagonal to one
            row[i] = 1.0;
            mat.push(row);
        }

        Matrix {
            row: size,
            col: size,
            mat,
        }
    }

    fn augment_with(self, mat: Matrix) -> AugmentedMatrix {
        // check that rows match
        if self.row != mat.row {
            panic!("Number of rows doesn't match.");
        }

        let col = self.col + mat.col;
        let mut new_mat: Vec<Vec<f32>> = vec![];

        // for each row
        for i in 0..self.row {
            let mut new_row: Vec<f32> = vec![];
            // push element from self
            for &element in self.mat[i].iter() {
                new_row.push(element);
            }
            // push elements from mat
            for &element in mat.mat[i].iter() {
                new_row.push(element);
            }
            new_mat.push(new_row);
        }

        AugmentedMatrix {
            row: self.row,
            col,
            div_col: self.col,
            mat: new_mat
        }
    }
}

impl fmt::Display for Matrix {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        // get "length" of numbers to figure out adaptive print
        let mut longest = 0;
        for row in self.mat.iter() {
            for &element in row.iter() {
                let mut length = usize::from((element / 10.0).floor()) + DECIMAL_POINTS_IN_PRINT + 1;
                // account for minus sign
                if element < 0.0 {
                    length += 1;
                }
                if length > longest {
                    longest = length;
                }
            }
        }
        // print the matrix.
        let mut output: String = "".to_string();
        for row in self.mat.iter() {
            output += "|";
            for &element in row.iter() {
                let mut length = usize::from((element / 10.0).floor()) + DECIMAL_POINTS_IN_PRINT + 1;
                // account for minus sign.
                if element < 0.0 {
                    length += 1;
                }
                let padding = longest - length;
                output += &format!("{0} {1:.dec$}", String::from(" ").repeat(padding), element, dec=DECIMAL_POINTS_IN_PRINT);
            }
            output += " |\n";
        }
        write!(f, "{}\n", output)
    }
}

impl AugmentedMatrix {
    fn row_add(&mut self, source_row: usize, target_row: usize) {
        for i in 0..self.col {
            self.mat[target_row][i] += self.mat[source_row][i];
        }
    }

    fn row_mult(&mut self, source_row: usize, constant: f32) {
        if constant == 0.0 {
            panic!("Multiplying by zero is not allowed.");
        } 
        for i in 0..self.col {
            self.mat[source_row][i] *= constant;
        }
    }

    // switch elements of two rows
    fn row_switch(&mut self, row_a: usize, row_b: usize) {
        if row_a == row_b {
            // no need to switch
            return;
        }
        let mut temp: f32;
        for i in 0..self.col {
            temp = self.mat[row_a][i];
            self.mat[row_a][i] = self.mat[row_b][i];
            self.mat[row_b][i] = temp;
        }
    }

    fn row_reduce(&mut self) {
        // rearrange rows so zeros are not on diagonal (bad algorithm).
        let mut all_good: bool;
        loop {
            all_good = true;
            for n in 0..self.div_col {
                if self.mat[n][n] == 0.0 {
                    all_good = false;
                    self.row_switch(n, (n+1) % self.row);
                    println!("switch\n{}", self);
                }
            }
            if all_good {
                break;
            }
        }

        // bring nth term to one, and sub from others
        for n in 0..self.div_col {
            let n_term = self.mat[n][n];
            // make n_term be equal to one
            if n_term != 1.0 {
                self.row_mult(n, 1.0 / n_term);
                println!("mult\n{}", self);
            }
            // make every other term in column a zero
            for i in 0..self.row {
                if i == n {
                    continue;
                } else {
                    let n_term_in_i_row = self.mat[i][n];
                    if n_term_in_i_row == 0.0 {
                        continue;
                    }
                    self.row_mult(n, -n_term_in_i_row);
                    self.row_add(n, i);
                    self.row_mult(n, -1.0 / n_term_in_i_row);
                    println!("add\n{}", self); // multiple steps, but it's clear
                }
            }
        }
    }

    fn row_echelon_form(&mut self) -> bool {
        for row in self.mat.iter() {
            match leading_term(row) {
                Some(term) => if term != 1.0 {return false;},
                None => continue
            }
        }
        return true;
    }

    fn reduced_row_echelon_form(&mut self) -> bool {
        if !self.row_echelon_form() {
            return false;
        }

        // get columns with ones in them.
        let mut cols_with_ones: Vec<usize> = vec![];
        for (i, row) in self.mat.iter().enumerate() {
            match leading_term(row) {
                Some(_term) => cols_with_ones.push(i),
                None => continue
            }
        }
        // check every column with a one to make sure it is the only non-zero term.
        for i in cols_with_ones.into_iter() {
            for row in self.mat.iter() {
                let element = row[i];
                if element == 0.0 {
                    continue;
                } else if element != 1.0 {
                    return false;
                }
            }
        }
        return true;
    }

    fn de_augment(self) -> (Matrix, Matrix) {
        let mut mat_a: Vec<Vec<f32>> = vec![];
        let mut mat_b: Vec<Vec<f32>> = vec![];

        for row in self.mat.into_iter() {
            mat_a.push(row[0..self.div_col].to_vec());
            mat_b.push(row[self.div_col..self.col].to_vec());
        }

        return (
            Matrix {
                row: self.row,
                col: self.div_col,
                mat: mat_a
            },
            Matrix {
                row: self.row,
                col: self.col - self.div_col,
                mat: mat_b
            }
        )
    }
}

fn leading_term(row: &Vec<f32>) -> Option<f32> {
    // find first non-zero term.
    for &element in row.iter() {
        if element == 0.0 {
            continue;
        } else {
            return Some(element);
        }
    }
    None
}

impl fmt::Display for AugmentedMatrix {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        // get "length" of numbers to figure out adaptive print
        let mut longest = 0;
        for row in self.mat.iter() {
            for &element in row.iter() {
                let mut length = usize::from((element / 10.0).floor()) + DECIMAL_POINTS_IN_PRINT + 1;
                // account for minus sign
                if element < 0.0 {
                    length += 1;
                }
                if length > longest {
                    longest = length;
                }
            }
        }
        // print the matrix
        let mut output: String = "".to_string();
        for row in self.mat.iter() {
            output += "|";
            for (i, &element) in row.iter().enumerate() {
                // column divider
                if i == self.div_col {
                    output += " :";
                }
                let mut length = usize::from((element / 10.0).floor()) + DECIMAL_POINTS_IN_PRINT + 1;
                // account for minus sign
                if element < 0.0 {
                    length += 1;
                }
                let padding = longest - length;
                output += &format!("{0} {1:.dec$}", String::from(" ").repeat(padding), element, dec=DECIMAL_POINTS_IN_PRINT);
            }
            output += " |\n";
        }
        write!(f, "{}\n", output)
    }
}

pub fn run() {
    let matrix: Matrix = Matrix::from(
        vec![
            vec![-3.0, 5.0, 1.0, 2.0],
            vec![2.0, -1.0, 0.0, 1.0],
            vec![1.0, 6.0, 2.0, -1.0],
            vec![0.0, 2.0, -2.0, 1.0]
        ]
    );

    let identity_4: Matrix = Matrix::identity(4);

    let mut augmented = matrix.augment_with(identity_4);
    println!("{}", augmented);

    augmented.row_reduce();
    let (new_identity, inverse_mat) = augmented.de_augment();

    // println!("{}", new_identity);
    println!("{}", inverse_mat);

    // augmented.row_add(0, 1);
    // println!("{}", augmented);

    // augmented.row_switch(0, 1);
    // println!("{}", augmented);

    // augmented.row_mult(2, 3.0);
    // println!("{}", augmented);
}