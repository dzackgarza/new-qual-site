---
schema: qual/card@1
id: P-ALGPAN11-14
kind: problem
title: Remainders in the Euclidean algorithm for 273 and 110
classification:
  areas:
  - algebra
  topics: []
relations: []
review: draft
audit:
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the retained Pantano 2011 algebra-review source scan and verified from the stated algebraic criterion.
---

::: {.problem}
![Source scan for this review problem.](../../../assets/attachments/algebra-review-pantano-2011/problem-14.png)
:::

::: {.solution}
Assertions II and III must hold, while I need not.
Hence the answer is $\boxed{\text{(D)}}$.

<1>1. Assertion II follows by induction.
::: {.proof}
For $n=1$ it is tautological.
If
\[
n(x\oplus y)=nx\oplus ny,
\]
then, using associativity and commutativity of $\oplus$,
\[
(n+1)(x\oplus y)
=n(x\oplus y)\oplus(x\oplus y)
=(nx\oplus x)\oplus(ny\oplus y)
=(n+1)x\oplus(n+1)y.
\]
:::

<1>2. Assertion III follows from associativity of $\odot$.
::: {.proof}
For fixed $x$, induction on $n$ gives
\[
x^m\odot x^n=x^{m+n}.
\]
Indeed the step from $n$ to $n+1$ is
\[
x^m\odot x^{n+1}
=x^m\odot(x^n\odot x)
=(x^m\odot x^n)\odot x
=x^{m+n+1}.
\]
:::

<1>3. Assertion I can fail.
::: {.proof}
Take $S=S_3$, let $\odot$ be its group multiplication, and transport the group law of the cyclic group $C_6$ to the same six-element set to define a commutative associative operation $\oplus$.
For noncommuting $x,y\in S_3$,
\[
(xy)^2=xyxy\ne xxyy=x^2y^2
\]
in general.
Thus I is not forced by the stated axioms.
:::
:::
