#[derive(Debug)]
struct Matrix {
    row: usize,
    col: usize,
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

    fn augment_with(self, mat: Matrix) -> Matrix {
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

        Matrix {
            row: self.row,
            col,
            mat: new_mat
        }
    }

    fn identity(size: usize) -> Matrix {
        let mut mat: Vec<Vec<f32>> = vec![];
        for i in 0..size {
            let mut row: Vec<f32> = vec![0.0; size];
            row[i] = 1.0;
            mat.push(row);
        }

        Matrix {
            row: size,
            col: size,
            mat,
        }
    }
}

// TODO
// Implement augmented matrices
// Implement row operations:
//   Switching rows
//   Multiplying row by non-zero const
//   Adding one row to another

pub fn run() {

    let I3: Matrix = Matrix::identity(3);

    let matrix: Matrix = Matrix::from(
        vec![
            vec![2.0, 3.0, 1.0],
            vec![3.0, 1.0, 2.0],
            vec![1.0, 2.0, 3.0]
        ]
    );

    let augmented = matrix.augment_with(I3);

    println!("{:?}", augmented);
}