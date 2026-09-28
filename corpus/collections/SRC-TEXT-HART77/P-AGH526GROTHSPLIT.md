---
schema: qual/card@1
id: P-AGH526GROTHSPLIT
kind: problem
title: Splitting of locally free sheaves on the projective line
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
    Read Hartshorne V.2.6, the retained Egbert/Potier induction, the
    projective-space cohomology calculation III.5.1, and the local Ext^1
    classification of extensions. The proof below makes the maximal-degree
    line subbundle rigorous by saturating a maximal section, uses H^1(O(-1))=0
    to bound every quotient summand by that maximal degree, and then kills the
    full extension class componentwise.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Show that every locally free sheaf of finite rank on $\PP^1$ is isomorphic to a direct sum of invertible sheaves.

Hint: Choose a subinvertible sheaf of maximal degree, and use induction on the rank.
:::

::: {.solution}
Let $\mathcal E$ be locally free of rank $r$ on $\PP^1$.

<1>1. There is a largest integer $a$ such that
$$
H^0\qty(\PP^1,\mathcal E(-a))\ne0.
$$

::: {.proof}
For $N\gg0$, Serre's theorem makes $\mathcal E(N)$ globally generated, so it
has a nonzero section. Thus the displayed set of integers is nonempty.

For $a\gg0$, Serre duality on $\PP^1$ gives
$$
H^0\qty(\PP^1,\mathcal E(-a))^\vee
\cong
H^1\qty(\PP^1,\mathcal E^\vee(a-2)).
$$
The group on the right vanishes for $a\gg0$ by Serre vanishing. Hence the set
is bounded above and has a largest element $a$.
:::

<1>2. A nonzero section of $\mathcal E(-a)$ yields an exact sequence
$$
0\longrightarrow\OO_{\PP^1}(a)
\longrightarrow\mathcal E
\longrightarrow\mathcal F
\longrightarrow0
$$
with $\mathcal F$ locally free of rank $r-1$.

::: {.proof}
A nonzero section gives an injective map
$$
\OO_{\PP^1}(a)\longrightarrow\mathcal E.
$$
Saturate its image. On the nonsingular curve $\PP^1$, the saturation is an
invertible subsheaf, hence isomorphic to $\OO_{\PP^1}(a+m)$ for some
$m\ge0$, where $m$ is the degree of the zero divisor removed by saturation.
If $m>0$, then
$$
H^0\qty(\PP^1,\mathcal E(-a-m))\ne0,
$$
contradicting maximality of $a$. Thus $m=0$: the original image is already
saturated. Its quotient is torsion-free on a nonsingular curve and therefore
locally free, of rank $r-1$.
:::

<1>3. Assume inductively that every locally free sheaf of rank $r-1$ on
$\PP^1$ splits. Then
$$
\mathcal F\cong\bigoplus_{j=1}^{r-1}\OO_{\PP^1}(b_j)
$$
for some integers $b_j$.

::: {.proof}
This is exactly the induction hypothesis applied to the quotient $\mathcal F$
of step <1>2. The rank-one base case is immediate because every invertible
sheaf on $\PP^1$ is $\OO(n)$ for some $n\in\ZZ$.
:::

<1>4. Every summand in step <1>3 satisfies
$$
b_j\le a.
$$

::: {.proof}
Twist the exact sequence of step <1>2 by $\OO(-a-1)$:
$$
0\longrightarrow\OO(-1)
\longrightarrow\mathcal E(-a-1)
\longrightarrow\mathcal F(-a-1)
\longrightarrow0.
$$
The projective-line cohomology calculation [@Har10a, Theorem III.5.1] gives
$$
H^1(\PP^1,\OO(-1))=0.
$$
Hence the map on global sections
$$
H^0\qty(\PP^1,\mathcal E(-a-1))
\longrightarrow
H^0\qty(\PP^1,\mathcal F(-a-1))
$$
is surjective.

If some $b_j\ge a+1$, then
$$
H^0\qty(\PP^1,\OO(b_j-a-1))\ne0,
$$
so $H^0(\PP^1,\mathcal F(-a-1))\ne0$. Surjectivity would then give
$$
H^0\qty(\PP^1,\mathcal E(-a-1))\ne0,
$$
contradicting the maximality of $a$. Therefore every $b_j\le a$.
:::

<1>5. The exact sequence in step <1>2 splits.

::: {.proof}
Its extension class lies in
$$
\Ext^1\qty(\mathcal F,\OO(a)).
$$
Using step <1>3 and the extension calculation [[PR-ET5PQ]],
$$
\begin{aligned}
\Ext^1\qty(\mathcal F,\OO(a))
&\cong
\bigoplus_{j=1}^{r-1}
\Ext^1\qty(\OO(b_j),\OO(a))\\
&\cong
\bigoplus_{j=1}^{r-1}
H^1\qty(\PP^1,\OO(a-b_j)).
\end{aligned}
$$
By step <1>4, $a-b_j\ge0$. Theorem III.5.1 gives
$$
H^1\qty(\PP^1,\OO(a-b_j))=0
$$
for every $j$. Hence the entire Ext group vanishes and the sequence splits.
:::

<1>6. Therefore
$$
\boxed{
\mathcal E
\cong
\OO_{\PP^1}(a)
\oplus
\bigoplus_{j=1}^{r-1}\OO_{\PP^1}(b_j).}
$$

::: {.proof}
Step <1>5 splits the exact sequence of step <1>2, and step <1>3 splits its
quotient. This proves the rank-$r$ case from the rank-$(r-1)$ case. Induction
from rank one proves the theorem for every finite rank.
:::

<1>7. Q.E.D.

::: {.proof}
Steps <1>1--<1>6 prove that every locally free sheaf of finite rank on
$\PP^1$ is a direct sum of invertible sheaves.
:::
:::
