---
schema: qual/card@1
id: P-WP76T
kind: problem
title: Maximal subgroups of a $p$-group have index $p$
classification:
  areas:
  - algebra
  topics:
  - p-Groups
  - Subgroups
  - Cosets and Lagrange
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
---

::: problem
- Show that every maximal subgroup of a $p\dash$group has index $p$.
:::

::: {.solution}
<1>1. Let $G$ be a finite $p$-group and $M$ a maximal subgroup of $G$.
::: {.proof}
setup.
:::

<1>2. $M$ is normal in $G$.
<2>1. $M$ is contained in its normalizer $N_G(M)$, and by maximality $N_G(M) = M$ or $N_G(M) = G$.
::: {.proof}
$M \le N_G(M) \le G$, and $M$ is maximal.
:::
<2>2. $N_G(M) \neq M$.
::: {.proof}
in a $p$-group, a proper subgroup is strictly contained in its normalizer (a standard fact: $N_G(M) > M$ for any proper subgroup $M$ of a $p$-group).
:::
<2>3. Hence $N_G(M) = G$, so $M \trianglelefteq G$.
::: {.proof}
<2>1 and <2>2.
:::

<1>3. $G/M$ is a group of order $p^k$ for some $k \ge 1$.
::: {.proof}
$|G| = p^n$ and $|M|$ divides $p^n$, so $|G/M| = p^k$.
:::

<1>4. $G/M$ has no proper nontrivial subgroup.
::: {.proof}
if $G/M$ had a proper nontrivial subgroup $H/M$, then $M < H < G$, contradicting the maximality of $M$.
:::

<1>5. Hence $G/M$ is a group of prime order, so $|G/M| = p$.
::: {.proof}
a group with no proper nontrivial subgroup is cyclic of prime order; since $|G/M| = p^k$ is a power of $p$, the prime is $p$.
:::

<1>6. Therefore $[G : M] = |G/M| = p$.
::: {.proof}
<1>5.
:::

<1>7. Q.E.D.
::: {.proof}
<1>6.
:::
:::
