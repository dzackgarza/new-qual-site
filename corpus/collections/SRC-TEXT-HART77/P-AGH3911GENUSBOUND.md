---
schema: qual/card@1
id: P-AGH3911GENUSBOUND
kind: problem
title: Castelnuovo's genus bound for a space curve of degree $d$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Flat Morphisms
  - Arithmetic Genus
  - Projections of Curves
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Exercise III.9.11 together with the projection degeneration of
    III.9.8.3--9.8.4. The proof uses a birational linear projection to a plane
    curve of the same degree, flatness to preserve the Hilbert polynomial, and
    the zero-dimensional nilpotent kernel of the special fibre to compare its
    arithmetic genus with that of the reduced plane curve.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Let $Y$ be a nonsingular curve of degree $d$ in $\PP_k^n$, over an algebraically closed field $k$. Show that
\[
0 \leq p_a(Y) \leq \frac{1}{2}(d-1)(d-2)
.\]

Hint: compare $Y$ to a suitable projection of $Y$ into $\PP^2$, as in (9.8.3) and (9.8.4).
:::

::: {.solution}
Put
$$
g=p_a(Y).
$$

::: pf

::: {.pf-step #s1}

One has $g\ge0$.

::: pf-proof

Because $Y$ is a nonsingular projective integral curve over the algebraically
closed field $k$,
$$
p_a(Y)=h^1(Y,\OO_Y)
$$
[[D-G1AEH|by the equality of the genera for a nonsingular projective curve]].
Therefore
$$
\boxed{p_a(Y)\ge0}.
$$

:::

:::

::: {.pf-step #s2}

There is a linear projection
$$
\pi:Y\longrightarrow C\subseteq\PP_k^2
$$
which is birational onto an integral plane curve $C$ of degree $d$.

::: pf-proof

If $n=2$, take $C=Y$ and $\pi=\id_Y$.

Assume $n\ge3$. Choose a general linear centre
$$
\Lambda\cong\PP^{n-3}\subseteq\PP^n
$$
disjoint from $Y$. Successive general projections reduce the ambient
dimension to $3$ without identifying the generic point of $Y$, and a general
projection from $\PP^3$ to $\PP^2$ is birational on a curve. This is the
generic-projection construction recorded in [[T-CRVEMBP3]]. Hence the
restriction of the projection from $\Lambda$ is a birational morphism onto an
integral plane curve $C$.

A general line $L\subseteq\PP^2$ pulls back to a hyperplane of $\PP^n$
containing $\Lambda$. Since $\pi$ has degree one on function fields, a general
such hyperplane meets $Y$ in exactly the points lying over $C\cap L$, with
the same total intersection multiplicity. Thus
$$
\deg C=\deg Y=d.
$$

:::

:::

::: {.pf-step #s3}

The projection construction of III.9.8.3 gives a flat family
$$
\mathcal Y\longrightarrow\AA^1
$$
whose fibre over $1$ is $Y$ and whose fibre $Y_0$ over $0$ has support $C$.

::: pf-proof

Choose homogeneous coordinates so that the projection of step [](#s2){.pf-ref} forgets
the last $n-2$ coordinates. For $t\ne0$, scale those omitted coordinates by
$t$. The resulting projective automorphisms carry $Y$ through an isotrivial
family over $\GG_m$. Taking its scheme-theoretic closure over $\AA^1$ gives
the flat family of Hartshorne III.9.8.3; the calculation in III.9.8.4 shows
that its special fibre is a scheme supported on the projected curve $C$.

Flatness preserves the Hilbert polynomial [@Har10a, Theorem III.9.9], hence
$$
P_{Y_0}=P_Y.
$$
In particular
$$
\deg Y_0=d
\qquad\text{and}\qquad
p_a(Y_0)=p_a(Y)=g.
$$

:::

:::

::: {.pf-step #s4}

The reduction of $Y_0$ is $C$, and the nilradical
$$
\mathcal N=\ker(\OO_{Y_0}\longrightarrow\OO_C)
$$
has zero-dimensional support.

::: pf-proof

By step [](#s3){.pf-ref}, the support of $Y_0$ is $C$, so
$$
(Y_0)_{\mathrm{red}}=C.
$$
The exact sequence
$$
0\longrightarrow\mathcal N
\longrightarrow\OO_{Y_0}
\longrightarrow\OO_C
\longrightarrow0
$$
gives
$$
P_{Y_0}=P_C+P_{\mathcal N}.
$$
Steps [](#s2){.pf-ref} and [](#s3){.pf-ref} give
$$
\deg Y_0=d=\deg C.
$$
For a one-dimensional projective scheme, the leading coefficient of the
Hilbert polynomial is its degree. Hence the linear terms of $P_{Y_0}$ and
$P_C$ cancel, so $P_{\mathcal N}$ is constant. Therefore $\mathcal N$ has
zero-dimensional support. Since it is coherent on the projective curve $C$,
it has finite length.

:::

:::

::: {.pf-step #s5}

The special fibre has arithmetic genus at most that of its reduced plane support:
$$
p_a(Y_0)\le p_a(C).
$$

::: pf-proof

There is an exact sequence
$$
0\longrightarrow\mathcal N
\longrightarrow\OO_{Y_0}
\longrightarrow\OO_C
\longrightarrow0.
$$
Since $\mathcal N$ is supported at finitely many closed points,
$$
H^i(C,\mathcal N)=0\quad(i>0),
\qquad
\chi(\mathcal N)=h^0(C,\mathcal N)=\operatorname{length}(\mathcal N)\ge0.
$$
Additivity of Euler characteristic gives
$$
\chi(\OO_{Y_0})
=\chi(\OO_C)+\operatorname{length}(\mathcal N).
$$
For a projective curve $Z$,
$$
p_a(Z)=1-\chi(\OO_Z).
$$
Consequently
$$
p_a(Y_0)
=p_a(C)-\operatorname{length}(\mathcal N)
\le p_a(C).
$$

:::

:::

::: {.pf-step #s6}

The plane curve $C$ has
$$
p_a(C)=\frac12(d-1)(d-2).
$$

::: pf-proof

By step [](#s2){.pf-ref}, $C\subseteq\PP^2$ is a plane curve of degree $d$.
The plane-curve Hilbert-polynomial calculation of
[[P-AGH72ARITHGENUS|Hartshorne I.7.2(b)]] gives
$$
\boxed{p_a(C)=\binom{d-1}{2}=\frac12(d-1)(d-2)}.
$$

:::

:::

::: {.pf-step #s7}

The required upper bound follows.

::: pf-proof

By steps [](#s3){.pf-ref} and [](#s5){.pf-ref},
$$
p_a(Y)=p_a(Y_0)\le p_a(C).
$$
Applying step [](#s6){.pf-ref} yields
$$
\boxed{p_a(Y)\le\frac12(d-1)(d-2)}.
$$
Together with step [](#s1){.pf-ref} this proves
$$
0\le p_a(Y)\le\frac12(d-1)(d-2).
$$

:::

:::

::: pf-qed

Step [](#s1){.pf-ref} proves the lower bound. Steps [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref}, [](#s5){.pf-ref} and [](#s6){.pf-ref} compare $Y$ through the
flat projection degeneration with a degree-$d$ plane curve, and step [](#s7){.pf-ref}
gives the upper bound.

:::

:::

:::
