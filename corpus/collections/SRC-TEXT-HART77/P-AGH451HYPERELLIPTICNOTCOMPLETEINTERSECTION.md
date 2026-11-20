---
schema: qual/card@1
id: P-AGH451HYPERELLIPTICNOTCOMPLETEINTERSECTION
kind: problem
title: A hyperelliptic curve is never a complete intersection
classification:
  areas:
  - algebraic-geometry
  topics:
  - Hyperelliptic Curves
  - Canonical Divisor
  - Embeddings
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.5.1 together with the cited Exercise IV.3.3 and the
    definition of hyperelliptic curves in IV.1.7. Cross-checked the canonical
    very-ampleness obstruction against standard treatments of the
    hyperelliptic canonical map.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    A retained solution read at this exercise. Read Yang Pi-Yeh, Hartshorne
    Solutions (9 June 2019), Solution 4.5.1, printed p. 95,
    rendered as page images from
    tmp/sources/lfwin-hartshorne-solutions.pdf, whose PDF page is the printed
    page. Checked against the book: Hartshorne IV.5.1, whose printed page
    the card's earlier events record; this pass did not reopen it, and the
    comparison is against the statement the card carries. Recomputed the contradiction's shape: (4.3.3) applies only for $g\ge2$, which is the range in which a hyperelliptic curve has a $g^1_2$, and (5.2) gives $\abs K=(g-1)g^1_2$ there, so the two statements are mutually exclusive for every $g\ge2$.
    Not checked: Yang's Solutions outside printed p. 95; the
    book's own page in this pass; and the printed book itself.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    The card now carries a published-solution remark naming Yang Pi-Yeh's
    Solution 4.5.1 at printed p. 95; it had none before. No
    step, statement or hypothesis of the card changes.
---

::: {.problem}
Show that a hyperelliptic curve can never be a complete intersection in any projective space.
Cf. (Ex. 3.3).
:::

::: {.solution}
The argument is the card's own, and it is checked against Hartshorne's Exercise IV.5.1, printed p. 348. Yang Pi-Yeh, *Hartshorne Solutions*, Solution 4.5.1, printed p. 95, gives it in one line from (4.3.3) and Proposition 5.2; the steps below write out the argument those two results carry, starting from the hyperelliptic involution.

Let $X$ be hyperelliptic of genus $g\ge2$.  Choose a finite morphism
$$
f:X\longrightarrow\PP^1
$$
of degree $2$, and let
$$
D=f^*(Q)
$$
for some point $Q\in\PP^1$.

::: pf

::: {.pf-step #s1}

The divisor $D$ satisfies
$$
\deg D=2,
\qquad
\ell(D)\ge2.
$$

::: pf-proof

Since $f$ has degree $2$,
$$
\deg f^*(Q)=2.
$$
Moreover
$$
\OO_X(D)\cong f^*\OO_{\PP^1}(1).
$$
Pullback of the two-dimensional space
$$
H^0(\PP^1,\OO_{\PP^1}(1))
$$
injects into $H^0(X,\OO_X(D))$, because $f$ is surjective.  Hence
$$
\ell(D)\ge2.
$$

:::

:::

::: {.pf-step #s2}

For every canonical divisor $K$ on $X$,
$$
\boxed{\ell(K-D)\ge g-1.}
$$

::: pf-proof

Riemann--Roch applied to $D$ gives
$$
\ell(D)-\ell(K-D)
=
\deg D+1-g
=
3-g.
$$
Therefore
$$
\ell(K-D)
=
\ell(D)+g-3
\ge
2+g-3
=
g-1.
$$

:::

:::

::: {.pf-step #s3}

The canonical divisor of a hyperelliptic curve is not very ample.

::: pf-proof

Suppose $K$ were very ample.  Then the embedding defined by the complete
linear system $\linearsystem{K}$ separates every subscheme of length $2$.  In particular,
the restriction map
$$
H^0(X,\OO_X(K))
\longrightarrow
H^0(D,\OO_X(K)\restrict_D)
$$
is surjective.

The divisor $D$ has length $2$, so the target has dimension $2$.  Since
$$
\ell(K)=g,
$$
the exact sequence
$$
0\longrightarrow\OO_X(K-D)
\longrightarrow\OO_X(K)
\longrightarrow\OO_X(K)\restrict_D
\longrightarrow0
$$
would therefore give
$$
\ell(K-D)=g-2.
$$
This contradicts step [](#s2){.pf-ref}, which gives
$$
\ell(K-D)\ge g-1.
$$
Hence $K$ is not very ample.

:::

:::

::: {.pf-step #s4}

The curve $X$ cannot be a complete intersection in any projective
space.

::: pf-proof

Suppose, to the contrary, that
$$
X\subseteq\PP^n
$$
were a complete-intersection curve.  Since $g\ge2$,
[[P-AGH433COMPLETEINTERSECTIONCANONICAL|Exercise IV.3.3]] says that its
canonical divisor is very ample.  This contradicts step [](#s3){.pf-ref}.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} show that a hyperelliptic curve has non-very-ample
canonical divisor, while step [](#s4){.pf-ref} contradicts the complete-intersection
very-ampleness theorem.

:::

:::

:::

::: {.remark title="Published solution"}
Yang Pi-Yeh, *Hartshorne Solutions* (9 June 2019), Solution 4.5.1, printed p. 95, is the whole entry: 'By 4.3.3 and proposition 5.2, trivial.' The composition is exact --- a complete intersection of genus $\geq2$ has $K$ very ample by (4.3.3), while on a hyperelliptic curve $\abs K=(g-1)g^1_2$ is not very ample by (5.2) --- and it is the argument the card carries, its step [](#s3){.pf-ref} being the non-very-ampleness and [](#s4){.pf-ref} the conclusion. What the entry does not do is exhibit either ingredient: both are quoted, and a reader who wants the computation has to take it from the book's own propositions.
:::
