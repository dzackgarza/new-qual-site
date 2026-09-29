---
schema: qual/card@1
id: P-AGH5212ELLRULEDAMPLE
kind: problem
title: Base points and very ampleness on a ruled surface over an elliptic curve
classification:
  areas:
  - algebraic-geometry
  topics:
  - Surfaces
  - Ruled Surfaces
  - Picard Group
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-19
  note: >-
    Read Hartshorne V.2.12, the retained Egbert companion pointer to
    Fuentes--Pedreira, V.2.11, and the preceding stability and e=-1 elliptic
    ruled-surface cards. For e>=0, the assertions follow from V.2.11 and the
    degree-2/degree-3 base-point-free/very-ample thresholds on an elliptic
    curve. The exceptional e=-1 case is proved directly: the normalized
    rank-two bundle has degree 1 and is stable, so its twists have the H^1
    vanishings required for fibrewise generation and separation of all
    length-two subschemes. Necessity in (b) follows by restricting to C_0.
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
---

::: {.problem}
Let $X$ be a ruled surface with invariant $e$ over an elliptic curve $C$, and let $\mfb$ be a divisor on $C$.

a. If $\deg \mfb \geqslant e+2$, then there is a section $D \sim C_0+\mfb f$ such that $|D|$ has no base points.

b. The linear system $\left|C_0+\mfb f\right|$ is very ample if and only if $\deg \mfb \geqslant e+3$.

Note.
The case $e=-1$ will require special attention.
:::

::: {.solution}
Put
$$
m=\deg\mfb,
$$
and let $\mfe$ represent $\det\mathcal E$ as in (2.8.1). Thus
$$
\deg\mfe=-e.
$$
Write
$$
\pi:X=\PP(\mathcal E)\longrightarrow C,
\qquad
L=\OO_X(C_0+\mfb f).
$$

::: pf

::: {.pf-step #s1}

On the elliptic curve $C$, every line bundle of positive degree is
nonspecial; degree at least $2$ is base-point free, and degree at least $3$
is very ample.

::: pf-proof

Since
$$
K_C\cong\OO_C,
$$
Serre duality gives
$$
H^1(C,M)^\vee\cong H^0(C,M^{-1}).
$$
If $\deg M>0$, then $M^{-1}$ has negative degree and no nonzero section, so
$M$ is nonspecial.

The base-point-free and very-ample degree bounds are the genus-one cases of
the standard curve criteria [[T-D8TUX]]: degree at least $2g=2$ is
base-point free, and degree at least $2g+1=3$ is very ample.

:::

:::

::: {.pf-step #s2}

If $e\ge0$ and
$$
m\ge e+2,
$$
then part (a) holds.

::: pf-proof

One has
$$
\deg\mfb=m\ge2
$$
and
$$
\deg(\mfb+\mfe)=m-e\ge2.
$$
By step [](#s1){.pf-ref}, both complete linear systems are base-point free, and $\mfb$
is nonspecial. Hartshorne V.2.11, proved on
[[P-AGH5211VERYAMPLESECT]], therefore gives a section
$$
D\sim C_0+\mfb f
$$
and says that $|L|$ has no base points.

:::

:::

::: {.pf-step #s3}

Suppose $e=-1$. Then $\deg\mathcal E=1$, the normalized bundle
$\mathcal E$ is stable, and
$$
L\cong\OO_X(1)\tensor\pi^*\OO_C(\mfb),
\qquad
\pi_*L\cong\mathcal E\tensor\OO_C(\mfb).
$$

::: pf-proof

By definition of the invariant of a normalized ruled surface,
$$
e=-\deg\det\mathcal E.
$$
Thus $e=-1$ gives
$$
\deg\mathcal E=\deg\det\mathcal E=1.
$$
Hartshorne V.2.8, proved on [[P-AGH528STABLEBUNDLE]], says that a normalized
rank-two bundle is stable exactly when its degree is positive. Hence
$\mathcal E$ is stable.

Normalization gives an exact sequence
$$
0\longrightarrow\OO_C
\longrightarrow\mathcal E
\longrightarrow\det\mathcal E
\longrightarrow0.
$$
The corresponding quotient section is $C_0$.  The divisor formula for a
section of a projective bundle, as used in
[[P-AGH527ELLRULEDSECT]], gives
$$
\OO_X(C_0)\cong\OO_X(1)
$$
because the kernel is $\OO_C$. Therefore
$$
L
\cong
\OO_X(1)\tensor\pi^*\OO_C(\mfb).
$$
For Hartshorne's quotient convention,
$$
\pi_*\OO_X(1)\cong\mathcal E,
$$
so the projection formula gives the displayed formula for $\pi_*L$.

:::

:::

::: {.pf-step #s4}

Let $F$ be a stable vector bundle of positive degree on the elliptic
curve $C$. Then
$$
H^1(C,F)=0.
$$

::: pf-proof

Serre duality and $K_C\cong\OO_C$ give
$$
H^1(C,F)^\vee\cong H^0(C,F^\vee).
$$
The dual bundle $F^\vee$ is stable of negative degree. A nonzero section
would give a subsheaf $\OO_C\subseteq F^\vee$; after saturation this would
give a line subbundle of degree at least $0$, contradicting stability because
$$
0>\mu(F^\vee).
$$
Thus $H^0(C,F^\vee)=0$ and hence $H^1(C,F)=0$.

:::

:::

::: {.pf-step #s5}

If $e=-1$ and $m\ge1$, then $|L|$ has no base points and contains a
section of $\pi$.

::: pf-proof

Put
$$
F=\mathcal E\tensor\OO_C(\mfb).
$$
Twisting preserves stability, and
$$
\deg F
=
\deg\mathcal E+2m
=
1+2m.
$$
For every point $P\in C$, the stable bundle
$$
F(-P)
$$
has degree
$$
1+2m-2=2m-1>0.
$$
Step [](#s4){.pf-ref} therefore gives
$$
H^1(C,F(-P))=0.
$$
The exact sequence
$$
0\to F(-P)\to F\to F|_P\to0
$$
shows that
$$
H^0(C,F)\twoheadrightarrow F|_P
$$
for every $P$.

By step [](#s3){.pf-ref} and cohomology and base change,
$$
F|_P
\cong
H^0\bigl(F_P,L|_{F_P}\bigr),
\qquad
L|_{F_P}\cong\OO_{\PP^1}(1).
$$
Thus the complete system $|L|$ restricts to the complete
$|\OO_{\PP^1}(1)|$ on every ruling fibre. In particular $|L|$ has no base
points.

The incidence argument of [[P-AGH5211VERYAMPLESECT]], step [](#s4){.pf-ref}, now applies
verbatim: the sections vanishing identically on a fixed fibre form a
codimension-two subspace of $H^0(X,L)$, so a general divisor in $|L|$
contains no fibre. Since
$$
L\cdot f=1,
$$
such a divisor is a section of $\pi$. This proves part (a) in the exceptional
$e=-1$ case.

:::

:::

::: {.pf-step #s6}

Part (a) holds for every ruled surface over $C$ satisfying
$$
\deg\mfb\ge e+2.
$$

::: pf-proof

The standard invariant bound quoted in [[P-AGH525INVARIANTE]] for a ruled
surface over a genus-one curve is
$$
e\ge-1.
$$
If $e\ge0$, apply step [](#s2){.pf-ref}. If $e=-1$, the hypothesis is exactly
$$
m\ge1,
$$
so step [](#s5){.pf-ref} applies.

:::

:::

::: {.pf-step #s7}

If $e\ge0$ and
$$
m\ge e+3,
$$
then $L$ is very ample.

::: pf-proof

The two line bundles on the base have degrees
$$
\deg\mfb=m\ge3,
\qquad
\deg(\mfb+\mfe)=m-e\ge3.
$$
Hence both are very ample by step [](#s1){.pf-ref}.

For every point $P\in C$,
$$
\deg(\mfb-P)=m-1>0
$$
and
$$
\deg(\mfb+\mfe-P)=m-e-1>0.
$$
Step [](#s1){.pf-ref} makes both line bundles nonspecial. Hartshorne V.2.11(b), proved
on [[P-AGH5211VERYAMPLESECT]], therefore says that
$$
C_0+\mfb f
$$
is very ample.

:::

:::

::: {.pf-step #s8}

If $e=-1$ and
$$
m\ge2,
$$
then $L$ separates every zero-dimensional subscheme of $X$ of length $2$.

::: pf-proof

Keep
$$
F=\mathcal E\tensor\OO_C(\mfb)
$$
from step [](#s5){.pf-ref}. It is stable of degree
$$
1+2m.
$$

First let $Z$ be a length-two subscheme contained in one fibre $F_P$.
The bundle $F(-P)$ has positive degree $2m-1$, so step [](#s4){.pf-ref} gives
$$
H^1(C,F(-P))=0.
$$
Thus global sections of $L$ restrict surjectively to
$$
H^0(F_P,\OO_{F_P}(1)),
$$
and $\OO_{\PP^1}(1)$ separates $Z$.

Now suppose $Z$ is not contained in a fibre. Its scheme-theoretic image is a
degree-two effective divisor $A$ on $C$, and $Z\to A$ is an isomorphism, as
in [[P-AGH5211VERYAMPLESECT]], step [](#s8){.pf-ref}. The twist
$$
F(-A)
$$
is stable of degree
$$
1+2m-4=2m-3>0.
$$
Step [](#s4){.pf-ref} gives
$$
H^1(C,F(-A))=0,
$$
so
$$
H^0(C,F)\twoheadrightarrow H^0(A,F|_A).
$$

Over the Artinian scheme $A$, the subscheme $Z\cong A$ is a section of
$$
\PP(\mathcal E|_A)\longrightarrow A.
$$
It therefore corresponds to an invertible quotient of
$$
F|_A=\mathcal E|_A\tensor\OO_A(\mfb).
$$
Since $A$ is affine, taking global sections of that quotient is surjective.
Consequently
$$
H^0(X,L)\longrightarrow H^0(Z,L|_Z)
$$
is surjective. Thus every length-two subscheme is separated.

:::

:::

::: {.pf-step #s9}

If $e=-1$ and $m\ge2$, then $L$ is very ample.

::: pf-proof

By step [](#s8){.pf-ref}, the complete linear system of $L$ separates every
zero-dimensional subscheme of length $2$. The closed-immersion criterion
[[T-DIVMAPPN]] therefore makes $L$ very ample.

:::

:::

::: {.pf-step #s10}

If $L$ is very ample, then
$$
\boxed{m\ge e+3}.
$$

::: pf-proof

The restriction of a very ample line bundle to a closed subscheme is very
ample. In particular,
$$
L|_{C_0}
\cong
\OO_C(\mfb+\mfe)
$$
must be very ample on the elliptic curve $C_0\cong C$.

Its degree is
$$
m-e.
$$
A very ample line bundle on an elliptic curve has degree at least $3$:
Riemann--Roch gives $h^0(M)=\deg M$ for positive-degree $M$, while an
embedding of a positive-genus curve requires at least three independent
sections. Hence
$$
m-e\ge3,
$$
or equivalently
$$
m\ge e+3.
$$

:::

:::

::: {.pf-step #s11}

Therefore
$$
\boxed{
|C_0+\mfb f|\text{ is very ample}
\iff
\deg\mfb\ge e+3.}
$$

::: pf-proof

For sufficiency, the invariant bound gives either $e\ge0$, handled by step
[](#s7){.pf-ref}, or $e=-1$, where $m\ge e+3=2$ and step [](#s9){.pf-ref} applies. Necessity is step
[](#s10){.pf-ref}. This proves part (b).

:::

:::

::: pf-qed

Step [](#s6){.pf-ref} proves part (a), and steps [](#s7){.pf-ref}, [](#s8){.pf-ref}, [](#s9){.pf-ref}, [](#s10){.pf-ref} and [](#s11){.pf-ref} prove part (b).

:::

:::

:::
