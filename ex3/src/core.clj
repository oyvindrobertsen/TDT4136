(ns core
  (require [parse])
  (require [astar])
  (require [graphics])
  (:gen-class))

(defn solve
  [board cost-fn]
  (let [board (parse/parse-board board)
        path (astar/search board cost-fn)]
    (graphics/draw-grid board path))
  )

(defn -main
  "Accepts a filename, attempts to parse the file to a search tree and perform A* on it."
  [& args]
  (let [b-f [["resources/board-1-1.txt" astar/cost]
             ["resources/board-1-2.txt" astar/cost]
             ["resources/board-1-3.txt" astar/cost]
             ["resources/board-1-4.txt" astar/cost]
             ["resources/board-2-1.txt" astar/weighted-cost]
             ["resources/board-2-2.txt" astar/weighted-cost]
             ["resources/board-2-3.txt" astar/weighted-cost]
             ["resources/board-2-4.txt" astar/weighted-cost]]]
    (doseq [[b f] b-f] (solve b f))))
