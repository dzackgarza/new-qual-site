---
schema: qual/card@1
id: P-ACDEH
kind: problem
title: Entire functions of quadratic growth are polynomials of degree at most $2$
classification:
  areas:
  - complex-analysis
  topics:
  - entire-functions
  - polynomials
  - liouville-s-theorem
  - cauchy-estimates
relations: []
review: draft
solved: true
---

::: problem
Let $f(z)$ be entire and assume that $f(z) \leq M |z|^2$ outside some disk for some constant $M$.
Show that $f(z)$ is a polynomial in $z$ of degree $\leq 2$.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Prove that if $f$ is entire and $\abs{f(z)} \leq M \abs z^2$ for all $z$ outside some disk (i.e. for $\abs z \geq R_0$), then $f$ is a polynomial of degree $\leq 2$.

<1>1. Write $f(z) = \sum_{n=0}^{\infty} a_n z^n$.
Proof: $f$ is entire.

<1>2. For $R \geq R_0$, $M(R) := \max_{\abs z = R} \abs{f(z)} \leq M R^2$.
Proof: By hypothesis applied on the circle $\abs z = R$.

<1>3. For $n \geq 3$ and $R \geq R_0$, $\abs{a_n} \leq \frac{M(R)}{R^n} \leq \frac{M R^2}{R^n} = M R^{2-n}$.
Proof: Cauchy's estimate <1>2.

<1>4. $a_n = 0$ for all $n \geq 3$.
Proof: <1>3 holds for arbitrarily large $R$, and $R^{2-n} \to 0$ as $R \to \infty$ for $n \geq 3$.

<1>5. $f(z) = a_0 + a_1 z + a_2 z^2$, a polynomial of degree at most $2$.
Proof: <1>1 and <1>4.

<1>6. Q.E.D. Proof: <1>5 is the claim.
:::
