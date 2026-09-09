---
schema: qual/card@1
id: P-UCTOP-SU07-8
kind: problem
title: Suspension of homology sphere is homotopy equivalent to S^4
classification:
  areas:
  - topology
  topics:
  - Homology
relations: []
review: draft
---

Let $M^3$ be a homology sphere – a closed 3-manifold having the same homology groups as $S^3$ – and let $X = \Sigma M$ be its suspension.
What are the fundamental group and homology groups of $X$?
Show that $X$ is homotopy-equivalent to $S^4$.

::: {.solution}
<1>1. The suspension $X=\Sigma M$ is simply connected.
::: {.proof}
The homology sphere $M$ is connected. The suspension is the union of the two open cones on $M$, each simply connected, with path-connected intersection homotopy equivalent to $M$. Van Kampen gives trivial fundamental group because the two cone groups are trivial.
:::

<1>2. Suspension shifts reduced homology by one degree:
$$
\widetilde H_i(X;\mathbb Z)\cong\widetilde H_{i-1}(M;\mathbb Z).
$$
:::
::: {.proof}
Apply the reduced Mayer--Vietoris sequence to the decomposition of $\Sigma M$ into two contractible cone neighborhoods whose intersection deformation-retracts onto $M$.
:::

<1>3. Hence
$$
H_i(X;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i=0,4,\\
0,&\text{otherwise}.
\end{cases}
$$
:::
::: {.proof}
By hypothesis $M$ has the homology of $S^3$, so its only nonzero reduced homology group is $\widetilde H_3(M)\cong\mathbb Z$. Apply <1>2.
:::

<1>4. The space $X$ is $3$-connected.
::: {.proof}
By <1>1 it is simply connected. If $\pi_2(X)$ were the first nonzero higher homotopy group, the Hurewicz theorem would give $\pi_2(X)\cong H_2(X)$, contradicting <1>3; hence $\pi_2(X)=0$. Repeating the same argument in degree $3$ gives $\pi_3(X)=0$ because $H_3(X)=0$.
:::

<1>5. The Hurewicz homomorphism
$$
\pi_4(X)\longrightarrow H_4(X)\cong\mathbb Z
$$
is an isomorphism.
::: {.proof}
Apply Hurewicz to the $3$-connected space $X$.
:::

<1>6. Choose $f:S^4\to X$ representing a class mapping to a generator of $H_4(X)$.
::: {.proof}
Such a class exists by the isomorphism in <1>5.
:::

<1>7. The map $f$ is an integral homology equivalence.
::: {.proof}
It is an isomorphism on $H_4$ by construction and on $H_0$ because both spaces are connected. All other reduced homology groups of both $S^4$ and $X$ vanish by <1>3.
:::

<1>8. Therefore
$$
\boxed{\Sigma M\simeq S^4}.
$$
:::
::: {.proof}
Both spaces are simply connected CW complexes: $M$ is a closed manifold and hence has CW type, and suspension preserves CW type. By the homological Whitehead theorem, a homology equivalence between simply connected CW complexes is a homotopy equivalence. Apply this to $f$.
:::
:::

