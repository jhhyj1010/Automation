// test_0813.cpp
#include <vector>
#include <iostream>
#include <cassert>

std::vector<int> order(int cityNodes, std::vector<int>& cityFrom, std::vector<int>& cityTo, int company);

void test_basic_connectivity() {
    int cityNodes = 4;
    std::vector<int> cityFrom = {1, 2, 2};
    std::vector<int> cityTo = {2, 3, 4};
    int company = 1;
    std::vector<int> expected = {2, 3, 4};
    std::vector<int> result = order(cityNodes, cityFrom, cityTo, company);
    assert(result == expected);
}

void test_multiple_distances() {
    int cityNodes = 5;
    std::vector<int> cityFrom = {1, 1, 2, 3, 4};
    std::vector<int> cityTo = {2, 3, 4, 5, 5};
    int company = 1;
    std::vector<int> expected = {2, 3, 4, 5};
    std::vector<int> result = order(cityNodes, cityFrom, cityTo, company);
    assert(result == expected);
}

void test_no_direct_connection() {
    int cityNodes = 4;
    std::vector<int> cityFrom = {1, 2};
    std::vector<int> cityTo = {2, 3};
    int company = 1;
    std::vector<int> expected = {2, 3};
    std::vector<int> result = order(cityNodes, cityFrom, cityTo, company);
    assert(result == expected);
}

void test_large_number_of_cities() {
    int cityNodes = 1000;
    std::vector<int> cityFrom, cityTo;
    for (int i = 1; i < cityNodes; ++i) {
        cityFrom.push_back(i);
        cityTo.push_back(i + 1);
    }
    int company = 1;
    std::vector<int> expected;
    for (int i = 2; i <= cityNodes; ++i) {
        expected.push_back(i);
    }
    std::vector<int> result = order(cityNodes, cityFrom, cityTo, company);
    assert(result == expected);
}

int main() {
    test_basic_connectivity();
    test_multiple_distances();
    test_no_direct_connection();
    test_large_number_of_cities();
    std::cout << "All tests passed!" << std::endl;
    return 0;
}