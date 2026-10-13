---
schema: qual/card@1
id: P-UGAP08S-01
kind: problem
title: Left cancellation by an injective function
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: The retained extraction drops the subject of “is injective”; the surrounding statement uniquely forces this to be f, since f∘g=f∘h is left-cancelled.
---

::: {.problem}
Suppose $f,g,h:A\to A$ are functions. Prove that if $f$ is injective and
\[
f\circ g=f\circ h,
\]
then $g=h$.
:::

::: {.solution}
<1>1. Let
\[
x\in A
\]
be arbitrary.

::: {.proof}
To prove equality of functions
\[
g=h,
\]
it suffices to prove
\[
g(x)=h(x)
\]
for every $x\in A$.
:::

<1>2. The hypothesis
\[
f\circ g=f\circ h
\]
gives
\[
f(g(x))=f(h(x)).
\]

::: {.proof}
Evaluate the two equal functions at the chosen point $x$.
:::

<1>3. Since $f$ is injective,
\[
g(x)=h(x).
\]

::: {.proof}
Injectivity means
\[
f(a)=f(b)
\quad\Longrightarrow\quad
a=b.
\]
Apply this to
\[
a=g(x),
\qquad
b=h(x),
\]
using step <1>2.
:::

<1>4. Therefore
\[
\boxed{
g=h.
}
\]

::: {.proof}
The point $x\in A$ was arbitrary, so step <1>3 holds for every $x$.
Thus the two functions agree pointwise.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the desired conclusion.
:::
:::
