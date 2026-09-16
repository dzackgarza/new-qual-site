---
schema: qual/card@1
id: P-CASP21B
kind: problem
title: "Polynomial approximation of z-bar on arcs and the full unit circle"
classification:
  areas:
  - complex-analysis
  topics:
  - Polynomial Approximation
  - Mergelyan Theorem
  - Uniform Convergence
relations: []
review: draft
---

::: {.problem}
Let $K$ be a proper closed arc of the unit circle $|z| = 1$.

(i) Is there a sequence of polynomials $P_n(z)$ such that $P_n(z) \to \bar{z}$ uniformly in $K$?

(ii) Is there a sequence of polynomials $P_n(z)$ such that $P_n(z) \to \bar{z}$ uniformly on the circle $|z| = 1$?

Please justify your answers.
:::

::: {.solution}
(i) Yes. Since $K$ is a proper closed arc of the unit circle, its complement
in $\mathbb C$ is connected and $K$ has empty interior. The function
$z\mapsto\bar z$ is continuous on $K$. By Mergelyan's theorem, every
continuous function on $K$ is uniformly approximable there by polynomials.
Thus there are polynomials $P_n$ with
\[
P_n\to\bar z
\]
uniformly on $K$.

(ii) No. On $|z|=1$ one has $\bar z=1/z$. If polynomials $P_n$ converged
uniformly to $1/z$ on the unit circle, then
\[
0=\int_{|z|=1}P_n(z)\,dz
\longrightarrow
\int_{|z|=1}\frac{dz}{z}=2\pi i,
\]
a contradiction.
:::
