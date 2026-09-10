---
schema: qual/card@1
id: P-TKCUS
kind: problem
title: $x^{p^d}-x$ divides $x^{p^n}-x$ iff $d$ divides $n$
classification:
  areas:
  - algebra
  topics:
  - Finite Fields
  - Polynomials
  - Factorization
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
- event: solution-written
  by: OpenAI GPT-5.6 Sol
  date: 2026-09-09
---

::: problem
- Show that $x^{p^d} - x \divides x^{p^n} - x \iff d \divides n$
:::

::: {.solution}
Work in $\mathbb F_p[x]$. Factor
\[
x^{p^m}-x=x\bigl(x^{p^m-1}-1\bigr).
\]
Since the ring is a domain, cancellation of the common factor $x$ gives
\[
x^{p^d}-x\mid x^{p^n}-x
\iff
x^{p^d-1}-1\mid x^{p^n-1}-1.
\]
For positive integers $A,B$ over any field,
\[
x^A-1\mid x^B-1\iff A\mid B.
\]
Indeed, if $B=qA+r$ with $0\le r<A$, division by $x^A-1$ leaves remainder $x^r-1$, which vanishes exactly when $r=0$.

Hence
\[
x^{p^d}-x\mid x^{p^n}-x
\iff p^d-1\mid p^n-1.
\]
Finally, for integers $p>1$,
\[
p^d-1\mid p^n-1\iff d\mid n,
\]
by the same Euclidean-division argument on the exponents. Therefore
\[
\boxed{x^{p^d}-x\mid x^{p^n}-x\iff d\mid n}.
\]
:::
