(ns parse-test
  (:require [clojure.test :refer :all]
            [parse :refer :all]))

(deftest bin-parse-text-file-from-resources-test
  (testing "that bin-parse can read and properly parse from resources"
    (is (= #parse.Board{
                        :start [3 1],
                        :end [1 2],
                        :data ((1 1 1 1 1 1 1)
                               (1 0 0 0 0 0 1)
                               (1 0 0 0 0 0 1)
                               (1 1 1 1 1 1 1))}
           (bin-parse "resources/test-board.txt")))))

(deftest bin-trans-dot-test
  (testing "that bin-trans can translate . to 0"
    (is (= 0 (bin-trans \.)))))

(deftest bin-trans-wall-test
  (testing "that bin-trans can translate # to 1"
    (is (= 1 (bin-trans \#)))))

(deftest bin-trans-start-test
  (testing "that bin-trans correctly translates start character as 0"
    (is (= 0 (bin-trans \A)))))

(deftest bin-trans-end-test
  (testing "that bin-trans correctly translates end character as 0"
    (is (= 0 (bin-trans \B)))))


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
    (is (= [7 4] (dimensions (bin-parse "resources/test-board.txt"))))
    ))
