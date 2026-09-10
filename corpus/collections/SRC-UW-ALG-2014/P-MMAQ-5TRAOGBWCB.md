---
schema: qual/card@1
id: P-MMAQ-5TRAOGBWCB
kind: problem
title: $x^p-t$ is irreducible over $\mathbb{F}_p(t)$ and splits as a $p$-th power
  in its splitting field
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Splitting Fields
  - Irreducibility Criteria
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-10
---

::: problem
Let $p$ be a prime, let $\mathbb F_p$ be the $p$-element field,
and let $K=\mathbb F_p(t)$ be the field of rational functions in
$t$ with coefficients in $\mathbb F_p$. Consider the polynomial $f(x)=
x^p-t\in K[x]$.

-   Show that $f$ does not have a root in $K$.

-   Let $E$ be the splitting field of $f$ over $K$.
    Find the factorization of $f$ over $E$.

-   Conclude that $f$ is irreducible over $K$.
:::


::: solution
<1>1. The polynomial \(f(X)=X^p-t\) has no root in \(K=\mathbb F_p(t)\).
::: {.proof}
Suppose \(r\in K\) satisfies \(r^p=t\). Write
\[
r=\frac{a(t)}{b(t)}
\]
with coprime \(a,b\in\mathbb F_p[t]\), \(b\ne0\). Then
\[
a(t)^p=t\,b(t)^p.
\]
Let \(v_t\) denote the exponent of the irreducible polynomial \(t\) in a nonzero polynomial. Taking \(v_t\) gives
\[
p\,v_t(a)=1+p\,v_t(b),
\]
which is impossible modulo \(p\). Hence \(f\) has no root in \(K\).
:::

<1>2. If \(\alpha\) is a root of \(f\) in a splitting field \(E\), then
\[
f(X)=(X-\alpha)^p
\]
in \(E[X]\).
::: {.proof}
We have \(\alpha^p=t\). Since the characteristic is \(p\), all intermediate binomial coefficients \(\binom pj\) vanish in \(\mathbb F_p\), so
\[
(X-\alpha)^p=X^p-\alpha^p=X^p-t=f(X).
\]
Thus \(\alpha\) is the unique root of \(f\) in an algebraic closure, with multiplicity \(p\).
:::

<1>3. The polynomial \(f(X)=X^p-t\) is irreducible over \(K\).
::: {.proof}
Suppose \(f\) were reducible in \(K[X]\). Since \(f\) is monic, it would have a monic factor \(g\in K[X]\) of degree \(r\) with
\[
1\le r\le p-1.
\]
Over the splitting field \(E\), <1>2 shows that every root of \(g\) must equal \(\alpha\). Hence
\[
g(X)=(X-\alpha)^r.
\]
The coefficient of \(X^{r-1}\) in this polynomial is \(-r\alpha\). Because \(1\le r<p\), the element \(r\in\mathbb F_p\) is nonzero, hence invertible. Since \(g\in K[X]\), we obtain
\[
\alpha=-r^{-1}[X^{r-1}]g\in K,
\]
contradicting <1>1. Therefore \(f\) is irreducible over \(K\).
:::
:::
