#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>
#include <cmath>

using namespace std;

struct Point {
	Point() {}
	Point(int x, int y): x(x), y(y) {}
	int x, y;
};

bool xComp(Point a, Point b) {
	return (a.x < b.x) || (a.x == b.x && a.y < b.y);
}
bool yComp(Point a, Point b) {
	return (a.y < b.y) || (a.y == b.y && a.x < b.x);
}

int main() {
	int w, h, num_zomb;
	cin >> h >> w >> num_zomb;

	vector<Point> zombies(num_zomb);

	for (int i = 0; i < num_zomb; i++) {
		cin >> zombies[i].y >> zombies[i].x;
	}

	int target;
	cin >> target;

	vector<Point> vBars;
	vector<Point> hBars;
	for (Point zomb: zombies) {
		if (zomb.x - target >= 1) {
			vBars.emplace_back(zomb.x - target, zomb.y);
		}
		if (zomb.x + target <= w) {
			vBars.emplace_back(zomb.x + target, zomb.y);
		}
		if (zomb.y - target >= 1) {
			hBars.emplace_back(zomb.x, zomb.y - target);
		}
		if (zomb.y + target <= h) {
			hBars.emplace_back(zomb.x, zomb.y + target);
		}
	}

	sort(vBars.begin(), vBars.end(), xComp);
	sort(hBars.begin(), hBars.end(), yComp);

	long long total = 0;

	sort(zombies.begin(), zombies.end(), xComp);
	int zombPosLeft = 0;
	int zombPosRight = 0;
	for (int i = 0; i < vBars.size();) {
		int x = vBars[i].x;

		while (zombPosLeft < zombPosRight && abs(zombies[zombPosLeft].x - vBars[i].x) >= target) {
			zombPosLeft++;
		}
		while (zombPosRight < num_zomb && abs(zombies[zombPosRight].x - vBars[i].x) < target) {
			zombPosRight++;
		}

		vector<Point> events;
		for (int z = zombPosLeft; z < zombPosRight; z++) {
			int dist = abs(zombies[z].x - vBars[i].x);
			events.emplace_back(min(zombies[z].y+dist+1, h+1),  1);
			events.emplace_back(max(zombies[z].y-dist,   1), -1);
		}
		cout << "X: " << x << ", " << i << ", ";
		while (i < vBars.size() && vBars[i].x == x) {
			events.emplace_back(min(vBars[i].y+target+1, h+1), -420);
			events.emplace_back(max(vBars[i].y-target,   1),  420);
			i++;
		}
		cout << i << "  " << zombPosRight - zombPosLeft << "\t --- ";
		sort(events.begin(), events.end(), xComp);

		int isCounting = 0;
		int counter = 0;
		int prevX = 1;
		for (Point event: events) {
			if (isCounting > 0 && counter == 0) {
				total += event.x - prevX;
			}
			if (event.y == 420) {
				isCounting++;
			} else if (event.y == -420) {
				isCounting--;
			} else {
				counter += event.y;
			}
			prevX = event.x;
		}
		cout << total << endl;
	}
	cout << total << endl;

	sort(zombies.begin(), zombies.end(), yComp);
	zombPosLeft = 0;
	zombPosRight = 0;
	for (int i = 0; i < hBars.size();) {
		int y = hBars[i].y;

		while (zombPosLeft < zombPosRight && abs(zombies[zombPosLeft].y - hBars[i].y) > target) {
			zombPosLeft++;
		}
		while (zombPosRight < num_zomb && abs(zombies[zombPosRight].y - hBars[i].y) <= target) {
			zombPosRight++;
		}

		vector<Point> events;
		for (int z = zombPosLeft; z < zombPosRight; z++) {
			int dist = abs(zombies[z].y - hBars[i].y);
			if (dist < target) {
				events.emplace_back(min(zombies[z].x+dist+1, h+1),  1);
				events.emplace_back(max(zombies[z].x-dist,   1), -1);
			} 
			if (zombies[z].x+target <= h) {
				events.emplace_back(zombies[z].x+target+1,  1);
				events.emplace_back(zombies[z].x+target, -1);
			}
			if (zombies[z].x-target >= 1) {
				events.emplace_back(zombies[z].x-target+1,  1);
				events.emplace_back(zombies[z].x-target, -1);
			}
		}
		while (i < hBars.size() && hBars[i].y == y) {
			events.emplace_back(min(hBars[i].x+target,   h+1), -420);
			events.emplace_back(max(hBars[i].x-target+1, 1),  420);
			i++;
		}
		sort(events.begin(), events.end(), xComp);

		int isCounting = 0;
		int counter = 0;
		int prevX = 1;
		for (Point event: events) {
			if (isCounting > 0 && counter == 0) {
				total += event.x - prevX;
			}
			if (event.y == 420) {
				isCounting++;
			} else if (event.y == -420) {
				isCounting--;
			} else {
				counter += event.y;
			}
			prevX = event.x;
		}
	}



	cout << total << endl;
}