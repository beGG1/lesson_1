package main

import "fmt"

func ReadInt() int {
	var i int
	for {
		fmt.Println("Enter an integer number")
		_, err := fmt.Scanf("%d", &i)

		if err == nil {
			return i
		}
	}
}
