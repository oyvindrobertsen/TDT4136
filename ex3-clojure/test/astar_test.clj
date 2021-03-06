(ns astar-test
  (:require [clojure.test :refer :all]
            [astar :refer :all]
            [parse :refer :all]))

(deftest manhattan-distance-test
  (testing "that manhattan distance calculation works correctly"
    (is (= 4 (manhattan-distance [0 0] [2 2])))))

(deftest manhattan-distance-negative-test
  (testing "that manhattan distance calculation handles negative coords"
    (is (= 4 (manhattan-distance [0 0] [-2 -2])))))

(deftest cost-estimate-test
  (testing "that the cost estimate function correctly calculates the estimate
           for the given state."
    (let [board #parse.Board{
                             :start [0 0]
                             :end [1 1]
                             :weights [[ 0  0 -1]
                                       [-1  0 -1]
                                       [-1 -1 -1]]
                             }]
      (is (= [2 2 0] (cost board [1 1]))))))

(deftest detect-valid-adjacent-nodes-naive-test
  (testing "that the edges function correctly returns all possible moves"
    (is (= [[0 1] [1 0] [1 2] [2 1]] (edges [[0 0 0]
                                             [0 0 0]
                                             [0 0 0]] 3 3 {} [1 1])))))

(deftest detect-valid-adjacent-nodes-test
  (testing "that the edges function works correctly for valid input"
    (is (= [[1 0]] (edges [[ 0  0 -1]
                           [-1  0 -1]
                           [-1 -1 -1]] 3 3 {} [1 1])))))

(deftest edges-doesnt-add-nodes-in-closed-map-test
  (testing "that the edges function does not return nodes that are present in
           the closed map."
    (is (= () (edges [[ 0  0 -1]
                      [-1  0 -1]
                      [-1 -1 -1]] 3 3 (hash-map [1 0] [0 0]) [1 1])))))

(deftest backtracing-path-test
  (testing "that the path backtracing function works correctly."
    (is (= [[0 0] [1 0] [1 1]] (path [1 1] [1 0] (hash-map [1 0] [0 0]))))))

(deftest bin-search-test
  (testing "that the search function correctly finds the shortest path."
    (is (= [[0 0] [1 0] [1 1]] (search #parse.Board{
                                                    :start [0 0]
                                                    :end [1 1]
                                                    :weights [[ 0  0 -1]
                                                              [-1  0 -1]
                                                              [-1 -1 -1]]
                                                    } cost)))))

(deftest bin-search-parse-test
  (testing "that the search function works with a parsed board"
    (is (= [[3 1] [2 1] [2 2] [1 2]] (search (parse-board "resources/test-board.txt") cost)))))

(deftest weighted-search-parse-test
  (testing "that the search function correctly finds the shortest path for
           weighted boards."
    (is (= [] (search (parse-board "resources/board-2-1.txt") weighted-cost)))))
