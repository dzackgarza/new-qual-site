---
schema: qual/card@1
id: E-HAT-3.F-3
kind: problem
title: "$\\operatorname{Ext}(A, \\QQ) = 0$"
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
Show that $\operatorname{Ext}(A, \QQ) = 0$ for all $A$.
[Consider the homology with $\QQ$ coefficients of a Moore space $M(A, n)$.]
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

Divisibility and injectivity of $\QQ$:

::: pf-proof

::: pf-step

An abelian group $D$ is divisible if for every $d \in D$ and non-zero integer $n \in \ZZ$, there exists $x \in D$ such that $nx = d$.
$\QQ$ is divisible because $n(q/n) = q$ for all $q \in \QQ$ and $n \in \ZZ \setminus \{0\}$.

::: pf-proof

arithmetic of rational numbers.

:::

:::

::: pf-step

By Baer’s Criterion, an abelian group (a $\ZZ$-module) is injective if and only if it is divisible.
Thus $\QQ$ is an injective $\ZZ$-module.

::: pf-proof

Baer's Criterion for modules over principal ideal domains.

:::

:::

:::

:::

::: {.pf-step #s2}

Vanishing of $\operatorname{Ext}(A, \QQ)$ via free resolutions:

::: pf-proof

::: pf-step

Let $A$ be any abelian group, and choose a free presentation (resolution):
$$
0 \longrightarrow F_1 \xrightarrow{\;d\;} F_0 \longrightarrow A \longrightarrow 0,
$$
where $F_0, F_1$ are free abelian groups.

::: pf-proof

every abelian group is a quotient of a free abelian group with free kernel.

:::

:::

::: pf-step

Applying the contravariant functor $\operatorname{Hom}_\ZZ(-, \QQ)$ yields the long exact sequence:
$$
0 \longrightarrow \operatorname{Hom}(A, \QQ) \longrightarrow \operatorname{Hom}(F_0, \QQ) \xrightarrow{\;d^* \;} \operatorname{Hom}(F_1, \QQ) \longrightarrow \operatorname{Ext}^1(A, \QQ) \longrightarrow 0.
$$

::: pf-proof

derived functor long exact sequence for $\operatorname{Ext}$.

:::

:::

::: pf-step

Because $\QQ$ is injective, every homomorphism $\phi: F_1 \to \QQ$ extends along the inclusion $d: F_1 \hookrightarrow F_0$ to a homomorphism $\widetilde{\phi}: F_0 \to \QQ$ such that $\widetilde{\phi} \circ d = \phi$.
Thus the dual map $d^*: \operatorname{Hom}(F_0, \QQ) \to \operatorname{Hom}(F_1, \QQ)$ is surjective.

::: pf-proof

definition of injective module.

:::

:::

::: pf-step

By exactness:
$$
\operatorname{Ext}^1(A, \QQ) \cong \operatorname{coker}(d^*) = \operatorname{Hom}(F_1, \QQ) / \operatorname{Im}(d^*) = 0.
$$

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
By the Universal Coefficient Theorem for cohomology with $\QQ$ coefficients:
$$
0 \longrightarrow \operatorname{Ext}(H_n(X), \QQ) \longrightarrow H^{n+1}(X; \QQ) \longrightarrow \operatorname{Hom}(H_{n+1}(X), \QQ) \longrightarrow 0.
$$

::: pf-proof

Universal Coefficient Theorem for Cohomology.

:::

:::

::: pf-step

Since $\QQ$ is a field, $H_{n+1}(X; \QQ) \cong H_{n+1}(X) \otimes \QQ = 0 \otimes \QQ = 0$, so $H^{n+1}(X; \QQ) = 0$.
The exact sequence forces $\operatorname{Ext}(A, \QQ) = 0$.

::: pf-proof

exactness with vanishing middle group.

:::

:::

:::

:::

::: pf-step

Conclusion:
$\operatorname{Ext}(A, \QQ) = 0$ for every abelian group $A$. Q.E.D.

::: pf-proof

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref} and [](#s3){.pf-ref}.

:::

:::

:::

:::
