---
schema: qual/card@1
id: E-HAT-3.F-3
kind: problem
title: "$\\operatorname{Ext}(A, \\mathbb{Q}) = 0$"
classification:
  areas:
  - topology
  topics:
  - Cohomology
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: {.problem}
Show that $\operatorname{Ext}(A, \mathbb{Q}) = 0$ for all $A$.
[Consider the homology with $\mathbb{Q}$ coefficients of a Moore space $M(A, n)$.]
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Divisibility and injectivity of $\mathbb{Q}$:

::: pf-proof

::: pf-step

An abelian group $D$ is divisible if for every $d \in D$ and non-zero integer $n \in \mathbb{Z}$, there exists $x \in D$ such that $nx = d$.
$\mathbb{Q}$ is divisible because $n(q/n) = q$ for all $q \in \mathbb{Q}$ and $n \in \mathbb{Z} \setminus \{0\}$.

::: pf-proof

arithmetic of rational numbers.

:::

:::

::: pf-step

By Baer’s Criterion, an abelian group (a $\mathbb{Z}$-module) is injective if and only if it is divisible.
Thus $\mathbb{Q}$ is an injective $\mathbb{Z}$-module.

::: pf-proof

Baer's Criterion for modules over principal ideal domains.

:::

:::

:::

:::

::: {.pf-step #s2}

Vanishing of $\operatorname{Ext}(A, \mathbb{Q})$ via free resolutions:

::: pf-proof

::: pf-step

Let $A$ be any abelian group, and choose a free presentation (resolution):
\[
0 \longrightarrow F_1 \xrightarrow{\;d\;} F_0 \longrightarrow A \longrightarrow 0,
\]
where $F_0, F_1$ are free abelian groups.

::: pf-proof

every abelian group is a quotient of a free abelian group with free kernel.

:::

:::

::: pf-step

Applying the contravariant functor $\operatorname{Hom}_\mathbb{Z}(-, \mathbb{Q})$ yields the long exact sequence:
\[
0 \longrightarrow \operatorname{Hom}(A, \mathbb{Q}) \longrightarrow \operatorname{Hom}(F_0, \mathbb{Q}) \xrightarrow{\;d^* \;} \operatorname{Hom}(F_1, \mathbb{Q}) \longrightarrow \operatorname{Ext}^1(A, \mathbb{Q}) \longrightarrow 0.
\]

::: pf-proof

derived functor long exact sequence for $\operatorname{Ext}$.

:::

:::

::: pf-step

Because $\mathbb{Q}$ is injective, every homomorphism $\phi: F_1 \to \mathbb{Q}$ extends along the inclusion $d: F_1 \hookrightarrow F_0$ to a homomorphism $\widetilde{\phi}: F_0 \to \mathbb{Q}$ such that $\widetilde{\phi} \circ d = \phi$.
Thus the dual map $d^*: \operatorname{Hom}(F_0, \mathbb{Q}) \to \operatorname{Hom}(F_1, \mathbb{Q})$ is surjective.

::: pf-proof

definition of injective module.

:::

:::

::: pf-step

By exactness:
\[
\operatorname{Ext}^1(A, \mathbb{Q}) \cong \operatorname{coker}(d^*) = \operatorname{Hom}(F_1, \mathbb{Q}) / \operatorname{Im}(d^*) = 0.
\]

::: pf-proof

surjectivity of $d^*$.

:::

:::

:::

:::

::: {.pf-step #s3}

Alternative topological perspective via Moore spaces:

::: pf-proof

::: pf-step

Let $X = M(A, n)$ be a Moore space with $\widetilde{H}_n(X) \cong A$ and $\widetilde{H}_i(X) = 0$ for all $i \neq n$.
By the Universal Coefficient Theorem for cohomology with $\mathbb{Q}$ coefficients:
\[
0 \longrightarrow \operatorname{Ext}(H_n(X), \mathbb{Q}) \longrightarrow H^{n+1}(X; \mathbb{Q}) \longrightarrow \operatorname{Hom}(H_{n+1}(X), \mathbb{Q}) \longrightarrow 0.
\]

::: pf-proof

Universal Coefficient Theorem for Cohomology.

:::

:::

::: pf-step

Since $\mathbb{Q}$ is a field, $H_{n+1}(X; \mathbb{Q}) \cong H_{n+1}(X) \otimes \mathbb{Q} = 0 \otimes \mathbb{Q} = 0$, so $H^{n+1}(X; \mathbb{Q}) = 0$.
The exact sequence forces $\operatorname{Ext}(A, \mathbb{Q}) = 0$.

::: pf-proof

exactness with vanishing middle group.

:::

:::

:::

:::

::: pf-step

Conclusion:
$\operatorname{Ext}(A, \mathbb{Q}) = 0$ for every abelian group $A$. Q.E.D.

::: pf-proof

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref}.

:::

:::

:::

:::
