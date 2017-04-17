#include <iostream>
#include <vector>
#include <string>

using namespace std;

int WIDTH;

class Grid {
public:
	Grid() {
		for (int r = 0; r < WIDTH; r++) {
			string x;
			cin >> x;
			for (int c = 0; c < WIDTH; c++) {
				if (x[c] == 'R') {
					rows ^= 1 << c;
					columns ^= 1 << r;
				}
			}
		}
	}

	bool isSimilar(Grid other) {
		return ((rows^other.rows) == 0) && ((columns^other.columns) == 0);
	}

	unsigned short rows = 0;
	unsigned short columns = 0;
};

int main() {
	int num_grids;
	cin >> WIDTH >> num_grids;

	vector<Grid> grids(num_grids);

	int pairs = 0;

	vector<bool> solved(num_grids, false);

	for (int a = 0; a < num_grids; a++) {
		if (!solved[a]) {
			int size = 1;
			for (int b = a+1; b < num_grids; b++) {
				if (!solved[b]) {
					if (grids[a].isSimilar(grids[b])) {
						solved[b] = true;
						size += 1;
					}
				}
			}
			pairs += (size)*(size-1)/2;
		}
	}

	cout << pairs << endl;
}