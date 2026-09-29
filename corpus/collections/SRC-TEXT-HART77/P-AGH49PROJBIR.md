---
schema: qual/card@1
id: P-AGH49PROJBIR
kind: problem
title: Projection from a general point is birational onto its image
classification:
  areas:
  - algebraic-geometry
  topics:
  - Birational Geometry
  - Projective Varieties
  - Morphisms
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared the statement and required references with the retained Hartshorne I.4.9 transcription. The proof uses a separating transcendence basis and a primitive element to choose a general linear coordinate system in which the last coordinate is unnecessary for the function field, while the projection center lies off X.'
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $X$ be a projective variety of dimension $r$ in $\PP^n$, with $n \geq r + 2$.
Show that for a suitable choice of a point $P \notin X$ and a linear subspace $\PP^{n-1} \subseteq \PP^n$, the projection from $P$ to $\PP^{n-1}$ induces a birational morphism of $X$ onto its image $X' \subseteq \PP^{n-1}$.

This shows in particular that the birational map making $X$ birational to a hypersurface can be obtained by a finite number of such projections.
:::

::: {.solution}
Let $K=k(X)$ be the function field of $X$.
We use that $k$ is algebraically closed, hence perfect, so every finitely generated extension of $k$ is separably generated [@Har10a, Theorem I.4.8A].

::: pf

::: {.pf-step #s1}

After a projective linear change of coordinates, the rational functions
$$
u_i=\frac{x_i}{x_0}\qquad(1\le i\le r+1)
$$
generate $K$ over $k$.

::: pf-proof

Choose a hyperplane not containing $X$ and call its equation $x_0=0$.
On the dense affine open $X\cap D_+(x_0)$, the coordinate ratios $x_i/x_0$, $1\le i\le n$, generate $K$ as a field over $k$.

Since $K/k$ is separably generated of transcendence degree $r$, Theorem I.4.7A permits, after an invertible linear change among these affine linear coordinates, a separating transcendence basis $u_1,\ldots,u_r$ chosen from them.
Thus $K$ is finite separable over
$$
F=k(u_1,\ldots,u_r).
$$
The remaining affine coordinates generate this finite extension.
By the primitive element theorem [@Har10a, Theorem I.4.6A], a suitable $k$-linear combination of those remaining coordinates is a primitive element $u_{r+1}$ for $K/F$.
Replacing one remaining projective coordinate by the same linear combination gives
$$
K=k(u_1,\ldots,u_r,u_{r+1}).
$$

The choices just made persist on a nonempty Zariski-open set of linear coordinate systems.
For the transcendence basis, nonvanishing of $du_1\wedge\cdots\wedge du_r$ in $\Omega_{K/k}^r$ is an open nonvanishing condition on the linear coefficients.
For the primitive element, if $K/F$ is replaced by a finite normal extension containing it, failure of a linear combination to separate two distinct $F$-embeddings is one linear equation in its coefficients; only finitely many pairs of embeddings occur.
Hence primitive linear combinations form a nonempty open subset of the relevant coefficient space.
Finally, the condition that the last coordinate point $[0:\cdots:0:1]$ lie outside the transformed $X$ is also open and nonempty, because $X\subsetneq\PP^n$.
The parameter space of projective coordinate systems is irreducible, so these finitely many nonempty open conditions can be imposed simultaneously.
We henceforth use such a coordinate system.

:::

:::

::: {.pf-step #s2}

Projection from
$$
P=[0:\cdots:0:1]\notin X
$$
to the hyperplane $H=V(x_n)\cong\PP^{n-1}$ restricts to a morphism
$$
\pi:X\longrightarrow X'\coloneqq\overline{\pi(X)}\subseteq H.
$$

::: pf-proof

Projection from $P$ is
$$
[x_0:\cdots:x_n]\longmapsto[x_0:\cdots:x_{n-1}].
$$
Its only indeterminacy point is $P$.
Since $P\notin X$, its restriction to $X$ is everywhere defined and is a morphism, by the coordinate description of projection in Exercise I.3.14.
The image of the irreducible space $X$ is irreducible, so its closure $X'$ is a projective variety.

:::

:::

::: {.pf-step #s3}

The induced map of function fields $k(X')\hookrightarrow K$ is an isomorphism.

::: pf-proof

On the dense open set $x_0\ne0$, the projection retains the affine coordinate functions
$$
u_i=x_i/x_0\qquad(1\le i\le n-1).
$$
Therefore its pullback identifies $k(X')$ with the subfield
$$
k(u_1,\ldots,u_{n-1})\subseteq K.
$$
Because $n\ge r+2$, one has $r+1\le n-1$.
Step [](#s1){.pf-ref} shows that the first $r+1$ of these retained functions already generate $K$.
Hence
$$
k(X')=k(u_1,\ldots,u_{n-1})=K.
$$

:::

:::

::: {.pf-step #s4}

The morphism $\pi:X\to X'$ is birational.

::: pf-proof

A dominant morphism of varieties is birational exactly when it induces an isomorphism of function fields [@Har10a, Proposition I.4.4].
Dominance holds by the definition of $X'$ as the closure of the image, and step [](#s3){.pf-ref} gives the required function-field isomorphism.
Thus the chosen projection is birational onto its image.

:::

:::

::: {.pf-step #s5}

Repeating the construction reduces the ambient projective dimension to $r+1$.

::: pf-proof

If the current ambient dimension is greater than $r+1$, step [](#s4){.pf-ref} replaces the variety birationally by one in a projective space of dimension one less.
Its dimension remains $r$, because birational varieties have the same function field and therefore the same transcendence degree over $k$.
After finitely many repetitions the image lies in $\PP^{r+1}$, where an $r$-dimensional projective variety has codimension one and is therefore a hypersurface by [[P-AGH28HYPERSURFACE]].
This proves the final assertion in the statement.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref} and [](#s4){.pf-ref} construct the required point, projection, and birational morphism; step [](#s5){.pf-ref} gives the stated finite iteration to a hypersurface.

:::

:::

:::
