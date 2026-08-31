---
schema: qual/card@1
id: P-HHEF6
kind: problem
title: Jordan–Hölder theorem
classification:
  areas:
  - algebra
  topics:
  - Subgroup Series
  - Simple Groups
  - Classification
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
State and prove the Jordan-Holder theorem for finite groups.
:::

::: {.solution}
<1>1. Statement: any two composition series of a finite group $G$ have the same length, and the same composition factors (up to isomorphism and permutation).
::: {.proof}
statement of the Jordan–Hölder theorem.
:::

<1>2. Proof by induction on $|G|$.
::: {.proof}
setup.
:::

<1>3. Let $1 = G_0 \trianglelefteq G_1 \trianglelefteq \cdots \trianglelefteq G_m = G$ and $1 = H_0 \trianglelefteq H_1 \trianglelefteq \cdots \trianglelefteq H_n = G$ be two composition series.
::: {.proof}
take two composition series.
:::

<1>4. If $G_1 = H_1$, then by induction the series $G_1 \trianglelefteq \cdots \trianglelefteq G$ and $H_1 \trianglelefteq \cdots \trianglelefteq H$ have the same factors, so the full series do too.
::: {.proof}
induction hypothesis applied to $G_1 = H_1$.
:::

<1>5. If $G_1 \neq H_1$, then $G_1 H_1 = G$ (since $G_1$ and $H_1$ are distinct maximal normal subgroups, their product is $G$).
::: {.proof}
$G_1 H_1$ is a normal subgroup of $G$ containing $G_1$ properly, so by maximality of $G_1$ it is $G$.
:::

<1>6. By the second isomorphism theorem, $G/G_1 \cong H_1/(G_1 \cap H_1)$ and $G/H_1 \cong G_1/(G_1 \cap H_1)$.
::: {.proof}
second isomorphism theorem.
:::

<1>7. Let $1 = K_0 \trianglelefteq \cdots \trianglelefteq K_r = G_1 \cap H_1$ be a composition series of $G_1 \cap H_1$.
::: {.proof}
$G_1 \cap H_1$ has a composition series.
:::

<1>8. Then $G$ has composition series with factors: (factors of $G_1 \cap H_1$), $G_1/(G_1 \cap H_1)$, $G/G_1$, and also (factors of $G_1 \cap H_1$), $H_1/(G_1 \cap H_1)$, $G/H_1$.
::: {.proof}
refine the series through $G_1 \cap H_1$.
:::

<1>9. By <1>6, the multiset $\{G_1/(G_1 \cap H_1), G/G_1\}$ equals $\{H_1/(G_1 \cap H_1), G/H_1\}$.
::: {.proof}
<1>6.
:::

<1>10. Hence the two composition series have the same factors (up to isomorphism and permutation).
::: {.proof}
<1>8 and <1>9.
:::

<1>11. Q.E.D.
::: {.proof}
<1>10.
:::
:::
