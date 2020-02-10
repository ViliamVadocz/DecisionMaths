use std::fmt;

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
        for row in self.mat.iter() {
            write!(f, "|");
            for &element in row.iter() {
                write!(f, " {}", element);
            }
            write!(f, " |\n");
        }
        write!(f, "")
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
            return
        }
        let mut temp: f32;
        for i in 0..self.col {
            temp = self.mat[row_a][i];
            self.mat[row_a][i] = self.mat[row_b][i];
            self.mat[row_b][i] = temp;
        }
    }
}

impl fmt::Display for AugmentedMatrix {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        for row in self.mat.iter() {
            write!(f, "|");
            for (i, &element) in row.iter().enumerate() {
                if i == self.div_col {
                    write!(f, " :");
                }
                write!(f, " {}", element);
            }
            write!(f, " |\n");
        }
        write!(f, "")
    }
}

pub fn run() {
    let matrix: Matrix = Matrix::from(
        vec![
            vec![2.0, 3.0, 1.0],
            vec![3.0, 1.0, 2.0],
            vec![1.0, 2.0, 3.0]
        ]
    );

    let identity_3: Matrix = Matrix::identity(3);

    println!("{}", matrix);
    println!("{}", identity_3);

    let mut augmented = matrix.augment_with(identity_3);
    println!("{}", augmented);

    augmented.row_add(0, 1);
    println!("{}", augmented);

    augmented.row_switch(0, 1);
    println!("{}", augmented);

    augmented.row_mult(2, 3.0);
    println!("{}", augmented);
}