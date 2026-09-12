---
schema: qual/card@1
id: P-BKS09-9B
kind: problem
title: Berkeley Spring 2009 prelim problem 9B
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---

::: {.problem}
Prove that the sequence of functions $f _ { n } ( x ) = \sin n x$ has no pointwise convergent subsequence. (Hint: show that given any subsequence and any interval of positive length there is a subinterval such that some element of the subsequence is at least $1 / 2$ on this subinterval, and another element is at most $- 1 / 2 . )$ )

Remark. This is an example from Ch. 7 of W. Rudin’s Principles of Mathematical Analysis, which is treated by the author using a result from the more advanced chapter on Lebesgue measure, namely the bounded convergence theorem. According to it, if a sequence of bounded continuous functions $g _ { k } \ ( = ( \sin n _ { k } x - \sin n _ { k + 1 } x ) ^ { 2 }$ in this example) tends to 0 pointwise, then $\textstyle \int g _ { k } ( t ) d t$ tend to 0 too. (In the example, the integral over the period $[ 0 , 2 \pi ]$ is equal to 2π regardless of k.) Below, an elementary proof is given; it is due to Evan O’Dorney (a high-school student taking Givental’s H104 class).
:::
