---
schema: qual/card@1
id: P-ALGS13G
kind: problem
title: Finite separable degrees are $p$-powers when all finite degrees are divisible by $p$
classification:
  areas:
  - algebra
  topics:
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Let $F$ be a field and $p$ be a prime.
Suppose that the degree of any finite field extension $E/F$ is divisible by $p$.
Prove that the degree of any finite separable extension $E/F$ is a power of $p$.
:::

::: {.solution}
<1>1. Let $E/F$ be finite separable and let $N$ be its normal closure; then $N/F$ is finite Galois with $G=\Gal(N/F)$.
::: {.proof}
normal closure of separable extension is Galois.
:::

<1>2. For any $H\le G$, $[N^H\!:\!F]=[G\!:\!H]$.
::: {.proof}
Galois correspondence.
:::

<1>3. By hypothesis every $N^H/F$ with $H<G$ has degree divisible by $p$, so every proper $H<G$ has $[G\!:\!H]$ divisible by $p$.
::: {.proof}
<1>2.
:::

<1>4. Hence every maximal subgroup of $G$ has index $p$.
::: {.proof}
maximal subgroups have prime index; by <1>3 the prime is $p$.
:::

<1>5. A finite group whose maximal subgroups all have index $p$ is a $p$-group.
::: {.proof}
induction on $|G|$ (if $G$ not $p$-group, a Sylow $q$-subgroup for $q\neq p$ lies in a maximal subgroup of index $q$).
:::

<1>6. So $|G|$ is a power of $p$, hence $[E\!:\!F]=[G\!:\!H]$ is a power of $p$.
::: {.proof}
<1>5 and <1>2 with $H=\Gal(N/E)$.
:::

<1>7. Q.E.D.
::: {.proof}
<1>6.
:::
:::
