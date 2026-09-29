---
schema: qual/card@1
id: P-AGH418ARITHGENUSSINGULAR
kind: problem
title: The arithmetic genus of a singular curve and the local invariants $\delta_P$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Genus
  - Curves
  - Riemann-Roch
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.1.8 and its normalization exact sequence. Parts (a)--(b)
    are derived directly from cohomology. For part (c), the completion argument
    and the node/cusp normalization quotients were checked independently against
    the local delta-invariant conventions in the corpus.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Let $X$ be an integral projective scheme of dimension 1 over $k$, and let $\tilde{X}$ be its normalization (II, Ex.
3.8). Then there is an exact sequence of sheaves on $X$,
$$
0 \to \OO_X \to f_* \OO_{\tilde X} \to \sum_{P \in X} \tilde\OO_P/\OO_P \to 0
$$
where $\tilde\OO_P$ is the integral closure of $\OO_P$.
For each $P \in X$, let $\delta_P=\operatorname{length}(\tilde\OO_P/\OO_P)$.

a. Show that $p_a(X)=p_a(\tilde{X})+\sum_{P \in X} \delta_P$.
Hint: Use (III, Ex.
4.1) and (III, Ex.
5.3).

b. If $p_a(X)=0$, show that $X$ is already nonsingular and in fact isomorphic to $\PP^1$.
This strengthens (1.3.5).

c. \* If $P$ is a node or an ordinary cusp (I, Ex.
5.6, Ex.
5.14), show that $\delta_P=1$.
Hint: Show first that $\delta_P$ depends only on the analytic isomorphism class of the singularity at $P$.
Then compute $\delta_P$ for the node and cusp of suitable plane cubic curves.
See (V, 3.9.3) for another method.
:::

::: {.solution}
Let
$$
\nu:\widetilde X\longrightarrow X
$$
be the normalization and put
$$
\mathcal Q
=
\nu_*\mco_{\widetilde X}/\mco_X.
$$
Thus
$$
\mathcal Q_P
=
\widetilde\mco_P/\mco_P,
\qquad
\operatorname{length}_{\mco_P}\mathcal Q_P
=
\delta_P.
$$

::: pf

::: {.pf-step #s1}

The sheaf $\mathcal Q$ is supported at finitely many closed points and
$$
\dim_kH^0(X,\mathcal Q)
=
\sum_{P\in X}\delta_P.
$$

::: pf-proof

The normalization is an isomorphism over the regular locus of the
one-dimensional scheme $X$. Hence $\mathcal Q$ is supported on the finite
singular locus.

At a closed point $P$, the residue field is $k$ because $k$ is
algebraically closed. A finite-length $\mco_P$-module therefore has
$k$-dimension equal to its length. Since a sheaf supported on finitely
many closed points is the direct sum of its stalk skyscraper sheaves,
$$
H^0(X,\mathcal Q)
\cong
\bigoplus_{P\in X}\mathcal Q_P.
$$
Taking dimensions gives the formula.

:::

:::

::: {.pf-step #s2}

There is a short exact sequence
$$
0
\longrightarrow
H^0(X,\mathcal Q)
\longrightarrow
H^1(X,\mco_X)
\longrightarrow
H^1(\widetilde X,\mco_{\widetilde X})
\longrightarrow
0.
$$

::: pf-proof

Apply cohomology to
$$
0
\longrightarrow
\mco_X
\longrightarrow
\nu_*\mco_{\widetilde X}
\longrightarrow
\mathcal Q
\longrightarrow
0.
$$
Because $\nu$ is finite,
$$
H^i(X,\nu_*\mco_{\widetilde X})
\cong
H^i(\widetilde X,\mco_{\widetilde X}).
$$
Also
$$
H^1(X,\mathcal Q)=0
$$
because $\mathcal Q$ has zero-dimensional support.

Both $X$ and $\widetilde X$ are integral and projective, so
$$
H^0(X,\mco_X)
\cong
H^0(\widetilde X,\mco_{\widetilde X})
\cong
k.
$$
The first map is the identity on constants. The long exact sequence
therefore reduces to the displayed short exact sequence.

:::

:::

::: {.pf-step #s3}

One has
$$
\boxed{
p_a(X)
=
p_a(\widetilde X)
+
\sum_{P\in X}\delta_P.
}
$$

::: pf-proof

For an integral projective curve $C$ over $k$,
$$
p_a(C)
=
1-\chi(\mco_C)
=
h^1(C,\mco_C)
$$
because $h^0(C,\mco_C)=1$. Thus step [](#s2){.pf-ref} and step [](#s1){.pf-ref} give
$$
p_a(X)
=
p_a(\widetilde X)
+
\sum_{P\in X}\delta_P.
$$
This proves part (a).

:::

:::

::: {.pf-step #s4}

If $p_a(X)=0$, then $X$ is nonsingular.

::: pf-proof

By step [](#s3){.pf-ref},
$$
0
=
p_a(\widetilde X)
+
\sum_P\delta_P.
$$
The normalization $\widetilde X$ is a smooth projective curve, so
$p_a(\widetilde X)\ge0$, and every $\delta_P$ is a nonnegative integer.
Hence
$$
p_a(\widetilde X)=0
\qquad\text{and}\qquad
\delta_P=0
$$
for every $P$.

Thus
$$
\widetilde\mco_P=\mco_P
$$
for every $P$, so every local ring of $X$ is integrally closed. A
one-dimensional noetherian integrally closed local domain is a DVR and
therefore regular. Hence $X$ is nonsingular.

:::

:::

::: {.pf-step #s5}

If $p_a(X)=0$, then
$$
X\cong\PP^1.
$$

::: pf-proof

By step [](#s4){.pf-ref}, $X$ is a smooth projective curve. Its genus is
$$
g=p_a(X)=0.
$$
Exercise
[[P-AGH416MAPTOP1DEGREE|IV.1.6]]
gives a finite morphism
$$
f:X\longrightarrow\PP^1
$$
of degree at most $1$. Since $f$ is nonconstant, its degree is positive,
so
$$
\deg f=1.
$$
A finite degree-one morphism of integral smooth projective curves is
birational, and a finite birational morphism to the normal curve $\PP^1$
is an isomorphism. This proves part (b).

:::

:::

::: {.pf-step #s6}

The number $\delta_P$ depends only on the analytic isomorphism class of the singularity.

::: pf-proof

Put
$$
A=\mco_{X,P},
\qquad
B=\widetilde\mco_P.
$$
The quotient
$$
B/A
$$
has finite length. Completion is exact on finite $A$-modules, and a
finite-length module is unchanged by completion. Hence
$$
\operatorname{length}_A(B/A)
=
\operatorname{length}_{\widehat A}
\left(
(B\otimes_A\widehat A)/\widehat A
\right).
$$

The local ring $A$ is essentially of finite type over a field, hence
excellent. For such a one-dimensional reduced local ring, normalization
commutes with completion: $B\otimes_A\widehat A$ is the normalization of
$\widehat A$ in its total ring of fractions. Therefore
$$
\delta_P
=
\operatorname{length}_{\widehat A}
\left(
\overline{\widehat A}/\widehat A
\right).
$$
The right-hand side depends only on the isomorphism class of the completed
local ring $\widehat A$. Thus $\delta_P$ is an analytic invariant.

:::

:::

::: {.pf-step #s7}

If $P$ is an ordinary cusp, then
$$
\delta_P=1.
$$

::: pf-proof

Up to analytic isomorphism, an ordinary cusp has completed local ring
$$
\widehat A
\cong
k[[t^2,t^3]]
\subseteq
k[[t]].
$$
Its normalization is $k[[t]]$. Every power $t^n$ with $n\ge2$ lies in
$k[[t^2,t^3]]$, so every series in $k[[t]]$ is congruent modulo
$k[[t^2,t^3]]$ to a unique scalar multiple of $t$. Hence
$$
k[[t]]/k[[t^2,t^3]]
\cong
k\cdot t
$$
as a $k$-vector space. This quotient has length $1$. Step [](#s6){.pf-ref} therefore
gives
$$
\delta_P=1.
$$

:::

:::

::: {.pf-step #s8}

If $P$ is a node, then
$$
\delta_P=1.
$$

::: pf-proof

Up to analytic isomorphism, a node has completed local ring
$$
\widehat A
\cong
k[[x,y]]/(xy).
$$
Its normalization is
$$
k[[x]]\times k[[y]],
$$
with the map
$$
k[[x,y]]/(xy)
\longrightarrow
k[[x]]\times k[[y]]
$$
sending the class of a power series $h(x,y)$ to
$$
\bigl(h(x,0),h(0,y)\bigr).
$$
Its image consists exactly of the pairs
$$
(a(x),b(y))
$$
with the same constant term:
$$
a(0)=b(0).
$$
Therefore the homomorphism
$$
k[[x]]\times k[[y]]
\longrightarrow
k,
\qquad
(a,b)\longmapsto a(0)-b(0)
$$
is surjective and has image of $\widehat A$ as its kernel. Thus
$$
\bigl(k[[x]]\times k[[y]]\bigr)/\widehat A
\cong
k,
$$
which has length $1$. Step [](#s6){.pf-ref} gives
$$
\delta_P=1.
$$

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} prove part (a), steps [](#s4){.pf-ref} and [](#s5){.pf-ref} prove part (b), and
steps [](#s6){.pf-ref}, [](#s7){.pf-ref} and [](#s8){.pf-ref} prove part (c).

:::

:::

:::
