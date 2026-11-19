---
schema: qual/card@1
id: P-AGH417HYPERELLIPTIC
kind: problem
title: Hyperelliptic curves exist in every genus $g \geq 2$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Hyperelliptic Curves
  - Genus
  - Canonical Divisor
  - Linear Systems
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.1.7, the retained solution transcription, and the
    type-(g+1,2) quadric construction from IV.1.1.1. Part (a) is proved
    independently using IV.1.5 to rule out a canonical base point.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    A retained solution read at this exercise. Read Yang Pi-Yeh, Hartshorne
    Solutions (9 June 2019), Solution 4.1.7, printed p. 84,
    rendered as a page image from
    tmp/sources/lfwin-hartshorne-solutions.pdf, whose PDF page is the printed
    page. Checked against the book: Hartshorne IV.1.7, whose printed page
    the card's earlier events record; this pass did not reopen it, and the
    comparison is against the statement the card carries. Recomputed
    dim|K| = 1 at g = 2, the Riemann-Roch difference
    l(P) - l(K-P) = 0, and the degree-two projection off the quadric. Not checked: Yang's Solutions outside printed pp. 84-85; the
    book's own page in this pass; and the printed book itself.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    The remark now names Yang Pi-Yeh's Solution 4.1.7 at printed
    p. 84 beside the entry already there. No step, statement or
    hypothesis of the card changes.
---

::: {.problem}
A curve $X$ is called \dfn{hyperelliptic} if $g \geq 2$ and there exists a finite morphism $f: X \to \PP^1$ of degree 2.

(a) If $X$ is a curve of genus $g=2$, show that the canonical divisor defines a complete linear system $\abs{K}$ of degree 2 and dimension 1, without base points.
Use (II, 7.8.1) to conclude that $X$ is hyperelliptic.

(b) Show that the curves constructed in (1.1.1) all admit a morphism of degree 2 to $\PP^1$.
Thus there exist hyperelliptic curves of any genus $g \geq 2$.

Note: we will see later (Ex.
3.2) that there exist non-hyperelliptic curves.
See also (V, Ex.
2.10).
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

If $g=2$, then the canonical system has degree $2$ and dimension $1$:
$$
\deg K=2,
\qquad
\dim\abs{K}=1.
$$

::: pf-proof

For a smooth projective curve of genus $g$,
$$
\deg K=2g-2
$$
and
$$
\ell(K)=g.
$$
Thus for $g=2$,
$$
\deg K=2
$$
and
$$
\dim\abs{K}
=
\ell(K)-1
=
1.
$$

:::

:::

::: {.pf-step #s2}

The canonical system $\abs{K}$ has no base point.

::: pf-proof

Suppose that $P\in X$ were a base point of $\abs{K}$. Then every canonical section vanishes at $P$, so
$$
H^0(X,\mco_X(K-P))
=
H^0(X,\mco_X(K)).
$$
Hence
$$
\ell(K-P)=\ell(K)=2.
$$

Riemann--Roch for the degree-one divisor $P$ gives
$$
\ell(P)-\ell(K-P)
=
1+1-g
=
0,
$$
so
$$
\ell(P)=2.
$$
Therefore
$$
\dim\abs{P}
=
\ell(P)-1
=
1
=
\deg P.
$$
Since $P\ne0$, the equality criterion in
[[P-AGH415DIMLEQDEG|Exercise IV.1.5]]
would force $g=0$, contradicting $g=2$. Thus $\abs{K}$ has no base point.

:::

:::

::: {.pf-step #s3}

Every genus-$2$ curve is hyperelliptic.

::: pf-proof

By steps [](#s1){.pf-ref} and [](#s2){.pf-ref}, the complete linear system $\abs{K}$ is base-point free of dimension $1$. Hence it defines a morphism
$$
\varphi_{\abs{K}}:X\longrightarrow\PP^1
$$
with
$$
\varphi_{\abs{K}}^*\mco_{\PP^1}(1)
\cong
\mco_X(K).
$$
The map is nonconstant, hence finite. Taking degrees gives
$$
\deg\varphi_{\abs{K}}
=
\deg K
=
2.
$$
Thus $X$ is hyperelliptic. This proves part (a).

:::

:::

::: {.pf-step #s4}

The curves constructed in (IV.1.1.1) admit a finite morphism of degree $2$ to $\PP^1$.

::: pf-proof

In that construction, for every $g\ge2$ one obtains a smooth curve
$$
X\subseteq Q,
\qquad
Q\cong\PP^1\times\PP^1,
$$
whose divisor class has type $(g+1,2)$.

Take the ruling projection
$$
p:Q\longrightarrow\PP^1
$$
whose fibre class meets a divisor of type $(g+1,2)$ in degree $2$. The restriction
$$
p\restrict_X:X\longrightarrow\PP^1
$$
is nonconstant, hence finite. For any point $a\in\PP^1$, the fibre divisor is
$$
(p\restrict_X)^*(a)=X\cap p^{-1}(a),
$$
and its degree is the intersection number
$$
X\cdot p^{-1}(a)=2.
$$
Therefore
$$
\deg(p\restrict_X)=2.
$$
Hence every curve in the construction is hyperelliptic.

:::

:::

::: {.pf-step #s5}

Hyperelliptic curves exist in every genus $g\ge2$.

::: pf-proof

The construction in (IV.1.1.1) produces such a smooth curve for every $g\ge2$, and step [](#s4){.pf-ref} gives a degree-two morphism from each one to $\PP^1$. This proves part (b).

:::

:::

::: pf-qed

Step [](#s3){.pf-ref} proves part (a), and steps [](#s4){.pf-ref} and [](#s5){.pf-ref} prove part (b).

:::

:::

:::

::: {.remark title="Published solution"}
A. Egbert, *Solutions to Hartshorne's Algebraic Geometry* (2013), IV.1.7, printed pp. 207–208, text version `tmp/sources/hartshorne-solutions-egbert.md`, obtains hyperellipticity from $\dim\linearsystem{K_X}=g-1$ and $\deg K_X=2g-2$, so that for $g=2$ the canonical system is a base-point-free $g^1_2$ giving a degree-two morphism to $\PP^1$ by (II, 7.8.1).

Yang Pi-Yeh, *Hartshorne Solutions* (9 June 2019), Solution 4.1.7, printed p. 84, has (a) as follows: for $g=2$, $\deg K=2$ and $\dim\linearsystem{K}=\ell(K)-1=1$; Riemann--Roch at a point gives $\ell(P)-\ell(K-P)=1+1-2=0$, and $\dim\linearsystem{P}=1$ would be a degree-one map, impossible for $g>1$, so $\ell(P)=1$ and $\ell(K-P)=1$ — which is to say $P$ is not a base point of $\linearsystem{K}$. A base-point-free system of degree $2$ and dimension $1$ gives a degree-two morphism by (II, 7.8.1). Its (b) takes a curve of type $(g+1,2)$ on $\PP^1\times\PP^1$ and the second projection, finite and nonconstant by (II, 6.8), of degree $2$ by (II, 6.9).
:::
