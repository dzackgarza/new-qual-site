---
schema: qual/card@1
id: P-AGH439BERTINILEMMA
kind: problem
title: Bertini's lemma on general plane sections of a space curve
classification:
  areas:
  - algebraic-geometry
  topics:
  - Embeddings
  - Linear Systems
  - Curves
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne IV.3.9 and the secant/tangent dimension arguments used in
    the proof of IV.3.10. The proof below makes both bad loci explicit in the
    dual projective space. For multisecants it uses the Grassmannian secant
    surface together with Hartshorne's preceding result that not every secant
    of a nonplanar curve is a multisecant; this is the classical trisecant
    lemma in dimension one.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Prove the following lemma of Bertini: if $X$ is a curve of degree $d$ in $\PP^3$, not contained in any plane, then for almost all planes $H \subseteq \PP^3$ (meaning a Zariski open subset of the dual projective space $(\PP^3)^*$), the intersection $X \intersect H$ consists of exactly $d$ distinct points, no three of which are collinear.
:::

::: {.solution}
Write
$$
\check{\PP}^3=(\PP^3)^*
$$
for the dual projective space parametrizing planes in $\PP^3$.
In Chapter IV, a curve is nonsingular, so every point of $X$ has a
well-defined tangent line.

::: pf

::: {.pf-step #s1}

The locus
$$
B_{\mathrm{tan}}
=
\{H\in\check{\PP}^3:H\supseteq T_PX
\text{ for some }P\in X\}
$$
is closed and has dimension at most $2$.

::: pf-proof

Consider the incidence variety
$$
\mathcal T
=
\{(P,H)\in X\times\check{\PP}^3:T_PX\subseteq H\}.
$$
For a fixed point $P$, the planes containing the line $T_PX$ form a
projective line. Thus
$$
\mathcal T\longrightarrow X
$$
is a $\PP^1$-bundle and
$$
\dim\mathcal T=2.
$$

The incidence condition is closed, and $\mathcal T$ is projective. Hence its
image under the projection to $\check{\PP}^3$ is closed. This image is
$B_{\mathrm{tan}}$, so
$$
\dim B_{\mathrm{tan}}\le2.
$$

:::

:::

::: {.pf-step #s2}

Let
$$
G=\operatorname{Gr}(1,3)
$$
be the Grassmannian of lines in $\PP^3$. The family of secant lines of $X$
has irreducible closure
$$
S\subseteq G
$$
of dimension $2$.

::: pf-proof

On
$$
(X\times X)\setminus\Delta
$$
there is a morphism
$$
\sigma:(P,Q)\longmapsto\overline{PQ}.
$$
Its domain is irreducible of dimension $2$.

For a fixed line $\ell$, the fibre of $\sigma$ consists of ordered pairs of
distinct points in the finite set
$$
X\cap\ell.
$$
The set is finite because $X$ is not a line; indeed a line contained in the
integral curve $X$ would equal $X$, contradicting the hypothesis that $X$ is
not planar. Thus every fibre of $\sigma$ is finite.

Consequently the image has dimension $2$, and its closure $S$ is an
irreducible surface in $G$.

:::

:::

::: {.pf-step #s3}

The family
$$
M\subseteq S
$$
of multisecant lines has dimension at most $1$.

::: pf-proof

Let
$$
\mathcal U
\subseteq
\PP^3\times G
$$
be the universal line, and put
$$
\mathcal Z
=
(X\times G)\cap\mathcal U.
$$
The projection
$$
q:\mathcal Z\longrightarrow G
$$
is projective and has finite fibres, because no line is contained in $X$.
Hence $q$ is finite.

For $\ell\in G$, the fibre is the finite scheme
$$
X\cap\ell.
$$
The function
$$
\ell
\longmapsto
\operatorname{length}(X\cap\ell)
$$
is upper semicontinuous: it is the fibre dimension of the finite coherent
$\mco_G$-module $q_*\mco_{\mathcal Z}$. Therefore
$$
M
=
\{\ell\in S:
\operatorname{length}(X\cap\ell)\ge3\}
$$
is closed in $S$.

The secant argument used in Hartshorne's proof of the general projection
theorem shows that not every secant of a nonplanar curve is a multisecant
[@Har10a, Chapter IV, §3]. Hence
$$
M\ne S.
$$
Since $S$ is an irreducible surface by step [](#s2){.pf-ref},
$$
\boxed{\dim M\le1}.
$$
This is the curve case of the classical trisecant lemma.

:::

:::

::: {.pf-step #s4}

The locus
$$
B_{\mathrm{multi}}
=
\{H\in\check{\PP}^3:
H\supseteq\ell
\text{ for some }\ell\in M\}
$$
is closed and has dimension at most $2$.

::: pf-proof

Consider
$$
\mathcal M
=
\{(\ell,H)\in M\times\check{\PP}^3:\ell\subseteq H\}.
$$
For each line $\ell$, the planes containing $\ell$ form a $\PP^1$.
Thus
$$
\dim\mathcal M
=
\dim M+1
\le2
$$
by step [](#s3){.pf-ref}.

The incidence variety $\mathcal M$ is projective, so its image in
$\check{\PP}^3$ is closed. That image is $B_{\mathrm{multi}}$, proving
$$
\dim B_{\mathrm{multi}}\le2.
$$

:::

:::

::: {.pf-step #s5}

There is a nonempty Zariski-open subset
$$
U
=
\check{\PP}^3
\setminus
\bigl(B_{\mathrm{tan}}\cup B_{\mathrm{multi}}\bigr).
$$

::: pf-proof

The dual projective space has dimension
$$
\dim\check{\PP}^3=3.
$$
Steps [](#s1){.pf-ref} and [](#s4){.pf-ref} give two closed subsets of dimension at most $2$.
Their union is therefore a proper closed subset of the irreducible
threefold $\check{\PP}^3$. Its complement $U$ is nonempty and open.

:::

:::

::: {.pf-step #s6}

If $H\in U$, then the scheme-theoretic intersection
$$
X\cap H
$$
consists of exactly $d$ distinct reduced points.

::: pf-proof

Because $X$ is not contained in any plane, $H$ does not contain $X$.
Thus $H$ cuts on $X$ an effective hyperplane divisor of degree
$$
\deg X=d.
$$

Let $P\in X\cap H$. The local intersection multiplicity is greater than
$1$ exactly when the linear equation of $H$ has zero differential on the
one-dimensional tangent space $T_PX$, equivalently when
$$
T_PX\subseteq H.
$$
But $H\notin B_{\mathrm{tan}}$, so this never occurs. Every intersection
point therefore has multiplicity $1$.

The total degree of the hyperplane divisor is $d$, so it has exactly
$d$ distinct points.

:::

:::

::: {.pf-step #s7}

No three points of $X\cap H$ are collinear for $H\in U$.

::: pf-proof

Suppose distinct points
$$
P,Q,R\in X\cap H
$$
lay on one line $\ell$. Since a plane containing two points of a line
contains the whole line,
$$
\ell\subseteq H.
$$
The line $\ell$ meets $X$ in at least the three distinct points
$P,Q,R$, so
$$
\operatorname{length}(X\cap\ell)\ge3.
$$
Thus $\ell\in M$, which would imply
$$
H\in B_{\mathrm{multi}},
$$
contrary to $H\in U$.

:::

:::

::: pf-qed

For every plane
$$
H\in U,
$$
step [](#s6){.pf-ref} gives exactly $d$ distinct intersection points and step [](#s7){.pf-ref}
shows that no three are collinear. Step [](#s5){.pf-ref} says that $U$ is a nonempty
Zariski-open subset of the dual projective space. This is precisely the
asserted Bertini lemma.

:::

:::

:::
