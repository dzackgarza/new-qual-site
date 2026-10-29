---
schema: qual/card@1
id: P-NXDOU
kind: problem
title: Whether $\ZZ[3i]$ is a UFD
classification:
  areas:
  - prelim
  topics:
  - Factorization
  - Integral Domains
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---
::: {.problem}
Determine whether the ring $\ZZ[3i]$ is a UFD.
:::

::: {.solution}
Set $R=\ZZ[3i]$. For $a,b\in\ZZ$, define
$$
N(a+3bi)=(a+3bi)(a-3bi)=a^2+9b^2.
$$

::: pf

::: {.pf-step #s1}

The only units of $R$ are $\pm1$.

::: pf-proof

The norm is multiplicative. If $u\in R^\times$, then
$N(u)N(u^{-1})=1$, so $N(u)=1$. Conversely, an element of norm $1$ is a
unit because its complex conjugate is its inverse. The equation
$$
a^2+9b^2=1
$$
has only the solutions $b=0$ and $a=\pm1$. Hence
$R^\times=\{\pm1\}$.

:::

:::

::: {.pf-step #s2}

There is no element of $R$ having norm $3$.

::: pf-proof

If $a^2+9b^2=3$ and $b\ne0$, then the left side is at least $9$. If
$b=0$, then $a^2=3$, which has no integer solution.

:::

:::

::: {.pf-step #s3}

The elements $3$, $3i$, and $-3i$ are irreducible in $R$.

::: pf-proof

Each has norm $9$. Suppose one of them factors as $\alpha\beta$ with both
$\alpha$ and $\beta$ nonunits. By step [](#s1){.pf-ref}, the positive integers
$N(\alpha)$ and $N(\beta)$ are both greater than $1$, and
$$
N(\alpha)N(\beta)=9.
$$
Hence $N(\alpha)=N(\beta)=3$, contradicting step [](#s2){.pf-ref}. Therefore every
factorization has a unit factor, so each of the three elements is
irreducible.

:::

:::

::: {.pf-step #s4}

The element $9$ has two inequivalent factorizations into
irreducibles:
$$
9=3\cdot3=(3i)(-3i).
$$

::: pf-proof

By step [](#s3){.pf-ref}, all four displayed factors are irreducible. By step [](#s1){.pf-ref},
the only associates of $3$ are $3$ and $-3$. Neither $3i$ nor $-3i$ is
an associate of $3$. Thus the two factorizations cannot be obtained from
one another by permuting factors and multiplying factors by units.

:::

:::

::: {.pf-step #s5}

The ring $\ZZ[3i]$ is
$$
\boxed{\text{not a UFD}}.
$$

::: pf-proof

Step [](#s4){.pf-ref} exhibits an element with two inequivalent factorizations into
irreducibles, contradicting unique factorization.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} answers the question.

:::

:::

:::
