---
schema: qual/card@1
id: P-AGH273MORPROJSP
kind: problem
title: Morphisms between projective spaces
classification:
  areas:
  - algebraic-geometry
  topics:
  - Projective Space
  - Veronese Embedding
  - Linear Projection
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared both parts with the retained Hartshorne II.7.3 transcription. Corrected the unqualified projection onto the whole target by inserting the image's linear span, with a linear-inclusion counterexample. The proof establishes finiteness through the homogeneous coordinate subalgebra and retains arbitrary fields and dependent coordinates.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $\varphi: \PP^n_k \to \PP^m_k$ be a morphism.
Then

(a) either $\varphi(\PP^n) = \pt$, or $m \geq n$ and $\dim \varphi(\PP^n) = n$;

(b) in the second case, let $\PP^r\subseteq\PP^m$ be the linear span of the image.
Show that $\varphi$ can be obtained as the composition of

    1. a $d$-uple embedding $\PP^n \to \PP^N$ for a uniquely determined $d \geq 1$,
    2. a linear projection $\PP^N - L \to \PP^r$,
    3. the standard linear inclusion $\PP^r\hookrightarrow\PP^m$, and
    4. an automorphism of $\PP^m$ carrying that coordinate subspace to the image's linear span.

When the image is nondegenerate, $r=m$ and the inclusion is unnecessary.
Also, $\varphi$ has finite fibres.
:::

::: {.solution}
All morphisms are over $k$.
For $n=0$ the source is $\Spec k$, so the image is one point and only the first alternative of (a) applies.
Assume $n\ge1$, and put $S=k[x_0,\ldots,x_n]$ with its usual grading.

::: pf

::: {.pf-step #s1}

The morphism is defined by forms $f_0,\ldots,f_m\in S_d$ with no common zero, for a unique integer $d\ge0$.
When $d=0$, it is constant.

::: pf-proof

The [[D-5PQ5W|Picard group]] of $\PP_k^n$ is generated freely by $\OO(1)$ [@Har10a, Proposition II.6.4 and Corollary II.6.16].
Consequently $\varphi^*\OO_{\PP^m}(1)\cong\OO_{\PP^n}(d)$ for a unique integer $d$.
Pulling back the coordinate sections gives $m+1$ sections generating this invertible sheaf [@Har10a, Theorem II.7.1].
The global sections of $\OO(d)$ are $S_d$ for $d\ge0$ and zero for $d<0$ [@Har10a, Proposition II.5.13].
Generation excludes $d<0$ and gives the stated forms and their empty common zero locus.
The morphism has coordinates $[f_0:\cdots:f_m]$.
For $d=0$, these are constants in $k$, not all zero, so the morphism factors through their $k$-rational point.

:::

:::

::: {.pf-step #s2}

For $d>0$, the Veronese ring $R=\bigoplus_{q\ge0}S_{qd}$ is a finite module over $A=k[f_0,\ldots,f_m]$, where both rings are graded with $f_i$ of degree one.

::: pf-proof

Let $I=(f_0,\ldots,f_m)\subseteq S$.
The empty projective common zero locus implies that each $x_j$ has a power in $I$.
Indeed, on $D_+(x_j)$ the functions $f_i/x_j^d$ generate the unit ideal; clearing denominators in a unit-ideal expression gives $x_j^{b_j}\in I$ for some $b_j\ge1$.
Every monomial of sufficiently large total degree is divisible by one of these powers.
There is therefore $B\ge d$ with $S_q\subseteq I$ for every $q\ge B$.

If $h\in S_{qd}$ and $qd\ge B$, homogeneity gives
$$
h=\sum_{i=0}^m f_i h_i,\qquad h_i\in S_{(q-1)d}.
$$
Induction on $q$ expresses $h$ as an $A$-linear combination of monomials of degrees divisible by $d$ and smaller than $B$.
There are finitely many such monomials, proving that $R$ is a finite graded $A$-module.

:::

:::

::: {.pf-step #s3}

If $d>0$, the morphism is finite onto its image, and that image has dimension $n$.

::: pf-proof

The surjection $k[y_0,\ldots,y_m]\to A$, $y_i\mapsto f_i$, identifies $Y=\operatorname{Proj}A$ with a closed integral subscheme of $\PP^m$.
Also $\operatorname{Proj}R\cong\PP^n$ by the Veronese construction [@Har10a, Exercise II.5.13].
The graded inclusion $A\subseteq R$ induces the morphism $\varphi$ with target restricted to $Y$.

For every nonzero $f_i$, its inverse image of $D_+(f_i)\subseteq Y$ is the affine open $D_+(f_i)\subseteq\operatorname{Proj}R$.
The corresponding ring inclusion is
$$
(A[f_i^{-1}])_0\longrightarrow(R[f_i^{-1}])_0.
$$
If homogeneous elements $u_j$ of degrees $e_j$ generate $R$ as an $A$-module, then $u_j/f_i^{e_j}$ generate the right-hand ring as a module over the left-hand ring.
This follows by taking degree-zero parts of expressions in the localized graded module.
Thus these ring maps are finite and injective, so their maps on spectra are surjective by lying over.
The opens cover $Y$; hence $\PP^n\to Y$ is finite and surjective.
Composing with $Y\hookrightarrow\PP^m$ shows that $\varphi$ is itself finite.

Integral extensions preserve Krull dimension: going up lifts chains and incomparability prevents a strict chain from collapsing under contraction [@AM18, Chapter 5].
Step [](#s2){.pf-ref} makes $R$ integral over $A$.
The ring $S$ is integral over $R$, since each $x_j$ satisfies the monic equation $T^d-x_j^d=0$ with coefficient $x_j^d\in R$.
Therefore $\dim A=\dim R=\dim S=n+1$.
For a standard graded finite-type domain over $k$, its Proj has dimension one less than the ring [@Har10a, Chapter I, §2].
It follows that $\dim Y=n$, so $m\ge n$.
Every fibre of the finite morphism is the spectrum of a finite-dimensional algebra over its residue field, and thus has finitely many points.
Together with step [](#s1){.pf-ref}, this proves (a) and the fibre assertion of (b).

:::

:::

::: {.pf-step #s4}

For $d>0$, the morphism factors through the $d$-uple embedding, projection onto its image's linear span, and the stated linear inclusion and automorphism.

::: pf-proof

Let $V$ be the span of $f_0,\ldots,f_m$ in $S_d$, and write $r+1=\dim_kV$.
Choose a basis $g_0,\ldots,g_r$ of $V$ and extend it to a basis $g_0,\ldots,g_N$ of $S_d$, where
$$
N=\binom{n+d}{d}-1.
$$
The complete set of degree-$d$ monomials gives the $d$-uple closed embedding; replacing that monomial basis by the $g_i$ changes it by an ambient projective linear automorphism [@Har10a, Exercises I.2.12 and I.3.4].
Denote the resulting embedding by $\nu_d$.
The projection
$$
p:\PP^N\setminus L\longrightarrow\PP^r,\qquad
[z_0:\cdots:z_N]\longmapsto[z_0:\cdots:z_r],
\quad L=V_+(z_0,\ldots,z_r),
$$
is defined on $\nu_d(\PP^n)$ because the $g_0,\ldots,g_r$ span the same globally generating space as the $f_i$.

Write $f_i=\sum_{j=0}^r c_{ij}g_j$.
The matrix $C=(c_{ij})$ has rank $r+1$, since the $f_i$ span $V$.
Extend its columns to a basis of $k^{m+1}$, producing an invertible matrix and hence an automorphism $\alpha$ of $\PP^m$.
For the coordinate inclusion $\iota:\PP^r\hookrightarrow\PP^m$, the resulting factorization is
$$
\boxed{\varphi=\alpha\circ\iota\circ p\circ\nu_d.}
$$
Both sides have the same generating sections $f_i$, so this is equality of morphisms by Theorem II.7.1, not only equality on points.

No nonzero linear form vanishes on $p\nu_d(\PP^n)$: its pullback would be a zero linear combination of the basis elements $g_0,\ldots,g_r$.
Consequently $\alpha\iota(\PP^r)$ is exactly the linear span of the image.
When $r=m$, $\iota$ is the identity and the factorization has the three maps in the nondegenerate statement.

:::

:::

::: {.pf-step #s5}

The integer in the factorization is uniquely determined by $\varphi^*\OO(1)\cong\OO(d)$.

::: pf-proof

The pullback of $\OO(1)$ under a linear projection is $\OO(1)$ on its domain, because its defining linear forms generate that restricted line bundle.
Linear inclusions and projective linear automorphisms also preserve $\OO(1)$, and the $e$-uple embedding pulls it back to $\OO(e)$.
Thus any factorization of the stated kind gives $\varphi^*\OO(1)\cong\OO(e)$.
The uniqueness in step [](#s1){.pf-ref} forces $e=d$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} prove the alternatives and finite fibres.
Steps [](#s4){.pf-ref} and [](#s5){.pf-ref} give the general factorization and the uniqueness of its degree.

:::

:::

:::

::: {.remark title="Projection onto the linear span"}
The retained statement of Exercise II.7.3 projects directly onto $\PP^m$, which requires the image to be nondegenerate when the $d$-uple embedding uses the complete degree-$d$ system.
For example, $[x:y]\mapsto[x:y:0]$ from $\PP^1$ to $\PP^2$ pulls $\OO(1)$ back to $\OO(1)$.
It therefore has $d=1$ and $N=1$, and no surjective linear map $k^2\to k^3$ exists to define the claimed projection.
Even when $m=N$, the map $[x:y]\mapsto[x^2:y^2:0]$ has $d=2$ and image a line, whereas a linear projection $\PP^2\to\PP^2$ is an automorphism and cannot carry the nondegenerate Veronese conic into a line.
Projection onto $\PP^r$, followed by a linear inclusion, covers these cases without changing the morphism or its uniquely determined $d$.
:::
