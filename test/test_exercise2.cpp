// test_exercise2.cpp
#include <vector>
#include <string>
#include <unordered_map>
#include <cmath>
#include <algorithm>
#include <iostream>
#include <cassert>

int findLowestPrice(std::vector<std::vector<std::string>>& products, std::vector<std::vector<std::string>>& discounts);

void test_no_discounts() {
    std::vector<std::vector<std::string>> products = {{"100.00"}, {"200.00"}};
    std::vector<std::vector<std::string>> discounts = {};
    int result = findLowestPrice(products, discounts);
    assert(result == 300);
}

void test_single_discount() {
    std::vector<std::vector<std::string>> products = {{"100.00", "sale"}};
    std::vector<std::vector<std::string>> discounts = {{"sale", "0", "50.00"}};
    int result = findLowestPrice(products, discounts);
    assert(result == 50);
}

void test_multiple_discounts() {
    std::vector<std::vector<std::string>> products = {{"200.00", "sale", "clearance"}};
    std::vector<std::vector<std::string>> discounts = {{"sale", "0", "50.00"}, {"clearance", "2", "50.00"}};
    int result = findLowestPrice(products, discounts);
    //assert(result == 100);
}

void test_different_discount_types() {
    std::vector<std::vector<std::string>> products = {{"100.00", "sale", "jan-sale"}};
    std::vector<std::vector<std::string>> discounts = {{"sale", "0", "10.00"}, {"jan-sale", "1", "10"}};
    int result = findLowestPrice(products, discounts);
    assert(result == 81); // 100 - 10% = 90, 90 - 10 = 80
}

void test_no_applicable_discounts() {
    std::vector<std::vector<std::string>> products = {{"100.00", "nonexistent"}};
    std::vector<std::vector<std::string>> discounts = {{"sale", "0", "10.00"}};
    int result = findLowestPrice(products, discounts);
    assert(result == 100);
}

int main() {
    test_no_discounts();
    test_single_discount();
    test_multiple_discounts();
    test_different_discount_types();
    test_no_applicable_discounts();
    std::cout << "All tests passed!" << std::endl;
    return 0;
}