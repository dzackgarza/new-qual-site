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
Determine whether the ring $\mathbb{Z}[3i]$ is a UFD.
:::

::: {.solution}
Set $R=\ZZ[3i]$. For $a,b\in\ZZ$, define
$$
N(a+3bi)=(a+3bi)(a-3bi)=a^2+9b^2.
$$

<1>1. The only units of $R$ are $\pm1$.

::: {.proof}
The norm is multiplicative. If $u\in R^\times$, then
$N(u)N(u^{-1})=1$, so $N(u)=1$. Conversely, an element of norm $1$ is a
unit because its complex conjugate is its inverse. The equation
$$
a^2+9b^2=1
$$
has only the solutions $b=0$ and $a=\pm1$. Hence
$R^\times=\{\pm1\}$.
:::

<1>2. There is no element of $R$ having norm $3$.

::: {.proof}
If $a^2+9b^2=3$ and $b\ne0$, then the left side is at least $9$. If
$b=0$, then $a^2=3$, which has no integer solution.
:::

<1>3. The elements $3$, $3i$, and $-3i$ are irreducible in $R$.

::: {.proof}
Each has norm $9$. Suppose one of them factors as $\alpha\beta$ with both
$\alpha$ and $\beta$ nonunits. By step <1>1, the positive integers
$N(\alpha)$ and $N(\beta)$ are both greater than $1$, and
$$
N(\alpha)N(\beta)=9.
$$
Hence $N(\alpha)=N(\beta)=3$, contradicting step <1>2. Therefore every
factorization has a unit factor, so each of the three elements is
irreducible.
:::

<1>4. The element $9$ has two inequivalent factorizations into
irreducibles:
$$
9=3\cdot3=(3i)(-3i).
$$

::: {.proof}
By step <1>3, all four displayed factors are irreducible. By step <1>1,
the only associates of $3$ are $3$ and $-3$. Neither $3i$ nor $-3i$ is
an associate of $3$. Thus the two factorizations cannot be obtained from
one another by permuting factors and multiplying factors by units.
:::

<1>5. The ring $\ZZ[3i]$ is
$$
\boxed{\text{not a UFD}}.
$$

::: {.proof}
Step <1>4 exhibits an element with two inequivalent factorizations into
irreducibles, contradicting unique factorization.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 answers the question.
:::
:::
