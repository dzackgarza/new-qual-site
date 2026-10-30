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
---

::: {.problem}
Suppose the diagram
$$
\begin{array}{ccccccccccccc}
0&\to&A&\xrightarrow{i}&B&\xrightarrow{j}&C&\xrightarrow{k}&D&\xrightarrow{\ell}&E&\to&0\\
&&\downarrow{\scriptstyle\alpha}&&\downarrow{\scriptstyle\beta}&&\downarrow{\scriptstyle\gamma}&&\downarrow{\scriptstyle\delta}&&\downarrow{\scriptstyle\varepsilon}&&\\
0&\to&A'&\xrightarrow{i'}&B'&\xrightarrow{j'}&C'&\xrightarrow{k'}&D'&\xrightarrow{\ell'}&E'&\to&0
\end{array}
$$
is commutative and that the rows are exact. Show that if $\alpha$ is surjective and $\beta$ and $\delta$ are injective, then $\gamma$ is injective.
:::

::: {.solution}

Only the part of the diagram from $A$ to $D$ is used. Write the maps
$i,j,k$ as $f,g,h$ and $i',j',k'$ as $f',g',h'$, so the two exact rows are
$$
A\xrightarrow{f}B\xrightarrow{g}C\xrightarrow{h}D
$$
and
$$
A'\xrightarrow{f'}B'\xrightarrow{g'}C'\xrightarrow{h'}D',
$$
with vertical maps
$$
\alpha:A\to A',
\qquad
\beta:B\to B',
\qquad
\gamma:C\to C',
\qquad
\delta:D\to D'.
$$
Commutativity means
$$
\beta f=f'\alpha,
\qquad
\gamma g=g'\beta,
\qquad
\delta h=h'\gamma.
$$

::: pf

::: {.pf-step #s1-1}

Let
$$
c\in C
$$
and assume
$$
\gamma(c)=0.
$$
Then
$$
h(c)=0.
$$


::: pf-proof

By commutativity of the right square,
$$
\delta(h(c))
=
h'(\gamma(c))
=
h'(0)
=
0.
$$
Since
$$
\delta
$$
is injective,
$$
h(c)=0.
$$

:::

:::

::: {.pf-step #s1-2}

There exists
$$
b\in B
$$
such that
$$
g(b)=c.
$$


::: pf-proof

Exactness of the top row at $C$ gives
$$
\ker h
=
\operatorname{im}g.
$$
By step [](#s1-1){.pf-ref},
$$
c\in\ker h,
$$
so
$$
c=g(b)
$$
for some $b\in B$.

:::

:::

::: {.pf-step #s1-3}

One has
$$
\beta(b)\in\ker g'.
$$


::: pf-proof

Using step [](#s1-2){.pf-ref} and commutativity of the middle square,
$$
g'(\beta(b))
=
\gamma(g(b))
=
\gamma(c)
=
0.
$$
Thus
$$
\beta(b)\in\ker g'.
$$

:::

:::

::: {.pf-step #s1-4}

There exists
$$
a'\in A'
$$
such that
$$
f'(a')=\beta(b).
$$


::: pf-proof

Exactness of the bottom row at $B'$ gives
$$
\ker g'
=
\operatorname{im}f'.
$$
Apply this to step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

There exists
$$
a\in A
$$
such that
$$
\alpha(a)=a'.
$$


::: pf-proof

The map
$$
\alpha:A\to A'
$$
is surjective by hypothesis.

:::

:::

::: {.pf-step #s1-6}

One has
$$
\beta\bigl(b-f(a)\bigr)=0.
$$


::: pf-proof

By step [](#s1-4){.pf-ref},
$$
\beta(b)
=
f'(a').
$$
By step [](#s1-5){.pf-ref},
$$
a'=\alpha(a),
$$
so
$$
\beta(b)
=
f'(\alpha(a)).
$$
Commutativity of the left square gives
$$
f'\alpha
=
\beta f.
$$
Hence
$$
\beta(b)
=
\beta(f(a)).
$$
Subtracting,
$$
\beta\bigl(b-f(a)\bigr)=0.
$$

:::

:::

::: {.pf-step #s1-7}

One has
$$
b=f(a).
$$


::: pf-proof

The map
$$
\beta:B\to B'
$$
is injective. Apply injectivity to step [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

Therefore
$$
c=0.
$$


::: pf-proof

By step [](#s1-2){.pf-ref},
$$
c=g(b).
$$
By step [](#s1-7){.pf-ref},
$$
b=f(a),
$$
so
$$
c
=
g(f(a)).
$$
Exactness of the top row at $B$ implies
$$
\operatorname{im}f
\subseteq
\ker g,
$$
equivalently
$$
g\circ f=0.
$$
Thus
$$
c=0.
$$

:::

:::

::: {.pf-step #s1-9}

The map
$$
\boxed{
\gamma:C\to C'
}
$$
is injective.


::: pf-proof

Steps [](#s1-1){.pf-ref} through [](#s1-8){.pf-ref} show that
$$
\gamma(c)=0
\quad\Longrightarrow\quad
c=0.
$$
Thus
$$
\ker\gamma=0.
$$

:::

:::

::: pf-qed

Step [](#s1-9){.pf-ref} is exactly the desired injectivity.

:::

:::

:::
