---
schema: qual/card@1
id: P-CASP12E
kind: problem
title: "Boundary behavior of the Poisson integral on arcs of continuity"
classification:
  areas:
  - complex-analysis
  topics:
  - Harmonic Functions
relations: []
review: draft
---

::: problem
Let $f(e^{it})$ be a piecewise continuous, real-valued function on $\mathbb{T}$, and consider the harmonic function in the unit disk $\mathbb{D}$ given by $$u(z) := \frac{1}{2\pi}\int_{-\pi}^{\pi} P_r(\theta - t) f(e^{it})\,dt,$$ where $P_r(\theta)$ denotes the Poisson kernel and $z = re^{i\theta}$.
Suppose that $A \subset \mathbb{T}$ is an open sub-arc on which $f$ is continuous.
Show that $$\lim_{z \to a} u(z) = f(a)$$ for every $a = e^{i\theta} \in A$.
:::

::: solution
Fix $a=e^{i\theta_0}\in A$. Choose a closed arc $J\subset A$ whose interior
contains $a$. By continuity, for every $\varepsilon>0$ there is a smaller arc
$J_0\subset J$ about $a$ on which
\[
|f(e^{it})-f(a)|<\varepsilon.
\]
Since the Poisson kernel has integral $2\pi$,
\[
u(z)-f(a)=\frac1{2\pi}\int_{-\pi}^{\pi}
P_r(\theta-t)(f(e^{it})-f(a))\,dt.
\]
The contribution from $J_0$ has absolute value at most $\varepsilon$.

For $z=re^{i\theta}\to a$, the angular distance from $\theta$ to the
complement of $J_0$ is bounded below by a positive constant. On that
complement,
\[
P_r(\theta-t)=\frac{1-r^2}{1-2r\cos(\theta-t)+r^2}\longrightarrow0
\]
uniformly. Since the piecewise continuous boundary function is bounded, the
remaining integral therefore tends to $0$. Thus
\[
\lim_{z\to a}u(z)=f(a).
\]
:::
