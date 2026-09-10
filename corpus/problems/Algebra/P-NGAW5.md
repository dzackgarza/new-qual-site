---
schema: qual/card@1
id: P-NGAW5
kind: problem
title: Eisenstein's criterion
classification:
  areas:
  - algebra
  topics:
  - Irreducibility Criteria
  - Polynomials
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
State and prove Eisenstein's criterion.
:::

::: {.solution}
Let
\[
f(x)=a_nx^n+\cdots+a_1x+a_0\in\ZZ[x]
\]
be primitive. Suppose there is a prime $p$ such that
\[
p\nmid a_n,
\qquad
p\mid a_i\quad(0\le i<n),
\qquad
p^2\nmid a_0.
\]
Then $f$ is irreducible in $\QQ[x]$.

::: {.proof}
By Gauss's lemma it is enough to prove irreducibility in $\ZZ[x]$. Suppose
\[
f=gh
\]
with nonconstant $g,h\in\ZZ[x]$. Reduce modulo $p$. Since all nonleading coefficients of $f$ vanish modulo $p$,
\[
\bar f=\bar a_n x^n
\]
in $\FF_p[x]$. Thus
\[
\bar g=cx^r,
\qquad
\bar h=dx^s
\]
for some $r,s\ge1$ and nonzero $c,d\in\FF_p$.

Therefore the constant terms of both $g$ and $h$ are divisible by $p$. Their product is $a_0$, so
\[
p^2\mid a_0,
\]
contradicting the hypothesis.

Hence no nontrivial factorization exists, and $f$ is irreducible over $\QQ$.
:::
:::
