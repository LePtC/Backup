#include <iostream>
#include <vector>

std::vector<std::vector<int>> get_row_or_col(const std::vector<std::vector<int>> &array) {
    if (array.empty()) {
        return array;
    }
    int m = array.size();
    int n = array[0].size();
    for (int i = 1; i < m; ++i) {
        for (int j = 0; j < n; ++j) {
            if (array[i][j] != array[0][j]) {
                break;
            }
            if (j == n - 1) {
                return std::vector<std::vector<int>>{array[0]};
            }
        }
    }
    for (int j = 0; j < n; ++j) {
        for (int i = 1; i < m; ++i) {
            if (array[i][j] != array[0][j]) {
                break;
            }
            if (i == m - 1) {
                std::vector<std::vector<int>> result(m, std::vector<int>(1, array[0][j]));
                return result;
            }
        }
    }
    return array;
}

int main() {
    std::vector<std::vector<int>> array = {{1, 2, 3}, {1, 2, 3}, {1, 2, 3}};
    std::vector<std::vector<int>> result = get_row_or_col(array);
    for (const auto &row : result) {
        for (const auto &val : row) {
            std::cout << val << " ";
        }
        std::cout << std::endl;
    }
    return 0;
}
