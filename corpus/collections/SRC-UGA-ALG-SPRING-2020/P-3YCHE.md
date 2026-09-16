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
A finite extension $E/F$ is Galois if it is both normal and separable over $F$; equivalently, if $E$ is the splitting field over $F$ of a separable polynomial.

Let $\alpha=2^{1/4}$. The roots of $x^4-2$ are
\[
\alpha,-\alpha,i\alpha,-i\alpha,
\]
so the splitting field is
\[
E=\mathbb Q(\alpha,i).
\]
By Eisenstein at $2$, $x^4-2$ is irreducible, hence $[\mathbb Q(\alpha):\mathbb Q]=4$. Since $\mathbb Q(\alpha)\subset\mathbb R$, it does not contain $i$, so
\[
[E:\mathbb Q]=8.
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
\operatorname{Gal}(E/\mathbb Q)\cong D_8,
\]
the dihedral group of order $8$.

Take
\[
K=\mathbb Q(\alpha).
\]
This is an intermediate field of degree $4$, but it is not normal over $\mathbb Q$: the irreducible polynomial $x^4-2$ has the root $\alpha\in K$ but the conjugate root $i\alpha\notin K$ because $K\subset\mathbb R$. Hence $K/\mathbb Q$ is not Galois.
:::
