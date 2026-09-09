---
schema: qual/card@1
id: P-NPHUQ
kind: problem
title: $x^{p^n}-x$ is the product of all monic irreducibles of degree dividing $n$
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

::: problem
Show that over $\FF_p$,
\[
x^{p^n}-x
\]
is the product of all monic irreducible polynomials whose degrees divide $n$, each occurring once.
:::

::: {.solution}
The roots of
\[
x^{p^n}-x
\]
in an algebraic closure of $\FF_p$ are exactly the elements of the finite field
\[
\FF_{p^n}.
\]
Moreover,
\[
\frac{d}{dx}(x^{p^n}-x)=-1,
\]
so the polynomial is squarefree.

Let $f\in\FF_p[x]$ be monic irreducible of degree $d$, and let $\alpha$ be one of its roots. Then
\[
\FF_p(\alpha)\cong\FF_{p^d}.
\]
Therefore
\[
f\mid x^{p^n}-x
\]
if and only if $\alpha\in\FF_{p^n}$, equivalently
\[
\FF_{p^d}\subseteq\FF_{p^n}.
\]
The subfield theorem for finite fields gives
\[
\FF_{p^d}\subseteq\FF_{p^n}
\iff d\mid n.
\]

Hence the irreducible factors of $x^{p^n}-x$ are exactly the monic irreducibles whose degrees divide $n$. Since the polynomial is squarefree, each occurs with multiplicity one. Thus
\[
x^{p^n}-x
=\prod_{\substack{f\text{ monic irreducible}\\ \deg f\mid n}} f(x).
\]
:::
