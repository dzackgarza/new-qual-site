---
schema: qual/card@1
id: P-MMAQ-KGHDXFTO6Z
kind: problem
title: A finite field has irreducible polynomials of every positive degree
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Irreducibility Criteria
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: problem
Let $F$ be a finite field.
Show for any positive integer $n$ that there are irreducible polynomials of degree $n$ in $F[x]$.
:::

::: solution
<1>1. Write
\[
|F|=q.
\]
For $n=1$, an irreducible polynomial of degree $1$ is immediate, for example $x-a$ with $a\in F$.
:::

<1>2. Assume $n\ge2$, and let $\overline F$ be an algebraic closure of $F$. Define
\[
E=\{\alpha\in\overline F:\alpha^{q^n}=\alpha\}.
\]
Then $E$ is a field containing $F$.
::: {.proof}
The field $F$ has characteristic $p$ for some prime $p$, and $q$ is a power of $p$. If $a,b\in E$, then Frobenius gives
\[
(a+b)^{q^n}=a^{q^n}+b^{q^n}=a+b,
\]
and
\[
(ab)^{q^n}=a^{q^n}b^{q^n}=ab.
\]
Also $0,1\in E$. If $a\in E$ is nonzero, then
\[
(a^{-1})^{q^n}=(a^{q^n})^{-1}=a^{-1}.
\]
Hence $E$ is a subfield of $\overline F$.

For every $a\in F$, we have $a^q=a$, and therefore $a^{q^n}=a$. Thus $F\subseteq E$.
:::

<1>3. The field $E$ has exactly $q^n$ elements.
::: {.proof}
The polynomial
\[
P(x)=x^{q^n}-x
\]
has derivative
\[
P'(x)=q^n x^{q^n-1}-1=-1
\]
in characteristic $p$, because $p\mid q^n$. Thus $P$ has no repeated roots. Since $\overline F$ is algebraically closed, $P$ splits completely there into exactly $q^n$ distinct roots. By definition these roots are precisely the elements of $E$. Hence
\[
|E|=q^n.
\]
:::

<1>4. For each divisor $d$ of $n$, there is at most one subfield of $E$ having $q^d$ elements.
::: {.proof}
Let $K\subseteq E$ be a subfield with $|K|=q^d$. Every element $a\in K$ satisfies
\[
a^{q^d}=a.
\]
Therefore $K$ is contained in the root set of
\[
x^{q^d}-x.
\]
That polynomial has at most $q^d$ roots, while $K$ already has exactly $q^d$ elements. Hence $K$ is exactly its root set. Thus any subfield of $E$ with $q^d$ elements is uniquely determined.
:::

<1>5. Every proper intermediate field
\[
F\subseteq K\subsetneq E
\]
has $q^d$ elements for some proper divisor $d<n$ of $n$.
::: {.proof}
Since $E/F$ is a finite extension with
\[
[E:F]=n,
\]
the tower law gives
\[
[E:F]=[E:K][K:F].
\]
Thus
\[
d=[K:F]
\]
divides $n$. Because $K\ne E$, we have $d<n$. Since $|F|=q$, a $d$-dimensional vector space over $F$ has $q^d$ elements, so
\[
|K|=q^d.
\]
:::

<1>6. The union of all proper intermediate fields between $F$ and $E$ has fewer than $q^n$ elements.
::: {.proof}
By <1>4 and <1>5, there is at most one proper intermediate field for each proper divisor $d$ of $n$, and such a field has $q^d$ elements. Every proper divisor of $n$ is at most $n/2$. Hence the union has cardinality at most
\[
\sum_{\substack{d\mid n\\ d<n}}q^d
\le
\sum_{j=1}^{\lfloor n/2\rfloor}q^j.
\]
For $q\ge2$ and $n\ge2$,
\[
\sum_{j=1}^{\lfloor n/2\rfloor}q^j<q^n.
\]
Indeed, the left side is less than the full geometric sum
\[
1+q+\cdots+q^{n-1}=\frac{q^n-1}{q-1},
\]
and this is at most $q^n-1<q^n$. Thus the proper intermediate fields cannot cover $E$.
:::

<1>7. Choose
\[
\alpha\in E
\]
outside every proper intermediate field. Then
\[
F(\alpha)=E.
\]
::: {.proof}
The field $F(\alpha)$ is an intermediate field between $F$ and $E$. By the choice of $\alpha$, it cannot be proper. Hence it equals $E$.
:::

<1>8. The minimal polynomial of $\alpha$ over $F$ is irreducible of degree $n$.
::: {.proof}
By <1>7,
\[
F(\alpha)=E.
\]
Therefore
\[
\deg m_{\alpha,F}
=[F(\alpha):F]
=[E:F]
=n.
\]
By definition, the minimal polynomial $m_{\alpha,F}$ is irreducible in $F[x]$. Thus $F[x]$ contains an irreducible polynomial of degree $n$.
:::
