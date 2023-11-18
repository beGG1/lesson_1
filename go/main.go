package main

import "fmt"

func printMenu() {
	fmt.Println("1. Play game")
	fmt.Println("2. Binary search")
	fmt.Println("0. Exit")
}

func binarySearch(min_val int, max_val int, target int) {
	number_iterations := 0
	for {
		guess := (max_val-min_val)/2 + min_val
		number_iterations++
		fmt.Printf("min=%d, max=%d, guess=%d\n", min_val, max_val, guess)

		if guess == target {
			fmt.Printf("Search finished with %d iterations\n", number_iterations)
			_, _ = fmt.Scan()
			return
		} else if guess < target {
			min_val = guess + 1
		} else {
			max_val = guess - 1
		}
	}
}

func main() {
	for {
		printMenu()
		key := ReadInt()
		switch key {
		case 1:
			NewGame()
		case 2:
			target := ReadInt()
			binarySearch(0, 100, target)
		case 0:
			return
		default:
			continue
		}
	}
}
