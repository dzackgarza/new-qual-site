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

::: {.problem}
Let $M^3$ be a homology sphere – a closed 3-manifold having the same homology groups as $S^3$ – and let $X = \Sigma M$ be its suspension.
What are the fundamental group and homology groups of $X$?
Show that $X$ is homotopy-equivalent to $S^4$.
:::

::: {.solution}

::: pf

::: {.pf-step #x-simply-connected}
The suspension $X=\Sigma M$ is simply connected.

::: pf-proof
The homology sphere $M$ is connected. The suspension is the union of the two open cones on $M$, each simply connected, with path-connected intersection homotopy equivalent to $M$. Van Kampen gives trivial fundamental group because the two cone groups are trivial.
:::

:::

::: {.pf-step #suspension-homology-shift}
Suspension shifts reduced homology by one degree:
$$
\widetilde H_i(X;\mathbb Z)\cong\widetilde H_{i-1}(M;\mathbb Z).
$$

::: pf-proof
Apply the reduced Mayer--Vietoris sequence to the decomposition of $\Sigma M$ into two contractible cone neighborhoods whose intersection deformation-retracts onto $M$.
:::

:::

::: {.pf-step #homology-of-x}
Hence
$$
H_i(X;\mathbb Z)\cong
\begin{cases}
\mathbb Z,&i=0,4,\\
0,&\text{otherwise}.
\end{cases}
$$

::: pf-proof
By hypothesis $M$ has the homology of $S^3$, so its only nonzero reduced homology group is $\widetilde H_3(M)\cong\mathbb Z$. Apply step [](#suspension-homology-shift){.pf-ref}.
:::

:::

::: pf-step
The space $X$ is $3$-connected.

::: pf-proof
By step [](#x-simply-connected){.pf-ref} it is simply connected. If $\pi_2(X)$ were the first nonzero higher homotopy group, the Hurewicz theorem would give $\pi_2(X)\cong H_2(X)$, contradicting step [](#homology-of-x){.pf-ref}; hence $\pi_2(X)=0$. Repeating the same argument in degree $3$ gives $\pi_3(X)=0$ because $H_3(X)=0$.
:::

:::

::: {.pf-step #hurewicz-iso-degree4}
The Hurewicz homomorphism
$$
\pi_4(X)\longrightarrow H_4(X)\cong\mathbb Z
$$
is an isomorphism.

::: pf-proof
Apply Hurewicz to the $3$-connected space $X$.
:::

:::

::: pf-step
Choose $f:S^4\to X$ representing a class mapping to a generator of $H_4(X)$.

::: pf-proof
Such a class exists by the isomorphism in step [](#hurewicz-iso-degree4){.pf-ref}.
:::

:::

::: pf-step
The map $f$ is an integral homology equivalence.

::: pf-proof
It is an isomorphism on $H_4$ by construction and on $H_0$ because both spaces are connected. All other reduced homology groups of both $S^4$ and $X$ vanish by step [](#homology-of-x){.pf-ref}.
:::

:::

::: {.pf-step #suspension-equiv-s4}
Therefore
$$
\boxed{\Sigma M\simeq S^4}.
$$

::: pf-proof
Both spaces are simply connected CW complexes: $M$ is a closed manifold and hence has CW type, and suspension preserves CW type. By the homological Whitehead theorem, a homology equivalence between simply connected CW complexes is a homotopy equivalence. Apply this to $f$.
:::

:::

::: pf-qed
Steps [](#x-simply-connected){.pf-ref} and [](#homology-of-x){.pf-ref} give $\pi_1(X)$ and $H_*(X)$, and step [](#suspension-equiv-s4){.pf-ref} shows $X\simeq S^4$.
:::

:::

:::

