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
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    A retained solution read at this exercise. Read Yang Pi-Yeh, Hartshorne
    Solutions (9 June 2019), Solution 5.2.6, printed p. 103,
    rendered as a page image from
    tmp/sources/lfwin-hartshorne-solutions.pdf, whose PDF page is the printed
    page. Checked against the book: Hartshorne V.2.6, whose printed page
    the card's earlier events record; this pass did not reopen it, and the
    comparison is against the statement the card carries. Recomputed
    H^1(P^1, E(n)) = 0 for n large and H^0(P^1, E(-n)) = 0 for n
    large by Serre duality, the resulting 0 -> O(i) -> E -> F -> 0, and
    Ext^1(O(n_j), O(i)) = H^1(P^1, O(i - n_j)) = 0 for n_j <= i. Not checked: Yang's Solutions outside printed pp. 100-107; the
    book's own page in this pass; and the printed book itself.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    The remark now names Yang Pi-Yeh's Solution 5.2.6 at printed
    p. 103 beside Egbert's entry. No step, statement or hypothesis of
    the card changes.
---

::: {.problem}
Show that every locally free sheaf of finite rank on $\PP^1$ is isomorphic to a direct sum of invertible sheaves.

Hint: Choose a subinvertible sheaf of maximal degree, and use induction on the rank.
:::

::: {.solution}
Let $\mathcal E$ be locally free of rank $r$ on $\PP^1$.

::: pf

::: {.pf-step #s1}

There is a largest integer $a$ such that
$$
H^0\qty(\PP^1,\mathcal E(-a))\ne0.
$$

::: pf-proof

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

:::

::: {.pf-step #s2}

A nonzero section of $\mathcal E(-a)$ yields an exact sequence
$$
0\longrightarrow\OO_{\PP^1}(a)
\longrightarrow\mathcal E
\longrightarrow\mathcal F
\longrightarrow0
$$
with $\mathcal F$ locally free of rank $r-1$.

::: pf-proof

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

:::

::: {.pf-step #s3}

Assume inductively that every locally free sheaf of rank $r-1$ on
$\PP^1$ splits. Then
$$
\mathcal F\cong\bigoplus_{j=1}^{r-1}\OO_{\PP^1}(b_j)
$$
for some integers $b_j$.

::: pf-proof

This is exactly the induction hypothesis applied to the quotient $\mathcal F$
of step [](#s2){.pf-ref}. The rank-one base case is immediate because every invertible
sheaf on $\PP^1$ is $\OO(n)$ for some $n\in\ZZ$.

:::

:::

::: {.pf-step #s4}

Every summand in step [](#s3){.pf-ref} satisfies
$$
b_j\le a.
$$

::: pf-proof

Twist the exact sequence of step [](#s2){.pf-ref} by $\OO(-a-1)$:
$$
0\longrightarrow\OO(-1)
\longrightarrow\mathcal E(-a-1)
\longrightarrow\mathcal F(-a-1)
\longrightarrow0.
$$
The projective-line cohomology calculation [@Har77, Theorem III.5.1] gives
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

:::

::: {.pf-step #s5}

The exact sequence in step [](#s2){.pf-ref} splits.

::: pf-proof

Its extension class lies in
$$
\Ext^1\qty(\mathcal F,\OO(a)).
$$
Using step [](#s3){.pf-ref} and the extension calculation [[PR-ET5PQ]],
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
By step [](#s4){.pf-ref}, $a-b_j\ge0$. Theorem III.5.1 gives
$$
H^1\qty(\PP^1,\OO(a-b_j))=0
$$
for every $j$. Hence the entire Ext group vanishes and the sequence splits.

:::

:::

::: {.pf-step #s6}

Therefore
$$
\boxed{
\mathcal E
\cong
\OO_{\PP^1}(a)
\oplus
\bigoplus_{j=1}^{r-1}\OO_{\PP^1}(b_j).}
$$

::: pf-proof

Step [](#s5){.pf-ref} splits the exact sequence of step [](#s2){.pf-ref}, and step [](#s3){.pf-ref} splits its
quotient. This proves the rank-$r$ case from the rank-$(r-1)$ case. Induction
from rank one proves the theorem for every finite rank.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref}, [](#s5){.pf-ref} and [](#s6){.pf-ref} prove that every locally free sheaf of finite rank on
$\PP^1$ is a direct sum of invertible sheaves.

:::

:::

:::

::: {.remark title="Published solution"}
The exercise stands on printed p. 384 of Hartshorne, read in `tmp/sources/hartshorne-1977-algebraic-geometry.pdf`, where printed p. $N$ is PDF p. $N+15$, and the statement above is that page's text, the printed hint including.

Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), text version `tmp/sources/hartshorne-solutions-egbert.md`, Exercise V.2.6, PDF pp. 264--265: after Potier, he takes $i$ largest with $H^0(\mathcal E(-i))\neq0$, splits off $\OO(i)$ using $0\to\OO(i)\to\mathcal E\to\mathcal F\to0$ with $\mathcal F$ locally free, splits $\mathcal F$ by induction, has $j\le i$ for every summand because otherwise $\mathcal E(-i-1)$ would have a section, and splits the sequence because $H^1(X,\mathcal H om(\mathcal F,\OO(i)))=0$. That is steps [](#s1){.pf-ref} to [](#s5){.pf-ref}, with the saturation of the section's image and the Ext computation written out and Hartshorne III.5.1 in place of his Weibel 10.1 and III Ex. 6.1. Matches.

Yang Pi-Yeh, *Hartshorne Solutions* (9 June 2019), Solution 5.2.6, printed p. 103, proves the splitting by induction on the rank: (III, 8.8) gives $H^1(\PP^1,\mathcal E(n))=0$ for $n\gg0$ and Serre duality $H^0(\PP^1,\mathcal E(-n))=0$, so there is a largest $i$ with a section of $\mathcal E(-i)$, which gives $0\to\OO(i)\to\mathcal E\to\mathcal F\to0$ with $\mathcal F$ locally free of rank $r-1$; if $\mathcal F=\bigoplus_{j\le r-1}\OO(n_j)$, any $n_j>i$ would give a section of $\mathcal E(-n_j)$ and contradict the maximality of $i$, so all $n_j\le i$, and $\operatorname{Ext}^1(\OO(n_j),\OO(i))=H^1(\PP^1,\OO(i-n_j))=0$ makes the extension split. That is the printed hint's induction with the maximal-degree subinvertible sheaf replaced by the largest twist carrying a section.
:::
