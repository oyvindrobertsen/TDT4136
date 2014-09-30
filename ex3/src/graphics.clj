(ns graphics
  (require [parse])
  (:require [quil.core :as q]))

(defn draw-tile[b x y]
  (case b
    \r (q/fill 255 0 0)
    \g (q/fill 0 255 0)
    \b (q/fill 0 0 255)
    0  (q/fill 255 255 255)
    1  (q/fill 191 127 63)
    5  (q/fill 127 255 127)
    10 (q/fill 0 127 0)
    50 (q/fill 165 165 165)
    100 (q/fill 76 76 255)
    (q/fill 0 0 0))

  (q/rect x y 20 20))

(defn draw-dot[x y]
  (q/fill 0 0 0)
  (q/ellipse x y 5 5))

(defn enumerate[idx itm]
  [idx itm])

(defn draw [grid path]
  (q/smooth)
  (q/background 0)

  (let [s (.start grid)
        e (.end grid)]
    (doseq [row (map-indexed enumerate (.costs grid))]
      (doseq [tile (map-indexed enumerate (second row))]
        (let [y (first row)
              x (first tile)
              b (second tile)
              c (if (= [x y] s) \r (if (= [x y] e) \g b))]
              (draw-tile c (* 20 x) (* 20 y))
              (if (some #{[x y]} path) (draw-dot (+ 10 (* 20 x)) (+ 10 (* 20 y)))))))))

(defn draw-grid[grid]
  (let [d (parse/dimensions grid)
        x (first d)
        y (second d)
        h (* 20 x)
        w (* 20 y)
        path [[0 0] [1 1]]
        ]
    (q/sketch
      :title "grid"
      :setup (partial draw grid path)
      :size [h w])))
