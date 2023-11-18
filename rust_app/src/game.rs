use rand::Rng;
use crate::user_input;

pub fn new_game(min_val: u32, max_val: u32){
    let target: u32 = rand::thread_rng().gen_range(min_val..=max_val);

    loop {
        let guess: u32 = user_input::read_uint(&format!("Enter number from {min_val} and {max_val}"));

        if guess == target {
            println!("Congrats. You won");
            return
        } else if guess > target {
            println!("Less")
        } else {
            println!("More")
        }
    }
}