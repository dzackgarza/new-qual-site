---
schema: qual/card@1
id: E-HAT-3.1-1
kind: exercise
title: Hatcher Section 3.1 Exercise 1
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

# E-HAT-3.1-1

Show that $\operatorname{Ext}(H, G)$ is a contravariant functor of $H$ for fixed $G$, and a covariant functor of $G$ for fixed $H$.

::: {.solution}
<1>1. Definition of $\operatorname{Ext}(H, G)$: <2>1. For an abelian group $H$, choose a free resolution $0 \to F_1 \xrightarrow{d} F_0 \xrightarrow{\varepsilon} H \to 0$.
::: {.proof}
every abelian group is a quotient of a free abelian group, and subgroups of free abelian groups are free.
:::
<2>2. Applying $\operatorname{Hom}(-, G)$ yields the cochain complex:
\[
0 \to \operatorname{Hom}(F_0, G) \xrightarrow{d^*} \operatorname{Hom}(F_1, G) \to 0,
\]
where $d^*(\varphi) = \varphi \circ d$.
::: {.proof}
contravariance of the $\operatorname{Hom}(-, G)$ functor.
:::
<2>3. By definition, $\operatorname{Ext}(H, G) = \operatorname{coker}(d^*) = \operatorname{Hom}(F_1, G) / \operatorname{im}(d^*)$.
::: {.proof}
definition of Ext for abelian groups.
:::

<1>2. Contravariance of $\operatorname{Ext}(-, G)$ in the first variable $H$: <2>1. Let $\alpha: H \to H'$ be a group homomorphism, and let $0 \to F_1' \xrightarrow{d'} F_0' \xrightarrow{\varepsilon'} H' \to 0$ be a free resolution of $H'$.
::: {.proof}
setup.
:::
<2>2. By projectivity of $F_0$ and $F_1$, there exists a chain map $(\alpha_0, \alpha_1)$ lifting $\alpha$:
\[
\varepsilon' \circ \alpha_0 = \alpha \circ \varepsilon \quad \text{and} \quad d' \circ \alpha_1 = \alpha_0 \circ d.
\]
::: {.proof}
comparison theorem for projective resolutions.
:::
<2>3. Applying $\operatorname{Hom}(-, G)$ induces dual maps $\alpha_0^*: \operatorname{Hom}(F_0', G) \to \operatorname{Hom}(F_0, G)$ and $\alpha_1^*: \operatorname{Hom}(F_1', G) \to \operatorname{Hom}(F_1, G)$ satisfying $d^* \circ \alpha_0^* = \alpha_1^* \circ (d')^*$.
::: {.proof}
functoriality of $\operatorname{Hom}(-, G)$.
:::
<2>4. The commutativity implies $\alpha_1^*(\operatorname{im}((d')^*)) \subseteq \operatorname{im}(d^*)$, so $\alpha_1^*$ descends to a well-defined homomorphism on quotients:
\[
\alpha^*: \operatorname{Ext}(H', G) \longrightarrow \operatorname{Ext}(H, G), \quad [\psi] \mapsto [\psi \circ \alpha_1].
\]
::: {.proof}
quotient map between cokernels.
:::
<2>5. Any two lifts of $\alpha$ are chain homotopic, so the induced map $\alpha^*$ is independent of the choice of lift $(\alpha_0, \alpha_1)$.
::: {.proof}
chain homotopy induces the zero map on homology/cohomology.
:::
<2>6. It is direct that $(\operatorname{id}_H)^* = \operatorname{id}_{\operatorname{Ext}(H, G)}$ and $(\beta \circ \alpha)^* = \alpha^* \circ \beta^*$ for $\beta: H' \to H''$.
::: {.proof}
composition of chain maps.
:::
<2>7. Thus $\operatorname{Ext}(-, G)$ is a contravariant functor from the category of abelian groups to itself.
::: {.proof}
<2>4, <2>5, and <2>6.
:::

<1>3. Covariance of $\operatorname{Ext}(H, -)$ in the second variable $G$: <2>1. Let $\beta: G \to G'$ be a group homomorphism, and fix a free resolution $0 \to F_1 \xrightarrow{d} F_0 \to H \to 0$.
::: {.proof}
setup.
:::
<2>2. Post-composition with $\beta$ defines homomorphisms $\beta_*: \operatorname{Hom}(F_k, G) \to \operatorname{Hom}(F_k, G')$ by $\beta_*(\varphi) = \beta \circ \varphi$ for $k = 0, 1$.
::: {.proof}
covariance of $\operatorname{Hom}(F_k, -)$.
:::
<2>3. For any $\varphi \in \operatorname{Hom}(F_0, G)$, $\beta_*(d^*(\varphi)) = \beta \circ (\varphi \circ d) = (\beta \circ \varphi) \circ d = d^*(\beta_*(\varphi))$.
Thus $\beta_* \circ d^* = d^* \circ \beta_*$.
::: {.proof}
associativity of map composition.
:::
<2>4. This implies $\beta_*(\operatorname{im}(d^*_G)) \subseteq \operatorname{im}(d^*_{G'})$, so $\beta_*$ descends to a well-defined homomorphism:
\[
\beta_*: \operatorname{Ext}(H, G) \longrightarrow \operatorname{Ext}(H, G'), \quad [\varphi] \mapsto [\beta \circ \varphi].
\]
::: {.proof}
quotient map between cokernels.
:::
<2>5. It is direct that $(\operatorname{id}_G)_* = \operatorname{id}_{\operatorname{Ext}(H, G)}$ and $(\gamma \circ \beta)_* = \gamma_* \circ \beta_*$ for $\gamma: G' \to G''$.
::: {.proof}
composition of post-composition maps.
:::
<2>6. Thus $\operatorname{Ext}(H, -)$ is a covariant functor.
::: {.proof}
<2>4 and <2>5.
:::

<1>4. Conclusion: $\operatorname{Ext}(H, G)$ is contravariant in $H$ and covariant in $G$.
::: {.proof}
<1>2 and <1>3.
:::
Q.E.D.
:::
