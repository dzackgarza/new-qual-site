---
schema: qual/card@1
id: D-COHGODEMENT
kind: definition
title: The Godement resolution
classification:
  areas:
  - algebraic-geometry
  topics:
  - Flasque Sheaves
  - Resolutions
  - Sheaf Cohomology
relations:
- kind: uses
  target: D-COHFLQ
review: draft
prompts:
- What is the Godement resolution?
---

::: {.definition title="Godement resolution"}
Let $\mcf$ be a sheaf of abelian groups on a topological space $X$.
Put
$$
\mathcal{G}^0(\mcf)(U) = \prod_{x \in U} \mcf_x ,
$$
the sheaf of all, not necessarily continuous, sections of the espace étalé, with the injection $\mcf \to \mathcal{G}^0(\mcf)$ sending $s$ to its germs.
Inductively, with $\mathcal{Z}^0 = \mcf$ and $\mathcal{Z}^{n+1} = \operatorname{coker}\big(\mathcal{Z}^{n} \to \mathcal{G}^0(\mathcal{Z}^{n})\big)$, set $\mathcal{G}^n(\mcf) = \mathcal{G}^0(\mathcal{Z}^n)$ with differential $\mathcal{G}^n(\mcf) \to \mathcal{Z}^{n+1} \to \mathcal{G}^{n+1}(\mcf)$.
The complex $0 \to \mcf \to \mathcal{G}^0(\mcf) \to \mathcal{G}^1(\mcf) \to \cdots$ is the \dfn{Godement resolution}.
:::

::: {.proposition}
1. Each $\mathcal{G}^n(\mcf)$ is flasque.

2. The complex $0\to\mcf\to\mathcal{G}^\bullet(\mcf)$ is exact, and the construction is functorial in $\mcf$ and carries short exact sequences of sheaves to short exact sequences of complexes.

3. $H^i(X, \mcf) = H^i\big(\Gamma(X, \mathcal{G}^\bullet(\mcf))\big)$ for all $i\geq0$.
:::

::: {.proof}
**(1)**
For any sheaf $\mcg$ the group $\mathcal{G}^0(\mcg)(U)=\prod_{x\in U}\mcg_x$ restricts to $\mathcal{G}^0(\mcg)(V)=\prod_{x\in V}\mcg_x$ for $V\subseteq U$ by the projection, which is surjective: a family over $V$ extends to the family over $U$ that is zero off $V$.
So $\mathcal{G}^0(\mcg)$ is flasque for every $\mcg$, and $\mathcal{G}^n(\mcf)=\mathcal{G}^0(\mathcal{Z}^n)$ is flasque.

**(2)**
By construction $\mathcal{Z}^{n+1}$ is the cokernel of $\mathcal{Z}^n\to\mathcal{G}^n(\mcf)$, so
$$
0\to\mathcal{Z}^n\to\mathcal{G}^n(\mcf)\to\mathcal{Z}^{n+1}\to0
$$
is exact, and splicing these short exact sequences along $\mathcal{Z}^{n+1}\to\mathcal{G}^{n+1}(\mcf)$ exhibits $0\to\mcf\to\mathcal{G}^\bullet(\mcf)$ as exact.
Functoriality and exactness in $\mcf$ hold step by step: the stalk $\mcf\mapsto\mcf_x$ is an exact functor because a stalk is a filtered colimit ([[D-0QSI0]]), the product $\prod_{x\in U}$ is exact in $\Ab$ because a product of surjections of abelian groups is surjective, and a cokernel, taken of a short exact sequence of complexes that is exact in each degree, is again exact in each degree, so a short exact sequence $0\to\mcf'\to\mcf\to\mcf''\to0$ gives short exact sequences $0\to\mathcal{Z}'^n\to\mathcal{Z}^n\to\mathcal{Z}''^n\to0$ and $0\to\mathcal{G}^n(\mcf')\to\mathcal{G}^n(\mcf)\to\mathcal{G}^n(\mcf'')\to0$ by induction on $n$.

**(3)**
Each $\mathcal{G}^n(\mcf)$ is flasque by (1), hence $\globsec{X;-}$-acyclic ([[D-COHFLQ]]), so by [[D-DEFACYC]] the resolution of (2) computes the right derived functors of $\globsec{X;-}$, that is, $H^i(X,\mcf)\cong H^i\big(\Gamma(X,\mathcal{G}^\bullet(\mcf))\big)$.
:::

::: {.remark}
For a continuous map $f\colon X\to Y$, pushforwards of flasque sheaves are flasque [@Har77, Exercise II.1.16(d)], and the argument of [[D-COHFLQ]] with $f_*$ in place of $\Gamma(X,-)$ shows that flasque sheaves are $f_*$-acyclic; hence $R^if_*\mcf\cong\mathcal H^i\big(f_*\mathcal G^\bullet(\mcf)\big)$.
The complexes $\Gamma(X,\mathcal G^\bullet(\mcf))$ and $f_*\mathcal G^\bullet(\mcf)$ are functorial in $\mcf$ and involve no choice of injective resolution.
:::
