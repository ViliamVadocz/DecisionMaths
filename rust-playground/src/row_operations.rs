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
                panic!("rows don't match");
            }
        }
        Matrix {row, col, mat}
    }
}

// TODO
// Implement augmented matrices
// Implement row operations:
//   Switching rows
//   Multiplying row by non-zero const
//   Adding one row to another

pub fn run() {

    let matrix: Matrix = Matrix::from(
        vec![
            vec![1.0, 0.0, 0.0],
            vec![0.0, 1.0, 0.0],
            vec![0.0, 0.0, 1.0]
        ]
    );

    println!("{:?}", matrix);
}