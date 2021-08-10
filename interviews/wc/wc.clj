(ns exercises.wc
  (:require [clojure.java.io :as io]
            [clojure.string :as s]))

(defn wc1 [fp]
  ;; read whole file into string at once
  (-> fp
      slurp
      s/lower-case
      (s/split #"_+")
      frequencies))


(defn wc2 [fp]
  ;; iterate line by line
  (with-open [rdr (io/reader fp)]
    (reduce
      (fn [res line]
        (merge-with + res (-> line
                              s/lower-case
                              (s/split #"_+")
                              frequencies)))
      {} (line-seq rdr))))


(def fp "words")
(sort-by val > (wc1 fp))
(wc2 fp)
