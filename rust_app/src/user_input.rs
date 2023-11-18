use std::io;

pub fn read_uint(prompt: &str) -> u32 {
    println!("{}", prompt);

    loop {
        let mut var = String::new();
        io::stdin()
            .read_line(&mut var)
            .expect("Failed to read line");
        
        let var: u32 = match var.trim().parse(){
            Ok(num) => num,
            Err(_) => continue,
        };
        return var
    };
}
