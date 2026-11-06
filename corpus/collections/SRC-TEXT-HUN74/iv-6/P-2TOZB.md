---
schema: qual/card@1
id: P-2TOZB
kind: problem
title: Free modules over domains are torsion-free, but not conversely
classification:
  areas:
  - algebra
  topics:
  - Free Modules
  - Torsion
  - Integral Domains
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against an independent reproduction of the Hungerford IV.6 exercise statement.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: source-checked
  by: claude
  date: 2026-11-06
  note: >-
    Read against the printed exercise, Hungerford, Algebra (1974), section IV.6,
    exercise 2, book page 226, read from the page image: "Every free module over
    an arbitrary integral domain with identity is torsion-free. The converse is
    false (Exercise II.1.10)." The card states both halves and replaces the
    book's cross-reference by its content, Q as a torsion-free non-free Z-module,
    which is exactly what II.1.10(b) establishes. The proof was checked: a
    vanishing multiple of a finite basis expansion has all coefficients zero by
    independence, and a domain has no zero divisors; and Q is divisible, so
    halving a basis element and comparing basis coordinates in b = Σ 2n_i b_i
    would make the coefficient of b both 1 and even. Complete; no defect.
---

::: {.problem}
Show that every free module over a unital integral domain is torsion-free.
Show that the converse is false: $\QQ$ is a torsion-free $\ZZ$-module that is not free.
:::

::: {.solution}

::: pf

::: pf-step

Every free module over a unital integral domain is torsion-free.

::: pf-proof

Let $R$ be a unital integral domain and let $F$ be a free $R$-module with basis
$B$. Suppose $0\ne r\in R$ and $x\in F$ satisfy $rx=0$. Write the unique finite
basis expansion
$$
x=\sum_{i=1}^n a_i b_i,
$$
where the $b_i\in B$ are distinct. Then
$$
0=rx=\sum_{i=1}^n (ra_i)b_i.
$$
Linear independence of $B$ gives $ra_i=0$ for every $i$. Since $R$ is an
integral domain and $r\ne0$, each $a_i=0$. Thus $x=0$. Hence $F$ has no
nonzero torsion element.

:::

:::

::: pf-step

The converse is false.

::: pf-proof

Take $R=\ZZ$ and the $\ZZ$-module $\QQ$. It is torsion-free: if
$0\ne n\in\ZZ$ and $q\in\QQ$ satisfy $nq=0$, then $q=0$.

We show that $\QQ$ is not free as a $\ZZ$-module. Suppose it had a basis $B$,
and choose $b\in B$. Since $\QQ$ is divisible, there exists $c\in\QQ$ with
$2c=b$. Express
$$
c=\sum_{i=1}^m n_i b_i
$$
in the basis, where $n_i\in\ZZ$. Multiplying by $2$ gives
$$
b=\sum_{i=1}^m 2n_i b_i.
$$
By uniqueness of basis coordinates, the coefficient of $b$ on the right must be
$1$. But every coefficient there is even, a contradiction. Thus $\QQ$ is
torsion-free but not free.

:::

:::

:::

:::
