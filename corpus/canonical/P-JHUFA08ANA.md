---
schema: qual/card@1
id: P-JHUFA08ANA
kind: problem
title: "1) (15 points) Consider the mapping given by Let be the inverse image of j iterates of F applied to a measurable subset"
classification:
  areas:
  - real-analysis
  topics:
  - real-analysis-topics
solved: false
relations: []
---

1) (15 points) Consider the mapping $F : [ 0 , 1 ]  [ 0 , 1 ]$ given by $F ( s ) = s ^ { 2 }$

Let $F ^ { - j } ( A )$ be the inverse image of j iterates of F applied to a measurable subset $A \subset [ 0 , 1 ]$ . That is, if $F = F ^ { 1 }$ and $F ^ { j } , j = 2 , 3 , . .$ . is defined inductively as $F ^ { j } = F ^ { j - 1 } \circ F$ ， then $F ^ { - j } ( A ) = \{ x : F ^ { j } x = y$ , some $y \in A \}$

a) Given $N = 1 , 2 , \dots$ show that $\begin{array} { r } { \mu _ { N } ( A ) = N ^ { - 1 } \sum _ { j < N } | F ^ { - j } ( A ) | } \end{array}$ is a measure which is absolutely continuous with respect to Lebesgue measure. Here |B| denotes the Lebesgue measure of a measurable set.

b) Show that $\mu _ { N } ( [ a , b ] ) \to 0 { \mathrm { ~ i f ~ } } 0 < a < b \leq 1$

c) If f is a continuous function on [0, 1] does lim $\begin{array} { r } { \int _ { [ 0 , 1 ] } f ( s ) d \mu _ { N } ( s ) } \end{array}$ tend to a limit? If so, what is the limit?
