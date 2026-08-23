---
schema: qual/card@1
id: P-CASP22B
kind: problem
title: "Schwarz lemma for polynomial preimages: zeros, bounds, and equality cases"
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Polynomials
  - Holomorphic Functions
relations: []
review: draft
solved: false
---

::: problem
Let $p(z)$ be a nonconstant polynomial.
Let $G \subset \mathbb{C}$ be a component of the set $\{z : |p(z)| < 1\}$.

(a) Show that $p$ has at least one zero in $G$.

(b) Let $f$ be analytic in $G$ with $|f| \leq 1$.
Assume that $f$ has a zero at every zero of $p$ such that the order of vanishing of $f$ is at least that of $p$.
Show that $|f(z)| \leq |p(z)|$ and if $z = a$ is a zero of $p$ of order $k$, then $|f^{(k)}(a)| \leq |p^{(k)}(a)|$.

(c) If either $|f(a)| = |p(a)|$ for some $z = a$ that is not a zero of $p$ or if $|f^{(k)}(a)| = |p^{(k)}(a)|$ for some $z = a$ that is a zero of $p$ of order $k$, then $f(z) = cp(z)$ for some constant $c$.
:::
