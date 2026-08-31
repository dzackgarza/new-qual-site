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
<1>1. The norm function and units of $R = \mathbb{Z}[3i]$:
<2>1. Elements of $R = \mathbb{Z}[3i]$ are of the form $\alpha = a + 3bi$ where $a, b \in \mathbb{Z}$.
Define the multiplicative field norm $N: R \to \mathbb{Z}_{\ge 0}$ by:
\[
N(a + 3bi) = a^2 + 9b^2.
\]
<2>2. An element $\alpha \in R$ is a unit if and only if $N(\alpha) = 1$.
The equation $a^2 + 9b^2 = 1$ in integers has only the solutions $(a, b) = (\pm 1, 0)$.
Thus the group of units is $R^\times = \{ \pm 1 \}$.

<1>2. Irreducibility of $3$ and $3i$ in $R$:
<2>1. Suppose $3 = \alpha \beta$ for some $\alpha, \beta \in R$.
Taking norms:
\[
9 = N(3) = N(\alpha) N(\beta).
\]
If neither $\alpha$ nor $\beta$ is a unit, then $N(\alpha) = 3$ and $N(\beta) = 3$.
<2>2. For any $\alpha = a + 3bi \in R$, $N(\alpha) = a^2 + 9b^2$.
- If $b \neq 0$, then $a^2 + 9b^2 \ge 9 > 3$.
- If $b = 0$, then $a^2 = 3$, which has no integer solution.
Thus there are no elements of norm 3 in $R$.
Therefore $3$ is irreducible in $R$.
<2>3. Symmetrically, $N(3i) = 9$, so $3i$ and $-3i$ are also irreducible in $R$.

<1>3. Failure of unique factorization:
<2>1. Consider the element $9 \in R$, which has two factorizations into irreducibles:
\[
9 = 3 \cdot 3 = (3i) \cdot (-3i).
\]
<2>2. The irreducible factors $3$ and $3i$ are not associates in $R$, because the only units are $\pm 1$ and $3 \cdot (\pm 1) \neq 3i$ (since $i \notin R$).
Thus $9$ possesses two distinct factorizations into irreducible elements.

<1>4. Alternative integral closure argument:
<2>1. The fraction field of $R$ is $\mathbb{Q}(i)$, and the integral closure of $\mathbb{Z}$ in $\mathbb{Q}(i)$ is the ring of Gaussian integers $\mathbb{Z}[i]$.
The element $i \in \mathbb{Q}(i)$ is a root of the monic polynomial $x^2 + 1 \in R[x]$, but $i \notin R$.
Thus $R = \mathbb{Z}[3i]$ is not integrally closed, and hence cannot be a UFD.

<1>5. Conclusion:
$\mathbb{Z}[3i]$ is not a UFD. Q.E.D.
:::
