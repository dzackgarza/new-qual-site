---
schema: qual/card@1
id: P-AGH513VIRTGENUS
kind: problem
title: Adjunction formula and the virtual arithmetic genus of a divisor
classification:
  areas:
  - algebraic-geometry
  topics:
  - Surfaces
  - Adjunction
  - Canonical Divisor
  - Intersection Theory
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: >-
    Read Hartshorne V.1.3, the retained Egbert companion algebra for part (c),
    the surface Riemann--Roch formula, the Euler-characteristic definition of
    arithmetic genus, and the intersection-pairing conventions. The source
    statement needs no correction. The proof below derives the effective case
    from the divisor exact sequence and surface Riemann--Roch, proves linear
    equivalence invariance from the intersection pairing, and then expands the
    defining quadratic expression for the virtual genus identities.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Recall that the arithmetic genus of a projective scheme $D$ of dimension 1 is defined as
\[
p_a=1-\chi\left(\mathcal{O}_D\right)
.\]
See III, Ex. 5.3.

a. If $D$ is an effective divisor on the surface $X$, use (1.6) to show that
\[
2 p_a-2= D.(D+K)
.\]

b. $p_a(D)$ depends only on the linear equivalence class of $D$ on $X$.

c. More generally, for any divisor $D$ on $X$, we define the virtual arithmetic genus (which is equal to the ordinary arithmetic genus if $D$ is effective) by the same formula: $2 p_a-2=D .(D+K)$. Show that for any two divisors $C, D$ we have
\[
p_a(-D)=D^2-p_a(D)+2
\]
and
\[
p_a(C+D)=p_a(C)+p_a(D)+C . D-1 .
\]
:::

::: {.solution}
Let $K$ be a canonical divisor on $X$.

<1>1. If $D$ is effective, then
$$
\chi(\OO_D)
=
-\frac12D\cdot(D+K).
$$

::: {.proof}
Since $D$ is an effective Cartier divisor on the nonsingular surface $X$,
there is an exact sequence
$$
0
\longrightarrow
\OO_X(-D)
\longrightarrow
\OO_X
\longrightarrow
\OO_D
\longrightarrow0.
$$
Additivity of Euler characteristic gives
$$
\chi(\OO_D)
=
\chi(\OO_X)-\chi(\OO_X(-D)).
$$

Apply surface Riemann--Roch [[T-COHRRS]] to the divisor $-D$:
$$
\begin{aligned}
\chi(\OO_X(-D))
&=
\chi(\OO_X)
+\frac12(-D)\cdot(-D-K)\\
&=
\chi(\OO_X)
+\frac12D\cdot(D+K).
\end{aligned}
$$
Substitution yields the stated formula.
:::

<1>2. For an effective divisor $D$,
$$
\boxed{2p_a(D)-2=D\cdot(D+K)}.
$$

::: {.proof}
Because $D$ has dimension one, its arithmetic genus is
$$
p_a(D)=1-\chi(\OO_D)
$$
by [[D-COHEULER]].  Step <1>1 therefore gives
$$
\begin{aligned}
2p_a(D)-2
&=
-2\chi(\OO_D)\\
&=
D\cdot(D+K).
\end{aligned}
$$
This proves part (a).
:::

<1>3. For effective divisors, $p_a(D)$ depends only on the linear equivalence
class of $D$.

::: {.proof}
Suppose
$$
D\sim D'.
$$
The surface intersection pairing [[D-SRFINT]] depends only on linear
equivalence classes, so
$$
D^2=(D')^2,
\qquad
D\cdot K=D'\cdot K.
$$
Hence
$$
D\cdot(D+K)=D'\cdot(D'+K).
$$
Applying step <1>2 to $D$ and $D'$ gives
$$
2p_a(D)-2=2p_a(D')-2,
$$
and therefore
$$
p_a(D)=p_a(D').
$$
This proves part (b).
:::

<1>4. For an arbitrary divisor $D$, the virtual arithmetic genus is
$$
p_a(D)
=
1+\frac12D\cdot(D+K).
$$

::: {.proof}
This is exactly the definition in part (c), rewritten from
$$
2p_a(D)-2=D\cdot(D+K).
$$
By step <1>2 it agrees with the ordinary arithmetic genus whenever $D$ is
effective.
:::

<1>5. For every divisor $D$,
$$
\boxed{p_a(-D)=D^2-p_a(D)+2}.
$$

::: {.proof}
Using step <1>4,
$$
\begin{aligned}
p_a(-D)
&=
1+\frac12(-D)\cdot(-D+K)\\
&=
1+\frac12D^2-\frac12D\cdot K.
\end{aligned}
$$
On the other hand,
$$
\begin{aligned}
D^2-p_a(D)+2
&=
D^2-
\left(1+\frac12D^2+\frac12D\cdot K\right)+2\\
&=
1+\frac12D^2-\frac12D\cdot K.
\end{aligned}
$$
The two expressions agree.
:::

<1>6. For arbitrary divisors $C,D$,
$$
\boxed{
p_a(C+D)
=
p_a(C)+p_a(D)+C\cdot D-1
}.
$$

::: {.proof}
By bilinearity and symmetry of the intersection pairing,
$$
\begin{aligned}
p_a(C+D)
&=
1+\frac12(C+D)\cdot(C+D+K)\\
&=
1
+\frac12C\cdot(C+K)
+\frac12D\cdot(D+K)
+C\cdot D.
\end{aligned}
$$
Step <1>4 gives
$$
\frac12C\cdot(C+K)=p_a(C)-1
$$
and
$$
\frac12D\cdot(D+K)=p_a(D)-1.
$$
Substituting these identities yields
$$
p_a(C+D)
=
p_a(C)+p_a(D)+C\cdot D-1.
$$
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>2 proves part (a), step <1>3 proves part (b), and steps <1>4--<1>6
prove both identities in part (c).
:::
:::
