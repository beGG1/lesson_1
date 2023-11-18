package main

import (
	"fmt"
	"math/rand"
)

func NewGame() {
	target := rand.Intn(101)

	for {
		guess := ReadInt()

		if guess == target {
			fmt.Println("Congrats. You won")
			_, _ = fmt.Scan()
			return
		} else if guess > target {
			fmt.Println("Less")
			continue
		} else {
			fmt.Println("More")
			continue
		}
	}
}
