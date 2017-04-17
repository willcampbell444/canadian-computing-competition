#include <iostream>

int count(int* populations, int min, int max) {
	int sum = 0;
	if (max - min > 5000) {
		#pragma omp parallel for reduction (+:sum)
		for (int i = min; i < max; i++) {
			sum += populations[i];
		}
	} else {
		for (int i = min; i < max; i++) {
			sum += populations[i];
		}
	}
	return sum;
}

int main() {
	int num_stations, num_lines, num_actions;
	std::cin >> num_stations >> num_lines >> num_actions;

	int first[num_lines];
	int prevs[num_lines];
	int next[num_stations];

	for (int i = 0; i < num_lines; i++) {
		first[i] = -1;
	}

	int line, tmp;
	for (int station = 0; station < num_stations; station++) {
		std::cin >> line;
		line--;

		if (first[line] == -1) {
			first[line] = station;
			prevs[line] = station;
			next[station] = -1;
		} else {
			next[prevs[line]] = station;
			prevs[line] = station;
			next[station] = -1;
		}
	}

	int populations[num_stations];
	for (int i = 0; i < num_stations; i++) {
		std::cin >> populations[i];
	}

	int mode;
	for (int i = 0; i < num_actions; i++) {
		std::cin >> mode;
		if (mode == 1) {
			int min, max;
			std::cin >> min >> max;
			std::cout << count(populations, min-1, max) << "\n";
		} else {
			int line, current, previous_population, tmp;
			std::cin >> line;
			line--;
			current = first[line];
			previous_population = populations[current];
			while (next[current] != -1) {
				current = next[current];
				tmp = populations[current];
				populations[current] = previous_population;
				previous_population = tmp;
			}
			populations[first[line]] = previous_population;
		}
	}
}