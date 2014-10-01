(ns parse
  (:require [clojure.string :refer :all]))

(defrecord Board [start end weights])

(defn get-lines
  "Returns a vector of lines in text file at path."
  [path]
  (split-lines (slurp path)))

(defn int-trans
  "Mapping function, input-format -> integer representation"
  [chr]
  (case chr
    \# -1
    \w 100
    \m 50
    \f 10
    \g 5
    \r 1
    0))

(defn find-character
  "Finds the first occurence of given character in a grid, returns x y"
  [grid chr]
  (let [y (.indexOf grid (first (filter (fn [string] (.contains string (str chr))) grid)))
        x (.indexOf (nth grid y) (str chr))]
    (vector x y)))

(defn find-start
  "Given an untranslated board grid, returns the coords of the starting point."
  [grid]
  (find-character grid \A))

(defn find-end
  "Given an untranslated board grid, returns the coords of the ending point."
  [grid]
  (find-character grid \B))

(defn parse-board
  "Slurps the given file and parses it to a board object with info of start/end
  coordinates and the board represented as a 2D vector. Assumes a non-weighted
  board."
  [path]
  (let [grid (get-lines path)]
    (Board.
      (find-start grid) (find-end grid) 
      (into [] (map (fn [string] (into [] (map int-trans string))) grid)))))

(defn dimensions
  "Given a Board record, returns a [width height] vector"
  [board]
  (let [weights (.weights board)
        y (count weights)
        x (count (first weights))]
        [x y]))

(defn get-weight
  [board [x y]]
  (nth (nth (.weights board) y) x))
