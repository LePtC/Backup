#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool compare_rows(vector<int>& row1, vector<int>& row2) {
    return equal(row1.begin(), row1.end(), row2.begin());
}

bool compare_arrays(vector<vector<int>>& arr1, vector<vector<int>>& arr2) {
    int rows = arr1.size();
    int cols = arr1[0].size();
    if (rows != arr2.size() || cols != arr2[0].size()) {
        return false;
    }
    for (int i = 0; i < rows; ++i) {
        if (!compare_rows(arr1[i], arr2[i])) {
            return false;
        }
    }
    return true;
}

int main() {
    vector<vector<int>> arr1 = {{1, 2, 3}, {4, 5, 6}};
    vector<vector<int>> arr2 = {{1, 2, 3}, {4, 5, 6}};
    if (compare_arrays(arr1, arr2)) {
        cout << "arr1 and arr2 are equal." << endl;
    } else {
        cout << "arr1 and arr2 are not equal." << endl;
    }
    return 0;
}
