(ns astar-test
  (:require [clojure.test :refer :all]
            [astar :refer :all]))

(deftest manhattan-distance-test
  (testing "that manhattan distance calculation works correctly"
    (is (= 4 (manhattan-distance [0 0] [2 2])))))

(deftest manhattan-distance-negative-test
  (testing "that manhattan distance calculation handles negative coords"
    (is (= 4 (manhattan-distance [0 0] [-2 -2])))))

(deftest cost-estimate-test
  (testing "that the cost estimate function correctly calculates the estimate
           for the given state."
    (is (= [4 2 2] (cost [1 1] [0 0] [2 2])))))

(deftest detect-valid-adjacent-nodes-test
  (testing "that the edges function works correctly for valid input"
    (is (= [[1 0]] (edges [[0 0 1]
                           [1 0 1]
                           [1 1 1]] 3 3 {} [1 1])))))

(deftest edges-doesnt-add-nodes-in-closed-map-test
  (testing "that the edges function does not return nodes that are present in
           the closed map."
    (is (= () (edges [[0 0 1]
                      [1 0 1]
                      [1 1 1]] 3 3 (hash-map [1 0] [0 0]) [1 1])))))