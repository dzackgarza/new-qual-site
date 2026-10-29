---
schema: qual/card@1
id: E-XQ4BA
kind: problem
title: Automorphisms of $\CC$
classification:
  areas:
  - complex-analysis
  topics:
  - Biholomorphisms
  - Entire Functions
  - Liouville's Theorem
  - Singularities
relations: []
review: draft
---

::: {.exercise}
Show that $\Aut(\CC) = \theset{ z \mapsto az+b\st a\in \units{\CC}, b\in \CC }$.
:::

::: {.solution}

::: pf

::: pf-step
Every map $z\mapsto az+b$ with $a\in\units{\CC}$ and $b\in\CC$ lies in $\Aut(\CC)$.

::: pf-proof
It is entire, and $w\mapsto a^{-1}(w-b)$ is an entire two-sided inverse.
:::

:::

::: {.pf-step #pole}
If $f\in\Aut(\CC)$, then $f$ has a pole at $\infty$, so $f$ is a polynomial.

::: pf-proof
$f$ is entire, so $g(w)\coloneqq f(1/w)$ has an isolated singularity at $w=0$.
It is not removable: otherwise $f$ is bounded, hence constant by Liouville's theorem, and not injective.
Suppose it is essential.
By the Casorati--Weierstrass theorem, $f(\{\abs{z}>1\})$ is dense in $\CC$.
By the open mapping theorem, $f(\DD)$ is a nonempty open set, so it meets $f(\{\abs{z}>1\})$, which contradicts the injectivity of $f$.
So $\infty$ is a pole, and an entire function with a pole at $\infty$ is a polynomial.
:::

:::

::: pf-step
If $f\in\Aut(\CC)$, then $f(z) = az+b$ with $a\neq0$.

::: pf-proof
By step [](#pole){.pf-ref}, $f$ is a polynomial, of degree $n\ge1$ since $f$ is not constant.
If $n\ge2$, then $f'$ has a zero $z_0$, and $f$ is $k$-to-one near $z_0$ for some $k\ge2$, which contradicts injectivity.
So $n=1$.
:::

:::

:::

:::
