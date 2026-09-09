---
schema: qual/card@1
id: E-AMD-TSKS3JTO
kind: problem
title: $x^{p^n}-x$ is the product of monic irreducibles in $\FF_p[x]$ of degree dividing
  $n$
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Factorization
  - Irreducibility Criteria
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: {.exercise}
Show that $x^{p^n} - x = \prod f_i(x)$ over all irreducible monic $f_i$ of degree $d$ dividing $n$.
:::


::: {.solution}
Work in an algebraic closure $\overline{\FF}_p$.

<1>1. The roots of $x^{p^n}-x$ are exactly the elements fixed by the $n$th power of Frobenius.
::: {.proof}
For $\alpha\in\overline{\FF}_p$,
\[
\alpha^{p^n}-\alpha=0
\quad\Longleftrightarrow\quad
\alpha^{p^n}=\alpha.
\]
These fixed points form the finite field $\FF_{p^n}$.
:::

<1>2. The polynomial $x^{p^n}-x$ is squarefree.
::: {.proof}
Its derivative in characteristic $p$ is
\[
\frac{d}{dx}(x^{p^n}-x)=p^n x^{p^n-1}-1=-1,
\]
so it has no repeated roots.
:::

<1>3. Let $f\in\FF_p[x]$ be monic irreducible of degree $d$, and let $\alpha$ be a root. Then $f\mid x^{p^n}-x$ if and only if $d\mid n$.
::: {.proof}
The roots of $f$ are the Frobenius conjugates
\[
\alpha,\alpha^p,\ldots,\alpha^{p^{d-1}},
\]
and $d$ is the least positive integer with $\alpha^{p^d}=\alpha$. Hence
\[
f\mid x^{p^n}-x
\quad\Longleftrightarrow\quad
\alpha^{p^n}=\alpha
\quad\Longleftrightarrow\quad
d\mid n.
\]
Indeed, writing $n=qd+r$ with $0\le r<d$, the equality $\alpha^{p^n}=\alpha$ and $\alpha^{p^d}=\alpha$ imply $\alpha^{p^r}=\alpha$; minimality of $d$ forces $r=0$.
:::

<1>4. Therefore
\[
x^{p^n}-x=\prod_{\substack{f\text{ monic irreducible in }\FF_p[x]\\ \deg f\mid n}} f(x).
\]
::: {.proof}
By <1>3, the irreducible divisors are exactly the displayed factors. By <1>2, each occurs with multiplicity one. Since both sides are monic, their irreducible factorizations agree exactly.
:::
:::
