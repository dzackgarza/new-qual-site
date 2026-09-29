---
schema: qual/card@1
id: E-HAT-3.1-1
kind: problem
title: Functoriality of $\operatorname{Ext}(H,G)$ in both variables
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
Show that $\operatorname{Ext}(H, G)$ is a contravariant functor of $H$ for fixed $G$, and a covariant functor of $G$ for fixed $H$.
:::

::: {.solution}
::: pf

::: pf-step
Definition of $\operatorname{Ext}(H, G)$:

::: pf-proof

::: pf-step
For an abelian group $H$, choose a free resolution $0 \to F_1 \xrightarrow{d} F_0 \xrightarrow{\varepsilon} H \to 0$.

::: pf-proof
every abelian group is a quotient of a free abelian group, and subgroups of free abelian groups are free.
:::

:::

::: pf-step
Applying $\operatorname{Hom}(-, G)$ yields the cochain complex:
\[
0 \to \operatorname{Hom}(F_0, G) \xrightarrow{d^*} \operatorname{Hom}(F_1, G) \to 0,
\]
where $d^*(\varphi) = \varphi \circ d$.

::: pf-proof
contravariance of the $\operatorname{Hom}(-, G)$ functor.
:::

:::

::: pf-step
By definition, $\operatorname{Ext}(H, G) = \operatorname{coker}(d^*) = \operatorname{Hom}(F_1, G) / \operatorname{im}(d^*)$.

::: pf-proof
definition of Ext for abelian groups.
:::

:::

:::

:::

::: {.pf-step #s2}
Contravariance of $\operatorname{Ext}(-, G)$ in the first variable $H$:

::: pf-proof

::: pf-step
Let $\alpha: H \to H'$ be a group homomorphism, and let $0 \to F_1' \xrightarrow{d'} F_0' \xrightarrow{\varepsilon'} H' \to 0$ be a free resolution of $H'$.

::: pf-proof
setup.
:::

:::

::: pf-step
By projectivity of $F_0$ and $F_1$, there exists a chain map $(\alpha_0, \alpha_1)$ lifting $\alpha$:
\[
\varepsilon' \circ \alpha_0 = \alpha \circ \varepsilon \quad \text{and} \quad d' \circ \alpha_1 = \alpha_0 \circ d.
\]

::: pf-proof
comparison theorem for projective resolutions.
:::

:::

::: pf-step
Applying $\operatorname{Hom}(-, G)$ induces dual maps $\alpha_0^*: \operatorname{Hom}(F_0', G) \to \operatorname{Hom}(F_0, G)$ and $\alpha_1^*: \operatorname{Hom}(F_1', G) \to \operatorname{Hom}(F_1, G)$ satisfying $d^* \circ \alpha_0^* = \alpha_1^* \circ (d')^*$.

::: pf-proof
functoriality of $\operatorname{Hom}(-, G)$.
:::

:::

::: {.pf-step #s2-4}
The commutativity implies $\alpha_1^*(\operatorname{im}((d')^*)) \subseteq \operatorname{im}(d^*)$, so $\alpha_1^*$ descends to a well-defined homomorphism on quotients:
\[
\alpha^*: \operatorname{Ext}(H', G) \longrightarrow \operatorname{Ext}(H, G), \quad [\psi] \mapsto [\psi \circ \alpha_1].
\]

::: pf-proof
quotient map between cokernels.
:::

:::

::: {.pf-step #s2-5}
Any two lifts of $\alpha$ are chain homotopic, so the induced map $\alpha^*$ is independent of the choice of lift $(\alpha_0, \alpha_1)$.

::: pf-proof
chain homotopy induces the zero map on homology/cohomology.
:::

:::

::: {.pf-step #s2-6}
It is direct that $(\operatorname{id}_H)^* = \operatorname{id}_{\operatorname{Ext}(H, G)}$ and $(\beta \circ \alpha)^* = \alpha^* \circ \beta^*$ for $\beta: H' \to H''$.

::: pf-proof
composition of chain maps.
:::

:::

::: pf-step
Thus $\operatorname{Ext}(-, G)$ is a contravariant functor from the category of abelian groups to itself.

::: pf-proof
Steps [](#s2-4){.pf-ref}, [](#s2-5){.pf-ref}, and [](#s2-6){.pf-ref}.
:::

:::

:::

:::

::: {.pf-step #s3}
Covariance of $\operatorname{Ext}(H, -)$ in the second variable $G$:

::: pf-proof

::: pf-step
Let $\beta: G \to G'$ be a group homomorphism, and fix a free resolution $0 \to F_1 \xrightarrow{d} F_0 \to H \to 0$.

::: pf-proof
setup.
:::

:::

::: pf-step
Post-composition with $\beta$ defines homomorphisms $\beta_*: \operatorname{Hom}(F_k, G) \to \operatorname{Hom}(F_k, G')$ by $\beta_*(\varphi) = \beta \circ \varphi$ for $k = 0, 1$.

::: pf-proof
covariance of $\operatorname{Hom}(F_k, -)$.
:::

:::

::: pf-step
For any $\varphi \in \operatorname{Hom}(F_0, G)$, $\beta_*(d^*(\varphi)) = \beta \circ (\varphi \circ d) = (\beta \circ \varphi) \circ d = d^*(\beta_*(\varphi))$.
Thus $\beta_* \circ d^* = d^* \circ \beta_*$.

::: pf-proof
associativity of map composition.
:::

:::

::: {.pf-step #s3-4}
This implies $\beta_*(\operatorname{im}(d^*_G)) \subseteq \operatorname{im}(d^*_{G'})$, so $\beta_*$ descends to a well-defined homomorphism:
\[
\beta_*: \operatorname{Ext}(H, G) \longrightarrow \operatorname{Ext}(H, G'), \quad [\varphi] \mapsto [\beta \circ \varphi].
\]

::: pf-proof
quotient map between cokernels.
:::

:::

::: {.pf-step #s3-5}
It is direct that $(\operatorname{id}_G)_* = \operatorname{id}_{\operatorname{Ext}(H, G)}$ and $(\gamma \circ \beta)_* = \gamma_* \circ \beta_*$ for $\gamma: G' \to G''$.

::: pf-proof
composition of post-composition maps.
:::

:::

::: pf-step
Thus $\operatorname{Ext}(H, -)$ is a covariant functor.

::: pf-proof
Steps [](#s3-4){.pf-ref} and [](#s3-5){.pf-ref}.
:::

:::

:::

:::

::: pf-step
Conclusion: $\operatorname{Ext}(H, G)$ is contravariant in $H$ and covariant in $G$.

::: pf-proof
Steps [](#s2){.pf-ref} and [](#s3){.pf-ref}.
:::

:::

:::
