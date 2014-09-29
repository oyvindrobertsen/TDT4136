(ns astar
  (:require [parse :refer :all]))
(use '[clojure.data.priority-map])

(defn manhattan-distance 
  "Calculates the manhattan distance between two points on a 2D grid"
  [[x1 y1] [x2 y2]]
  (+ (Math/abs (- x2 x1)) (Math/abs (- y2 y1))))


(defn cost
 "Calculates the total estimated cost of a solution path from start through 
 curr to end."
 [curr start end]
  (let [g (manhattan-distance start curr)
        h (manhattan-distance curr end)
        f (+ g h)]
    [f g h]))

(defn edges
  "Returns a list of all , non-closed nodes adjacent to the x, y pair
  passed. Adjacent meaning the four cardinal directions."
  [grid width height closed [x y]]
  (for [tx (range (- x 1) (+ x 2))
        ty (range (- y 1) (+ y 2))
        :when (and (>= tx 0)
                   (>= ty 0)
                   (<= tx width)
                   (<= tx height)
                   (== (manhattan-distance [x y] [tx ty]) 1)
                   (not= [x y] [tx ty])
                   (not= (nth (nth grid ty) tx) 1)
                   (not (contains? closed [tx ty])))]
    [tx ty]))

(defn search
  "Performs the actual search recursively. Has two overloads based on arity.
  The first one is used as the entrypoint to the recursive function. The first
  overload initializes the various data structures needed in the subsequent
  recursive calls."
  ([board]
   (let [open (priority-map-by
                (fn [x y]
                  (if (= x y)
                    0
                    (let [[f1 _ h1] x
                          [f2 _ h2] y]
                      (if (= f1 f2)
                        (if (< h1 h2) -1 1)
                        (if (< f1 f2) -1 1)))))
                (.start board) (cost (.start board) (.start board) (.end board)))
         closed {}
         [width height] (dimensions board)
         [sx sy] (.start board)
         [ex ey] (.end board)]
     ; Verify that start and end coordinates are not unreachable.
     (when (and (not= (nth (nth (.data board) sy) sx) 1)
                (not= (nth (nth (.data board) ey) ex) 1))
       (search board width height open closed))))
  ([x y] 2))
