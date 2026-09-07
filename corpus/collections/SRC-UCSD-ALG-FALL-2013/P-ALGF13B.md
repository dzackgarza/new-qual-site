---
schema: qual/card@1
id: P-ALGF13B
kind: problem
title: $D[x]$ a PID forces $D$ to be a field
classification:
  areas:
  - algebra
  topics:
  - Ideals
  - Polynomials
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Problem 2 of the official UCSD Algebra Qualifying Exam, Fall 2013; the statement agrees with the source.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified the principal-ideal argument showing every nonzero element of D is a unit.
---

::: {.problem}
Let $D$ be an integral domain.
Prove that if $D[x]$ is a PID, then $D$ is a field.
:::

::: {.solution}
Let \(0
eq a\in D\). We prove that \(a\) is a unit.

<1>1. The ideal \((a,x)\subseteq D[x]\) is principal.
::: {.proof}
By hypothesis \(D[x]\) is a principal ideal domain, so there exists \(f(x)\in D[x]\) such that
\[
(a,x)=(f).
\]
Thus \(f\mid a\) and \(f\mid x\) in \(D[x]\).
:::

<1>2. The generator \(f\) is a unit of \(D[x]\).
::: {.proof}
Because \(f\mid a\) and \(a
eq0\) is constant, degree additivity in the domain \(D[x]\) gives
\[
\deg f=0.
\]
Hence \(f\in D\setminus\{0\}\).
Since \(f\mid x\), write
\[
x=f g(x).
\]
Then \(g\) has degree \(1\). Write
\[
g(x)=cx+d
\qquad(c,d\in D).
\]
Comparing coefficients of \(x\) in \(x=f(cx+d)\) gives
\[
fc=1.
\]
Thus \(f\) is a unit in \(D\), hence also in \(D[x]\).
:::

<1>3. The element \(a\) is a unit in \(D\).
::: {.proof}
By <1>2,
\[
(a,x)=(f)=D[x].
\]
Therefore there exist \(r(x),s(x)\in D[x]\) such that
\[
1=a r(x)+x s(x).
\]
Evaluating at \(x=0\) yields
\[
1=a r(0).
\]
Hence \(a\) is a unit of \(D\).
:::

<1>4. Therefore \(D\) is a field.
::: {.proof}
Every nonzero element \(a\in D\) is a unit by <1>3, which is exactly the definition of a field for an integral domain.
:::
:::
