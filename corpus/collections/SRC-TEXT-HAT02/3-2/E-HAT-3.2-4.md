---
schema: qual/card@1
id: E-HAT-3.2-4
kind: problem
title: Hatcher Section 3.2 Exercise 4
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 3.2, Exercise 4; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

# E-HAT-3.2-4

Apply the Lefschetz fixed point theorem to show that every map $f: \mathbb{CP}^n \to \mathbb{CP}^n$ has a fixed point if $n$ is even, using the fact that $f^*: H^*(\mathbb{CP}^n; \mathbb{Z}) \to H^*(\mathbb{CP}^n; \mathbb{Z})$ is a ring homomorphism.
When $n$ is odd show there is a fixed point unless $f^*(\alpha) = -\alpha$, for $\alpha$ a generator of $H^2(\mathbb{CP}^n; \mathbb{Z})$.

::: {.solution}
Let $\alpha\in H^2(\mathbb{CP}^n;\mathbb Z)$ be the standard generator. Since $f^*$ is a ring map, there is an integer $d$ such that
\[
f^*(\alpha)=d\alpha,
\qquad
f^*(\alpha^j)=d^j\alpha^j.
\]
Each even-dimensional cohomology group is infinite cyclic and the odd groups vanish. Hence the Lefschetz number is
\[
L(f)=1+d+d^2+\cdots+d^n.
\]
If $n$ is even, this integer is never zero. Indeed for $d\ge0$ it is positive; for $d<0$, writing $d=-r$ with $r\ge1$, one gets
\[
1-r+r^2-\cdots+r^n=\frac{r^{n+1}+1}{r+1}>0.
\]
Thus $L(f)\ne0$, so the Lefschetz fixed point theorem gives a fixed point.

If $n$ is odd, then
\[
1+d+\cdots+d^n=0
\]
can occur only for $d=-1$: for $d\ge0$ the sum is positive, and for $d=-r<0$,
\[
1-r+r^2-\cdots-r^n=(1-r)(1+r^2+\cdots+r^{n-1}),
\]
which vanishes exactly when $r=1$. Therefore every map has a fixed point unless
\[
f^*(\alpha)=-\alpha.
\]
:::
