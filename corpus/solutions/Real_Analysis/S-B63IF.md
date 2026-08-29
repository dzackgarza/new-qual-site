---
schema: qual/card@1
id: S-B63IF
kind: solution
title: Solution to P-4KTFN
classification:
  areas:
  - real-analysis
  topics:
  - Fatou
  - Convergence of Integrals
  - Counterexamples
relations:
- kind: solves
  target: P-4KTFN
review: draft
---

:::{.solution}
(a) If $f_n$ are non-negative, then $\int \liminf_{n\to\infty} f_n \le \liminf_{n\to\infty} \int f_n$.

(b) If $f_n\to f$ almost everywhere and $|f_n|\le g$ for some integrable function $g$ and all $n$, then $\int |f-f_n| \to 0$.

Proof: Since $|f_n|\le g$ and $f_n\to f$ almost everywhere, we also have $|f|\le g$ almost everywhere, so the functions $2g-|f-f_n|$ are non-negative. Thus we can apply Fatou's lemma to get
$$\int \liminf_{n\to\infty} 2g-|f-f_n| \le \liminf_{n\to\infty} \int (2g-|f-f_n|).$$
The left side simplifies to $\int 2g$ and the right side simplifies to $\int 2g - \limsup_{n\to\infty}\int |f-f_n|$. Thus by canceling and rearranging we get $\limsup \int |f-f_n| \le 0$, and since it's a limsup of non-negative quantities this implies the limit exists and equals 0. $\square$

(c) Let $f_n = n\cdot\chi_{[0,1/n]}$. $f_n\to0$ almost everywhere but $\int f_n = 1$ for all $n$.
:::
