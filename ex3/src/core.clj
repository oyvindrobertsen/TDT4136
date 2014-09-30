(ns core
  (require [parse])
  (require [astar])
  (require [graphics])
  (:gen-class))

(defn -main
  "Accepts a filename, attempts to parse the file to a search tree and perform A* on it."
  [& args]
  (let [board (parse/parse-board (str "resources/board-1-4.txt"))
        path (astar/search board)]
    (graphics/draw-grid board path)))
