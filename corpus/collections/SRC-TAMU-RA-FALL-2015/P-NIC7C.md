---
schema: qual/card@1
id: P-NIC7C
kind: problem
title: Every functional on $X$ factors through an injective closed-range operator
  $T:X\to Y$
classification:
  areas:
  - real-analysis
  topics:
  - Dual Spaces
  - Functional Analysis
  - Norms
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
  note: Checked against Problem 4.6 in the preserved TAMU August 2015 source notes, matching the official Fall 2015 exam statement.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-11
---

::: {.problem}
Let $X,Y$ be Banach spaces and $T:X\to Y$ be a one-to-one, bounded and linear operator for which the range $T(X)$ is closed in $Y$.
Show that for each continuous linear functional $\phi$ on $X$ there is a continuous linear functional $\psi$ on $Y$, so that $\phi=\psi\circ T$.
:::

::: {.solution}
Because $T$ is one-to-one, it is a linear bijection from $X$ onto $T(X)$. The range $T(X)$ is closed in the Banach space $Y$, hence is itself Banach. Therefore the bounded inverse theorem applied to
\[
T:X\longrightarrow T(X)
\]
shows that $T^{-1}:T(X)\to X$ is bounded.

Fix $\phi\in X^*$ and define
\[
\lambda:T(X)\to\mathbb C,\qquad \lambda(y)=\phi(T^{-1}y).
\]
Then $\lambda$ is linear and continuous, with
\[
|\lambda(y)|\le \|\phi\|\,\|T^{-1}\|\,\|y\|.
\]
By the Hahn--Banach theorem, $\lambda$ extends to some $\psi\in Y^*$. For every $x\in X$,
\[
(\psi\circ T)(x)=\psi(Tx)=\lambda(Tx)=\phi(x).
\]
Hence $\phi=\psi\circ T$.
:::
