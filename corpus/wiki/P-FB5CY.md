---
schema: qual/card@1
id: P-FB5CY
kind: problem
title: "1. We want some power series centered at 4 with convergence radius 1,\u2026"
classification:
  areas: []
  topics: []
relations: []
review: draft
---
1. We want some power series centered at 4 with convergence radius 1, so something of the form $\sum_n f(n)(x-4)^n$ with $L = \lim \frac{a_{n+1}}{a_n} = 1$. 

    Then, by plugging in $5$ and $3$, we find that we want $\sum (-1)^n f(n)$ to converge but $\sum f(n)$ to diverge. The canonical example of this is the harmonic series with $f(n) = \frac 1 n$, so we can just take 
$$f(x) = \sum_n \frac{(x-4)^n}{n}. \qed$$ 

