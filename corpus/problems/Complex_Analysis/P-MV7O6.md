---
schema: qual/card@1
id: P-MV7O6
kind: problem
title: Maximum modulus principle on the interior of a simple closed contour
classification:
  areas:
  - complex-analysis
  topics:
  - Maximum Modulus Principle
relations: []
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
review: draft
---

::: problem
Let $\Omega$ be a simply connected open set and let $\gamma$ be a simple closed contour in $\Omega$ and enclosing a bounded region $U$ anticlockwise.
Let $f: \ \Omega \to {\mathbb C}$ be a holomorphic function and $|f(z)|\leq M$ for all $z\in \gamma$.
Prove that $|f(z)|\leq M$ for all $z\in U$.
:::

::: solution
**Theorem.**  
If $f:\Omega\to\mathbb C$ is holomorphic, $\gamma$ is a simple closed contour in $\Omega$, and
$|f|\le M$ on $\gamma$, then $|f(z)|\le M$ for every $z\in U$.

*Proof.*

1. Let $\overline U$ be the closure of $U$ together with $\gamma$. Since $\gamma\subset\Omega$ is a simple closed contour, $\overline U\subset\Omega$ and $f$ is holomorphic on an open neighborhood of $\overline U$.
2. Assume for contradiction that there exists $z_0\in U$ with $|f(z_0)|>M$.
3. Define $g(z)=\dfrac{f(z)}{f(z_0)}$. Then $g$ is holomorphic on a neighborhood of $\overline U$, and $|g(z)|\le 1$ for all $z\in\gamma$.
4. By the maximum modulus principle, $|g(z)|\le 1$ for all $z\in U$.
5. We have $|g(z_0)|=1$, so $|g|$ attains its maximum at an interior point. By the strong form of the maximum modulus principle, $g$ is constant on $U$, hence on $\overline U$.
6. Then $f\equiv f(z_0)$ on $U$, so $|f|\equiv |f(z_0)|>M$ on $\gamma$, contradicting the boundary bound.

Therefore no such $z_0$ exists and $|f(z)|\le M$ for all $z\in U$.
:::
