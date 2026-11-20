---
schema: qual/card@1
id: P-AGH413NONPROPERISAFFINE
kind: problem
title: A regular one-dimensional scheme that is not proper over $k$ is affine
classification:
  areas:
  - algebraic-geometry
  topics:
  - Curves
  - Riemann-Roch
  - Embeddings
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Exercise IV.1.3 and its compactification/IV.1.2 hint. Cross-checked
    regular-curve compactification and finiteness of a nonconstant morphism of
    proper curves against Stacks Project Tags 0H1F and 0CCL.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    A retained solution read at this exercise. Read Yang Pi-Yeh, Hartshorne
    Solutions (9 June 2019), Solution 4.1.3, printed p. 84,
    rendered as a page image from
    tmp/sources/lfwin-hartshorne-solutions.pdf, whose PDF page is the printed
    page. Checked against the book: Hartshorne IV.1.3, whose printed page
    the card's earlier events record; this pass did not reopen it, and the
    comparison is against the statement the card carries. Recomputed
    the embedding with finite complement, the divisor of f from the previous
    entry, and the identity X = f^{-1}(A^1). Not checked: Yang's Solutions outside printed pp. 84-85; the
    book's own page in this pass; and the printed book itself.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    The remark now names Yang Pi-Yeh's Solution 4.1.3 at printed
    p. 84 beside the entry already there. No step, statement or
    hypothesis of the card changes.
---

::: {.problem}
Let $X$ be an integral, separated, regular, one-dimensional scheme of finite type over $k$, which is not proper over $k$.
Then $X$ is affine.

Hint: Embed $X$ in a (proper) curve $\bar{X}$ over $k$, and use (Ex.
1.2) to construct a morphism $f: \bar{X} \to \PP^1$ such that $f^{-1}(\AA^1)=X$.
:::

::: {.solution}

::: pf

::: pf-step

There is an open immersion
$$
j:X\hookrightarrow\bar X
$$
into a regular projective integral curve $\bar X$, and
$$
\bar X\setminus X=\{P_1,\ldots,P_r\}
$$
is a finite nonempty set of closed points.

::: pf-proof

A regular separated curve of finite type over a field has a regular
projective compactification. Equivalently, one may take a projective
completion and then normalize it; regularity of $X$ identifies $X$
with an open subscheme of the normalization.

Because $\bar X$ is a noetherian integral curve, every proper closed
subset is zero-dimensional and hence finite. Thus the complement of the
dense open $X$ consists of finitely many closed points.

Finally $r>0$. If the complement were empty, then
$$
X=\bar X
$$
would be projective, hence proper over $k$, contrary to the hypothesis.

:::

:::

::: {.pf-step #s2}

There exists a nonconstant rational function
$$
f\in K(\bar X)
$$
whose poles occur precisely at $P_1,\ldots,P_r$.

::: pf-proof

Apply
[[P-AGH412POLESATFINITESET|Exercise IV.1.2]]
on the proper regular curve $\bar X$ to the finite set
$$
P_1,\ldots,P_r.
$$
It gives a rational function $f$ having a pole of positive order at
every $P_i$ and regular at every point of
$$
\bar X\setminus\{P_1,\ldots,P_r\}=X.
$$
Since $f$ has at least one pole, it is not constant.

:::

:::

::: {.pf-step #s3}

The rational function $f$ determines a morphism
$$
\bar f:\bar X\longrightarrow\PP^1
$$
such that
$$
\bar f^{-1}(\infty)=\{P_1,\ldots,P_r\}.
$$

::: pf-proof

A nonzero rational function on a regular complete curve defines the
usual morphism to $\PP^1$: where $f$ is regular use the affine
coordinate $z=f$, and near a pole use the affine coordinate
$$
w=f^{-1}
$$
around $\infty$. Regularity of the local rings of $\bar X$ makes
these two descriptions glue.

A point maps to $\infty$ exactly when $f$ has a pole there. By step
[](#s2){.pf-ref}, these are precisely the points $P_1,\ldots,P_r$. Hence
$$
\bar f^{-1}(\AA^1)
=
\bar X\setminus\{P_1,\ldots,P_r\}
=
X.
$$

:::

:::

::: pf-step

The morphism
$$
\bar f:\bar X\longrightarrow\PP^1
$$
is finite.

::: pf-proof

The morphism is nonconstant by step [](#s2){.pf-ref}. Both source and target are
proper integral curves, and $\bar X$ is regular. Therefore the standard
finiteness theorem for maps of proper curves
[[D-MORFIN|finite morphisms between proper curves]]
applies: a nonconstant morphism
$$
\bar X\longrightarrow\PP^1
$$
is finite.

:::

:::

::: {.pf-step #s5}

The scheme $X$ is affine.

::: pf-proof

By step [](#s3){.pf-ref},
$$
X=\bar f^{-1}(\AA^1).
$$
Base change of a finite morphism is finite, so restriction gives a finite
morphism
$$
f:X\longrightarrow\AA^1.
$$
Finite morphisms are affine. Since
$$
\AA^1=\Spec k[t]
$$
is affine, its inverse image under the finite morphism $f$ is affine.
Thus $X$ is affine.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is exactly the required conclusion.

:::

:::

:::

::: {.remark title="Published solution"}
The exercise is Hartshorne, IV.1, exercise 1.3, read in `tmp/sources/hartshorne-1977-algebraic-geometry.md`; the statement above is its text, the printed bracketed hint included.

Jinhyun Park, *Solutions to Hartshorne's Algebraic Geometry*, Chapter IV §1, Exercise 3, text version `tmp/sources/hartshorne-solutions-park.md`, closes $X$ to a projective nonsingular $\bar X$ with finite complement, uses Exercise 2 to find $f$ with poles exactly at the complementary points, and concludes that $f^{-1}(\AA^1)=X$ is affine because $f$ is finite by (II, 6.8); his second proof embeds $\bar X$ by a very ample divisor supported on the complement. Lomont, Chapter IV §1, Exercise 1.3, text version `tmp/sources/hartshorne-solutions-lomont.md`, gives the first route.

Yang Pi-Yeh, *Hartshorne Solutions* (9 June 2019), Solution 4.1.3, follows the hint: (II, 4.10.2(e)) embeds $X$ as an open subset of a complete variety $\bar X$, whose complement is a finite set $\{P_1,\ldots,P_r\}$; the previous exercise then gives $f\in K(\bar X)$ with poles exactly at the $P_i$; and since such an $f$ is a finite morphism $\bar X\to\PP^1$, $X=f^{-1}(\AA^1)$ is affine. The finiteness of $f$ is where the regularity and the one-dimensionality enter.
:::
