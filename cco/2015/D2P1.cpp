#include <iostream>
#include <vector>

using namespace std;

int n, m;

void clear(vector<vector<char> >& peices, int r, int c) {
	int nextR = r;
	int nextC = c;

	if (peices[nextR][nextC] == 'S') {
		do {
			nextR++;
		} while (nextR < n && peices[nextR][nextC] == '.');
		if (nextR < n) {
			clear(peices, nextR, nextC);
		}
	} else if (peices[nextR][nextC] == 'N') {
		do {
			nextR--;
		} while (nextR >= 0 && peices[nextR][nextC] == '.');
		if (nextR >= 0) {
			clear(peices, nextR, nextC);
		}
	} else if (peices[nextR][nextC] == 'E') {
		do {
			nextC++;
		} while (nextC < m && peices[nextR][nextC] == '.');
		if (nextC < m) {
			clear(peices, nextR, nextC);
		}
	} else if (peices[nextR][nextC] == 'W') {
		do {
			nextC--;
		} while (nextC >= 0 && peices[nextR][nextC] == '.');
		if (nextC >= 0) {
			clear(peices, nextR, nextC);
		}
	}

	peices[r][c] = '.';
	cout << '(' << r << "," << c << ')' << endl;
}

int main() {
	cin >> n >> m;
	vector<vector<char> > peices(n, vector<char>(m));
	for (int r = 0; r < n; r++) {
		for (int c = 0; c < m; c++) {
			cin >> peices[r][c];
		}
	}

	for (int r = 0; r < n; r++) {
		for (int c = 0; c < m; c++) {
			if (peices[r][c] != '.') {
				clear(peices, r, c);
			}
		}
	}
}