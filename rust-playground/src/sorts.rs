pub fn run() {
    let numbers: Vec<i32> = vec![4, -3, -2, 1, 2, -4, 5, 0, -7, -8, 6, 3, 8, -6, -5, 9, -9, 7, -1];
    println!("{:?}", numbers);
    
    let sorted = count_sort(numbers);
    println!("{:?}", sorted);
}

// really simple sort
fn simple_sort(mut numbers: Vec<i32>) -> Vec<i32> {
    let mut sorted: Vec<i32> = vec![];

    for _ in 0..numbers.len() {

        // find smallest
        let mut index: usize = 0;
        let mut smallest: i32 = numbers[0];
        for (i, &number) in numbers.iter().enumerate() {
            if &number < &smallest {
                index = i;
                smallest = number;
            }
        
        }

        // remove smallest and push it onto sorted
        numbers.remove(index);
        sorted.push(smallest);
    }

    return sorted;
}

// my version of counting sort
fn count_sort(numbers: Vec<i32>) -> Vec<i32> {
    // find range
    let mut smallest: i32 = numbers[0];
    let mut largest: i32 = numbers[0];
    for &number in numbers.iter() {
        if &number > &largest {
            largest = number;
        } else if &number < &smallest {
            smallest = number;
        }
    }
    
    // count which numbers appear
    let size: usize = (largest - smallest + 1) as usize;
    let mut track: Vec<usize> = vec![0;size];
    for &number in numbers.iter() {
        let index: usize = (number - smallest) as usize;
        track[index] += 1;
    }

    // create new list
    let mut sorted: Vec<i32> = vec![];
    for (i, &value) in track.iter().enumerate() {
        // skip zeros
        if value == 0 {
            continue;
        }
        // push the index 
        let number: i32 = i as i32;
        for _ in 0..value {
            sorted.push(number + smallest);
        }
    }

    return sorted;
}
