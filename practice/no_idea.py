from collections import Counter
def happiness(arr, a, b):
	happy_score = 0
	count_arr = Counter(arr)
	set_array = set(arr)
	intrs_a = set_array.intersection(a)
	intrs_b = set_array.intersection(b)
	for e in intrs_a:
		happy_score += count_arr[e]
	for e in intrs_b:
		happy_score -= count_arr[e]
	return happy_score


if __name__=='__main__':
	n, m = map(int, input().split())
	arr = list(map(int, input().split()))
	a = set(map(int, input().split()))
	b = set(map(int, input().split()))
	print(happiness(arr, a, b))
