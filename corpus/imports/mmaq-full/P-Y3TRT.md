---
schema: qual/card@1
id: P-Y3TRT
kind: problem
title: "Let g : $[0, 1] \\times [0, 1] \\to [0, 1]$ be a continuous function and…"
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---

:::{.problem title="?"}
Let g : $[0, 1] \times [0, 1] \to [0, 1]$ be a continuous function and let $\{f_n\}$ be a sequence of functions such that 

$$f_n(x)=\begin{cases}{0,   0\leq x\leq 1/n},\\{\int_0^{x-\frac1n} g(t,f_n(t))dt, 1/n\leq x \leq 1.}\end{cases}$$

With the help of the Arzela-Ascoli theorem or otherwise, show that there exists a continuous function $f : [0, 1] \to \mathbb{R}$ such that 

$f(x) = \int_0^x g(t, f(t))dt$

for all $x \in [0, 1]$. 

> Hint: first show that $|f_n(x_1) - f_n(x_2)| \leq |x_1 - x_2|$.
:::
