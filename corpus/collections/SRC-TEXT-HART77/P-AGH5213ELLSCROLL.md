---
schema: qual/card@1
id: P-AGH5213ELLSCROLL
kind: problem
title: Existence of elliptic scrolls of given degree
classification:
  areas:
  - algebraic-geometry
  topics:
  - Surfaces
  - Ruled Surfaces
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-19
  note: >-
    Read Hartshorne V.2.13, the retained Egbert companion calculation, and
    the preceding invariant and elliptic ruled-surface very-ampleness cards.
    The companion has the intended route: choose a ruled surface of invariant
    e and embed by C_0+n f. Its final dimension line conflates h^0 with the
    projective-space dimension; the proof below keeps h^0=2n-e=d and hence
    embeds by the complete system in P^{d-1}. The e=-1 case is supplied by
    V.2.5(c), e=0 by V.2.5(a), and e>0 by the explicit normalized split bundle
    O_C direct-sum L with deg L=-e.
- event: solution-written
  by: chatgpt
  date: 2026-09-19
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-19
---

::: {.problem}
For every $e \geqslant-1$ and $n \geqslant e+3$, there is an elliptic scroll of degree $d=2 n-e$ in $\PP^{d-1}$.
In particular, there is an elliptic scroll of degree 5 in $\PP^4$.
:::

::: {.solution}
Fix an elliptic curve $C$.

::: pf

::: {.pf-step #s1}

For every integer
$$
e\ge-1
$$
there is a ruled surface
$$
\pi:X=\PP(\mathcal E)\longrightarrow C
$$
with invariant $e$.

::: pf-proof

For $e=-1$, Hartshorne V.2.5(c), proved on [[P-AGH525INVARIANTE]], gives a
ruled surface over the genus-one curve $C$ with invariant $-1$.

For $e=0$, V.2.5(a) gives an indecomposable normalized rank-two bundle with
invariant zero.

Now let $e>0$. Choose a line bundle $M$ of degree $-e$ on $C$ and put
$$
\mathcal E=\OO_C\oplus M.
$$
The summand $\OO_C$ gives a nonzero global section. If $N$ has negative
degree, then both
$$
N
\qquad\text{and}\qquad
M\tensor N
$$
have negative degree and hence no sections. Thus
$$
H^0(C,\mathcal E\tensor N)=0,
$$
so $\mathcal E$ is normalized. Since
$$
\deg\det\mathcal E=-e,
$$
the invariant of $\PP(\mathcal E)$ is $e$.

:::

:::

::: {.pf-step #s2}

Let $C_0$ be the normalized section and $f$ a ruling fibre. Then
$$
C_0^2=-e,
\qquad
C_0\cdot f=1,
\qquad
f^2=0.
$$

::: pf-proof

These are the standard intersection formulas for a normalized geometrically
ruled surface: the invariant is
$$
e=-C_0^2,
$$
while a section meets every fibre once and distinct fibres are disjoint.

:::

:::

::: {.pf-step #s3}

Choose a divisor $\mfb$ on $C$ with
$$
\deg\mfb=n,
$$
and put
$$
D=C_0+\mfb f.
$$
If
$$
n\ge e+3,
$$
then $D$ is very ample.

::: pf-proof

This is exactly Hartshorne V.2.12(b), proved on
[[P-AGH5212ELLRULEDAMPLE]]: on a ruled surface over an elliptic curve,
$$
|C_0+\mfb f|
$$
is very ample if and only if
$$
\deg\mfb\ge e+3.
$$

:::

:::

::: {.pf-step #s4}

The embedding defined by $|D|$ makes every ruling fibre a line.

::: pf-proof

By step [](#s2){.pf-ref},
$$
D\cdot f
=
(C_0+\mfb f)\cdot f
=
1.
$$
Hence
$$
\OO_X(D)|_f\cong\OO_{\PP^1}(1).
$$
Because the complete system $|D|$ is very ample by step [](#s3){.pf-ref}, its
restriction embeds each fibre as a projective line. Thus the image is a
scroll over the elliptic curve $C$.

:::

:::

::: {.pf-step #s5}

The degree of this embedded scroll is
$$
\boxed{d=2n-e}.
$$

::: pf-proof

For a surface embedded by the very ample divisor $D$, its degree is $D^2$.
Using step [](#s2){.pf-ref},
$$
\begin{aligned}
D^2
&=(C_0+\mfb f)^2\\
&=C_0^2+2n(C_0\cdot f)+n^2f^2\\
&=-e+2n\\
&=2n-e.
\end{aligned}
$$

:::

:::

::: {.pf-step #s6}

The complete linear system $|D|$ has
$$
\boxed{h^0(X,\OO_X(D))=2n-e=d}.
$$

::: pf-proof

Let $\mfe$ be the divisor on $C$ with
$$
\OO_C(\mfe)\cong\det\mathcal E.
$$
Then
$$
\deg\mfe=-e.
$$

The section restriction calculation from Hartshorne V.2.11, proved in
[[P-AGH5211VERYAMPLESECT]], gives, because $\mfb$ is nonspecial,
$$
h^0(X,\OO_X(C_0+\mfb f))
=
h^0(C,\OO_C(\mfb))
+
h^0(C,\OO_C(\mfb+\mfe)).
$$
Here
$$
\deg\mfb=n>0,
\qquad
\deg(\mfb+\mfe)=n-e\ge3>0.
$$
On the elliptic curve, Riemann--Roch and Serre duality give
$$
h^0(C,L)=\deg L
$$
for every positive-degree line bundle $L$. Therefore
$$
h^0(X,\OO_X(D))
=
n+(n-e)
=
2n-e
=
d.
$$

:::

:::

::: {.pf-step #s7}

The complete linear system $|D|$ embeds $X$ as an elliptic scroll of
degree $d$ in
$$
\boxed{\PP^{d-1}}.
$$

::: pf-proof

Step [](#s3){.pf-ref} gives very ampleness, so the complete system defines a closed
immersion
$$
X\hookrightarrow\PP\bigl(H^0(X,\OO_X(D))^\vee\bigr).
$$
By step [](#s6){.pf-ref} the target is $\PP^{d-1}$. Step [](#s4){.pf-ref} identifies the image as a
scroll over the elliptic curve, and step [](#s5){.pf-ref} gives degree $d$.

:::

:::

::: {.pf-step #s8}

There is an elliptic scroll of degree $5$ in $\PP^4$.

::: pf-proof

Take
$$
e=-1,
\qquad
n=2.
$$
Then
$$
n=e+3,
$$
so the construction applies, and
$$
d=2n-e=4+1=5.
$$
Step [](#s7){.pf-ref} therefore gives an elliptic scroll of degree $5$ in
$$
\PP^{5-1}=\PP^4.
$$

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref}, [](#s5){.pf-ref}, [](#s6){.pf-ref} and [](#s7){.pf-ref} prove the asserted existence for every $e\ge-1$ and
$n\ge e+3$, and step [](#s8){.pf-ref} gives the stated degree-five example.

:::

:::

:::
