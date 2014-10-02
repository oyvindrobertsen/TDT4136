(ns core
  (require [parse])
  (require [astar])
  (require [graphics])
  (:gen-class))

(defn solve
  [board]
  (let [astar-path (astar/search board astar/weighted-cost astar/f-h-sort)
        djikstra-path (astar/search board (fn djikstra-cost [board curr closed]
                                            (let [g (+ (astar/manhattan-distance (.start board) curr)
                                                       (parse/get-weight board curr)
                                                       (if (nil? (closed curr))
                                                         0
                                                         (second (djikstra-cost board (closed curr) closed))))
                                                  h 0
                                                  f (+ g  h)]
                                              [f g h])) astar/f-h-sort)]
    (graphics/draw-grid board astar-path "A*")
    (graphics/draw-grid board djikstra-path "Djikstra")))

(defn -main
  "Accepts a filename, attempts to parse the file to a search tree and perform A* on it."
  [& args]
  (let [b [
           ;["resources/board-1-1.txt" astar/cost]
           ;["resources/board-1-2.txt" astar/cost]
           ;["resources/board-1-3.txt" astar/cost]
           ;["resources/board-1-4.txt" astar/cost]
           ;["resources/board-2-1.txt" astar/weighted-cost]
           "resources/board-2-2.txt"
           ;"resources/board-2-3.txt"
           ;"resources/board-2-4.txt"
           ]]
    (doseq [b b] (solve (parse/parse-board b)))))
