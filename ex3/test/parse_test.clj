(ns parse-test
  (:require [clojure.test :refer :all]
            [parse :refer :all]))

(deftest bin-parse-text-file-from-resources-test
  (testing "that bin-parse can read and properly parse from resources"
    (is (= 1 (bin-parse "resources/board-1-1.txt")))))
