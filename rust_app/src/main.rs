mod game;
mod user_input;

fn print_menu() {
    print!("1. New game\n");
    print!("2. Binary search\n");
    print!("0. Exit\n");
}

fn binary_search(mut min_val: u32, mut max_val: u32, target: u32){
    let mut num_iter: u32 = 0;
    loop {
        let guess: u32 = (max_val - min_val) / 2 + min_val;
        num_iter += 1;
        print!("min={}, max={}, guess={}\n", min_val, max_val, guess);

        if guess == target {
            print!("Congrats! You won))\n"); 
            print!("Number of iterations {num_iter}\n");
            return;
        } else if guess > target {
            max_val = guess - 1
        } else {
            min_val = guess + 1
        };
    };
}

fn main() {
    loop {
        print_menu();

        let key: u32 = user_input::read_uint("Enter number from 0 to 2: ");
        match key{
            1 => game::new_game(0, 100),
            2 => {
                let target: u32 = user_input::read_uint("Enter nubber from 0 to 100");
                binary_search(0, 100, target);
            },
            0 => return,
            _ => continue
        }
    }
}
