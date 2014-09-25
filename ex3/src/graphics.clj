(ns graphics
  (:require [quil.core :as q]))

(defn setup []
  (q/smooth)
  (q/frame-rate 10)
  (q/background 0))

(defn r[]
  (q/random 255))

(defn draw[]
  (q/stroke-weight 0)
  (q/fill (r) (r) (r))

  (let [side 20
        x    (q/random (q/width))
        y    (q/random (q/height))]
    (q/rect x y side side)))

(q/defsketch example
  :title "Hello quil"
  :setup setup
  :draw draw
  :size [400 400])
