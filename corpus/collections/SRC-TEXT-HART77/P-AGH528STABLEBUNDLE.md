---
schema: qual/card@1
id: P-AGH528STABLEBUNDLE
kind: problem
title: Stability of rank two bundles and classification of the unstable indecomposables
classification:
  areas:
  - algebraic-geometry
  topics:
  - Ruled Surfaces
  - Picard Group
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne V.2.8 and the retained companion proof. The corpus
    transcription in part (c) said "up to isomorphism"; that statement is
    false because tensoring by any line bundle preserves rank, indecomposability,
    and (non-)semistability while generally changing the isomorphism class.
    The companion proof itself twists the unique maximal destabilizing line
    subbundle to O_C before extracting the extension data. The selected card is
    therefore repaired to the mathematically coherent classification up to
    tensoring by an invertible sheaf. The proof below also supplies the
    boundedness and uniqueness of the maximal destabilizing line subbundle.
- event: source-corrected
  by: chatgpt
  date: 2026-09-18
  note: Replaced the impossible "up to isomorphism" in part (c) by "up to tensoring with an invertible sheaf".
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
A locally free sheaf $\mathcal{E}$ on a curve $C$ is said to be **stable** if for every quotient locally free sheaf
\[
\mathcal{E} \rightarrow \mathcal{F} \rightarrow 0, \qquad \mathcal{F} \neq \mathcal{E}, \mathcal{F} \neq 0
,\]
we have
\[
(\operatorname{deg} \mathcal{F}) / \operatorname{rank} \mathcal{F}>(\operatorname{deg} \mathcal{E}) / \operatorname{rank} \mathcal{E}
.\]
Replacing $>$ by $\geqslant$ defines **semistable**.

a. A decomposable $\mathcal{E}$ is never stable.

b. If $\mathcal{E}$ has rank 2 and is normalized, then $\mathcal{E}$ is stable (respectively, semistable) if and only if $\deg \mathcal{E}>0$ (respectively, $\geqslant 0$).

c. Show that the indecomposable locally free sheaves $\mathcal{E}$ of rank 2 that are not semistable are classified, up to tensoring with an invertible sheaf, by giving
    (1) an integer $0<e \leqslant 2 g-2$,
    (2) an element $\mathcal{L} \in \Pic C$ of degree $-e$, and
    (3) a nonzero $\xi \in H^1\left(\mathcal{L}\dual\right)$, determined up to a nonzero scalar multiple.
:::

::: {.solution}
For a nonzero locally free sheaf $\mathcal F$ on $C$, write
$$
\mu(\mathcal F)=\frac{\deg\mathcal F}{\operatorname{rank}\mathcal F}.
$$

<1>1. For a rank-two bundle $\mathcal E$, stability is equivalent to
$$
\deg\mathcal A<\frac12\deg\mathcal E
$$
for every line subbundle $\mathcal A\subsetneq\mathcal E$; semistability is
equivalent to the same inequalities with $\le$.

::: {.proof}
If
$$
0\longrightarrow\mathcal A
\longrightarrow\mathcal E
\longrightarrow\mathcal F
\longrightarrow0
$$
has locally free nonzero proper quotient, then both $\mathcal A$ and
$\mathcal F$ have rank one and
$$
\deg\mathcal F=\deg\mathcal E-\deg\mathcal A.
$$
Thus
$$
\deg\mathcal F>\frac12\deg\mathcal E
$$
is equivalent to
$$
\deg\mathcal A<\frac12\deg\mathcal E.
$$
The same rearrangement with weak inequalities proves the semistable statement.
:::

<1>2. A decomposable rank-two bundle is never stable.

::: {.proof}
Write
$$
\mathcal E=\mathcal A\oplus\mathcal B
$$
with $\mathcal A,\mathcal B$ invertible, and after interchanging the summands
assume
$$
\deg\mathcal A\le\deg\mathcal B.
$$
Then
$$
\deg\mathcal A
\le
\frac{\deg\mathcal A+\deg\mathcal B}{2}
=
\frac12\deg\mathcal E.
$$
Since $\mathcal A$ is a line subbundle, step <1>1 shows that $\mathcal E$ is
not stable. This proves part (a).
:::

<1>3. If a rank-two bundle $\mathcal E$ is normalized, then every line
subbundle $\mathcal A\subseteq\mathcal E$ satisfies
$$
\deg\mathcal A\le0.
$$

::: {.proof}
The inclusion
$$
\mathcal A\hookrightarrow\mathcal E
$$
is a nonzero section of
$$
\mathcal E\tensor\mathcal A^{-1}.
$$
If $\deg\mathcal A>0$, then $\mathcal A^{-1}$ has negative degree, contrary
to the defining vanishing for a normalized bundle. Hence
$$
\deg\mathcal A\le0.
$$
:::

<1>4. If a rank-two bundle $\mathcal E$ is normalized, then it contains
$\OO_C$ as a line subbundle.

::: {.proof}
Normalization gives
$$
H^0(C,\mathcal E)\ne0.
$$
Choose a nonzero section
$$
\OO_C\longrightarrow\mathcal E
$$
and saturate its image. The saturation is an invertible subsheaf
$\mathcal A\subseteq\mathcal E$ of the form
$$
\mathcal A\cong\OO_C(D)
$$
for an effective divisor $D$, because saturation removes exactly the zero
divisor of the section. Thus
$$
\deg\mathcal A\ge0.
$$
Step <1>3 gives the reverse inequality, so $\deg D=0$, hence $D=0$ and
$$
\mathcal A\cong\OO_C.
$$
:::

<1>5. If $\mathcal E$ has rank two and is normalized, then
$$
\boxed{\mathcal E\text{ is stable}\iff\deg\mathcal E>0.}
$$

::: {.proof}
Suppose first that $\deg\mathcal E>0$. For every line subbundle
$\mathcal A\subseteq\mathcal E$, step <1>3 gives
$$
\deg\mathcal A\le0
<
\frac12\deg\mathcal E.
$$
Step <1>1 gives stability.

Conversely, if $\mathcal E$ is stable, step <1>4 gives a line subbundle
$$
\OO_C\subseteq\mathcal E.
$$
Applying step <1>1 to this subbundle gives
$$
0<\frac12\deg\mathcal E,
$$
so $\deg\mathcal E>0$.
:::

<1>6. If $\mathcal E$ has rank two and is normalized, then
$$
\boxed{\mathcal E\text{ is semistable}\iff\deg\mathcal E\ge0.}
$$

::: {.proof}
If $\deg\mathcal E\ge0$, then step <1>3 gives, for every line subbundle,
$$
\deg\mathcal A\le0
\le
\frac12\deg\mathcal E,
$$
so step <1>1 gives semistability.

Conversely, semistability and the subbundle $\OO_C\subseteq\mathcal E$ from
step <1>4 give
$$
0\le\frac12\deg\mathcal E.
$$
Thus $\deg\mathcal E\ge0$. Steps <1>5--<1>6 prove part (b).
:::

<1>7. Let $\mathcal E$ be a rank-two bundle that is not semistable. Among all
line subbundles of $\mathcal E$, there is one of maximal degree.

::: {.proof}
First, line subbundles exist. For $n\gg0$, $\mathcal E(n)$ is generated by
global sections. A nonzero section gives a rank-one subsheaf, whose saturation
is an invertible subsheaf; twisting back gives a line subbundle of
$\mathcal E$.

Their degrees are bounded above. Fix an ample line bundle $\OO_C(1)$ of degree
$h>0$. For $n\gg0$, the bundle
$$
\mathcal E^\vee(n)
$$
is globally generated. If
$$
\mathcal A\subseteq\mathcal E
$$
is a line subbundle, dualizing its locally free quotient gives a surjection
$$
\mathcal E^\vee\twoheadrightarrow\mathcal A^\vee.
$$
After twisting by $\OO_C(n)$, the line bundle
$$
\mathcal A^\vee(n)
$$
is a quotient of a globally generated bundle and is therefore globally
generated. Hence its degree is nonnegative:
$$
-\deg\mathcal A+nh\ge0.
$$
Thus
$$
\deg\mathcal A\le nh.
$$
The possible degrees are integers, so they have a maximum.
:::

<1>8. A non-semistable rank-two bundle $\mathcal E$ has a unique line
subbundle $\mathcal A$ of maximal degree, and
$$
2\deg\mathcal A>\deg\mathcal E.
$$

::: {.proof}
Non-semistability gives, by step <1>1, a line subbundle of degree strictly
greater than $\deg\mathcal E/2$. Hence a maximal-degree line subbundle
$\mathcal A$ from step <1>7 also satisfies
$$
2\deg\mathcal A>\deg\mathcal E.
$$

Suppose $\mathcal B$ is a second maximal-degree line subbundle, and write
$$
a=\deg\mathcal A=\deg\mathcal B.
$$
If $\mathcal A$ and $\mathcal B$ have the same generic line in
$\mathcal E$, their saturated images agree, so $\mathcal A=\mathcal B$.
Otherwise their wedge gives a nonzero map of line bundles
$$
\mathcal A\tensor\mathcal B
\longrightarrow
\det\mathcal E.
$$
A nonzero map of line bundles on a projective curve forces the degree of the
source to be at most the degree of the target. Thus
$$
2a\le\deg\mathcal E,
$$
contradicting $2a>\deg\mathcal E$. Hence $\mathcal A$ is unique.
:::

<1>9. Let $\mathcal E$ be indecomposable and not semistable, and let
$\mathcal A$ be its unique maximal-degree line subbundle. Then
$$
\mathcal E_0=\mathcal E\tensor\mathcal A^{-1}
$$
fits into a nonsplit exact sequence
$$
0\longrightarrow\OO_C
\longrightarrow\mathcal E_0
\longrightarrow\mathcal L
\longrightarrow0
$$
with
$$
\deg\mathcal L=-e<0.
$$

::: {.proof}
Tensoring the exact sequence determined by $\mathcal A\subseteq\mathcal E$
with $\mathcal A^{-1}$ gives
$$
0\longrightarrow\OO_C
\longrightarrow\mathcal E_0
\longrightarrow\mathcal L
\longrightarrow0,
$$
where
$$
\mathcal L
\cong
\det\mathcal E\tensor\mathcal A^{-2}.
$$
Therefore
$$
\deg\mathcal L
=
\deg\mathcal E-2\deg\mathcal A
<0
$$
by step <1>8. Write this degree as $-e$, so $e>0$.

If the extension split, $\mathcal E_0$ would be decomposable, hence so would
$\mathcal E=\mathcal E_0\tensor\mathcal A$. This contradicts the hypothesis.
Thus the extension is nonsplit.
:::

<1>10. The bundle $\mathcal E_0$ in step <1>9 is normalized, and its extension
class is a nonzero element
$$
\xi\in H^1(C,\mathcal L^\vee)
$$
well-defined up to nonzero scalar.

::: {.proof}
The inclusion $\OO_C\subseteq\mathcal E_0$ gives a nonzero global section.
If $\mathcal M$ has negative degree, tensoring the sequence of step <1>9 by
$\mathcal M$ gives
$$
0\longrightarrow\mathcal M
\longrightarrow\mathcal E_0\tensor\mathcal M
\longrightarrow\mathcal L\tensor\mathcal M
\longrightarrow0.
$$
Both end line bundles have negative degree, so both have zero global sections.
Hence
$$
H^0(C,\mathcal E_0\tensor\mathcal M)=0.
$$
Thus $\mathcal E_0$ is normalized.

Extensions of $\mathcal L$ by $\OO_C$ are classified by
$$
\Ext^1_C(\mathcal L,\OO_C)
\cong
H^1(C,\mathcal L^\vee)
$$
[[PR-ET5PQ]]. The sequence is nonsplit by step <1>9, so its class $\xi$ is
nonzero. Rescaling the inclusion of $\OO_C$, or equivalently the quotient to
$\mathcal L$, rescales $\xi$ without changing the isomorphism class of the
middle bundle. Thus only its nonzero scalar class is intrinsic.
:::

<1>11. The integer $e$ in step <1>9 satisfies
$$
\boxed{0<e\le2g-2}.
$$

::: {.proof}
The lower bound was proved in step <1>9. Since
$$
0\ne\xi\in H^1(C,\mathcal L^\vee),
$$
Serre duality gives
$$
0\ne
H^0(C,K_C\tensor\mathcal L).
$$
A line bundle with a nonzero section has nonnegative degree, so
$$
0
\le
\deg(K_C\tensor\mathcal L)
=
2g-2-e.
$$
Hence $e\le2g-2$.
:::

<1>12. Conversely, suppose one is given
$$
0<e\le2g-2,
\qquad
\deg\mathcal L=-e,
\qquad
0\ne\xi\in H^1(C,\mathcal L^\vee).
$$
Let
$$
0\longrightarrow\OO_C
\longrightarrow\mathcal E_0
\longrightarrow\mathcal L
\longrightarrow0
$$
be the corresponding extension. Then $\mathcal E_0$ is normalized,
indecomposable, and not semistable.

::: {.proof}
The same argument as in step <1>10 shows that $\mathcal E_0$ is normalized:
it has a section from $\OO_C$, while every negative twist has zero sections
because both end terms of the twisted extension have negative degree.

Its degree is
$$
\deg\mathcal E_0=\deg\mathcal L=-e<0.
$$
Part (b), step <1>6, therefore shows that $\mathcal E_0$ is not semistable.

It remains to prove indecomposability. Suppose
$$
\mathcal E_0\cong\mathcal B\oplus\mathcal C.
$$
Because $\mathcal E_0$ is normalized and has a nonzero section, one summand
has a nonzero section. By step <1>3 it has degree zero, and a degree-zero line
bundle with a nonzero section is trivial. Thus, after relabeling,
$$
\mathcal B\cong\OO_C,
\qquad
\mathcal C\cong\det\mathcal E_0\cong\mathcal L.
$$
Since $\deg\mathcal L<0$, one has $H^0(C,\mathcal L)=0$. Therefore the given
injection
$$
\OO_C\longrightarrow\OO_C\oplus\mathcal L
$$
has zero component in $\mathcal L$ and a nonzero scalar component in
$\OO_C$. It is the standard direct summand up to scalar, so the extension
splits. This contradicts $\xi\ne0$. Hence $\mathcal E_0$ is indecomposable.
:::

<1>13. The construction in steps <1>9--<1>12 gives a bijection between
tensor-equivalence classes of indecomposable non-semistable rank-two bundles
and the data
$$
\boxed{
\left(e,\mathcal L,[\xi]\right),
\quad
0<e\le2g-2,
\quad
\deg\mathcal L=-e,
\quad
[\xi]\in\PP H^1(C,\mathcal L^\vee).}
$$

::: {.proof}
Starting from $\mathcal E$, step <1>8 gives its unique maximal destabilizing
line subbundle $\mathcal A$. Tensoring by $\mathcal A^{-1}$ therefore gives a
canonically normalized representative $\mathcal E_0$ of its tensor-equivalence
class. The unique maximal-degree line subbundle of $\mathcal E_0$ is
$\OO_C$, and its quotient is the intrinsic line bundle
$$
\mathcal L=\det\mathcal E_0.
$$
Thus $e=-\deg\mathcal L$ is intrinsic as well. Once the subbundle and quotient
are fixed up to their scalar automorphisms, the extension class is determined
up to a nonzero scalar by the Ext classification.

Conversely, proportional nonzero extension classes give isomorphic middle
bundles after rescaling the subbundle or quotient, and step <1>12 shows that
every displayed triple produces an indecomposable non-semistable bundle.
Tensoring such a bundle by an arbitrary line bundle preserves
indecomposability and all slope inequalities after shifting every slope by the
same degree.

Finally, two normalized representatives produced in this way cannot become
isomorphic after a nontrivial line-bundle twist. Indeed, the unique
maximal-degree subbundle of $\mathcal E_0\tensor\mathcal M$ is $\mathcal M$,
whereas that of another normalized representative is $\OO_C$. An isomorphism
between them would force $\mathcal M\cong\OO_C$. Hence the triple displayed in
step <1>13 classifies the tensor-equivalence classes uniquely. This proves part
(c).
:::

<1>14. Q.E.D.

::: {.proof}
Step <1>2 proves part (a), steps <1>3--<1>6 prove part (b), and steps
<1>7--<1>13 prove the corrected classification in part (c).
:::
:::
