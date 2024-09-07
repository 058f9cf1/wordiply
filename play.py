import random

with open('words_alpha.txt', 'r') as file:
	words = file.read().splitlines()

long_words = [w for w in words if len(w) > 9]
random_word = long_words[random.randint(0, len(long_words))]
short_word_start = random.randint(0, len(random_word) - 3)
short_word = random_word[short_word_start:short_word_start + 3]
valids = sorted([w for w in words if short_word in w], key=len)

print("Starting word:", short_word)

best = 0
while True:
	guess = input("> ")
	if guess == "quit()":
		break
	elif guess in valids:
		length = len(guess)
		if length > best:
			best = length
		print("\033[A>", guess, "(length:", str(length) + ", best:", str(best) + ")\n", end='')
	else:
		print("\033[A\033[J", end='')

print("Longest 5 words were", valids[-5:], "(longest:", str(len(valids[-1])) + ")")
