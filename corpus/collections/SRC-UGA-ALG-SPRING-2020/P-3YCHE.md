---
schema: qual/card@1
id: P-3YCHE
kind: problem
title: Galois group of $x^4-2$ over $\QQ$ and a non-Galois intermediate field
classification:
  areas:
  - algebra
  topics:
  - Galois Theory
  - Splitting Fields
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-10
---

::: {.problem}
Let $f(x) = x^4-2 \in \QQ[x]$.

a. Define what it means for a finite extension field $E$ of a field $F$ to be a Galois extension.

b. Determine the Galois group $\gal(E/\QQ)$ for the polynomial $f(x)$, and justify your answer carefully.

c. Exhibit a subfield $K$ in $(b)$ such that $\QQ \leq K \leq E$ with $K$ not a Galois extension over $\QQ$.
Explain.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

A finite extension is Galois precisely when it is normal and separable.


::: pf-proof

A finite extension $E/F$ is Galois if it is both normal and separable over $F$; equivalently, if $E$ is the splitting field over $F$ of a separable polynomial.

:::

:::

::: {.pf-step #s1-2}

The splitting field $E$ of $x^4-2$ has degree eight over $\QQ$ and Galois group isomorphic to the dihedral group $D_8$.


::: pf-proof

Let $\alpha=2^{1/4}$. The roots of $x^4-2$ are
\[
\alpha,-\alpha,i\alpha,-i\alpha,
\]
so the splitting field is
\[
E=\QQ(\alpha,i).
\]
By Eisenstein at $2$, $x^4-2$ is irreducible, hence $[\QQ(\alpha):\QQ]=4$. Since $\QQ(\alpha)\subset\RR$, it does not contain $i$, so
\[
[E:\QQ]=8.
\]
Define automorphisms
\[
r(\alpha)=i\alpha,\qquad r(i)=i,
\]
and
\[
s(\alpha)=\alpha,\qquad s(i)=-i.
\]
Then $r$ has order $4$, $s$ has order $2$, and
\[
srs=r^{-1}.
\]
These generate $8$ distinct automorphisms, so
\[
\operatorname{Gal}(E/\QQ)\cong D_8,
\]
the dihedral group of order $8$.

:::

:::

::: {.pf-step #s1-3}

The intermediate field $K=\QQ(\alpha)$ is not Galois over $\QQ$.


::: pf-proof

Take
\[
K=\QQ(\alpha).
\]
This is an intermediate field of degree $4$, but it is not normal over $\QQ$: the irreducible polynomial $x^4-2$ has the root $\alpha\in K$ but the conjugate root $i\alpha\notin K$ because $K\subset\RR$. Hence $K/\QQ$ is not Galois.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} and [](#s1-2){.pf-ref}, and [](#s1-3){.pf-ref} prove parts (a), (b), and (c), respectively.

:::

:::

:::
