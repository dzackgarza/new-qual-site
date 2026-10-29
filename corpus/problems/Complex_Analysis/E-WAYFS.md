---
schema: qual/card@1
id: E-WAYFS
kind: problem
title: Zeros of $\sin(\pi z)$ and singularities of $\csc(\pi z)$
classification:
  areas:
  - complex-analysis
  topics:
  - Zeros
  - Residues
  - Trigonometry
  - Poles
relations: []
review: draft
---

::: {.exercise}
Show that the complex zeros of $f(z) \definedas \sin(\pi z)$ are exactly $\ZZ$, and each is order 1. Calculate the residue of $1/\sin(\pi z)$ at $z=n\in \ZZ$.

:::

::: {.solution}
::: pf

::: pf-step
The zeros of $\sin(\pi z)$ are exactly the integers.

::: pf-proof
$\sin(\pi z) = \frac{1}{2i}(e^{i\pi z} - e^{-i\pi z})$ vanishes if and only if $e^{2\pi i z} = 1$, that is, $2\pi i z = 2\pi i k$ for some $k\in\ZZ$.
:::

:::

::: {.pf-step #simple}
Each zero $k\in\ZZ$ has order $1$.

::: pf-proof
Since $\sin(\pi z) = (-1)^k\sin(\pi(z-k))$,
$$
\sin(\pi z) = (-1)^k\qty{\pi(z-k) - \frac{\pi^3}{3!}(z-k)^3 + \cdots} = (z-k)g(z),
$$
where $g$ is entire and $g(k) = (-1)^k\pi \neq 0$.
:::

:::

::: pf-step
$\Res_{z=k}\frac{1}{\sin(\pi z)} = \boxed{\frac{(-1)^k}{\pi}}$.

::: pf-proof
By step [](#simple){.pf-ref}, $\frac{1}{\sin(\pi z)} = \frac{1}{(z-k)g(z)}$ has a simple pole at $k$ with residue $\frac{1}{g(k)} = \frac{(-1)^k}{\pi}$.
:::

:::

:::

:::
