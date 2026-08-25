---
schema: qual/card@1
id: P-RASP23C
kind: problem
title: "Multiplicative convolution on R_+"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
---

::: problem
Let $\mathbb{R}_+ = [0, \infty)$, $f, g \in L^1(\mathbb{R}_+, m)$, and consider
$$
h(x) = \int_0^\infty f(y) g\!\left(\frac{x}{y}\right) \frac{dy}{y}.
$$
Show that $h$ is well-defined (i.e., $y \mapsto f(y) g(x/y) / y$ is in $L^1(\mathbb{R}_+, m)$ for a.e. $x \in \mathbb{R}_+$), $h \in L^1(\mathbb{R}_+)$, and
$$
\|h\|_{L^1} \leq \|f\|_{L^1} \|g\|_{L^1}.
$$

Comment: You may use without proof that $g(x/y)$ is Lebesgue measurable on $\mathbb{R}_+^2$.
:::
