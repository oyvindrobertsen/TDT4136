(ns core
  (require [parse])
  (require [astar])
  (require [graphics])
  (:gen-class))

(defn solve
  [board cost-fn]
  (let [sorters [[astar/f-h-sort "A*"]
                 [astar/g-sort "Dijkstra"]]
        board (parse/parse-board board)]
   (doseq [[sort-fn title] sorters]
        (let [path (astar/search board cost-fn sort-fn)]
          (graphics/draw-grid board path title)))))

(defn -main
  "Accepts a filename, attempts to parse the file to a search tree and perform A* on it."
  [& args]
  (let [b-f [
             ;["resources/board-1-1.txt" astar/cost]
             ;["resources/board-1-2.txt" astar/cost]
             ;["resources/board-1-3.txt" astar/cost]
             ;["resources/board-1-4.txt" astar/cost]
             ["resources/board-2-1.txt" astar/weighted-cost]
             ["resources/board-2-2.txt" astar/weighted-cost]
             ["resources/board-2-3.txt" astar/weighted-cost]
             ["resources/board-2-4.txt" astar/weighted-cost]
             ]]
    (doseq [[b f] b-f] (solve b f))))
