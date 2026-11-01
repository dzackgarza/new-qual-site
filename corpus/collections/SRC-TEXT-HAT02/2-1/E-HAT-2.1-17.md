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
  note: 'Checked against Hatcher, Algebraic Topology, Section 2.1, Exercise 17 and its figure. The figure has A as the central separating circle and B as the nonseparating circle on the right handle.'
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
  note: 'Computed part (a) from the long exact sequence and part (b) from the source figure: collapsing A gives a wedge of two tori, while collapsing B gives a torus with two points identified.'
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read the computation from the long exact sequence: for $m$ points in $S^2$ the sequence gives $H_2=\ZZ$, $H_1=\ZZ^{m-1}$ and $H_0=0$, and for the torus the same method gives $H_2=\ZZ$, $H_1=\ZZ^{m+1}$ and $H_0=0$; part (b) is read at the level of the stated quotients $X/A$ and $X/B$.
- event: solution-reviewed
  by: claude
  date: 2026-11-01
  note: >-
    Read line by line, every case. (a) With `A` a set of `m >= 1` points, `H_0(A) = Z^m` and `H_k(A)
    = 0` for `k > 0`. For `S^2`: `H_k(S^2,A) = H_k(S^2)` for `k >= 2` since `H_{k-1}(A) = 0`, giving
    `Z` in degree `2`; the low-degree segment `0 -> H_1(S^2,A) -> Z^m -> Z -> H_0(S^2,A) -> 0` with
    the sum map has `H_1 = ker = Z^{m-1}` and `H_0 = 0`. For `T^2`: again degree `2` is `H_2(T^2) =
    Z`, and the segment is `0 -> Z^2 -> H_1(T^2,A) -> Z^{m-1} -> 0`, which splits because the quotient
    is free, giving `Z^{m+1}`, with `H_0 = 0`. (b) For the separating circle `A`, cutting along it and
    capping gives two tori meeting in a point, so `X/A = T^2 vee T^2`; `(X,A)` is a good pair, so
    `H_*(X,A) = reduced H_*(T^2 vee T^2)`, i.e. `Z^4` in degree `1`, `Z^2` in degree `2`, nothing else,
    and the reduced degree-zero group vanishes as stated. For the nonseparating circle `B`, cutting
    gives a genus-one surface with two boundary circles, so `X/B` is a torus with two points
    identified, and identifying two points of a path-connected space is homotopy equivalent to
    wedging on `S^1`, so `X/B = T^2 vee S^1` and `H_*(X,B)` is `Z^3` in degree `1`, `Z` in degree `2`.
    The case `A = empty` is separate and is the reason `m >= 1` was assumed. With `A` empty there is no
    `H_0(A) -> H_0(X)` to be surjective, and `H_k(X, empty) = H_k(X)`, so the answers are the absolute
    groups: for `S^2`, `Z` in degrees `0` and `2` and `0` in degree `1` (note `H_0` is `Z`, not `0`,
    and the formula `Z^{m-1}` does not extend to `m = 0`); for `T^2`, `Z`, `Z^2`, `Z` in degrees
    `0`, `1`, `2`. All the hypotheses used are checked: nonemptiness of `A` for surjectivity of `H_0(A) -> H_0(X)`,
    with the empty case now stated separately as the absolute groups, goodness of the pairs for the `X/A` and `X/B` identifications, and freeness of `Z^{m-1}` for the
    splitting. No correction was needed.
---

::: {.problem}
(a) Compute the homology groups $H_n(X, A)$ when $X$ is $S^2$ or $S^1 \times S^1$ and $A$ is a finite set of points in $X$.

(b) Compute the groups $H_n(X, A)$ and $H_n(X, B)$ for $X$ a closed orientable surface of genus two with $A$ and $B$ the circles shown.
[What are $X/A$ and $X/B$?]
:::

::: {.solution}
Let $A$ first denote a finite set of $m\ge1$ points in a connected space $X$ equal to $S^2$ or $T^2=S^1\times S^1$.

::: pf

::: pf-step

For $X=S^2$,
$$
H_k(S^2,A)\cong
\begin{cases}
\ZZ,&k=2,\\
\ZZ^{m-1},&k=1,\\
0,&\text{otherwise}.
\end{cases}
$$

::: pf-proof

Since $A$ is finite,
$$
H_0(A)\cong\ZZ^m,
\qquad
H_k(A)=0\quad(k>0).
$$
For $k\ge2$, the long exact sequence gives
$$
H_k(S^2,A)\cong H_k(S^2),
$$
so only degree $2$ contributes $\ZZ$.
In low degrees the exact segment is
$$
0\to H_1(S^2,A)\to\ZZ^m
\xrightarrow{\epsilon}\ZZ\to H_0(S^2,A)\to0,
$$
where $\epsilon$ sums coordinates. Hence
$$
H_1(S^2,A)\cong\ker\epsilon\cong\ZZ^{m-1},
\qquad
H_0(S^2,A)=0.
$$

:::

:::

::: pf-step

For $X=T^2$,
$$
H_k(T^2,A)\cong
\begin{cases}
\ZZ,&k=2,\\
\ZZ^{m+1},&k=1,\\
0,&\text{otherwise}.
\end{cases}
$$

::: pf-proof

Again $H_k(T^2,A)\cong H_k(T^2)$ for $k\ge2$, so degree $2$ is $\ZZ$. The low-degree exact sequence is
$$
0\to\ZZ^2\to H_1(T^2,A)
\to\ZZ^m\xrightarrow{\epsilon}\ZZ\to0.
$$
Thus there is a short exact sequence
$$
0\to\ZZ^2\to H_1(T^2,A)\to\ZZ^{m-1}\to0.
$$
Since the quotient is free abelian, the sequence splits, giving
$$
H_1(T^2,A)\cong\ZZ^{m+1}.
$$
Also $H_0(T^2,A)=0$.

Now let $X$ be the genus-two closed orientable surface and let $A,B$ be the circles in Hatcher's figure.

:::

:::

::: pf-step

Collapsing the separating circle $A$ gives
$$
X/A\cong T^2\vee T^2.
$$
Therefore
$$
H_k(X,A)\cong
\begin{cases}
\ZZ^4,&k=1,\\
\ZZ^2,&k=2,\\
0,&\text{otherwise}.
\end{cases}
$$

::: pf-proof

The circle $A$ in the figure separates the two handles. Collapsing it to a point turns each side into a torus, with the two resulting tori meeting only at the collapsed point. Since $(X,A)$ is a good pair,
$$
H_k(X,A)\cong\widetilde H_k(X/A).
$$
The reduced homology of $T^2\vee T^2$ is the direct sum of the reduced homologies of the two tori, giving the displayed groups.

:::

:::

::: pf-step

Collapsing the nonseparating circle $B$ gives a torus with two distinct points identified. This space is homotopy equivalent to
$$
T^2\vee S^1.
$$
Hence
$$
H_k(X,B)\cong
\begin{cases}
\ZZ^3,&k=1,\\
\ZZ,&k=2,\\
0,&\text{otherwise}.
\end{cases}
$$

::: pf-proof

Cutting the genus-two surface along the nonseparating circle $B$ produces a genus-one surface with two boundary circles. Collapsing $B$ in the original surface amounts to capping each of these boundary circles to a point and then identifying the two resulting points. Capping gives a torus, so $X/B$ is a torus with two points identified.

For any path-connected space, identifying two distinct points is homotopy equivalent to adjoining a circle between them and then choosing a path already in the space, hence to wedging on an $S^1$. Thus
$$
X/B\simeq T^2\vee S^1.
$$
Again
$$
H_k(X,B)\cong\widetilde H_k(X/B),
$$
which gives the displayed result.

:::

:::

:::

:::
