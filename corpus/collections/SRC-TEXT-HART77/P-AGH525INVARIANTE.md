---
schema: qual/card@1
id: P-AGH525INVARIANTE
kind: problem
title: Which values of the invariant $e$ occur for ruled surfaces over a curve
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
  date: 2026-09-18
  note: >-
    Read Hartshorne V.2.5, the retained Egbert companion argument for all four
    parts, and the surrounding ruled-surface normalization conventions. The
    proof below replaces the companion's elementary-transform construction in
    (a) by explicit nonsplit normalized extensions. In (b) it makes precise
    the Serre-dual pullback criterion behind the subspaces L_E. Part (c) uses
    the intended incidence variety in P H^1(O_C(-D)); its dimension is at most
    2d-3, strictly below g+d-2 when d<=g. For (d), both the printed exercise
    note and the retained companion cite Nagata's general theorem e>=-g.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Let $C$ be a curve of genus $g \geqslant 1$.

a. Show that for each $0 \leqslant e \leqslant 2 g-2$ there is a ruled surface $X$ over $C$ with invariant $e$, corresponding to an indecomposable $\mathcal{E}$.
Cf.
(2.12).

b. Let $e<0$, let $D$ be any divisor of degree $d=-e$, and let $\xi \in H^1(\mathcal{L}(-D))$ be a nonzero element defining an extension
\[
0 \rightarrow \mathcal{O}_C \rightarrow \mathcal{E} \rightarrow \mathcal{L}(D) \rightarrow 0 .
\]
Let $H \subseteq|D+K|$ be the sublinear system of codimension 1 defined by $\ker \xi$, where $\xi$ is considered as a linear functional on $H^0(\mathcal{L}(D+K))$.
For any effective divisor $E$ of degree $d-1$, let $L_E \subseteq|D+K|$ be the sublinear system $|D+K-E|+E$.
Show that $\mathcal{E}$ is normalized if and only if for each $E$ as above, $L_E \nsubseteq H$.
Cf.
proof of $(2.15)$.

c. Now show that if $-g \leqslant e<0$, there exists a ruled surface $X$ over $C$ with invariant $e$.

Hint: For any given $D$ in (b), show that a suitable $\xi$ exists, using an argument similar to the proof of (II, 8.18).

d. For $g=2$, show that $e \geqslant-2$ is also necessary for the existence of $X$.

Note.
It has been shown that $e \geqslant-g$ for any ruled surface (Nagata [8]).
:::

::: {.solution}
Recall that a rank-two bundle $\mathcal E$ on $C$ is normalized when
$$
H^0(C,\mathcal E)\ne0
$$
but
$$
H^0(C,\mathcal E\tensor\mathcal M)=0
$$
for every invertible sheaf $\mathcal M$ of negative degree. For a normalized
bundle defining $X=\PP(\mathcal E)$, the invariant is
$$
e=-\deg\det\mathcal E.
$$

<1>1. Fix
$$
0\le e\le2g-2.
$$
There is an invertible sheaf $\mathcal L$ of degree $-e$ with
$$
\Ext^1_C(\mathcal L,\OO_C)\ne0.
$$

::: {.proof}
Choose an effective divisor $A$ of degree $2g-2-e$ and put
$$
\mathcal L=\OO_C(A-K_C).
$$
Then $\deg\mathcal L=-e$, and
$$
\Ext^1_C(\mathcal L,\OO_C)
\cong H^1(C,\mathcal L^{-1})
=H^1\qty(C,\OO_C(K_C-A)).
$$
Serre duality gives
$$
H^1\qty(C,\OO_C(K_C-A))^\vee
\cong H^0(C,\OO_C(A)),
$$
which is nonzero because $A$ is effective.
:::

<1>2. A nonzero class in step <1>1 defines a normalized extension
$$
0\longrightarrow\OO_C
\longrightarrow\mathcal E
\longrightarrow\mathcal L
\longrightarrow0.
$$

::: {.proof}
The inclusion of $\OO_C$ gives $H^0(C,\mathcal E)\ne0$. Let $\mathcal M$ have
negative degree. Tensoring the extension by $\mathcal M$ gives
$$
0\longrightarrow\mathcal M
\longrightarrow\mathcal E\tensor\mathcal M
\longrightarrow\mathcal L\tensor\mathcal M
\longrightarrow0.
$$
Both end terms have negative degree because $\deg\mathcal L=-e\le0$. Hence
both have zero $H^0$, and the long exact sequence gives
$$
H^0(C,\mathcal E\tensor\mathcal M)=0.
$$
Thus $\mathcal E$ is normalized.
:::

<1>3. The bundle $\mathcal E$ in step <1>2 is indecomposable.

::: {.proof}
Suppose
$$
\mathcal E\cong\mathcal A\oplus\mathcal B
$$
with $\mathcal A,\mathcal B$ invertible. Since $H^0(C,\mathcal E)\ne0$, one
summand, say $\mathcal A$, has a nonzero section, so $\deg\mathcal A\ge0$. If
$\deg\mathcal A>0$, twisting by the negative-degree line bundle
$\mathcal A^{-1}$ produces an $\OO_C$ summand and contradicts normalization.
Thus $\deg\mathcal A=0$, and its nonzero section forces
$\mathcal A\cong\OO_C$. Consequently
$$
\mathcal B\cong\det\mathcal E\cong\mathcal L.
$$

If $\mathcal L$ is nontrivial of degree zero or has negative degree, then
$H^0(C,\mathcal L)=0$, so the injection
$\OO_C\to\OO_C\oplus\mathcal L$ has only a nonzero constant component in the
$\OO_C$ summand and splits. If $\mathcal L\cong\OO_C$, the injection is a
nonzero constant vector in $k^2$, and a constant change of basis again splits
it. Either conclusion contradicts the choice of a nonzero extension class.
:::

<1>4. For every $0\le e\le2g-2$ there is an indecomposable ruled surface over
$C$ with invariant $e$.

::: {.proof}
For the normalized bundle in steps <1>2--<1>3,
$$
\deg\det\mathcal E=\deg\mathcal L=-e.
$$
Thus $X=\PP(\mathcal E)$ has invariant $e$, and step <1>3 gives
indecomposability. This proves part (a).
:::

<1>5. For part (b), let
$$
0\longrightarrow\OO_C
\longrightarrow\mathcal E
\longrightarrow\OO_C(D)
\longrightarrow0
$$
be the given extension, with $d=\deg D=-e>0$ and class
$$
0\ne\xi\in H^1(C,\OO_C(-D)).
$$
Under Serre duality, $\xi$ is a nonzero linear functional on
$$
V=H^0(C,\OO_C(K_C+D)),
$$
and the subsystem $H$ is $\PP(\ker\xi)$.

::: {.proof}
There are natural identifications
$$
\Ext^1_C\qty(\OO_C(D),\OO_C)
\cong H^1(C,\OO_C(-D))
$$
and
$$
H^1(C,\OO_C(-D))^\vee
\cong H^0(C,\OO_C(K_C+D)).
$$
This is exactly the interpretation of $\xi$ and $H$ in the statement.
:::

<1>6. Let $F$ be any effective divisor with $\deg F\le d-1$. Pulling the
extension in step <1>5 back along
$$
\OO_C(D-F)\hookrightarrow\OO_C(D)
$$
gives a class
$$
\beta_F(\xi)\in H^1(C,\OO_C(F-D)),
$$
and
$$
\boxed{\beta_F(\xi)=0\iff L_F\subseteq H,}
\qquad
L_F=|K_C+D-F|+F.
$$

::: {.proof}
Let $s_F$ be the canonical section of $\OO_C(F)$. The inclusion is
multiplication by $s_F$. Under Serre duality, the dual of the induced map
$\beta_F$ is therefore
$$
H^0\qty(C,\OO_C(K_C+D-F))
\xrightarrow{\cdot s_F}
H^0\qty(C,\OO_C(K_C+D)).
$$
Its projective image is precisely $L_F$. Hence $\beta_F(\xi)=0$ exactly when
$\xi$ annihilates that image, equivalently when $L_F\subseteq H$.
:::

<1>7. If an effective divisor $E$ of degree $d-1$ satisfies
$$
L_E\subseteq H,
$$
then $\mathcal E$ is not normalized.

::: {.proof}
Step <1>6 gives $\beta_E(\xi)=0$, so the pulled-back extension
$$
0\longrightarrow\OO_C
\longrightarrow\mathcal E_E
\longrightarrow\OO_C(D-E)
\longrightarrow0
$$
splits. The splitting followed by $\mathcal E_E\to\mathcal E$ embeds
$\OO_C(D-E)$ in $\mathcal E$. Its degree is one, so twisting by its inverse,
which has degree $-1$, gives a nonzero section of a negative twist of
$\mathcal E$. Thus $\mathcal E$ is not normalized.
:::

<1>8. Conversely, if $\mathcal E$ is not normalized, then some effective
divisor $E$ of degree $d-1$ satisfies
$$
L_E\subseteq H.
$$

::: {.proof}
There is a negative-degree line bundle $\mathcal M$ and a nonzero morphism
$$
\mathcal M^{-1}\longrightarrow\mathcal E.
$$
Saturating its image gives a line subbundle
$$
\mathcal A\hookrightarrow\mathcal E
$$
with $a=\deg\mathcal A>0$. Its composite with the quotient
$\mathcal E\to\OO_C(D)$ is nonzero, because a zero composite would factor
$\mathcal A$ through $\OO_C$, whereas
$H^0(C,\mathcal A^{-1})=0$.

The nonzero map $\mathcal A\to\OO_C(D)$ has an effective zero divisor $F$ and
identifies
$$
\mathcal A\cong\OO_C(D-F).
$$
Thus $\deg F=d-a\le d-1$. Since this inclusion already lifts to $\mathcal E$,
the pullback extension along $\mathcal A\to\OO_C(D)$ splits. By step <1>6,
$$
L_F\subseteq H.
$$

Choose an effective divisor $T$ of degree $a-1$ and set $E=F+T$. Then
$\deg E=d-1$, and every section divisible by $E$ is divisible by $F$. Hence
$$
L_E\subseteq L_F\subseteq H.
$$
:::

<1>9. Therefore
$$
\boxed{
\mathcal E\text{ is normalized}
\iff
L_E\nsubseteq H
\text{ for every effective }E\text{ of degree }d-1.}
$$

::: {.proof}
Steps <1>7--<1>8 prove the two contrapositives. This proves part (b).
:::

<1>10. For part (c), put $d=-e$, so
$$
1\le d\le g,
$$
and fix any divisor $D$ of degree $d$. Then
$$
\dim H^1(C,\OO_C(-D))=g+d-1.
$$

::: {.proof}
Serre duality gives
$$
H^1(C,\OO_C(-D))^\vee
\cong H^0(C,\OO_C(K_C+D)).
$$
Because $d>0$, the line bundle $\OO_C(K_C+D)$ is nonspecial. Riemann--Roch
therefore gives
$$
h^0(C,\OO_C(K_C+D))
=(2g-2+d)+1-g
=g+d-1.
$$
:::

<1>11. Assume $d\ge2$. For an effective divisor $E$ of degree $d-1$, the
nonzero classes $[\xi]$ for which
$$
L_E\subseteq H_\xi
$$
form a projective linear subspace of
$$
\PP H^1(C,\OO_C(-D))
$$
of dimension $d-2$.

::: {.proof}
Put
$$
V=H^0(C,\OO_C(K_C+D)),
$$
so $\dim V=g+d-1$ by step <1>10. Let
$$
W_E
=
s_EH^0(C,\OO_C(K_C+D-E))
\subseteq V.
$$
Since
$$
\deg(K_C+D-E)=2g-1,
$$
this line bundle is nonspecial, and Riemann--Roch gives
$$
\dim W_E=g.
$$
By step <1>6, the bad classes are exactly
$$
\PP(W_E^\perp)\subseteq\PP(V^*).
$$
Its dimension is
$$
(g+d-1-g)-1=d-2.
$$
:::

<1>12. If $2\le d\le g$, the union of the bad extension classes in step
<1>11 is a proper subset of
$$
\PP H^1(C,\OO_C(-D)).
$$

::: {.proof}
Effective divisors of degree $d-1$ are parametrized by
$$
\Sym^{d-1}C,
$$
which has dimension $d-1$. The spaces
$$
H^0(C,\OO_C(K_C+D-E))
$$
have constant dimension $g$ by step <1>11. The universal effective divisor on
$C\times\Sym^{d-1}C$, together with cohomology and base change, therefore gives
a rank-$g$ subbundle of the trivial bundle with fibre $V$. Its annihilator
projectivizes to a closed incidence variety
$$
I\subseteq\Sym^{d-1}C\times\PP(V^*)
$$
whose fibre over $E$ is $\PP(W_E^\perp)$.

Hence
$$
\dim I=(d-1)+(d-2)=2d-3.
$$
The first factor is projective, so the image of $I$ in $\PP(V^*)$ is closed
and has dimension at most $2d-3$. On the other hand,
$$
\dim\PP(V^*)=g+d-2.
$$
Since $d\le g$,
$$
2d-3\le g+d-3<g+d-2.
$$
Thus the bad locus cannot fill the projective extension space.
:::

<1>13. For every integer $1\le d\le g$ there is a nonzero extension class
$\xi$ satisfying the normalization criterion of part (b).

::: {.proof}
If $d=1$, the only effective divisor of degree $d-1=0$ is $E=0$, and
$$
L_0=|K_C+D|
$$
cannot be contained in the proper hyperplane $H_\xi$ defined by any nonzero
$\xi$. Such classes exist because step <1>10 gives
$$
h^1(C,\OO_C(-D))=g>0.
$$

If $2\le d\le g$, step <1>12 shows that the bad classes form a proper closed
subset of the projective extension space. Choose $[\xi]$ outside it. Then
$$
L_E\nsubseteq H_\xi
$$
for every effective $E$ of degree $d-1$, so step <1>9 says that the
corresponding bundle is normalized.
:::

<1>14. For every
$$
-g\le e<0
$$
there exists a ruled surface over $C$ with invariant $e$.

::: {.proof}
Set $d=-e$, choose a divisor $D$ of degree $d$, and choose the normalized
extension from step <1>13:
$$
0\longrightarrow\OO_C
\longrightarrow\mathcal E
\longrightarrow\OO_C(D)
\longrightarrow0.
$$
Then
$$
\deg\det\mathcal E=d,
$$
so $X=\PP(\mathcal E)$ has invariant
$$
-\deg\det\mathcal E=-d=e.
$$
This proves part (c).
:::

<1>15. If $g=2$, every ruled surface over $C$ has
$$
\boxed{e\ge-2}.
$$

::: {.proof}
The note printed with this exercise cites Nagata [8] for the general theorem
$$
e\ge-g
$$
for a ruled surface over a genus-$g$ curve. The retained companion source also
identifies part (d) as a direct application of Theorem 1 in Nagata's cited
self-intersection paper. Specializing the stated theorem to $g=2$ gives
$$
e\ge-2,
$$
as required.
:::

<1>16. Q.E.D.

::: {.proof}
Steps <1>1--<1>4 prove part (a), steps <1>5--<1>9 prove part (b), steps
<1>10--<1>14 prove part (c), and step <1>15 proves part (d) from the general
Nagata bound explicitly cited by the exercise.
:::
:::
