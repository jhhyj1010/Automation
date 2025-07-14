#include <vector>
#include <iostream>
#include <unordered_map>
//Given an array of integers, its degree is defined as the number of occurrence of the element that occurs most frequently. Given a list of integers, determine two properties of the array: its degree and its length of the shortest sub-array that shares that degree.
using namespace std;
void array_degree(vector<int> &nums) {
    unordered_map<int, int> freq;
    unordered_map<int, int> first;
    unordered_map<int, int> last;
    int degree = 0;
    int length = 0;
    for (int i = 0; i < nums.size(); i++) {
        if (first.find(nums[i]) == first.end()) {
            first[nums[i]] = i;
        }
        last[nums[i]] = i;
        freq[nums[i]]++;
        degree = max(degree, freq[nums[i]]);
    }
    for (auto &p : freq) {
        if (p.second == degree) {
            length = min(length, last[p.first] - first[p.first] + 1);
        }
    }
    cout << "Degree: " << degree << endl;
    cout << "Length: " << length << endl;
}
int main() {
    vector<int> nums = {1,2,1,3,2};//{1, 2, 2, 3, 1, 4, 2};
    array_degree(nums);
    return 0;
}