---
schema: qual/card@1
id: E-HAT-2.1-17
kind: problem
title: Relative homology of surfaces with point and circle subsets
classification:
  areas:
  - topology
  topics:
  - Homology
  - Relative Homology
  - Surfaces
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Hatcher, Algebraic Topology, Section 2.1, Exercise 17 and its figure. The figure has A as the central separating circle and B as the nonseparating circle on the right handle.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Computed part (a) from the long exact sequence and part (b) from the source figure: collapsing A gives a wedge of two tori, while collapsing B gives a torus with two points identified.
---

(a) Compute the homology groups $H_n(X, A)$ when $X$ is $S^2$ or $S^1 \times S^1$ and $A$ is a finite set of points in $X$.

(b) Compute the groups $H_n(X, A)$ and $H_n(X, B)$ for $X$ a closed orientable surface of genus two with $A$ and $B$ the circles shown.
[What are $X/A$ and $X/B$?]

::: {.solution}
Let $A$ first denote a finite set of $m\ge1$ points in a connected space $X$ equal to $S^2$ or $T^2=S^1\times S^1$.

<1>1. For $X=S^2$,
\[
H_k(S^2,A)\cong
\begin{cases}
\mathbb Z,&k=2,\\
\mathbb Z^{m-1},&k=1,\\
0,&\text{otherwise}.
\end{cases}
\]
::: {.proof}
Since $A$ is finite,
\[
H_0(A)\cong\mathbb Z^m,
\qquad
H_k(A)=0\quad(k>0).
\]
For $k\ge2$, the long exact sequence gives
\[
H_k(S^2,A)\cong H_k(S^2),
\]
so only degree $2$ contributes $\mathbb Z$.
In low degrees the exact segment is
\[
0\to H_1(S^2,A)\to\mathbb Z^m
\xrightarrow{\epsilon}\mathbb Z\to H_0(S^2,A)\to0,
\]
where $\epsilon$ sums coordinates. Hence
\[
H_1(S^2,A)\cong\ker\epsilon\cong\mathbb Z^{m-1},
\qquad
H_0(S^2,A)=0.
\]
:::

<1>2. For $X=T^2$,
\[
H_k(T^2,A)\cong
\begin{cases}
\mathbb Z,&k=2,\\
\mathbb Z^{m+1},&k=1,\\
0,&\text{otherwise}.
\end{cases}
\]
::: {.proof}
Again $H_k(T^2,A)\cong H_k(T^2)$ for $k\ge2$, so degree $2$ is $\mathbb Z$. The low-degree exact sequence is
\[
0\to\mathbb Z^2\to H_1(T^2,A)
\to\mathbb Z^m\xrightarrow{\epsilon}\mathbb Z\to0.
\]
Thus there is a short exact sequence
\[
0\to\mathbb Z^2\to H_1(T^2,A)\to\mathbb Z^{m-1}\to0.
\]
Since the quotient is free abelian, the sequence splits, giving
\[
H_1(T^2,A)\cong\mathbb Z^{m+1}.
\]
Also $H_0(T^2,A)=0$.
:::

Now let $X$ be the genus-two closed orientable surface and let $A,B$ be the circles in Hatcher's figure.

<1>3. Collapsing the separating circle $A$ gives
\[
X/A\cong T^2\vee T^2.
\]
Therefore
\[
H_k(X,A)\cong
\begin{cases}
\mathbb Z^4,&k=1,\\
\mathbb Z^2,&k=2,\\
0,&\text{otherwise}.
\end{cases}
\]
::: {.proof}
The circle $A$ in the figure separates the two handles. Collapsing it to a point turns each side into a torus, with the two resulting tori meeting only at the collapsed point. Since $(X,A)$ is a good pair,
\[
H_k(X,A)\cong\widetilde H_k(X/A).
\]
The reduced homology of $T^2\vee T^2$ is the direct sum of the reduced homologies of the two tori, giving the displayed groups.
:::

<1>4. Collapsing the nonseparating circle $B$ gives a torus with two distinct points identified. This space is homotopy equivalent to
\[
T^2\vee S^1.
\]
Hence
\[
H_k(X,B)\cong
\begin{cases}
\mathbb Z^3,&k=1,\\
\mathbb Z,&k=2,\\
0,&\text{otherwise}.
\end{cases}
\]
::: {.proof}
Cutting the genus-two surface along the nonseparating circle $B$ produces a genus-one surface with two boundary circles. Collapsing $B$ in the original surface amounts to capping each of these boundary circles to a point and then identifying the two resulting points. Capping gives a torus, so $X/B$ is a torus with two points identified.

For any path-connected space, identifying two distinct points is homotopy equivalent to adjoining a circle between them and then choosing a path already in the space, hence to wedging on an $S^1$. Thus
\[
X/B\simeq T^2\vee S^1.
\]
Again
\[
H_k(X,B)\cong\widetilde H_k(X/B),
\]
which gives the displayed result.
:::
:::
