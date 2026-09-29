---
schema: qual/card@1
id: P-AGH76DEGONELINEAR
kind: problem
title: Pure dimensional algebraic sets of degree $1$ are exactly the linear varieties
classification:
  areas:
  - algebraic-geometry
  topics:
  - Degree
  - Linear Varieties
  - Hilbert Polynomials
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-18
  note: Read Exercise I.7.6, Proposition I.7.6, and Theorem I.7.7 in the Hartshorne source. The proof first uses positivity and additivity of degree to force irreducibility, proves the curve case by a hyperplane through two points, and then inducts on dimension by hyperplane sections.
- event: solution-written
  by: chatgpt
  date: 2026-09-18
---

::: {.problem}
Show that an algebraic set $Y$ of pure dimension $r$, meaning that every irreducible component of $Y$ has dimension $r$, has degree $1$ if and only if $Y$ is a linear variety (Ex. 2.11).

*Hint:* First, use (7.7) and treat the case $\dim Y = 1$.
Then do the general case by cutting with a hyperplane and using induction.
:::

::: {.solution}
::: pf

::: {.pf-step #pure-dim-degree-one-irreducible}
A pure-dimensional algebraic set of degree one is irreducible.

::: pf-proof
Write the irreducible decomposition
$$
Y=Y_1\cup\cdots\cup Y_m.
$$
All components have the same dimension $r$ by purity, and distinct components meet in dimension strictly less than $r$.
Repeated application of Proposition I.7.6(b) gives
$$
\deg Y=\sum_{i=1}^m\deg Y_i.
$$
Each $\deg Y_i$ is a positive integer by Proposition I.7.6(a).
If $\deg Y=1$, this forces $m=1$ and $\deg Y_1=1$.
Thus $Y$ is a variety.
:::

:::

::: {.pf-step #degree-one-point-is-linear}
A zero-dimensional algebraic set of degree one is a point, hence a linear variety.

::: pf-proof
By step [](#pure-dim-degree-one-irreducible){.pf-ref} it is irreducible.
An irreducible zero-dimensional projective variety over the algebraically closed field $k$ is a single closed point.
A point is a projective linear subspace of dimension zero.
:::

:::

::: {.pf-step #degree-one-curve-is-line}
An irreducible projective curve of degree one is a line.

::: pf-proof
Let $Y\subseteq\PP^n$ be an irreducible curve with $\deg Y=1$.
If $n=1$, then the only one-dimensional closed irreducible subset is $\PP^1$ itself, so the result is immediate.

Assume $n\ge2$ and choose two distinct points $P,Q\in Y$.
Suppose some hyperplane $H$ contains $P$ and $Q$ but does not contain $Y$.
Theorem I.7.7, applied to the degree-one hypersurface $H$, gives
$$
\sum_{R\in Y\cap H} i(Y,H;R)=\deg Y\cdot\deg H=1,
$$
because every zero-dimensional component is a point of degree one.
But both $P$ and $Q$ occur in the sum with positive intersection multiplicity, a contradiction.

Hence every hyperplane containing $P$ and $Q$ contains all of $Y$.
The intersection of all hyperplanes containing $P$ and $Q$ is their projective span, the line
$$
L=\overline{PQ}.
$$
Thus $Y\subseteq L$.
Since both are irreducible closed subsets of dimension one, $Y=L$.
:::

:::

::: {.pf-step #degree-one-induction-step}
Assume inductively that every degree-one variety of dimension $r-1$ is linear. Then every degree-one variety $Y$ of dimension $r\ge2$ is linear.

::: pf-proof
If $Y=\PP^n$, then it is already linear, so assume $r<n$.
Choose a hyperplane $H$ not containing $Y$.
The irreducible components $Z_j$ of $Y\cap H$ all have dimension $r-1$ by the projective dimension theorem.
Theorem I.7.7 gives
$$
\sum_j i(Y,H;Z_j)\deg Z_j
=\deg Y\cdot\deg H=1.
$$
Every intersection multiplicity and every degree in this sum is a positive integer.
Consequently there is exactly one component $Z$, with
$$
i(Y,H;Z)=1,
\qquad
\deg Z=1.
$$
By the induction hypothesis, the reduced intersection is an $(r-1)$-dimensional linear subspace; write it as $L$.

Choose $P\in Y\setminus H$ and let
$$
M=\langle L,P\rangle.
$$
This is an $r$-dimensional linear subspace.
We claim $Y\subseteq M$.
Suppose instead that $Q\in Y\setminus M$.
Then $P\notin\langle L,Q\rangle$; otherwise $Q$ would lie in $\langle L,P\rangle=M$.
Choose a hyperplane $H'$ containing the $r$-plane $\langle L,Q\rangle$ but not $P$.
Then $H'$ does not contain $Y$, while
$$
L\cup\{Q\}\subseteq Y\cap H'.
$$

Applying Theorem I.7.7 to $H'$ again shows that $Y\cap H'$ has exactly one irreducible component of dimension $r-1$ and degree one.
Since it contains the $(r-1)$-plane $L$, that unique component must be $L$ itself.
But then $Q\in L$, contradicting $Q\notin M$.
Therefore $Y\subseteq M$.
Both $Y$ and $M$ are irreducible closed subsets of dimension $r$, so
$$
Y=M.
$$
Thus $Y$ is linear.
:::

:::

::: {.pf-step #linear-variety-has-degree-one}
Every linear variety has degree one.

::: pf-proof
A projective linear variety of dimension $r$ is projectively equivalent to the standard coordinate subspace $\PP^r\subseteq\PP^n$.
Its homogeneous coordinate ring is a polynomial ring in $r+1$ variables, so its Hilbert polynomial is
$$
\binom{t+r}{r}
=\frac{1}{r!}t^r+\text{lower terms}.
$$
Hence its degree is
$$
r!\cdot\frac1{r!}=1.
$$
:::

:::

::: pf-qed
Steps [](#pure-dim-degree-one-irreducible){.pf-ref}, [](#degree-one-point-is-linear){.pf-ref}, [](#degree-one-curve-is-line){.pf-ref} and [](#degree-one-induction-step){.pf-ref} prove that every pure-dimensional degree-one algebraic set is a linear variety, and step [](#linear-variety-has-degree-one){.pf-ref} proves the converse.
:::

:::
:::
