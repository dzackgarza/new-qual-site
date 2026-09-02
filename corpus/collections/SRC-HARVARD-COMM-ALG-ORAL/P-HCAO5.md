---
schema: qual/card@1
id: P-HCAO5
kind: problem
title: A root over an extension gives a linear factor
classification:
  areas:
  - algebra
  topics:
  - Polynomial Roots
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Let $F$ be a field, let $E/F$ be a field extension, and let $p(x) \in F[x]$.
If $a \in E$ and $p(a)=0$, show that
\[
p(x)=(x-a)q(x)
\]
for some $q(x) \in E[x]$.
:::

::: {.solution}
<1>1. Apply the Division Algorithm in the polynomial ring $E[x]$: <2>1. Since $F \subseteq E$, we have $F[x] \subseteq E[x]$, so $p(x)$ can be viewed as an element of $E[x]$.
::: {.proof}
canonical inclusion of polynomial rings.
:::
<2>2. In $E[x]$, the polynomial $x - a$ has degree 1 and is monic.
::: {.proof}
$a \in E$.
:::
<2>3. By the Euclidean division algorithm in $E[x]$, there exist unique polynomials $q(x), r(x) \in E[x]$ such that:
\[
p(x) = (x - a) q(x) + r(x), \quad \text{where } \deg r(x) < \deg(x - a) = 1 \text{ or } r(x) = 0.
\]
::: {.proof}
Division Algorithm for polynomials over a field.
:::
<2>4. Since $\deg r(x) < 1$, $r(x)$ is a constant polynomial $c \in E$.
::: {.proof}
polynomials of degree $< 1$ are constants.
:::

<1>2. Evaluate at $x = a$: <2>1. Applying the evaluation homomorphism $\operatorname{ev}_a: E[x] \to E$ to both sides:
\[
p(a) = (a - a) q(a) + r(a) = 0 \cdot q(a) + c = c.
\]
::: {.proof}
evaluation homomorphism properties.
:::
<2>2. By hypothesis, $p(a) = 0$, so $c = 0$.
::: {.proof}
hypothesis $p(a) = 0$.
:::
<2>3. Thus the remainder polynomial is zero: $r(x) = 0$.
::: {.proof}
<2>1 and <2>2.
:::

<1>3. Conclusion: $p(x) = (x - a) q(x)$ for $q(x) \in E[x]$.
::: {.proof}
<1>1 and <1>2.
:::
Q.E.D.
:::
