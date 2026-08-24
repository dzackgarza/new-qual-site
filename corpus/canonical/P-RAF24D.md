---
schema: qual/card@1
id: P-RAF24D
kind: problem
title: No uniform rate in the Riemann–Lebesgue lemma on $[0,1]$
classification:
  areas:
  - real-analysis
  topics:
  - Fourier Analysis
  - Integrals
  - Counterexamples
relations: []
review: draft
---

::: problem
Recall that the Riemann–Lebesgue lemma implies that for all $f \in L^1([0,1], m)$,
\[
\lim_{n \to \infty} \int_0^1 f(x) e^{inx}\, dx = 0.
\]
Show that there is no rate of convergence for the above limit that is independent of $f$.
Specifically, show that there cannot exist any sequence of positive numbers $(a_n)$ such that $a_n \to \infty$ and for every $f \in L^1([0,1], m)$ there is a constant $C_f < \infty$ with
\[
\left| \int_0^1 f(x) e^{inx}\, dx \right| \le \frac{C_f}{a_n}
\quad\text{for each } n \in \mathbb{N}.
\]
Hint: If such $(a_n)$ existed, find a sequence of linear functionals that yields a contradiction.
:::
