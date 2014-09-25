(ns parse
  (:require [clojure.string :refer :all]))

(defrecord Board [start end data])

(defn get-lines
  "Returns a vector of lines in text file at path."
  [path]
  (split-lines (slurp path)))

(defn bin-trans
  "Mapping function, input format -> binary representation"
  [chr]
  (case chr
    \# 1
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

(defn bin-parse
  "Slurps the given file and parses it to a board object with info of start/end
  coordinates and the board represented as a 2D vector. Assumes a non-weighted
  board."
  [path]
  (let [grid (get-lines path)]
    (Board. (find-start grid) (find-end grid) (map 
                                                (fn [string] (map bin-trans string))
                                                grid))))

(defn dimensions
  "Given a Board record, returns a [width height] vector"
  [board]
  (let [data (.data board)
        y (count data)
        x (count (get data 0))]
        [x y]))
