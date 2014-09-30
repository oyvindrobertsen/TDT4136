(ns core
  (require [parse])
  (require [astar])
  (require [graphics])
  (:gen-class))

(defn -main
  "Accepts a filename, attempts to parse the file to a search tree and perform A* on it."
  [& args]
  (graphics/draw-grid (parse/parse-board "resources/board-2-1.txt")))
