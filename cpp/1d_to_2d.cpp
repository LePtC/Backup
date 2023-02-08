#include <vector>
#include <algorithm>

using namespace std;

vector<vector<int>> fill_square(vector<vector<int>>& arr) {
    int rows = arr.size();
    int cols = arr[0].size();
    int size = max(rows, cols);
    vector<vector<int>> result(size, vector<int>(size, 0));
    if (rows < size) {
        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < size; ++j) {
                result[j][i] = arr[i][0];
            }
        }
    }
    else {
        for (int i = 0; i < size; ++i) {
            for (int j = 0; j < cols; ++j) {
                result[i][j] = arr[0][j];
            }
        }
    }
    return result;
}



int main() {
    vector<vector<int>> arr = {{1, 2, 3}, {4, 5, 6}};
    auto result = fill_square(arr);
    for (const auto& row : result) {
        for (const auto& col : row) {
            cout << col << " ";
        }
        cout << endl;
    }
    return 0;
}

