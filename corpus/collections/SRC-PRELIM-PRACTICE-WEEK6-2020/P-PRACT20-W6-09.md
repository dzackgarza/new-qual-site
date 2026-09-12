---
schema: qual/card@1
id: P-PRACT20-W6-09
kind: problem
title: "Week 6: Miscellaneous Topics, problem 9"
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Let $\alpha \neq K \subseteq \mathbb { R } ^ { n }$ . Which of the following statements are true?

(A) If K is compact, then every continuous real-valued function on K is bounded.

(B) If every continuous real-valued function on K is bounded, then K is compact.

(C) If K is compact, then K is connected.
:::

::: {.solution}
(A) is true; indeed, defining $U _ { n } = f ^ { - 1 } ( [ - n , n ] )$ for $n \in \mathbb { N } .$ , we see that $U _ { n }$ forms an open cover of K. By compactness there is a finite subcover and since the sets $U _ { n }$ are nested, we will have $K \subset U _ { N }$ for some $N \in \mathbb { N } .$ . But then $| f ( x ) | \leq N$ for all $x \in K$

(B) is true.
We prove this by contrapositive.
If K is not compact, then it is either not closed or not bounded (by the Heine-Borel theorem).
If K is not closed, then there is $x _ { 0 } \in \mathbb { R } ^ { n }$ such that $x _ { 0 } \notin K$ but $x _ { 0 }$ is a limit point of K. Then putting $\begin{array} { r } { f ( x ) = \frac { 1 } { \left\| x - x _ { 0 } \right\| } } \end{array}$ gives a function which is continuous and unbounded on K. If K is unbounded, then $f ( x ) = \| { \dot { x } } \|$ is continuous and unbounded on K. Contrapositively, if every continuous function on K is bounded, then K is compact.

(C) is false.
The set $K = [ - 2 , - 1 ] ^ { n } \cup [ 1 , 2 ] ^ { n }$ is compact but not connected.
:::
