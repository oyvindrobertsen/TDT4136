(ns parse-test
  (:require [clojure.test :refer :all]
            [parse :refer :all]))

(deftest parse-text-file-from-resources-test
  (testing "that parse-board can read and properly parse from resources"
    (is (= #parse.Board{
                        :start [3 1],
                        :end [1 2],
                        :weights ((-1 -1 -1 -1 -1 -1 -1)
                                  (-1  0  0  0  0  0 -1)
                                  (-1  0  0  0  0  0 -1)
                                  (-1 -1 -1 -1 -1 -1 -1))}
           (parse-board "resources/test-board.txt")))))

(deftest int-trans-test
  (testing ""
    (is (= 100 (int-trans \w)))
    (is (=  50 (int-trans \m)))
    (is (=  10 (int-trans \f)))
    (is (=   5 (int-trans \g)))
    (is (=   1 (int-trans \r)))
    (is (=   0 (int-trans \A)))
    (is (=   0 (int-trans \B)))
    (is (=  -1 (int-trans \#)))))


(deftest find-character-test
  (testing "that find-character returns a [x y] pair for the given grid and
           characters"
    (is (= [1 1] (find-character [
                                "###"
                                "#A#"
                                "###"
                                ] \A)))))

(deftest dimensions-test
  (testing "the reported dimensions of a board"
    (is (= [3 3] (dimensions (->Board [0 0] [0 0] [[0 0 0]
                                                   [1 1 1]
                                                   [0 0 0]]))))
    (is (= [7 4] (dimensions (parse-board "resources/test-board.txt"))))))
