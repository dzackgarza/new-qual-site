---
schema: qual/card@1
id: P-YR75I
kind: problem
title: Entire functions converging uniformly on line segments converge uniformly on
  compacta
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Uniform Convergence
  - Sequences of Functions
  - Normal Families
relations: []
review: draft
---

::: problem
Suppose $\theset{f_n}_{n\in \NN}$ is a sequence of entire functions where

- $f_n \to g$ pointwise for some $g:\CC\to\CC$.

- On every line segment in $\CC$, $f_n \to g$ uniformly.

Show that

- $g$ is entire, and

- $f_n\to g$ uniformly on every compact subset of $\CC$.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Suppose $(f_n)$ is a sequence of entire functions with $f_n \to g$ pointwise, and $f_n \to g$ uniformly on every line segment in $\CC$.
Show that $g$ is entire and $f_n \to g$ uniformly on every compact subset of $\CC$.

<1>1. $g$ is holomorphic on $\CC$.
<2>1. It suffices to show $\oint_\gamma g = 0$ for every closed polygonal path $\gamma$.
Proof: Morera's theorem.
<2>2. For a closed polygonal path $\gamma$ (a finite union of line segments), $\int_\gamma g = \lim_n \int_\gamma f_n$.
Proof: $\gamma$ is a finite union of line segments; on each, $f_n \to g$ uniformly by hypothesis, so the integrals converge.
<2>3. $\int_\gamma g = 0$.
Proof: each $f_n$ is entire, so $\oint_\gamma f_n = 0$ (Cauchy's theorem); <2>2 gives the limit $0$.

<1>2. $f_n \to g$ uniformly on compact sets.
<2>1. Let $K \subset \CC$ be compact; choose a bounded polygonal domain $\Omega$ with $K \subset \Omega$ and $\dist(K, \bd\Omega) > 0$.
Proof: e.g. a large square (or union of squares) around $K$, whose boundary is a finite union of line segments.
<2>2. For $z \in K$: $f_n(z) - g(z) = \frac{1}{2\pi i}\oint_{\bd\Omega} \frac{f_n(\zeta) - g(\zeta)}{\zeta - z}\, d\zeta$.
Proof: Cauchy integral formula applied to the holomorphic functions $f_n$ and $g$ (entire by <1>1) on the domain $\Omega$.
<2>3. $\sup_{z \in K}|f_n(z) - g(z)| \le \frac{\operatorname{length}(\bd\Omega)}{2\pi\, d} \sup_{\zeta \in \bd\Omega}|f_n(\zeta) - g(\zeta)|$ where $d = \dist(K, \bd\Omega)$.
Proof: bound the integral in <2>2: $|\zeta - z| \ge d$.
<2>4. The right-hand side tends to $0$.
Proof: $\bd\Omega$ is a finite union of line segments, and $f_n \to g$ uniformly on each, so $\sup_{\bd\Omega}|f_n - g| \to 0$.

<1>3. Q.E.D. Proof: <1>1 shows $g$ is entire; <1>2 shows uniform convergence on compacta.
:::
