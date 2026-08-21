---
schema: qual/card@1
id: E-HAT-1.1-15
kind: exercise
title: Naturality square for basepoint-change homomorphisms
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Natural Transformations
relations: []
review: draft
solved: false
---

Given a map $f: X \to Y$ and a path $h: I \to X$ from $x_0$ to $x_1$, show that $f_* \beta_h = \beta_{fh} f_*$ in the diagram:

$$\begin{array}{rcl}
\pi_1(X, x_1) & \xrightarrow{\beta_h} & \pi_1(X, x_0) \\
\downarrow f_* & & \downarrow f_* \\
\pi_1(Y, f(x_1)) & \xrightarrow{\beta_{fh}} & \pi_1(Y, f(x_0))
\end{array}$$
