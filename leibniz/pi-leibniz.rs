use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();

    let count: i128 = args[1].trim().parse()
        .expect("Not a number");

    let mut k  = 1.0;
    let mut pi = 0.0;

    println!("Performing {} loops", count);
    for i in 0..count {
        if i % 2 == 0 {
            pi += 4.0 / k;
        } else {
            pi -= 4.0 / k;
        }
        k += 2.0;
        if args.len() >= 3 {
            println!("\x1b[0;37m{}: \x1b[0;32mπ = {} \x1b[0;37m| \x1b[0;36mk = {}", i, pi, k);
        }
    }
    println!("\x1b[1;32mπ = {}", pi);
}
