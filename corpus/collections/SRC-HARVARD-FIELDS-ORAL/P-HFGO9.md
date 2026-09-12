---
schema: qual/card@1
id: P-HFGO9
kind: problem
title: A field containing a root of every polynomial is algebraically closed
classification:
  areas: [algebra]
  topics: [Field Theory]
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against the preserved Harvard Fields and Galois Theory oral-question extraction.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Suppose every nonconstant polynomial over a field $F$ has a root in $F$.
Prove that $F$ is algebraically closed.
:::

::: solution
Let
\[
f(x)\in F[x]
\]
be nonconstant. By hypothesis, $f$ has a root $\alpha_1\in F$. Therefore
\[
f(x)=(x-\alpha_1)f_1(x)
\]
for some $f_1(x)\in F[x]$ of degree one less than $f$.

<1>1. Repeating this argument factors $f$ completely into linear factors over
$F$.
::: proof
Proceed by induction on $\deg f$. The assertion is trivial in degree $1$.
For degree $n>1$, choose a root $\alpha_1\in F$ by hypothesis and write
\[
f=(x-\alpha_1)f_1,
\qquad
\deg f_1=n-1.
\]
If $f_1$ is nonconstant, the hypothesis applies to it as well, and the induction
hypothesis gives a factorization of $f_1$ into linear factors over $F$.
Thus $f$ splits completely over $F$.
:::

<1>2. Hence $F$ is algebraically closed.
::: proof
A field is algebraically closed precisely when every nonconstant polynomial over
it splits into linear factors, equivalently when every such polynomial has all
its roots in the field. This is exactly <1>1.
:::
:::
