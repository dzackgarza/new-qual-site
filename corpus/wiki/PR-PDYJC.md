---
schema: qual/card@1
id: PR-PDYJC
kind: proposition
title: "Sector to sector"
classification:
  areas:
  - complex-analysis
  topics:
  - conformal-maps
  - complex-logarithm
relations: []
review: draft
---
:::{.proposition title="Sector to sector"}
For $0 < \alpha < 2$:
\[
F_\alpha: S_{\pi \over \alpha }^\circ &\mapstofrom S_{\pi}^\circ = \HH^\circ \\
\ts{z\st 0 < \Arg(z) < {\pi\over \alpha} } &\mapstofrom \ts{w\st 0 < \Arg(w) < \pi } \\
z &\mapsto z^\alpha \\
w^{1\over \alpha} &\mapsfrom w
.\]
Note that if you look at the image of $\HH$ under $z\mapsto z^{\alpha}$, you get
\[
\ts{z \st 0 < \Arg(z) < \pi } &\mapstofrom \ts{0 < \Arg(w) < \alpha \pi }
.\]
For the inverse, choose a branch cut of $\log$ deleting the negative real axis, or more generally fix $0 < \arg w < \alpha \pi$.

**Boundary behavior:**

- As $x$ travels from $-\infty\to 0$, $F_\alpha(x)$ travels *away* from infinity along the ray $\theta = \alpha \pi$, so $L = \ts{ e^{t \alpha \pi } \st t\in (0, \infty) }$, from $\infty\to 0$.
- As $x$ travels from $0\to \infty$, $F_\alpha(x)$ travels from $0\to \infty$ along $\RR$.

:::
