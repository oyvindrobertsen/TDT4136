(ns astar-test
  (:require [clojure.test :refer :all]
            [astar :refer :all]))

(deftest manhattan-distance-test
  (testing "that manhattan distance calculation works correctly"
    (is (= 4 (manhattan-distance [0 0] [2 2])))))

(deftest manhattan-distance-negative-test
  (testing "that manhattan distance calculation handles negative coords"
    (is (= 4 (manhattan-distance [0 0] [-2 -2])))))
