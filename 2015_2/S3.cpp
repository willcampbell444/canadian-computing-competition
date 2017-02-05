#include <iostream>

int main() {
	int G, P;
	std::cin >> G;
	std::cin >> P;

	bool gates[G];

	for (int i = 0; i < G; i++) {
		gates[i] = false;
	}
	
	int loaded = 0;

	for (int p = 0; p < P; p++) {
		int plane;
		std::cin >> plane;
		plane -= 1;

		while (plane > -1 && gates[plane]) {
			plane -= 1;
		}

		if (plane > -1) {
			gates[plane] = true;
			loaded += 1;
		} else {
			break;
		}
	}

	std::cout << loaded << std::endl;
}