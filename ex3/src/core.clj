(ns core
  (require [parse])
  (require [astar])
  (require [graphics])
  (:gen-class))

(defn solve
  [board]
  (let [board (parse/parse-board board)
        path (astar/search board)]
    (graphics/draw-grid board path))
  )

(defn -main
  "Accepts a filename, attempts to parse the file to a search tree and perform A* on it."
  [& args]
  (let [boards ["resources/board-1-1.txt"
               "resources/board-1-2.txt"
               "resources/board-1-3.txt"
               "resources/board-1-4.txt"
               "resources/board-2-1.txt"
               "resources/board-2-2.txt"
               "resources/board-2-3.txt"
               "resources/board-2-4.txt"
               ]]
    (doseq [board boards] (solve board))))
