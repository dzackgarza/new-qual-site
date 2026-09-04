---
schema: qual/card@1
id: E-GRXN4
kind: problem
title: Sums and products of poles and essential singularities
classification:
  areas:
  - complex-analysis
  topics:
  - Poles
  - Essential Singularities
  - Laurent Series
  - Counterexamples
relations: []
review: draft
---

::: {.exercise}
Determine whether each statement is true, proving it or giving a counterexample.

- If $f,g$ have a pole at $a$, then $f+g$ has a pole at $a$.

- If $f,g$ have a pole at $a$, then $fg$ has a pole at $a$.

- If $f$ has an essential singularity at $z_0$ and $g$ has a pole at $z_0$, then $z_0$ is an essential singularity for $f+g$.

- If $f$ has a pole of order $N$ at $z_0$ then $f^2$ has a pole of order $2N$ at $z_0$.
:::

::: {.solution}
- The first statement is false.
  Take
  \[
  f(z)={1\over z-a},
  \qquad
  g(z)=-{1\over z-a};
  \]
  then both have simple poles at $a$, but $f+g=0$.

- The second statement is true.
  If $f$ and $g$ have pole orders $m,n$, write
  \[
  f(z)=(z-a)^{-m}u(z),
  \qquad
  g(z)=(z-a)^{-n}v(z),
  \]
  where $u,v$ are holomorphic and nonzero at $a$.
  Then
  \[
  f(z)g(z)=(z-a)^{-(m+n)}u(z)v(z),
  \]
  and $u(a)v(a)\neq0$, so $fg$ has a pole of order $m+n$.

- The third statement is true.
  If $g$ has a pole of order $N$, its Laurent series has no terms below degree $-N$.
  An essential singularity of $f$ has infinitely many nonzero negative Laurent coefficients.
  Therefore the coefficients of $f+g$ below degree $-N$ are exactly those of $f$, so infinitely many remain; hence $f+g$ is essential at $z_0$.

- The fourth statement is true.
  Write
  \[
  f(z)=(z-z_0)^{-N}u(z),
  \qquad u(z_0)\neq0.
  \]
  Then
  \[
  f(z)^2=(z-z_0)^{-2N}u(z)^2,
  \]
  and $u(z_0)^2\neq0$, so $f^2$ has a pole of order $2N$.
:::
