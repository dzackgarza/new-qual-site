---
schema: qual/card@1
id: P-AGH46CREMONA
kind: problem
title: The standard quadratic plane Cremona transformation
classification:
  areas:
  - algebraic-geometry
  topics:
  - Birational Geometry
  - Rational Maps
  - Projective Space
relations:
- kind: uses
  target: P-AGH42RATMAPDOM
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-17
  note: 'Compared all three parts and the reference to V.4.2.3 with Hartshorne I.4.6. The standard quadratic formula is an involution on the dense torus and is represented by a morphism away from the three coordinate vertices.'
- event: solution-written
  by: chatgpt
  date: 2026-09-17
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-17
  note: 'Checked the involution calculation and maximal domain against standard references on the quadratic Cremona transformation. Maximality at each base point is proved by restricting a hypothetical extension to the two coordinate lines through that point, whose punctured parts map to two different target vertices.'
---

::: {.problem}
A birational map of $\PP^2$ into itself is called a *plane Cremona transformation*. One example, called a *quadratic transformation*, is the rational map $\varphi: \PP^2 \dashrightarrow \PP^2$ given by
$$
(a_0, a_1, a_2) \mapsto (a_1 a_2,\ a_0 a_2,\ a_0 a_1)
$$
when no two of $a_0, a_1, a_2$ are $0$.

(a) Show that $\varphi$ is birational, and is its own inverse.

(b) Find open sets $U, V \subseteq \PP^2$ such that $\varphi: U \to V$ is an isomorphism.

(c) Find the open sets where $\varphi$ and $\varphi^{-1}$ are defined, and describe the corresponding morphisms. See also (V, 4.2.3).
:::

::: {.solution}
Write homogeneous coordinates as $[a_0:a_1:a_2]$ and put
$$
\varphi([a_0:a_1:a_2])
=
[a_1a_2:a_0a_2:a_0a_1]
$$
whenever the three displayed coordinates are not all zero.

::: pf

::: {.pf-step #s1}

On the dense open torus
$$
T=D_+(a_0a_1a_2)
$$
we have
$$
\varphi^2=\operatorname{id}_T.
$$

::: pf-proof

If $a_0a_1a_2\ne0$, then
$$
\begin{aligned}
\varphi^2([a_0:a_1:a_2])
&=
[a_0^2a_1a_2:a_0a_1^2a_2:a_0a_1a_2^2]\\
&=[a_0:a_1:a_2],
\end{aligned}
$$
after cancelling the common nonzero scalar $a_0a_1a_2$.
The same hypothesis shows that $\varphi(T)\subseteq T$.
Thus $\varphi|_T$ is its own set-theoretic inverse.

:::

:::

::: {.pf-step #s2}

The restriction
$$
\varphi|_T:T\xrightarrow{\sim}T
$$
is an isomorphism; hence $\varphi$ is birational and is its own inverse as a rational map.

::: pf-proof

The three quadratic forms
$$
a_1a_2,\qquad a_0a_2,\qquad a_0a_1
$$
have no common zero on $T$, so they define a morphism $T\to\PP^2$.
Its image lies in $T$, and step [](#s1){.pf-ref} shows that the same morphism is its inverse there.
Therefore it is an isomorphism $T\cong T$.

The open set $T$ is nonempty and hence dense in the irreducible variety $\PP^2$.
An isomorphism on dense open subsets defines a birational map, and the identity $\varphi^2=\operatorname{id}$ on $T$ says that its inverse rational map is represented by the same quadratic transformation.
This proves (a), and also answers (b) with
$$
\boxed{U=V=T}.
$$

:::

:::

::: {.pf-step #s3}

The quadratic formula defines a morphism precisely on
$$
D
=
\PP^2\setminus
\{[1:0:0],[0:1:0],[0:0:1]\}.
$$

::: pf-proof

The three defining quadrics vanish simultaneously exactly when at least two of $a_0,a_1,a_2$ vanish.
In projective space this happens at precisely the three coordinate vertices.
Away from them, homogeneous forms of the same degree with no common zero define a morphism
$$
\varphi_D:D\to\PP^2,
\qquad
[a_0:a_1:a_2]
\longmapsto
[a_1a_2:a_0a_2:a_0a_1].
$$

:::

:::

::: {.pf-step #s4}

The rational map $\varphi$ cannot be extended across any of the three omitted coordinate vertices.

::: pf-proof

By symmetry it suffices to consider
$$
P_0=[1:0:0].
$$
Suppose a morphism representing $\varphi$ extended to an open neighborhood $W$ of $P_0$.
After replacing $W$ by $W\cap D_+(a_0)$, assume $W\subseteq D_+(a_0)$.

Let
$$
L_1=Z(a_1),
\qquad
L_2=Z(a_2).
$$
Both lines pass through $P_0$.
On $L_1\setminus\{P_0\}$ we have $a_2\ne0$, so
$$
\varphi([a_0:0:a_2])=[0:1:0].
$$
Thus the restriction of the hypothetical extension to the irreducible open curve $W\cap L_1$ is equal to the constant point $[0:1:0]$ on the dense open subset obtained by deleting $P_0$.
Because a point of $\PP^2$ is closed, its inverse image is closed; hence density forces the value at $P_0$ also to be $[0:1:0]$.

On the other hand, on $L_2\setminus\{P_0\}$,
$$
\varphi([a_0:a_1:0])=[0:0:1].
$$
The same argument forces the value at $P_0$ to be $[0:0:1]$.
These values are distinct, a contradiction.

Permuting the coordinates gives the same contradiction at $[0:1:0]$ and $[0:0:1]$.
Therefore none of the three vertices belongs to the domain of definition of the rational map.

:::

:::

::: {.pf-step #s5}

Both $\varphi$ and $\varphi^{-1}$ have maximal domain $D$, and on that domain both are represented by the same quadratic formula.

::: pf-proof

Steps [](#s3){.pf-ref} and [](#s4){.pf-ref} show that $D$ is exactly the maximal domain of $\varphi$ in the sense of [[P-AGH42RATMAPDOM]].
By step [](#s2){.pf-ref} the inverse rational map satisfies
$$
\varphi^{-1}=\varphi.
$$
It therefore has the same maximal domain and the same representing morphism
$$
[a_0:a_1:a_2]
\longmapsto
[a_1a_2:a_0a_2:a_0a_1].
$$
This proves (c).

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} prove (a) and (b), while steps [](#s3){.pf-ref}, [](#s4){.pf-ref} and [](#s5){.pf-ref} prove (c).

:::

:::

:::
