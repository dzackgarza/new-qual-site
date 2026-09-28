---
schema: qual/card@1
id: P-AGH517ALGEQUIV
kind: problem
title: Algebraic equivalence of divisors implies numerical equivalence
classification:
  areas:
  - algebraic-geometry
  topics:
  - Surfaces
  - Intersection Theory
  - Picard Group
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne V.1.7, the retained Egbert companion proof, the flat-family
    Hilbert-polynomial theorem III.9.9, and the local very-ampleness results.
    The proof below makes the compatibility of prealgebraic equivalence with
    translation and negation explicit, realizes linear equivalence by a pencil
    of effective divisors, and then extends constancy of intersection from very
    ample divisors to arbitrary divisor classes.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Let $X$ be a surface.
Recall that we have defined an algebraic family of effective divisors on $X$, parametrized by a nonsingular curve $T$, to be an effective Cartier divisor $D$ on $X \times T$, flat over $T$ (III, 9.8.5). In this case, for any two closed points $0,1 \in T$, we say the corresponding divisors $D_0, D_1$ on $X$ are prealgebraically equivalent.

Two arbitrary divisors are prealgebraically equivalent if they are differences of prealgebraically equivalent effective divisors.
Two divisors $D, D^{\prime}$ are algebraically equivalent if there is a finite sequence $D=D_0, D_1, \ldots, D_n=D^{\prime}$ with $D_i$ and $D_{i+1}$ prealgebraically equivalent for each $i$.

a. Show that the divisors algebraically equivalent to 0 form a subgroup of $\Div X$.

b. Show that linearly equivalent divisors are algebraically equivalent.

Hint: If $(f)$ is a principal divisor on $X$, consider the principal divisor $(t f-u)$ on $X \times \PP^1$, where $t, u$ are the homogeneous coordinates on $\PP^1$.

c. Show that algebraically equivalent divisors are numerically equivalent.

Hint: Use (III, 9.9) to show that for any very ample $H$, if $D$ and $D^{\prime}$ are algebraically equivalent, then $D . H=D^{\prime} . H$.

Note.
The theorem of Néron and Severi states that the group of divisors modulo algebraic equivalence, called the Néron-Severi group, is a finitely generated abelian group.
Over $\CC$ this can be proved easily by transcendental methods (App.
B, §5) or as in (Ex.
1.8) below.
Over a field of arbitrary characteristic, see Lang and Néron [1] for a proof, and Hartshorne [6] for further discussion.
Since $\Num X$ is a quotient of the Néron-Severi group, it is also finitely generated, and hence free, since it is torsion-free by construction.
:::

::: {.solution}
Write $D\sim_{\mathrm{pa}}D'$ for prealgebraic equivalence and
$D\sim_{\mathrm{alg}}D'$ for algebraic equivalence.

<1>1. Prealgebraic equivalence is symmetric, is preserved by negation, and is
preserved by translating both divisors by the same divisor.

::: {.proof}
For effective divisors, symmetry follows by interchanging the two parameter
points in the same flat family.

Suppose arbitrary divisors $D,D'$ are prealgebraically equivalent. By
definition there are effective divisors $A,B,A',B'$ such that
$$
D=A-B,
\qquad
D'=A'-B',
$$
with
$$
A\sim_{\mathrm{pa}}A',
\qquad
B\sim_{\mathrm{pa}}B'.
$$
Then
$$
-D=B-A,
\qquad
-D'=B'-A',
$$
so the same definition gives
$$
-D\sim_{\mathrm{pa}}-D'.
$$

Let $E=E_+-E_-$ with $E_+,E_-$ effective. If a flat family of effective
Cartier divisors connects $A$ to $A'$, adding the constant divisor
$E_+\times T$ gives a flat family connecting $A+E_+$ to $A'+E_+$; locally its
equation is the product of the family equation with the fixed Cartier
equation, and the fibrewise Cartier criterion of Hartshorne III.9.8.5 applies.
The same statement holds for $B+E_-$ and $B'+E_-$. Hence
$$
D+E=(A+E_+)-(B+E_-)
\sim_{\mathrm{pa}}
(A'+E_+)-(B'+E_-)=D'+E.
$$
:::

<1>2. The set
$$
\boxed{\{D\in\Div X:D\sim_{\mathrm{alg}}0\}}
$$
is a subgroup of $\Div X$.

::: {.proof}
It contains $0$. Suppose
$$
0=D_0\sim_{\mathrm{pa}}D_1\sim_{\mathrm{pa}}\cdots
\sim_{\mathrm{pa}}D_r=D.
$$
Negating each step and using step <1>1 gives an algebraic-equivalence chain
from $0$ to $-D$. Thus the set is closed under inverses.

Now suppose $D\sim_{\mathrm{alg}}0$ and $E\sim_{\mathrm{alg}}0$. Choose a
chain from $0$ to $D$ and a chain from $0$ to $E$. By the translation property
in step <1>1, translating the second chain by $D$ gives a chain from $D$ to
$D+E$. Concatenating the two chains gives
$$
0\sim_{\mathrm{alg}}D+E.
$$
Hence the displayed set is closed under addition and inverses, proving part
(a).
:::

<1>3. If $D$ and $D'$ are linearly equivalent, then
$$
\boxed{D\sim_{\mathrm{pa}}D'},
$$
and therefore $D\sim_{\mathrm{alg}}D'$.

::: {.proof}
Choose an effective divisor $G$ whose coefficients are large enough that
$$
A=D+G,
\qquad
A'=D'+G
$$
are both effective. Since $D\sim D'$, the effective divisors $A,A'$ are
linearly equivalent. Let $\mcl$ be their common invertible sheaf and let
$s_0,s_1\in H^0(X,\mcl)$ be sections whose zero divisors are $A,A'$. If the
two sections are proportional then $A=A'$ and there is nothing to prove.
Otherwise, on $X\times\PP^1$ the universal pencil section
$$
t s_0+u s_1
$$
of
$$
p_X^*\mcl\tensor p_{\PP^1}^*\OO_{\PP^1}(1)
$$
is nonzero on every fibre over $\PP^1$. Its zero scheme is therefore an
effective Cartier divisor flat over $\PP^1$ by Hartshorne III.9.8.5, and its
fibres over $[1:0]$ and $[0:1]$ are $A$ and $A'$. Thus
$$
A\sim_{\mathrm{pa}}A'.
$$
The constant family shows $G\sim_{\mathrm{pa}}G$, so the definition for
arbitrary divisors gives
$$
D=A-G\sim_{\mathrm{pa}}A'-G=D'.
$$
This pencil is the homogeneous form of the source hint using $(tf-u)$.
Thus part (b) follows.
:::

<1>4. Let $H$ be a very ample divisor. If effective divisors $A,A'$ are
prealgebraically equivalent, then
$$
A\cdot H=A'\cdot H.
$$

::: {.proof}
Let $\mathcal A\subseteq X\times T$ be a flat family of effective Cartier
divisors with fibres $A$ and $A'$ at two closed points of the nonsingular
curve $T$. The divisor $H$ embeds
$$
X\hookrightarrow\PP^N,
$$
and hence gives a projective flat family
$$
\mathcal A\hookrightarrow\PP^N\times T.
$$
By Hartshorne III.9.9, recorded in [[T-COHFLATCHI]], all fibres have the same
Hilbert polynomial. In particular, they have the same degree in $\PP^N$.
For a divisor on the surface $X$, this degree is its intersection number with
$H$. Therefore
$$
A\cdot H=A'\cdot H.
$$
:::

<1>5. If arbitrary divisors $D,D'$ are algebraically equivalent, then
$$
D\cdot H=D'\cdot H
$$
for every very ample divisor $H$.

::: {.proof}
First suppose $D\sim_{\mathrm{pa}}D'$. Write
$$
D=A-B,
\qquad
D'=A'-B'
$$
with $A\sim_{\mathrm{pa}}A'$ and $B\sim_{\mathrm{pa}}B'$ effective.
Step <1>4 and bilinearity give
$$
D\cdot H
=A\cdot H-B\cdot H
=A'\cdot H-B'\cdot H
=D'\cdot H.
$$
If $D\sim_{\mathrm{alg}}D'$, apply this equality to each consecutive pair in
an algebraic-equivalence chain and use transitivity of equality.
:::

<1>6. Every divisor $E$ on $X$ is a difference of two very ample divisors.

::: {.proof}
Fix a very ample divisor $H_0$. Since $\OO_X(H_0)$ is ample, for all
sufficiently large $n$ the sheaf
$$
\OO_X(E+(n-1)H_0)
$$
is generated by global sections. Part (d) of [[P-AGH275AMPLEPROPS]] then shows
that
$$
\OO_X(E+nH_0)
=
\OO_X(H_0)\tensor\OO_X(E+(n-1)H_0)
$$
is very ample. The divisor $nH_0$ is also very ample. Hence
$$
E=(E+nH_0)-nH_0
$$
is a difference of very ample divisors.
:::

<1>7. Algebraic equivalence implies numerical equivalence:
$$
\boxed{D\sim_{\mathrm{alg}}D'\Longrightarrow D\equiv_{\mathrm{num}}D'}.
$$

::: {.proof}
Let $E$ be any divisor. By step <1>6, write
$$
E=H_1-H_2
$$
with $H_1,H_2$ very ample. Step <1>5 gives
$$
D\cdot H_i=D'\cdot H_i
\qquad(i=1,2).
$$
Therefore
$$
\begin{aligned}
D\cdot E
&=D\cdot H_1-D\cdot H_2\\
&=D'\cdot H_1-D'\cdot H_2\\
&=D'\cdot E.
\end{aligned}
$$
Since this holds for every divisor $E$, the divisors $D,D'$ are numerically
equivalent. This proves part (c).
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>2 proves part (a), step <1>3 proves part (b), and steps <1>4--<1>7
prove part (c).
:::
:::
