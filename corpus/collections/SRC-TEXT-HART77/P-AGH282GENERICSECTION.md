---
schema: qual/card@1
id: P-AGH282GENERICSECTION
kind: problem
title: A nowhere-vanishing section of a high-rank locally free sheaf
classification:
  areas:
  - algebraic-geometry
  topics:
  - Locally Free Sheaves
  - Global Sections
  - Bertini's Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: Compared the statement and Bertini-method hint with the retained Hartshorne II.8.2 transcription. Made the source's algebraically closed field convention explicit. The proof reduces a possibly infinite-dimensional generating space to a finite one and bounds the closure of the incidence image without assuming the variety is proper.
- event: solution-written
  by: chatgpt
  date: 2026-09-17
---

::: {.problem}
Let $k$ be an algebraically closed field and let $X$ be a variety of dimension $n$ over $k$.
Let $\mce$ be a locally free sheaf of finite rank $r>n$ on $X$, and let $V \subseteq \Gamma(X, \mce)$ be a vector space of global sections which generate $\mce$.
Then show that there is an element $s \in V$ such that for each $x \in X$ we have $s_x \not\in \mfm_x \mce_x$.
Conclude that there is a morphism $\OO_X \to \mce$ giving rise to an exact sequence
$$
0 \to \OO_X \to \mce \to \mce' \to 0,
$$
where $\mce'$ is also locally free.
:::

::: {.hint}
Use a method similar to the proof of Bertini's theorem (II.8.18).
:::

::: {.solution}
The value of a section at $x$ means its image in the fibre $\mce(x)=\mce_x\otimes_{\OO_{X,x}}\kappa(x)$.
Thus the required condition is nonzero fibre value at every scheme point, not just nonzero germ.

::: pf

::: {.pf-step #s1}

There is a finite-dimensional subspace $W\subseteq V$ which generates $\mce$.

::: pf-proof

At every point choose finitely many sections from $V$ that generate the stalk, using the assumed [[D-MODGG|global generation]] and finite rank.
Their images generate on a neighborhood: the cokernel of the map from a finite free sheaf is coherent and vanishes at that stalk, so it vanishes after shrinking.
The variety $X$ is quasi-compact, so finitely many such neighborhoods cover it.
The span $W$ of the sections chosen on that finite cover is finite-dimensional and generates at every point.
Write $m=\dim_kW$ and choose a basis $s_1,\ldots,s_m$.
In particular, $m\ge r$.

:::

:::

::: {.pf-step #s2}

Let $I\subseteq X\times_k\AA_k^m$ be the incidence subscheme defined by the vanishing of the universal section $\sum_j a_js_j$, where $a_1,\ldots,a_m$ are the coordinates on $\AA^m$.
Then $I$ is the total space of a vector bundle of rank $m-r$ on $X$, and
$$
\dim I=n+m-r<m.
$$

::: pf-proof

The evaluation map $W\otimes_k\OO_X\twoheadrightarrow\mce$ is surjective.
It splits locally because the target is locally free: on a framed open, choose local lifts of a basis.
Its kernel is consequently locally free of rank $m-r$.

On such an open, change the frame of $W\otimes_k\OO_X$ according to this splitting.
The vanishing of the universal section is then the vanishing of $r$ independent fibre coordinates, leaving an affine space of dimension $m-r$ over that open.
These local descriptions identify $I$ with the total space of the kernel bundle.
In particular, $I$ is integral and has dimension $n+m-r$, since its trivializing opens are products of nonempty opens of the integral variety $X$ with $\AA^{m-r}$.
The inequality follows from $r>n$.

:::

:::

::: {.pf-step #s3}

There is a section $s\in W$ with no zero on $X$.

::: pf-proof

Let $Z$ be the reduced closure of the image of the second projection $I\to\AA^m$.
The induced dominant morphism from the integral variety $I$ to $Z$ gives an inclusion of function fields.
Dimensions of integral finite-type schemes over a field equal the transcendence degrees of their function fields, so
$$
\dim Z\le\dim I<m
$$
[@Har10a, Chapter I, §§1 and 4].
Thus $\AA^m\setminus Z$ is a nonempty open subset and contains a $k$-rational point $a=(a_1,\ldots,a_m)$, since $k$ is algebraically closed.
Choose this point and put $s=\sum_j a_js_j\in W\subseteq V$.

The fibre of $I\to\AA^m$ over $a$ is exactly the zero subscheme of $s$.
It is empty because $a$ is outside the closure of the image.
Consequently $s_x\notin\mathfrak m_x\mce_x$ for every $x\in X$, as required.
The argument uses the closure of the incidence image; it does not require that the projection be proper or that the image itself be closed.

:::

:::

::: {.pf-step #s4}

The map $\OO_X\to\mce$ defined by $1\mapsto s$ is injective with a locally free cokernel of rank $r-1$.

::: pf-proof

Fix $x\in X$ and express $s$ in a local frame $e_1,\ldots,e_r$ as $s=\sum_i b_ie_i$.
Step [](#s3){.pf-ref} says that at least one $b_i$ is outside the maximal ideal at $x$.
Reorder the frame so that this is $b_1$, and shrink until $b_1$ is a unit.
The list $s,e_2,\ldots,e_r$ is then a frame, since its change-of-basis determinant is $b_1$.
In this frame, the map from $\OO_X$ is the inclusion of the first summand, with free cokernel of rank $r-1$.
These local descriptions prove global injectivity and local freeness of the cokernel $\mce'$, giving the stated short exact sequence.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref} produce the section in the prescribed space $V$, and step [](#s4){.pf-ref} proves the exact sequence with locally free quotient.

:::

:::

:::

::: {.remark}
The proof also works over any infinite field: every nonempty open subset of $\AA_k^m$ has a $k$-point, since a nonzero polynomial cannot vanish on all of $k^m$ when $k$ is infinite.
This follows by induction on $m$ from the finiteness of the roots of a nonzero polynomial in one variable.
:::
