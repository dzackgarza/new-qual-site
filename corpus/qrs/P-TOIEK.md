---
schema: qual/card@1
id: P-TOIEK
kind: problem
title: "1. Suppose $f_n \\rightrightarrows g$ with each $f_n$ bounded; we want\u2026"
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
---
  1. Suppose $f_n \rightrightarrows g$ with each $f_n$ bounded; we want to show that all of the $f_n$ are uniformly bounded by some $M$, i.e.
  $$
  \exists M \suchthat \forall x\in \RR, \forall n\in \NN, \quad \abs{f_n(x)} \leq M.
  $$
  - Since each $f_n$ is bounded, we can produce some $M_n$ such that $\abs{f_n(x)} \leq M < \infty$.
  - Since $f_n \rightrightarrows g$, we can give ourselves an epsilon of room and get an $N$ such that $n\geq N \implies \abs{f_n(x) - g(x)} < \varepsilon$. We then write
  $$
  f_n(x) = f_n(x) - g(x) + g(x) - f_N(x) + f_N(x) \\
  \implies \abs{f_n(x)} \leq \abs{f_n(x) - g(x)} + \abs{g(x) - f_N(x)} + \abs{f_N(x)} \\
  \leq \varepsilon + \varepsilon + M_N
  $$

  by the above two statements. But $N<\infty$, so we can choose $M = \max\theset{M_1, M_2, \cdots M_{N-1}, 2\varepsilon + M_N}$ as a uniform bound. Then just take $\varepsilon \to 0$. (Maybe not necessary?)

