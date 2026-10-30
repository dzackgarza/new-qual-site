---
schema: qual/card@1
id: P-UGAP08S-01
kind: problem
title: Left cancellation by an injective function
classification:
  areas: [prelim]
  topics:
  - Functions and Relations
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
$$
f\circ g=f\circ h,
$$
then $g=h$.
:::

::: {.solution}

::: pf

::: pf-step

Let
$$
x\in A
$$
be arbitrary.


::: pf-proof

To prove equality of functions
$$
g=h,
$$
it suffices to prove
$$
g(x)=h(x)
$$
for every $x\in A$.

:::

:::

::: {.pf-step #s1-2}

The hypothesis
$$
f\circ g=f\circ h
$$
gives
$$
f(g(x))=f(h(x)).
$$


::: pf-proof

Evaluate the two equal functions at the chosen point $x$.

:::

:::

::: {.pf-step #s1-3}

Since $f$ is injective,
$$
g(x)=h(x).
$$


::: pf-proof

Injectivity means
$$
f(a)=f(b)
\quad\Longrightarrow\quad
a=b.
$$
Apply this to
$$
a=g(x),
\qquad
b=h(x),
$$
using step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{
g=h.
}
$$


::: pf-proof

The point $x\in A$ was arbitrary, so step [](#s1-3){.pf-ref} holds for every $x$.
Thus the two functions agree pointwise.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} is the desired conclusion.

:::

:::

:::
