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
Prove that for a SES $0\into A\into B\into C$, the group $\ext(C,A)$ classifies extensions of $C$ by $A$ up to isomorphism.
:::

::: {.solution}
<1>1. An extension of $C$ by $A$ is a short exact sequence
$$
0\to A\xrightarrow{i}B\xrightarrow{p}C\to0,
$$
and two extensions are equivalent when there is an isomorphism of their middle terms commuting with the maps from $A$ and to $C$.
::: {.proof}
This is the standard Yoneda notion of equivalence of extensions.
:::

<1>2. Choose a free resolution
$$
0\to K\xrightarrow{j}F\xrightarrow{q}C\to0.
$$
Pulling an extension back along $q:F\to C$ produces a split extension of $F$ by $A$.
::: {.proof}
Because $F$ is free, hence projective, the surjection from the pullback middle term onto $F$ admits a section.
:::

<1>3. A choice of splitting determines a homomorphism $\phi:K\to A$, well-defined modulo maps $K\to A$ extending to $F$.
::: {.proof}
Lift the identity of $F$ to the pullback middle term. Restricting this lift to $K=\ker q$ lands in the copy of $A$, giving $\phi$. Changing the splitting by a map $F\to A$ changes $\phi$ by its restriction to $K$.
:::

<1>4. Therefore an extension determines a class
$$
[\phi]\in \operatorname{coker}\bigl(\operatorname{Hom}(F,A)\to\operatorname{Hom}(K,A)\bigr)
=\operatorname{Ext}^1(C,A).
$$
::: {.proof}
Applying $\operatorname{Hom}(-,A)$ to the length-one free resolution identifies this cokernel with $\operatorname{Ext}^1(C,A)$.
:::

<1>5. Conversely, a homomorphism $\phi:K\to A$ defines an extension by the pushout
$$
B_\phi=(A\oplus F)/\langle(\phi(k),-j(k)):k\in K\rangle.
$$
Then
$$
0\to A\to B_\phi\to C\to0
$$
is exact.
::: {.proof}
The map $A\to B_\phi$ is induced by the first summand, and $B_\phi\to C$ is induced by $q:F\to C$. The defining relations identify exactly the kernel coming from $K$, giving exactness.
:::

<1>6. Two maps $\phi,\phi'$ give equivalent extensions exactly when their difference extends to a map $F\to A$.
::: {.proof}
If $\phi'-\phi=h\circ j$, then $(a,f)\mapsto(a+h(f),f)$ descends to an isomorphism $B_\phi\to B_{\phi'}$ commuting with $A$ and $C$. Conversely, an equivalence of extensions yields such a change of splitting after pullback to $F$.
:::

<1>7. Hence equivalence classes of extensions of $C$ by $A$ are naturally in bijection with
$$
\boxed{\operatorname{Ext}^1(C,A).}
$$
Under this bijection the Baer sum of extensions corresponds to addition in $\operatorname{Ext}^1(C,A)$.
::: {.proof}
Steps <1>2--<1>6 construct mutually inverse assignments. The compatibility with addition is the standard pushout/pullback description of the Baer sum.
:::
:::
