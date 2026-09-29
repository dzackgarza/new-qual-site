---
schema: qual/card@1
id: P-AMD-DNJBGQNL
kind: problem
title: $Inn(G)$ is characteristic in $Aut(G)$
classification:
  areas:
  - algebra
  topics:
  - Automorphisms
  - Normal Subgroups
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    Checked against UCSD Math 200A Fall 2016 Homework 4, Exercise 3(b). Restored
    the source hypothesis that G is simple. The previous solution incorrectly
    concluded characteristicity for every group and relied on an unsupported
    uniqueness assertion about normal subgroups of Aut(G).
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: >-
    For nonabelian simple G, the center is trivial and I=Inn(G) is a nontrivial
    simple normal subgroup of A=Aut(G). For Phi in Aut(A), J=Phi(I) is another
    simple normal subgroup. If I∩J were trivial, normality would force I and J
    to commute elementwise; Exercise 3(a) and centerlessness would then force
    J to be trivial, a contradiction. Hence I∩J is nontrivial and simplicity
    gives I=J. The abelian simple case has I trivial and is immediate.
---

::: {.problem}
Let $G$ be a simple group.
Set
\[
A=\operatorname{Aut}(G),
\qquad
I=\operatorname{Inn}(G).
\]
Prove that every $\Phi\in\operatorname{Aut}(A)$ satisfies
\[
\Phi(I)=I.
\]
Hence prove that
\[
I\operatorname{char}A.
\]
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The subgroup $I$ is normal in $A$ for every group $G$.

::: pf-proof

For $g\in G$, write
\[
c_g(x)=gxg^{-1}.
\]
Let $\alpha\in A$.
Then for every $x\in G$,
\[
(\alpha c_g\alpha^{-1})(x)
=\alpha(g)x\alpha(g)^{-1}
=c_{\alpha(g)}(x).
\]
Thus
\[
\alpha c_g\alpha^{-1}=c_{\alpha(g)}\in I.
\]
Hence conjugation by every element of $A$ preserves $I$, so
\[
I\normal A.
\]

:::

:::

::: {.pf-step #s2}

If $G$ is abelian and simple, then $I\operatorname{char}A$.

::: pf-proof

If $G$ is abelian, every inner automorphism is the identity.
Hence
\[
I=\{1_A\}.
\]
The trivial subgroup is characteristic in every group, so the conclusion is immediate in this case.

Assume from now on that $G$ is nonabelian simple.

:::

:::

::: {.pf-step #s3}

The group $G$ is centerless.

::: pf-proof

The center $Z(G)$ is a normal subgroup of $G$.
Since $G$ is simple,
\[
Z(G)=\{e\}
\qquad\text{or}\qquad
Z(G)=G.
\]
The second alternative would make $G$ abelian, contrary to the present assumption.
Therefore
\[
Z(G)=\{e\}.
\]

:::

:::

::: {.pf-step #s4}

The group $I$ is a nontrivial simple normal subgroup of $A$ and is isomorphic to $G$.

::: pf-proof

The homomorphism
\[
G\longrightarrow I,
\qquad
g\longmapsto c_g,
\]
is surjective by definition and has kernel $Z(G)$.
By step [](#s3){.pf-ref} its kernel is trivial, so
\[
G\cong I.
\]
Thus $I$ is nontrivial and simple because $G$ is.
Normality follows from step [](#s1){.pf-ref}.

:::

:::

::: {.pf-step #s5}

Let $\Phi\in\operatorname{Aut}(A)$ and set
\[
J=\Phi(I).
\]
Then $J$ is a nontrivial simple normal subgroup of $A$.

::: pf-proof

Automorphisms preserve normal subgroups and restrict to isomorphisms onto their images.
By step [](#s4){.pf-ref}, $I$ is nontrivial, simple, and normal in $A$.
Therefore $J=\Phi(I)$ has the same three properties.

:::

:::

::: {.pf-step #s6}

The intersection $I\cap J$ is normal in both $I$ and $J$.

::: pf-proof

Both $I$ and $J$ are normal in $A$ by steps [](#s4){.pf-ref} and [](#s5){.pf-ref}. In particular, for $i\in I$,
\[
i(I\cap J)i^{-1}
=I\cap iJi^{-1}
=I\cap J,
\]
so $I\cap J\normal I$.
The same argument with $J$ shows
\[
I\cap J\normal J.
\]

:::

:::

::: {.pf-step #s7}

If $I\cap J\ne\{1_A\}$, then $I=J$.

::: pf-proof

By step [](#s6){.pf-ref}, $I\cap J$ is a nontrivial normal subgroup of the simple group $I$.
Hence
\[
I\cap J=I.
\]
It is also a nontrivial normal subgroup of the simple group $J$, so
\[
I\cap J=J.
\]
Therefore $I=J$.

:::

:::

::: {.pf-step #s8}

The alternative $I\cap J=\{1_A\}$ is impossible.

::: pf-proof

Assume for contradiction that
\[
I\cap J=\{1_A\}.
\]
Because $I\normal A$ and $J\normal A$, for $i\in I$ and $j\in J$ the commutator
\[
[i,j]=iji^{-1}j^{-1}
\]
lies in both $I$ and $J$.
Hence
\[
[i,j]\in I\cap J=\{1_A\}.
\]
Thus every element of $J$ commutes with every element of $I=\operatorname{Inn}(G)$.

But an element of $J$ is an automorphism of $G$.
Since $G$ is centerless by step [](#s3){.pf-ref}, Exercise 3(a) says that an automorphism of $G$ commuting with every inner automorphism must be the identity.
Therefore every element of $J$ is $1_A$, so
\[
J=\{1_A\}.
\]
This contradicts step [](#s5){.pf-ref}, which says that $J$ is nontrivial.

:::

:::

::: pf-step

Every automorphism $\Phi$ of $A$ preserves $I$.

::: pf-proof

By step [](#s8){.pf-ref},
\[
I\cap\Phi(I)\ne\{1_A\}.
\]
Applying step [](#s7){.pf-ref} with $J=\Phi(I)$ gives
\[
\Phi(I)=I.
\]
Since $\Phi\in\operatorname{Aut}(A)$ was arbitrary,
\[
I\operatorname{char}A.
\]
Together with step [](#s2){.pf-ref}, this covers both the abelian and nonabelian simple cases.

:::

:::

:::

:::
