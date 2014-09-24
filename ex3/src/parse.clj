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
  '_)

(defn find-character
  "Finds the first occurence of given character in a grid, returns x y"
  [grid chr]
  '_)

(defn find-start
  "Given an untranslated board grid, returns the coords of the starting point."
  [grid]
  (find-character grid "A"))

(defn find-end
  "Given an untranslated board grid, returns the coords of the ending point."
  [grid]
  (find-character grid "B"))

(defn bin-parse
  "Slurps the given file and parses it to a board object with info of start/end
  coordinates and the board represented as a 2D vector. Assumes a non-weighted
  board."
  [path]
  (let [grid (get-lines path)]
    (Board. (find-start grid) (find-end grid) (map bin-trans grid))))
