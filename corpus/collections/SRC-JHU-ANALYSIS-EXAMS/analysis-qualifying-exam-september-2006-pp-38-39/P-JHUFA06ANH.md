---
schema: qual/card@1
id: P-JHUFA06ANH
kind: problem
title: "Unique norming point for a functional on a space satisfying the parallelogram inequality"
classification:
  areas:
  - real-analysis
  topics:
  - Banach Spaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-08
  note: Checked against Problem 8 of the JHU Analysis Qualifying Exam, September 2006, in the preserved exam collection.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-08
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-08
---

::: {.problem}
Let $X$ be a real Banach space such that for all $x,y\in X$,
\[
\|x+y\|^2+\|x-y\|^2\le 2\|x\|^2+2\|y\|^2.
\]
Let $f:X\to\mathbb R$ be a linear functional with $\|f\|=1$. Prove that there exists a unique $x\in X$ such that
\[
\|x\|=1,
\qquad
f(x)=1.
\]
:::

::: {.solution}
<1>1. The norm satisfies the parallelogram identity.
::: {.proof}
Apply the assumed inequality to the pair $x+y,x-y$. Since
\[
(x+y)+(x-y)=2x,
\qquad
(x+y)-(x-y)=2y,
\]
we obtain
\[
4\|x\|^2+4\|y\|^2
\le 2\|x+y\|^2+2\|x-y\|^2.
\]
Dividing by $2$ gives
\[
2\|x\|^2+2\|y\|^2
\le \|x+y\|^2+\|x-y\|^2.
\]
Combining this with the original inequality yields equality:
\[
\|x+y\|^2+\|x-y\|^2
=2\|x\|^2+2\|y\|^2.
\]
:::

<1>2. The norm comes from a Hilbert-space inner product.
::: {.proof}
By the Jordan--von Neumann theorem, the parallelogram identity implies that
\[
\langle x,y\rangle
=\frac14\bigl(\|x+y\|^2-\|x-y\|^2\bigr)
\]
defines a real inner product whose induced norm is the given norm. Since $X$ is complete for that norm, $X$ is a Hilbert space.
:::

<1>3. Riesz representation gives existence and uniqueness of the norming point.
::: {.proof}
By the Riesz representation theorem, there exists a unique $u\in X$ such that
\[
f(x)=\langle x,u\rangle
\qquad(x\in X),
\]
and
\[
\|u\|=\|f\|=1.
\]
Therefore
\[
f(u)=\langle u,u\rangle=\|u\|^2=1,
\]
so $u$ is a required point.

If $x\in X$ also satisfies $\|x\|=1$ and $f(x)=1$, then
\[
1=\langle x,u\rangle\le\|x\|\,\|u\|=1.
\]
Equality holds in Cauchy--Schwarz. In a real Hilbert space this forces $x$ and $u$ to be linearly dependent, and because both have norm $1$ and $\langle x,u\rangle=1$, one must have $x=u$. Thus the norming point is unique.
:::
:::
