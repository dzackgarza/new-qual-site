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
---

::: {.problem}
Let $X$ be an integral, separated, regular, one-dimensional scheme of finite type over $k$, which is **not** proper over $k$.
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
into a regular projective integral curve \(\bar X\), and
$$
\bar X\setminus X=\{P_1,\ldots,P_r\}
$$
is a finite nonempty set of closed points.

::: pf-proof

A regular separated curve of finite type over a field has a regular
projective compactification. Equivalently, one may take a projective
completion and then normalize it; regularity of \(X\) identifies \(X\)
with an open subscheme of the normalization.

Because \(\bar X\) is a noetherian integral curve, every proper closed
subset is zero-dimensional and hence finite. Thus the complement of the
dense open \(X\) consists of finitely many closed points.

Finally \(r>0\). If the complement were empty, then
$$
X=\bar X
$$
would be projective, hence proper over \(k\), contrary to the hypothesis.

:::

:::

::: {.pf-step #s2}

There exists a nonconstant rational function
$$
f\in K(\bar X)
$$
whose poles occur precisely at \(P_1,\ldots,P_r\).

::: pf-proof

Apply
[[P-AGH412POLESATFINITESET|Exercise IV.1.2]]
on the proper regular curve \(\bar X\) to the finite set
$$
P_1,\ldots,P_r.
$$
It gives a rational function \(f\) having a pole of positive order at
every \(P_i\) and regular at every point of
$$
\bar X\setminus\{P_1,\ldots,P_r\}=X.
$$
Since \(f\) has at least one pole, it is not constant.

:::

:::

::: {.pf-step #s3}

The rational function \(f\) determines a morphism
$$
\bar f:\bar X\longrightarrow\PP^1
$$
such that
$$
\bar f^{-1}(\infty)=\{P_1,\ldots,P_r\}.
$$

::: pf-proof

A nonzero rational function on a regular complete curve defines the
usual morphism to \(\PP^1\): where \(f\) is regular use the affine
coordinate \(z=f\), and near a pole use the affine coordinate
$$
w=f^{-1}
$$
around \(\infty\). Regularity of the local rings of \(\bar X\) makes
these two descriptions glue.

A point maps to \(\infty\) exactly when \(f\) has a pole there. By step
[](#s2){.pf-ref}, these are precisely the points \(P_1,\ldots,P_r\). Hence
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
proper integral curves, and \(\bar X\) is regular. Therefore the standard
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

The scheme \(X\) is affine.

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
is affine, its inverse image under the finite morphism \(f\) is affine.
Thus \(X\) is affine.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is exactly the required conclusion.

:::

:::

:::
