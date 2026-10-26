---
schema: qual/card@1
id: P-WESTOP09-II5
kind: problem
title: A diagram chase proving injectivity of the middle vertical map
classification: {areas: [topology], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: The source diagram is represented only by an image placeholder in the retained Markdown. The text preserves the exactness of both rows, commutativity, and the hypotheses on the vertical maps alpha, beta, gamma, and delta, but not the object or horizontal-map labels.
---

::: {.problem}
Consider the commutative diagram in the source, whose two rows are exact. The vertical maps are labeled $\alpha,\beta,\gamma,\delta$ in order. Prove that if $\alpha$ is surjective and $\beta$ and $\delta$ are injective, then $\gamma$ is injective.

The objects and horizontal-map labels in the diagram are unrecovered from the retained Markdown extraction.
:::

Write the two exact rows abstractly as
\[
A\xrightarrow{f}B\xrightarrow{g}C\xrightarrow{h}D
\]
and
\[
A'\xrightarrow{f'}B'\xrightarrow{g'}C'\xrightarrow{h'}D',
\]
with vertical maps
\[
\alpha:A\to A',
\qquad
\beta:B\to B',
\qquad
\gamma:C\to C',
\qquad
\delta:D\to D'.
\]
Commutativity means
\[
\beta f=f'\alpha,
\qquad
\gamma g=g'\beta,
\qquad
\delta h=h'\gamma.
\]

::: pf

::: pf-step

Let
\[
c\in C
\]
and assume
\[
\gamma(c)=0.
\]
Then
\[
h(c)=0.
\]


::: pf-proof

By commutativity of the right square,
\[
\delta(h(c))
=
h'(\gamma(c))
=
h'(0)
=
0.
\]
Since
\[
\delta
\]
is injective,
\[
h(c)=0.
\]

:::

:::

::: pf-step

There exists
\[
b\in B
\]
such that
\[
g(b)=c.
\]


::: pf-proof

Exactness of the top row at $C$ gives
\[
\ker h
=
\operatorname{im}g.
\]
By step <1>1,
\[
c\in\ker h,
\]
so
\[
c=g(b)
\]
for some $b\in B$.

:::

:::

::: pf-step

One has
\[
\beta(b)\in\ker g'.
\]


::: pf-proof

Using step <1>2 and commutativity of the middle square,
\[
g'(\beta(b))
=
\gamma(g(b))
=
\gamma(c)
=
0.
\]
Thus
\[
\beta(b)\in\ker g'.
\]

:::

:::

::: pf-step

There exists
\[
a'\in A'
\]
such that
\[
f'(a')=\beta(b).
\]


::: pf-proof

Exactness of the bottom row at $B'$ gives
\[
\ker g'
=
\operatorname{im}f'.
\]
Apply this to step <1>3.

:::

:::

::: pf-step

There exists
\[
a\in A
\]
such that
\[
\alpha(a)=a'.
\]


::: pf-proof

The map
\[
\alpha:A\to A'
\]
is surjective by hypothesis.

:::

:::

::: pf-step

One has
\[
\beta\bigl(b-f(a)\bigr)=0.
\]


::: pf-proof

By step <1>4,
\[
\beta(b)
=
f'(a').
\]
By step <1>5,
\[
a'=\alpha(a),
\]
so
\[
\beta(b)
=
f'(\alpha(a)).
\]
Commutativity of the left square gives
\[
f'\alpha
=
\beta f.
\]
Hence
\[
\beta(b)
=
\beta(f(a)).
\]
Subtracting,
\[
\beta\bigl(b-f(a)\bigr)=0.
\]

:::

:::

::: pf-step

One has
\[
b=f(a).
\]


::: pf-proof

The map
\[
\beta:B\to B'
\]
is injective. Apply injectivity to step <1>6.

:::

:::

::: pf-step

Therefore
\[
c=0.
\]


::: pf-proof

By step <1>2,
\[
c=g(b).
\]
By step <1>7,
\[
b=f(a),
\]
so
\[
c
=
g(f(a)).
\]
Exactness of the top row at $B$ implies
\[
\operatorname{im}f
\subseteq
\ker g,
\]
equivalently
\[
g\circ f=0.
\]
Thus
\[
c=0.
\]

:::

:::

::: pf-step

The map
\[
\boxed{
\gamma:C\to C'
}
\]
is injective.


::: pf-proof

Steps <1>1--<1>8 show that
\[
\gamma(c)=0
\quad\Longrightarrow\quad
c=0.
\]
Thus
\[
\ker\gamma=0.
\]

:::

:::

::: pf-qed

Step <1>9 is exactly the desired injectivity.

:::

:::
