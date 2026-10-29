---
schema: qual/card@1
id: P-3QUC7
kind: problem
title: Maps $S^1\to X$ extend over $D^2$ when $\pi_1(X)=0$
classification:
  areas:
  - topology
  topics:
  - Fundamental Group
  - Homotopy
  - Quotient Spaces
relations: []
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
review: draft
---

::: {.problem}
Let $X$ be a path-connected topological space such that $\pi_1(X) = 0$. Prove that every continuous map $f: S^1 \to X$ can be extended to a continuous map $F: D^2 \to X$ (where $S^1 = \partial D^2$).
:::

::: {.solution}

View $S^1\subset D^2\subset\CC$, and define $q: S^1 \times [0, 1] \to D^2$ by $q(z, t) = (1 - t)z$.

::: pf

::: {.pf-step #quotient}

$q$ is a quotient map whose only nontrivial fiber is $S^1\times\{1\}=q^{-1}(0)$, and $q(z,0)=z$.

::: pf-proof

$q$ is continuous and surjective: $0=q(z,1)$, and $re^{i\theta}=q(e^{i\theta},1-r)$ for $0<r\le1$. For $t<1$ the point $(1-t)z\neq0$ determines $t$ and $z$. A continuous surjection from the compact space $S^1\times[0,1]$ to the Hausdorff space $D^2$ is closed, hence a quotient map.

:::

:::

::: {.pf-step #nullhomotopy}

There is a continuous $H: S^1 \times [0, 1] \to X$ with $H(z, 0) = f(z)$ and $H(z, 1) = x_0$ for all $z\in S^1$, where $x_0=f(1)$.

::: pf-proof

$f$ is a loop based at $x_0$, and $[f]\in\pi_1(X,x_0)=0$, so $f$ is homotopic to the constant loop at $x_0$.

:::

:::

::: pf-step

There is a continuous $F: D^2 \to X$ with $F|_{S^1}=f$.

::: pf-proof

By step [](#nullhomotopy){.pf-ref}, $H$ is constant on $S^1\times\{1\}$, so by step [](#quotient){.pf-ref} it is constant on the fibers of $q$. The universal property of quotient maps gives a continuous $F$ with $F\circ q=H$. For $z\in S^1$, $F(z)=F(q(z,0))=H(z,0)=f(z)$.

:::

:::

:::

:::
