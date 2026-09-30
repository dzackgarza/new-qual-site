---
schema: qual/card@1
id: P-AMD-HWZNNEDG
kind: problem
title: $\operatorname{Ext}(C,A)$ classifies extensions of $C$ by $A$
classification:
  areas:
  - topology
  topics:
  - Homological Algebra
  - Groups
relations: []
review: draft
---

::: {.problem}
Prove that for a SES $0\into A\into B\into C$, the group $\Ext(C,A)$ classifies extensions of $C$ by $A$ up to isomorphism.
:::

::: {.solution}

::: pf

::: pf-step

An extension of $C$ by $A$ is a short exact sequence
$$
0\to A\xrightarrow{i}B\xrightarrow{p}C\to0,
$$
and two extensions are equivalent when there is an isomorphism of their middle terms commuting with the maps from $A$ and to $C$.

::: pf-proof

This is the standard Yoneda notion of equivalence of extensions.

:::

:::

::: {.pf-step #s2}

Choose a free resolution
$$
0\to K\xrightarrow{j}F\xrightarrow{q}C\to0.
$$
Pulling an extension back along $q:F\to C$ produces a split extension of $F$ by $A$.

::: pf-proof

Because $F$ is free, hence projective, the surjection from the pullback middle term onto $F$ admits a section.

:::

:::

::: {.pf-step #s3}

A choice of splitting determines a homomorphism $\phi:K\to A$, well-defined modulo maps $K\to A$ extending to $F$.

::: pf-proof

Lift the identity of $F$ to the pullback middle term. Restricting this lift to $K=\ker q$ lands in the copy of $A$, giving $\phi$. Changing the splitting by a map $F\to A$ changes $\phi$ by its restriction to $K$.

:::

:::

::: {.pf-step #s4}

Therefore an extension determines a class
$$
[\phi]\in \operatorname{coker}\bigl(\operatorname{Hom}(F,A)\to\operatorname{Hom}(K,A)\bigr)
=\operatorname{Ext}^1(C,A).
$$

::: pf-proof

Applying $\operatorname{Hom}(-,A)$ to the length-one free resolution identifies this cokernel with $\operatorname{Ext}^1(C,A)$.

:::

:::

::: {.pf-step #s5}

Conversely, a homomorphism $\phi:K\to A$ defines an extension by the pushout
$$
B_\phi=(A\oplus F)/\langle(\phi(k),-j(k)):k\in K\rangle.
$$
Then
$$
0\to A\to B_\phi\to C\to0
$$
is exact.

::: pf-proof

The map $A\to B_\phi$ is induced by the first summand, and $B_\phi\to C$ is induced by $q:F\to C$. The defining relations identify exactly the kernel coming from $K$, giving exactness.

:::

:::

::: {.pf-step #s6}

Two maps $\phi,\phi'$ give equivalent extensions exactly when their difference extends to a map $F\to A$.

::: pf-proof

If $\phi'-\phi=h\circ j$, then $(a,f)\mapsto(a+h(f),f)$ descends to an isomorphism $B_\phi\to B_{\phi'}$ commuting with $A$ and $C$. Conversely, an equivalence of extensions yields such a change of splitting after pullback to $F$.

:::

:::

::: pf-step

Hence equivalence classes of extensions of $C$ by $A$ are naturally in bijection with
$$
\boxed{\operatorname{Ext}^1(C,A).}
$$
Under this bijection the Baer sum of extensions corresponds to addition in $\operatorname{Ext}^1(C,A)$.

::: pf-proof

Steps [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref}, [](#s5){.pf-ref} and [](#s6){.pf-ref} construct mutually inverse assignments. The compatibility with addition is the standard pushout/pullback description of the Baer sum.

:::

:::

:::

:::
