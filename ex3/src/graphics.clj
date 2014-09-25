(ns graphics
  (require [parse])
  (:require [quil.core :as q]))

(defn draw-tile[b x y]
  (case b
    1 (q/fill 0 0 0)
    (q/fill 255 255 255)
    )

  (q/rect x y 20 20))

(defn enumerate[idx itm]
  [idx itm])

(defn draw [grid]
  (q/smooth)
  (q/background 0)

  (doseq [row (map-indexed enumerate (.data grid))]
    (doseq [tile (map-indexed enumerate (second row))]
      (let [y (first row)
            x (first tile)
            b (second tile)]
            (draw-tile b (* 20 x) (* 20 y))
        ))))

(defn draw-grid[grid]
  (let [d (parse/dimensions grid)
        x (first d)
        y (second d)
        h (* 20 x)
        w (* 20 y)]
    (q/sketch
      :title "grid"
      :setup (partial draw grid)
      :size [h w])))
