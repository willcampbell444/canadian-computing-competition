#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int N, water;
	cin >> N >> water;

	vector<int> crackers(N);

	for (int i = 0; i < N; i++) {
		cin >> crackers[i];
	}

	sort(crackers.begin(), crackers.end());

	cout << max(crackers.back(), water) - min(crackers.front(), water) << " ";

	int left = 0;
	int right = crackers.size()-1;
	int prevTemp = water;
	long long taste1 = 0;

	while (right >= left) {
		taste1 += max(abs(prevTemp-crackers[right]), abs(water-crackers[right]));
		prevTemp = crackers[right];
		right--;

		if (right >= left) {
			taste1 += max(abs(prevTemp-crackers[left]), abs(water-crackers[left]));
			prevTemp = crackers[left];
			left++;
		}
	}

	left = 0;
	right = crackers.size()-1;
	prevTemp = water;
	long long taste2 = 0;

	while (right >= left) {
		taste2 += max(abs(prevTemp-crackers[left]), abs(water-crackers[left]));
		prevTemp = crackers[left];
		left++;

		if (right >= left) {
			taste2 += max(abs(prevTemp-crackers[right]), abs(water-crackers[right]));
			prevTemp = crackers[right];
			right--;
		}
	}

	cout << max(taste1, taste2) << endl;
}