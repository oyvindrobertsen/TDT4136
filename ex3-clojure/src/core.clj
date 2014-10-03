(ns core
  (require [parse])
  (require [astar])
  (require [graphics])
  (:gen-class))

(defn dijkstra-cost
  [board curr closed]
  (let [g (+ (astar/manhattan-distance (.start board) curr)
             (parse/get-weight board curr)
             (if (nil? (closed curr))
               0
               (second (dijkstra-cost board (closed curr) closed))))
        h 0
        f (+ g  h)]
    [f g h]))

(defn solve
  [board]
  (let [[a-path a-open a-closed] (astar/search board astar/weighted-cost astar/f-h-sort)
        [d-path d-open d-closed] (astar/search board dijkstra-cost astar/f-h-sort)
        [b-path b-open b-closed] (astar/astar-bfs board astar/weighted-cost)]
    (graphics/draw-grid board a-path a-open a-closed "A*")
    (graphics/draw-grid board d-path d-open d-closed "Djikstra")
    (graphics/draw-grid board b-path b-open b-closed "BFS")))

(defn -main
  "Accepts a filename, attempts to parse the file to a search tree and perform A* on it."
  [& args]
  (let [b [;"resources/board-1-1.txt"
           ;"resources/board-1-2.txt"
           "resources/board-1-3.txt"
           ;"resources/board-1-4.txt"
           ;"resources/board-2-1.txt"
           ;"resources/board-2-2.txt"
           ;"resources/board-2-3.txt"
           ;"resources/board-2-4.txt"
           ]]
    (doseq [b b] (solve (parse/parse-board b)))))
