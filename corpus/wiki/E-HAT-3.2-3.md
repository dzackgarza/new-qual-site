---
schema: qual/card@1
id: E-HAT-3.2-3
kind: exercise
title: Hatcher Section 3.2 Exercise 3
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
solved: false
---

# E-HAT-3.2-3

(a) Using the cup product structure, show there is no map $\mathbb{RP}^n \to \mathbb{RP}^m$ inducing a nontrivial map $H^1(\mathbb{RP}^m; \mathbb{Z}_2) \to H^1(\mathbb{RP}^n; \mathbb{Z}_2)$ if $n > m$.
What is the corresponding result for maps $\mathbb{CP}^n \to \mathbb{CP}^m$?

(b) Prove the Borsuk–Ulam theorem by the following argument.
Suppose on the contrary that $f: S^n \to \mathbb{R}^n$ satisfies $f(x) \neq f(-x)$ for all $x$.
Then define $g: S^n \to S^{n-1}$ by $g(x) = \bigl(f(x) - f(-x)\bigr) / \bigl|f(x) - f(-x)\bigr|$, so $g(-x) = -g(x)$ and $g$ induces a map $\mathbb{RP}^n \to \mathbb{RP}^{n-1}$.
Show that part (a) applies to this map.
