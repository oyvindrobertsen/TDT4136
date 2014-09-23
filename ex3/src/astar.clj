(ns astar)

(defn manhattan-distance 
  "Calculates the manhattan distance between two points on a 2D grid"
  [[x1 y1] [x2 y2]]
  (+ (Math/abs (- x1 x2)) (Math/abs (- y1 y2))))
