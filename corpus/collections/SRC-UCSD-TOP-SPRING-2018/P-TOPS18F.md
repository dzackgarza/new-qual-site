---
schema: qual/card@1
id: P-TOPS18F
kind: problem
title: "Suspension of a homology 3-sphere is homotopy equivalent to S^4"
classification:
  areas:
  - topology
  topics:
  - Homology
  - Suspensions
  - Homotopy Type
  - Manifolds
relations: []
review: draft
---

::: {.problem}
Let $M^3$ be a homology sphere — a closed $3$-manifold having the same homology groups as $S^3$ — and let $X = \Sigma M$ be its suspension.
What are the fundamental group and homology groups of $X$?
Show that $X$ is homotopy-equivalent to $S^4$.
:::

::: {.solution}
<1>1. Since $M$ is connected, its suspension $X=\Sigma M$ is simply connected.
::: {.proof}
Write the suspension as the union of its two open cones. Each cone is contractible and their intersection is homotopy equivalent to $M$, hence connected. Van Kampen gives trivial fundamental group.
:::

<1>2. Suspension shifts reduced homology:
$$\widetilde H_i(X;\mathbb Z)\cong\widetilde H_{i-1}(M;\mathbb Z).$$
Thus
$$\boxed{H_i(X;\mathbb Z)\cong\begin{cases}
\mathbb Z,&i=0,4,\\
0,&\text{otherwise.}
\end{cases}}$$
::: {.proof}
A homology $3$-sphere has reduced integral homology $\mathbb Z$ only in degree $3$. Apply the suspension isomorphism.
:::

<1>3. The space $X$ is $3$-connected and the Hurewicz map
$$\pi_4(X)\xrightarrow{\cong}H_4(X;\mathbb Z)\cong\mathbb Z$$
is an isomorphism.
::: {.proof}
Since $X$ is simply connected, Hurewicz gives $\pi_2(X)\cong H_2(X)=0$. Then $X$ is $2$-connected, so Hurewicz gives $\pi_3(X)\cong H_3(X)=0$. Thus it is $3$-connected, and Hurewicz in degree $4$ yields the displayed isomorphism.
:::

<1>4. Choose a map $g:S^4\to X$ representing a generator of $\pi_4(X)$. Then $g$ is an integral homology equivalence.
::: {.proof}
By <1>3, $g_*$ is an isomorphism on $H_4$. Both spaces are connected and have no other positive homology by <1>2 and the homology of $S^4$.
:::

<1>5. Therefore
$$\boxed{\Sigma M\simeq S^4.}$$
::: {.proof}
Both $S^4$ and $X$ have CW type and are simply connected. A homology equivalence between simply connected CW complexes is a homotopy equivalence by the homological Whitehead theorem.
:::
:::
