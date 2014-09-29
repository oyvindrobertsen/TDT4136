(ns astar)

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
  passed"
  [grid width height closed [x y]]
  (for [tx (range (- x 1) (+ x 2))
        ty (range (- y 1) (+ y 2))
        :when (and (>= tx 0)
                   (>= ty 0)
                   (<= tx width)
                   (<= tx height)
                   (not= [x y] [tx ty])
                   (not= (nth (nth grid ty) tx) 1)
                   (not (contains? closed [tx ty])))]
    [tx ty]))

(defn search
  ""
  []
  '_)
