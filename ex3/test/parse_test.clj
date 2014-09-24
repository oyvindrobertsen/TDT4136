(ns parse-test
  (:require [clojure.test :refer :all]
            [parse :refer :all]))

(deftest bin-parse-text-file-from-resources-test
  (testing "that bin-parse can read and properly parse from resources"
    (is (= 1 (bin-parse "resources/board-1-1.txt")))))

(deftest bin-trans-dot-test
  (testing "that bin-trans can translate . to 0"
    (is (= 0 (bin-trans '.')))))

(deftest bin-trans-wall-test
  (testing "that bin-trans can translate # to 1"
    (is (= 1 (bin-trans '#')))))
