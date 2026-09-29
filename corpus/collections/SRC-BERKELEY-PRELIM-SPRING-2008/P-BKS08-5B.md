---
schema: qual/card@1
id: P-BKS08-5B
kind: problem
title: The splitting field $\QQ(e^{2\pi i/5},\sqrt[5]{2})$ of $x^5-2$ is Galois of degree $20$
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 2008 preliminary-exam solution packet, which reproduces the problem statement with its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the splitting-field argument, Eisenstein degree five,
    cyclotomic degree four, and the degree divisibility/upper-bound argument
    against the vendored solution.
---

::: {.problem}
Let
$$
\zeta=e^{2\pi i/5},\qquad \alpha=\sqrt[5]{2}\in\mathbb R,
$$
and let
$$
E=\mathbb Q(\zeta,\alpha)\subset\mathbb C.
$$

(a) Show that $E/\mathbb Q$ is Galois.

(b) Compute $[E:\mathbb Q]$.
:::

::: {.solution}

::: pf

::: {.pf-step #roots-of-quintic}
The roots of $x^5-2$ are
$$
\alpha,\ \zeta\alpha,\ \zeta^2\alpha,\
\zeta^3\alpha,\ \zeta^4\alpha.
$$

::: pf-proof
Since $\alpha^5=2$ and $\zeta^5=1$,
$$
(\zeta^j\alpha)^5=2
$$
for $0\le j\le4$. These five numbers are distinct because the powers
of the primitive fifth root $\zeta$ are distinct, and a degree-$5$
polynomial has no further roots.
:::

:::

::: {.pf-step #splitting-field}
The field $E=\QQ(\zeta,\alpha)$ is the splitting field of
$x^5-2$ over $\QQ$.

::: pf-proof
Step [](#roots-of-quintic){.pf-ref} shows that all roots of $x^5-2$ lie in $E$. Conversely, any
splitting field contains the real root $\alpha$ and also contains
$(\zeta\alpha)/\alpha=\zeta$. Hence it contains both generators of
$E$. Therefore $E$ is exactly the splitting field.
:::

:::

::: {.pf-step #e-galois}
The extension $E/\QQ$ is Galois.

::: pf-proof
The polynomial $x^5-2$ is separable over $\QQ$: its derivative is
$5x^4$, and the two polynomials have no common root. A splitting field
of a separable polynomial is a finite Galois extension. Apply
step [](#splitting-field){.pf-ref}.
:::

:::

::: {.pf-step #degrees-four-five}
One has
$$
[\QQ(\zeta):\QQ]=4
\qquad\text{and}\qquad
[\QQ(\alpha):\QQ]=5.
$$

::: pf-proof
The primitive fifth root $\zeta$ has cyclotomic polynomial
$$
\Phi_5(x)=x^4+x^3+x^2+x+1,
$$
which is irreducible over $\QQ$, so its degree is $4$.

The polynomial $x^5-2$ is Eisenstein at $2$, hence irreducible over
$\QQ$. Since $\alpha$ is a root, its minimal polynomial has degree
$5$.
:::

:::

::: {.pf-step #divisible-by-20}
The integer $[E:\QQ]$ is divisible by $20$.

::: pf-proof
Since $\QQ(\zeta)\subseteq E$, the tower law gives
$$
[E:\QQ]=[E:\QQ(\zeta)]\cdot4,
$$
so $4$ divides $[E:\QQ]$. Similarly,
$\QQ(\alpha)\subseteq E$ and step [](#degrees-four-five){.pf-ref} give
$$
[E:\QQ]=[E:\QQ(\alpha)]\cdot5,
$$
so $5$ divides $[E:\QQ]$. Because $4$ and $5$ are coprime, $20$
divides $[E:\QQ]$.
:::

:::

::: {.pf-step #at-most-20}
One has
$$
[E:\QQ]\le20.
$$

::: pf-proof
Over $\QQ(\alpha)$, the element $\zeta$ satisfies the degree-$4$
polynomial $\Phi_5$. Hence
$$
[E:\QQ(\alpha)]\le4.
$$
Using $[\QQ(\alpha):\QQ]=5$ from step [](#degrees-four-five){.pf-ref} and the tower law gives
the claimed upper bound.
:::

:::

::: {.pf-step #degree-equals-20}
Therefore
$$
\boxed{[E:\QQ]=20}.
$$

::: pf-proof
Step [](#divisible-by-20){.pf-ref} says the positive integer $[E:\QQ]$ is a multiple of $20$,
while step [](#at-most-20){.pf-ref} says it is at most $20$.
:::

:::

::: pf-qed
Step [](#e-galois){.pf-ref} proves part (a), and step [](#degree-equals-20){.pf-ref} proves part (b).
:::

:::

:::
