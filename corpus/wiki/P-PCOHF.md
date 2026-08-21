---
schema: qual/card@1
id: P-PCOHF
kind: problem
title: Unique element of minimal norm in a closed convex subset of a Hilbert space
classification:
  areas:
  - real-analysis
  topics:
  - Hilbert Spaces
  - Norms
relations: []
review: draft
solved: true
---

::: problem
Prove that every closed convex $K \subset H$ a Hilbert space has a unique element of minimal norm.
:::

::: {.solution}
> **AI-Generated Solution**

<1>1. Let $d \da \inf_{x \in K}\norm{x}$, and choose a minimizing sequence $(x_n)$ in $K$ with $\norm{x_n} \to d$.
<1>2. $(x_n)$ is Cauchy.
Proof: by the parallelogram law in a Hilbert space, \[ \norm{x_n - x_m}^2 = 2\norm{x_n}^2 + 2\norm{x_m}^2 - 4\norm{\frac{x_n+x_m}{2}}^2 . \] Since $K$ is convex, $(x_n + x_m)/2 \in K$, so $\norm{(x_n+x_m)/2} \ge d$.
Hence \[ \norm{x_n - x_m}^2 \le 2\norm{x_n}^2 + 2\norm{x_m}^2 - 4d^2 \to 2d^2 + 2d^2 - 4d^2 = 0 \] as $n, m \to \infty$.
<1>3. $x_n$ converges to some $x \in K$ with $\norm{x} = d$.
Proof: $H$ is complete, so $x_n \to x$ for some $x \in H$; $K$ is closed, so $x \in K$; the norm is continuous, so $\norm{x} = \lim_n\norm{x_n} = d$.
<1>4. The minimizer is unique.
Proof: if $y \in K$ also satisfies $\norm{y} = d$, then by the parallelogram law and convexity (so $(x+y)/2 \in K$, hence $\norm{(x+y)/2} \ge d$), \[ \norm{x - y}^2 = 2\norm{x}^2 + 2\norm{y}^2 - 4\norm{\frac{x+y}{2}}^2 \le 2d^2 + 2d^2 - 4d^2 = 0, \] so $x = y$.
<1>5. Q.E.D.
:::
