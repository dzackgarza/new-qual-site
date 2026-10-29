---
schema: qual/card@1
id: E-TJ3WM
kind: problem
title: Holomorphic automorphisms of $\CC$ are the maps $z\mapsto az+b$ with $a\neq
  0$
classification:
  areas:
  - complex-analysis
  topics:
  - Biholomorphisms
  - Entire Functions
  - Singularities
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: {.exercise}
Show that $\Aut_\CC(\CC) = \theset{ z \mapsto az+b\st a\in \units{\CC}, b\in \CC }$.
:::

::: {.solution}

::: pf

::: {.pf-step #affine-is-automorphism}
Every affine map $z \mapsto az + b$ with $a \neq 0$ is a holomorphic automorphism of $\CC$.

::: pf-proof
It is entire, and its inverse $z \mapsto (z - b)/a$ is also entire.
:::

:::

::: {.pf-step #not-essential}
Let $f \in \Aut_\CC(\CC)$. Then $\infty$ is not an essential singularity of $f$.

::: pf-proof
By the open mapping theorem, $U\coloneqq f(\DD)$ is a nonempty open set. If $\infty$ were an essential singularity, then by Casorati–Weierstrass $f(\{\abs{z}>1\})$ would be dense in $\CC$ and so would meet $U$, giving $\abs{z}>1$ and $\abs{z'}<1$ with $f(z) = f(z')$. This contradicts injectivity.
:::

:::

::: {.pf-step #polynomial}
$f$ is a nonconstant polynomial.

::: pf-proof
$f$ is not constant, being injective. A nonconstant entire function has at $\infty$ either a pole or an essential singularity, so by step [](#not-essential){.pf-ref} it has a pole, of some order $m$. Writing $f(z) = \sum_{n\geq 0} c_n z^n$, the Laurent series of $f(1/w)$ at $0$ is $\sum_n c_n w^{-n}$, so $c_n = 0$ for $n>m$.
:::

:::

::: {.pf-step #degree-one}
The polynomial $f$ has degree exactly $1$.

::: pf-proof
If $\deg f = d \ge 2$, then $f'$ has degree $d-1\geq 1$ and so has a zero $c$. Then $f(z)-f(c)$ has a zero of order $m\geq 2$ at $c$, and $f$ is $m$-to-one on a punctured neighbourhood of $c$, contradicting injectivity. With step [](#polynomial){.pf-ref}, $d=1$.
:::

:::

::: pf-qed
By steps [](#affine-is-automorphism){.pf-ref} and [](#degree-one){.pf-ref}, $\Aut_\CC(\CC)$ consists exactly of the maps $z \mapsto az + b$ with $a \neq 0$.
:::

:::

:::
