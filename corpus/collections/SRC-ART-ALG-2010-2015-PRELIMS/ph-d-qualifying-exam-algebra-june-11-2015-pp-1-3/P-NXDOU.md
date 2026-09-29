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
::: pf

::: pf-step
The unit group of $R = \mathbb{Z}[3i]$ is $R^\times=\{\pm1\}$.

::: pf-proof

::: pf-step
Elements of $R = \mathbb{Z}[3i]$ are of the form $\alpha = a + 3bi$ where $a, b \in \mathbb{Z}$.
Define the multiplicative field norm $N: R \to \mathbb{Z}_{\ge 0}$ by:
\[
N(a + 3bi) = a^2 + 9b^2.
\]
:::

::: pf-step
An element $\alpha \in R$ is a unit if and only if $N(\alpha) = 1$.
The equation $a^2 + 9b^2 = 1$ in integers has only the solutions $(a, b) = (\pm 1, 0)$.
Thus the group of units is $R^\times = \{ \pm 1 \}$.
:::

:::

:::

::: pf-step
The elements $3$ and $\pm 3i$ are irreducible in $R$.

::: pf-proof

::: pf-step
Suppose $3 = \alpha \beta$ for some $\alpha, \beta \in R$.
Taking norms:
\[
9 = N(3) = N(\alpha) N(\beta).
\]
If neither $\alpha$ nor $\beta$ is a unit, then $N(\alpha) = 3$ and $N(\beta) = 3$.
:::

::: pf-step
For any $\alpha = a + 3bi \in R$, $N(\alpha) = a^2 + 9b^2$.
- If $b \neq 0$, then $a^2 + 9b^2 \ge 9 > 3$.
- If $b = 0$, then $a^2 = 3$, which has no integer solution.
Thus there are no elements of norm 3 in $R$.
Therefore $3$ is irreducible in $R$.
:::

::: pf-step
Since $N(\pm 3i) = 9$, the same norm argument shows that $3i$ and $-3i$ are also irreducible in $R$.
:::

:::

:::

::: {.pf-step #s3}
The element $9$ has two factorizations into irreducibles whose factors are not associates.

::: pf-proof

::: pf-step
Consider the element $9 \in R$, which has two factorizations into irreducibles:
\[
9 = 3 \cdot 3 = (3i) \cdot (-3i).
\]
:::

::: pf-step
The irreducible factors $3$ and $3i$ are not associates in $R$, because the only units are $\pm 1$ and $3 \cdot (\pm 1) \neq 3i$ (since $i \notin R$).
Thus $9$ possesses two distinct factorizations into irreducible elements.
:::

:::

:::

::: pf-step
$R$ is not integrally closed, which independently shows that $R$ is not a UFD.

::: pf-proof

::: pf-step
The fraction field of $R$ is $\mathbb{Q}(i)$, and the integral closure of $\mathbb{Z}$ in $\mathbb{Q}(i)$ is the ring of Gaussian integers $\mathbb{Z}[i]$.
The element $i \in \mathbb{Q}(i)$ is a root of the monic polynomial $x^2 + 1 \in R[x]$, but $i \notin R$.
Thus $R = \mathbb{Z}[3i]$ is not integrally closed, and hence cannot be a UFD.
:::

:::

:::

::: pf-qed
By step [](#s3){.pf-ref}, $\mathbb{Z}[3i]$ is not a UFD.
:::

:::
:::
