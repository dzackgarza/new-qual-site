---
schema: qual/card@1
id: P-4VJTF
kind: problem
title: Centers of $\GL_n(\FF_p)$ and $\SL_n(\FF_p)$ are scalar matrices
classification:
  areas:
  - algebra
  topics:
  - Matrix Groups
  - Centralizers and Normalizers
  - Finite Fields
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
- Let $\FF_p$ be the finite field with $p$ elements, where $p$ is a prime.
  Show that the centers of $\GL_n(\FF_p)$ and $\SL_n(\FF_p)$ consist only of scalar matrices.

  - Show that the scalars $\zeta$ that appear in scalar matrices $Z(\SL_n(\FF_p))$ are roots of unity in $\FF_p$, i.e. $\zeta^p = 1$.
:::

::: {.solution}
<1>1. Center of $\operatorname{GL}_n(\mathbb{F}_p)$ consists of scalar matrices:
<2>1. Let $A = (a_{ij}) \in Z(\operatorname{GL}_n(\mathbb{F}_p))$.
For any distinct indices $i \neq j$, consider the elementary transvection matrix $T_{ij} = I_n + e_{ij}$, where $e_{ij}$ has a 1 in position $(i, j)$ and 0 elsewhere.
Since $\det(T_{ij}) = 1$, $T_{ij} \in \operatorname{GL}_n(\mathbb{F}_p)$ (and in fact $T_{ij} \in \operatorname{SL}_n(\mathbb{F}_p)$).
::: {.proof}
elementary transvections have unit determinant.
:::
<2>2. Since $A$ commutes with $T_{ij}$:
\[
A(I_n + e_{ij}) = (I_n + e_{ij})A \implies A e_{ij} = e_{ij} A.
\]
::: {.proof}
cancellation of $A$.
:::
<2>3. Compute entries of both matrix products:
- The $(k, \ell)$-entry of $A e_{ij}$ is $a_{ki} \delta_{j\ell}$.
- The $(k, \ell)$-entry of $e_{ij} A$ is $\delta_{ki} a_{j\ell}$.
Equating the entries:
- For $k \neq i$ and $\ell = j$: $a_{ki} = 0$. Thus all off-diagonal entries of $A$ vanish, so $A = \operatorname{diag}(a_{11}, \dots, a_{nn})$ is diagonal.
- For $k = i$ and $\ell = j$: $a_{ii} = a_{jj}$. Thus all diagonal entries are equal.
::: {.proof}
matrix entry comparisons.
:::
<2>4. Therefore $A = \lambda I_n$ for some scalar $\lambda \in \mathbb{F}_p^\times$.
Since every scalar matrix commutes with all matrices, $Z(\operatorname{GL}_n(\mathbb{F}_p)) = \{\lambda I_n \mid \lambda \in \mathbb{F}_p^\times\} \cong \mathbb{F}_p^\times$.
::: {.proof}
scalar matrices form the full center.
:::

<1>2. Center of $\operatorname{SL}_n(\mathbb{F}_p)$ consists of scalar matrices:
<2>1. Every elementary transvection $T_{ij} = I_n + e_{ij}$ has determinant $\det(T_{ij}) = 1$, so $T_{ij} \in \operatorname{SL}_n(\mathbb{F}_p)$ for all $i \neq j$.
::: {.proof}
determinant of transvection is 1.
:::
<2>2. If $A \in Z(\operatorname{SL}_n(\mathbb{F}_p))$, $A$ must commute with all $T_{ij}$ ($i \neq j$).
The exact derivation in <1>1 (<2>2 and <2>3) shows that $A = \zeta I_n$ for some scalar $\zeta \in \mathbb{F}_p^\times$.
::: {.proof}
identical transvection commutation argument inside $\operatorname{SL}_n(\mathbb{F}_p)$.
:::

<1>3. Characterization of the scalars $\zeta \in Z(\operatorname{SL}_n(\mathbb{F}_p))$:
<2>1. A scalar matrix $\zeta I_n$ belongs to $\operatorname{SL}_n(\mathbb{F}_p)$ if and only if its determinant is 1:
\[
\det(\zeta I_n) = \zeta^n = 1.
\]
::: {.proof}
determinant of scalar matrix is $\zeta^n$.
:::
<2>2. Moreover, by Fermat's Little Theorem, every $\zeta \in \mathbb{F}_p^\times$ satisfies $\zeta^{p-1} = 1$.
Therefore $\zeta$ is a root of unity in $\mathbb{F}_p^\times$ whose order divides $\gcd(n, p - 1)$.
The center is:
\[
Z(\operatorname{SL}_n(\mathbb{F}_p)) = \{\zeta I_n \mid \zeta \in \mathbb{F}_p^\times, \, \zeta^n = 1\} \cong \mu_n(\mathbb{F}_p) \cong \mathbb{Z}_{\gcd(n, p-1)}.
\]
::: {.proof}
roots of $x^n - 1$ in the cyclic group $\mathbb{F}_p^\times \cong \mathbb{Z}_{p-1}$.
:::

<1>4. Conclusion:
Both centers consist precisely of scalar matrices, and $Z(\operatorname{SL}_n(\mathbb{F}_p)) \cong \mu_n(\mathbb{F}_p)$ is the group of $n$-th roots of unity in $\mathbb{F}_p$. Q.E.D.
::: {.proof}
<1>1 through <1>3.
:::
:::
