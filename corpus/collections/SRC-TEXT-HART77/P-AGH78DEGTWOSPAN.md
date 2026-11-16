---
schema: qual/card@1
id: P-AGH78DEGTWOSPAN
kind: problem
title: A variety of degree $2$ spans a linear space of dimension $r+1$
classification:
  areas:
  - algebraic-geometry
  topics:
  - Degree
  - Quadric Hypersurfaces
  - Linear Varieties
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: Read Exercise I.7.8 and its dependence on Exercises I.7.6--I.7.7 in Hartshorne. The proof chooses a nonsingular point, applies the secant-cone degree drop to obtain a degree-one variety of dimension r+1, identifies it as linear, and then identifies Y as a degree-two hypersurface in that span.
- event: solution-written
  by: chatgpt
  date: 2026-09-18

- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    Printed exercise read: Hartshorne, Algebraic Geometry (1977), I.7.8, printed
    p. 55 (PDF p. 70 of the checked-in extraction, where 7.7 and 7.8 follow the
    text of the section). A. Shichijo, R.Hartshorne "Algebraic Geometry" 演習問題への解答
    (2020/March), Chapter 1 section 7, Exercise 7.8, printed p. 9, read in the
    MinerU extraction tmp/sources/shitijyou-ch1-section7.md, is the only located
    treatment, and it is not a proof of either half: its 7.8 is "deg X < deg Y =
    2 by Ex 7.7b, so deg X = 1; dim X = dim Y + 1 by Ex 7.7a; X is linear by
    Ex 7.6; hence Y lies in a linear variety of dimension dim Y + 1", and it stops
    there. Both halves of that reduction fail on the same file. Its 7.7(a)
    proves X irreducible by supposing X = C union D, taking C' = Y cap C and
    D' = Y cap D, and inferring a contradiction from C' union D' = Y; but
    C' = Y with D' empty (or D' = Y with C' empty) is exactly what happens when
    C contains Y, and C = X is then possible, so the inference is invalid and
    dim X = r + 1 is not established. Its 7.7(b) chooses a hyperplane H through P
    with i(X,H;Z_j) = 1 for every component of X cap H and marks that choice with
    a literal (?) in the text on printed p. 9, so the degree drop deg X < deg Y
    it feeds into 7.8 is asserted there rather than proved. So neither the span
    half nor the quadric half is source-backed: the card's own steps
    join-degree-one, join-is-linear-span and y-is-quadric-hypersurface stand, the
    degree drop resting on the card's blow-up computation recorded in
    P-AGH77CONEDEGDROP, and the source is cited only for the shape of the
    reduction.
- event: source-checked
  by: claude
  date: 2026-11-15
  note: >-
    The paragraph after the remark ended was self-contradictory and is corrected:
    it said that all three retained sets "prove the first sentence" while the same
    paragraph said the published arguments for the degree drop it uses are
    incomplete. What the three sets do is reduce the first sentence to Exercise
    I.7.7 and stop; the degree drop of I.7.7(b) is the step Borcherds and
    Cutrone--Marshburn assume, Egbert attributes, and Shichijo marks (?) -- so the
    reduction is not a proof of the first sentence, and the card's own proof of
    the degree drop is what its steps join-degree-one and join-is-linear-span use.
    The second sentence is the card's throughout. No mathematics changed; the
    sentence was rewritten to say what the sets do.
---

::: {.problem}
Let $Y^r \subseteq \PP^n$ be a variety of degree $2$.
Show that $Y$ is contained in a linear subspace $L$ of dimension $r + 1$ in $\PP^n$.
Thus $Y$ is isomorphic to a quadric hypersurface in $\PP^{r+1}$ (Ex. 5.12).
:::

::: {.solution}
::: pf

::: pf-step
The variety $Y$ has a nonsingular point.

::: pf-proof
By Theorem I.5.3, the singular locus of a variety is a proper closed subset.
Hence its complement is a nonempty open subset of $Y$.
Choose
$$
P\in\Reg Y.
$$
:::

:::

::: {.pf-step #join-degree-one}
Let $X$ be the join of $P$ with $Y$ from Exercise I.7.7. Then
$$
\dim X=r+1,
\qquad
\deg X=1.
$$

::: pf-proof
Apply [[P-AGH77CONEDEGDROP|Exercise I.7.7]] to the degree-two variety $Y$ and the nonsingular point $P$.
It gives
$$
\dim X=r+1
$$
and
$$
0<\deg X<\deg Y=2.
$$
The degree of a nonempty projective variety is a positive integer by Proposition I.7.6(a), so necessarily
$$
\deg X=1.
$$
:::

:::

::: {.pf-step #join-is-linear-span}
The variety $X$ is a linear subspace
$$
\boxed{L\cong\PP^{r+1}\subseteq\PP^n}
$$
containing $Y$.

::: pf-proof
By definition of the join, $Y\subseteq X$.
Step [](#join-degree-one){.pf-ref} makes $X$ a projective variety of degree one.
By [[P-AGH76DEGONELINEAR|Exercise I.7.6]], every pure-dimensional degree-one projective algebraic set is linear.
Thus $X$ is a linear subspace $L\subseteq\PP^n$.
Its dimension is $r+1$ by step [](#join-degree-one){.pf-ref}, and it contains $Y$.
This proves the first assertion.
:::

:::

::: {.pf-step #y-is-quadric-hypersurface}
Inside $L\cong\PP^{r+1}$, the variety $Y$ is a quadric hypersurface.

::: pf-proof
The inclusion
$$
Y^r\subseteq L^{r+1}
$$
has codimension one.
The homogeneous coordinate ring of $L\cong\PP^{r+1}$ is a polynomial ring, hence a unique factorization domain.
Therefore the homogeneous prime ideal of the irreducible codimension-one subvariety $Y\subseteq L$ is principal, generated by an irreducible homogeneous polynomial $F$.

For a hypersurface, Proposition I.7.6(d) identifies the degree of the hypersurface with the degree of its defining homogeneous polynomial.
Since
$$
\deg Y=2,
$$
we obtain
$$
\deg F=2.
$$
Thus $Y$ is a quadric hypersurface in $L\cong\PP^{r+1}$.
:::

:::

::: pf-qed
Step [](#join-is-linear-span){.pf-ref} gives the required linear span of dimension $r+1$, and step [](#y-is-quadric-hypersurface){.pf-ref} identifies $Y$ inside that span as a quadric hypersurface.
:::

:::
:::

::: {.remark title="Published solution"}
Richard E. Borcherds, *Hartshorne, Chapter 1: Answers to exercises* (1994), text version `tmp/sources/hartshorne-solutions-borcherds.md`, Exercise 7.8, PDF p. 10: "applying 7.7 to $Y^r$ shows that $Y$ is contained in a degree $1$ variety $H$ of dimension $r+1$ in $\PP^n$, which by 7.6 is a linear variety and therefore isomorphic to $\PP^{r+1}$."
William Troiani, *Hartshorne Exercise Solutions* (October 2020), text version `tmp/sources/hartshorne-solutions-troiani.md`, stops at §I.5 and gives no solution to 7.8.
Andrew Egbert, *Solutions to Hartshorne's Algebraic Geometry* (October 3, 2013), text version `tmp/sources/hartshorne-solutions-egbert.md`, Exercise I.7.8, PDF p. 58: "ex.\ I.7.7 gives $Y$ is in degree $1$ variety of dim $r+1$ in $\PP^n$. By Ex I.7.6, this is linear, and thus isomorphic to $\PP^{r+1}$."
Joe Cutrone and Nick Marshburn, *Algebraic Geometry by Robin Hartshorne: Solutions*, text version `tmp/sources/hartshorne-solutions-cutrone-marshburn.md`, Exercise I.7.8, PDF p. 27: "let $Y^r\subseteq\PP^n$ be a variety of deg $2$. By ex 7, $Y$ is contained in a degree $1$ variety $H$ of dimension $r+1$ in $\PP^n$. By ex 6, this is a linear variety and thus isomorphic to $\PP^{r+1}$."
A. Shichijo, *R.Hartshorne "Algebraic Geometry" 演習問題への解答* (Solutions to the exercises in Hartshorne's *Algebraic Geometry*), 2020/March version, <https://shitijyou-a.github.io/math/alg-geo/har-ag-solutions/>, Chapter 1 section 7, Exercise 7.8, printed p. 9, gives the same reduction as the three sets above, from its Exercise 7.7, and stops at the linear span. Neither half of that reduction is proved on the same pages: its 7.7(a) argues that $X$ is irreducible by supposing $X=C\cup D$ and using $C'\cup D'=Y$ with $C'=Y\cap C$, which permits $C'=Y$, the case that gives no contradiction; and its 7.7(b) chooses a hyperplane through $P$ meeting every component of $X\cap H$ with multiplicity one and prints the author's own "（？）" against that choice.

All three retained sets reduce the first sentence to Exercise I.7.7 and stop there, and none proves the second, that $Y$ is a quadric hypersurface in that span. Their reduction does not by itself prove the first sentence either, because the degree drop of I.7.7(b), which it takes, is exactly where the published arguments are incomplete: Borcherds and Cutrone-Marshburn take the induction's identity $\deg(X\cap H)=\deg X$ as a step, Egbert takes it from Theorems 7.7 and 7.6(b), and Shichijo marks the choice of $H$ with "（？）". Steps [](#join-degree-one){.pf-ref} and [](#join-is-linear-span){.pf-ref} therefore give the degree-$1$ span through I.7.7 and I.7.6 as the three sets do, but with the card's own proof of the degree drop, recorded in [[P-AGH77CONEDEGDROP]] and not taken from any of them. Step [](#y-is-quadric-hypersurface){.pf-ref} supplies the second sentence: $Y$ has codimension one in $L\cong\PP^{r+1}$, the homogeneous coordinate ring of $L$ is a unique factorization domain, so the prime ideal of $Y$ is generated by one irreducible homogeneous form, whose degree is $2$ by I.7.6(d). Both sentences of the exercise are thus proved here.
:::
