---
schema: qual/card@1
id: P-BERK85S-08
kind: problem
title: Discrete harmonic oscillator and convergence to the sine function
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

:::{.problem}
Fix $h>0$ and consider
\[
\frac{y((n+2)h)-2y((n+1)h)+y(nh)}{h^2}=-y(nh),
\qquad n=0,1,2,\dots.
\]

1. Find the general solution by exponential substitution.
2. Find the solution satisfying
   \[
   y(0)=0,
   \qquad
   y(h)=h,
   \]
   and denote it by $S_h(nh)$.
3. For fixed $x$, put $h=x/n$. Prove that
   \[
   \lim_{n\to\infty}S_{x/n}(x)=\sin x.
   \]
:::
