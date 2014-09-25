(ns graphics
  (require [parse])
  (:require [quil.core :as q]))

(defn draw-tile[b x y]
  (case b
    0 (q/fill 0 0 0)
    (q/fill 255 255 255)
    )

  (q/rect x y 20 20))

(defn draw [grid]
  (q/smooth)
  (q/background 0)
  (draw-tile 1 0 0)
  (draw-tile 1 20 20)
)

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
