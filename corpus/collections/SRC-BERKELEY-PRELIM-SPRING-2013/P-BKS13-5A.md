---
schema: qual/card@1
id: P-BKS13-5A
kind: problem
title: A trigonometric polynomial exceeds its constant term in modulus
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Compared the authored statement with page 2 of the retained Spring 2013 solution PDF and independently reviewed the maximum-modulus argument.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the boundary identification with the polynomial g and the interior-maximum contradiction.
---

::: {.problem}
Let $n \geq 1$ and let $\{ a _ { 0 } , a _ { 1 } , \ldots , a _ { n } \}$ be complex numbers such that $a _ { n } \neq 0$ . For $\theta \in \mathbf { R }$ , define

$$
f ( \theta ) = a _ { 0 } + a _ { 1 } e ^ { i \theta } + a _ { 2 } e ^ { 2 i \theta } + . . . + a _ { n } e ^ { n i \theta } .
$$

Prove that there exists $\theta \in \mathbf { R }$ such that $| f ( \theta ) | > | a _ { 0 } |$
:::

::: {.solution}
Define the polynomial
$$
g(z)
\coloneqq
a_0+a_1z+\cdots+a_nz^n.
$$

::: pf

::: {.pf-step #s1}

For every real $\theta$,
$$
f(\theta)=g(e^{i\theta}).
$$

::: pf-proof

Substituting
$$
z=e^{i\theta}
$$
into the definition of $g$ gives
$$
g(e^{i\theta})
=
a_0+a_1e^{i\theta}+\cdots+a_ne^{ni\theta}
=
f(\theta).
$$

:::

:::

::: {.pf-step #s2}

Suppose, for contradiction, that
$$
\abs{f(\theta)}
\leq
\abs{a_0}
$$
for every $\theta\in\RR$. Then
$$
\abs{g(z)}
\leq
\abs{a_0}
$$
for every $z$ with $\abs{z}\leq1$.

::: pf-proof

By step [](#s1){.pf-ref}, the assumed inequality says
$$
\abs{g(z)}
\leq
\abs{a_0}
$$
for every point $z$ of the unit circle. Since $g$ is holomorphic on a
neighborhood of the closed unit disk, the maximum modulus theorem gives
the same bound throughout the disk.

:::

:::

::: pf-step

Under the assumption of step [](#s2){.pf-ref}, the polynomial $g$ is constant.

::: pf-proof

At the interior point $z=0$,
$$
\abs{g(0)}
=
\abs{a_0}.
$$
Thus the upper bound from step [](#s2){.pf-ref} is attained at an interior point.
The maximum modulus principle therefore implies that $g$ is constant on
the unit disk, and hence everywhere as a polynomial.

:::

:::

::: {.pf-step #s4}

The assumption in step [](#s2){.pf-ref} is impossible.

::: pf-proof

If $g$ were constant, every coefficient of positive degree would vanish.
In particular,
$$
a_n=0,
$$
contradicting the hypothesis.

:::

:::

::: {.pf-step #s5}

Therefore there exists
$$
\boxed{\theta\in\RR}
$$
such that
$$
\abs{f(\theta)}
>
\abs{a_0}.
$$

::: pf-proof

Step [](#s4){.pf-ref} is the negation of the assumption that the displayed strict
inequality fails for every real $\theta$.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is the required conclusion.

:::

:::

:::
