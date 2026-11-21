---
schema: qual/card@1
id: P-BKS06-2B
kind: problem
title: Number of irreducible polynomials of prime degree over $\FF_2$
classification:
  areas: [prelim]
  topics:
  - Abstract Algebra
relations: []
review: draft
audit:
- event: solution-reviewed
  by: claude
  date: 2026-11-19
  note: >-
    Refereed, no defect found, and the count is right for the reason given: for n prime, every element
    of K = F_{2^n} outside F_2 has degree n over F_2, since its degree divides n and is not 1, and each
    irreducible of degree n is the minimal polynomial of exactly n elements of K, its n distinct
    conjugates. The 2^n - 2 non-rational elements are therefore partitioned into groups of n, giving
    (2^n - 2)/n. Checked that the n roots are distinct, which uses that F_2 is perfect so that f is
    separable, and that primeness of n is used only to exclude intermediate degrees.
---

::: {.problem}
Let $\FF_{2}$ be the field of $2$ elements.
Let $n$ be a prime.
Show that there are exactly $(2^{n} - 2)/n$ degree-$n$ irreducible polynomials in $\FF_{2}[x]$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Let $K=\FF_{2^n}$. Every $a\in K-\FF_2$ has a minimal polynomial over $\FF_2$ that is irreducible of degree $n$.

::: pf-proof

The degree $[\FF_2(a):\FF_2]$ divides $[K:\FF_2]=n$ and is not $1$. Since $n$ is prime, it is $n$.

:::

:::

::: {.pf-step #s2}

Every irreducible $f\in\FF_2[x]$ of degree $n$ is the minimal polynomial of exactly $n$ elements of $K-\FF_2$.

::: pf-proof

The field $\FF_2[x]/(f)$ has $2^n$ elements, so it is isomorphic to $K$, and $f$ has a root in $K$. The extension $K/\FF_2$ is normal, because $K$ is the splitting field of $x^{2^n}-x$, so $f$ splits in $K$. It has $n$ distinct roots because $K/\FF_2$ is separable. The roots are not in $\FF_2$ because $n\ge2$ and $f$ is irreducible. The polynomial $f$ is monic, because $1$ is the only nonzero element of $\FF_2$, so it is the minimal polynomial of each of its roots, and of no other element.

:::

:::

::: pf-qed

By steps [](#s1){.pf-ref} and [](#s2){.pf-ref}, the map that sends $a\in K-\FF_2$ to its minimal polynomial is onto the set of irreducible polynomials of degree $n$, and each fiber has $n$ elements. Since $\abs{K-\FF_2}=2^n-2$, there are exactly $(2^n-2)/n$ such polynomials.

:::

:::

:::
