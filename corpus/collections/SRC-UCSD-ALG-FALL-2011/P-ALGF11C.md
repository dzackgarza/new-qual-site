---
schema: qual/card@1
id: P-ALGF11C
kind: problem
title: Unit ideal generators give an injective map into a product of localizations
classification:
  areas:
  - algebra
  topics:
  - Commutative Algebra
  - Localization
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Problem 3 of the official UCSD Algebra Qualifying Exam, Fall 2011; the statement agrees with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified the diagonal localization map and the bounded-exponent unit-ideal argument proving its kernel is zero.
---

::: {.problem}
Let $A$ be a commutative ring with unity, and assume that the elements $f_1, \ldots, f_n \in A$ generate the unit ideal $(1)$.
Show that there exists an injective ring homomorphism
\[
\phi \colon A \to \prod_{i=1}^n A_{f_i}.
\]
As usual, $A_f$ denotes the localization of $A$ at the set of powers of $f$.
:::


::: {.solution}
For each \(i\), let
\[
\lambda_i:A\longrightarrow A_{f_i}
\]
be the canonical localization map, and define
\[
\phi:A\longrightarrow\prod_{i=1}^n A_{f_i},
\qquad
\phi(a)=(\lambda_1(a),\ldots,\lambda_n(a)).
\]
This is a ring homomorphism.

::: pf

::: {.pf-step #power-annihilates}
If \(a\in\ker\phi\), then for every \(i\) some power of \(f_i\) annihilates \(a\).

::: pf-proof
Suppose \(a\in\ker\phi\).
Then
\[
\frac a1=0
\]
in \(A_{f_i}\) for every \(i\).
By the definition of localization, this means that for each \(i\) there exists an integer \(N_i\ge0\) such that
\[
f_i^{N_i}a=0.
\]
If necessary increase \(N_i\) so that \(N_i\ge1\).
:::

:::

::: {.pf-step #monomial-degree-bound}
There is an integer \(N\) such that every monomial of total degree \(N\) in \(f_1,\ldots,f_n\) is divisible by some \(f_i^{N_i}\).

::: pf-proof
Set
\[
N:=1+\sum_{i=1}^n(N_i-1).
\]
Consider a monomial
\[
f_1^{e_1}\cdots f_n^{e_n}
\]
with
\[
\sum_i e_i=N.
\]
If \(e_i<N_i\) for every \(i\), then
\[
\sum_i e_i\le\sum_i(N_i-1)=N-1,
\]
a contradiction.
Thus for some \(i\),
\[
e_i\ge N_i,
\]
so the monomial is divisible by \(f_i^{N_i}\).
:::

:::

::: pf-step
The kernel of \(\phi\) is zero.

::: pf-proof
Because \(f_1,\ldots,f_n\) generate the unit ideal, choose \(r_1,\ldots,r_n\in A\) such that
\[
r_1f_1+\cdots+r_nf_n=1.
\]
Let \(a\in\ker\phi\), and choose \(N_i\) and \(N\) as in steps [](#power-annihilates){.pf-ref} and [](#monomial-degree-bound){.pf-ref}.
Then
\[
a
=1^N a
=(r_1f_1+\cdots+r_nf_n)^N a.
\]
After expanding, every summand is an \(A\)-multiple of a monomial of total degree \(N\) in the \(f_i\).
By step [](#monomial-degree-bound){.pf-ref}, each such monomial is divisible by some \(f_i^{N_i}\), and by step [](#power-annihilates){.pf-ref},
\[
f_i^{N_i}a=0.
\]
Hence every summand in the expansion vanishes, so
\[
a=0.
\]
Therefore \(\ker\phi=0\), and \(\phi\) is injective.
:::

:::

:::
:::
