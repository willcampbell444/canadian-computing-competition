#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct Bunny {
	Bunny(int x, int y, int good): x(x), y(y), good(good) {}
	Bunny() {}
	float x, y, good, angle;
};

vector<Bunny> buns;

bool leftComp(Bunny a, Bunny b) {
	return (a.x < b.x) || (a.x == b.x && a.y < b.y);
}
bool angleComp(int a, int b) {
	return (buns[a].angle < buns[b].angle) || (buns[a].angle == buns[b].angle && leftComp(buns[a], buns[b]));
}

int main() {
	int num_bunnies;
	cin >> num_bunnies;
	float total = 0;
	buns.resize(num_bunnies);
	for (int i = 0; i < num_bunnies; i++) {
		cin >> buns[i].x >> buns[i].y >> buns[i].good;
		total += buns[i].good;
	}
	sort(buns.begin(), buns.end(), leftComp);

	int left = 0;
	int maxScore = -99999;
	for (int pivot = 0; pivot < num_bunnies; pivot++) {
		vector<int> byAngle;
		int vertCurrent = buns[pivot].good;
		vector<int> current;
		for (int i = 0; i < num_bunnies; i++) {
			if (buns[i].x != buns[pivot].x) {
				byAngle.push_back(i);
				buns[i].angle = (buns[i].y - buns[pivot].y)/(buns[i].x - buns[pivot].x);
			} else if (i != pivot) {
				vertCurrent += buns[i].good;
				current.push_back(i);
			}
		}
		sort(byAngle.begin(), byAngle.end(), angleComp);

		if (left + vertCurrent > maxScore) {
			maxScore = left + vertCurrent;
		}
		if (total - left > maxScore) {
			maxScore = total - left;
		}

		int sideOne = left;

		for (int x: current) {
			if (leftComp(buns[x], buns[pivot])) {
				sideOne += buns[x].good;
			}
		}

		int currentGood;
		for (int i = 0; i < byAngle.size(); i++) {

			current.clear();
			current.push_back(byAngle[i]);
			currentGood = buns[pivot].good+buns[byAngle[i]].good;
			while (i+1 < byAngle.size() && buns[byAngle[i]].angle == buns[byAngle[i+1]].angle) {
				i++;
				currentGood += buns[byAngle[i]].good;
				current.push_back(byAngle[i]);
			}

			for (int x: current) {
				if (leftComp(buns[x], buns[pivot])) {
					sideOne -= buns[x].good;
				}
			}

			if (sideOne + currentGood > maxScore) {
				maxScore = sideOne + currentGood;
			}
			if (total - sideOne > maxScore) {
				maxScore = total - sideOne;
			}

			for (int x: current) {
				if (!leftComp(buns[x], buns[pivot])) {
					sideOne += buns[x].good;
				}
			}
			
			if (sideOne + buns[pivot].good > maxScore) {
				maxScore = sideOne + buns[pivot].good;
			}
			if (total - sideOne > maxScore) {
				maxScore = total - sideOne;
			}
		}

		if (pivot+1 < num_bunnies && buns[pivot].x != buns[pivot+1].x) {
			left += vertCurrent;
		}
	}
	cout << maxScore << endl;
}