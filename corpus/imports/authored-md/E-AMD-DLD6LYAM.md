---
schema: qual/card@1
id: E-AMD-DLD6LYAM
kind: exercise
title: Groups of order $12$ with a normal subgroup of order $4$ are isomorphic to
  $A_4$
classification:
  areas:
  - algebra
  topics:
  - Classification
  - Normal Subgroups
  - Sylow Theory
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}
Show that if $|G| = 12$ and $G$ is a non-abelian group with a normal subgroup of order $4$ (or equivalently, $n_3 = 4$), then $G \cong A_4$.
:::

::: solution
**Goal:** Prove that if a group $G$ of order $12$ has a normal subgroup $V \trianglelefteq G$ of order $4$ and is non-abelian (or equivalently, has $n_3 = 4$ Sylow 3-subgroups), then $G$ is isomorphic to the alternating group $A_4$.

<1>1. Semidirect product structure $G \cong V \rtimes P$:
    *Proof:*
    <2>1. Let $V \trianglelefteq G$ be the normal subgroup of order $|V| = 4$.
    <2>2. Let $P \in \operatorname{Syl}_3(G)$ be a Sylow 3-subgroup of order $|P| = 3$.
    <2>3. Since $\gcd(|V|, |P|) = \gcd(4, 3) = 1$, Lagrange's Theorem gives $V \cap P = \{e\}$.
    <2>4. The product $V P$ has order $\frac{|V| |P|}{|V \cap P|} = \frac{4 \cdot 3}{1} = 12 = |G|$, so $G = V P$.
    <2>5. Because $V \trianglelefteq G$, $G$ is an internal semidirect product:
        $$G \cong V \rtimes_\theta P,$$
        where $\theta: P \to \operatorname{Aut}(V)$ is the conjugation action $\theta(y)(x) = y x y^{-1}$.

<1>2. Determination of the isomorphism type of $V$:
    *Proof:*
    <2>1. Up to isomorphism, there are two groups of order $4$: $\mathbb{Z}_4$ and the Klein four-group $V_4 \cong \mathbb{Z}_2 \times \mathbb{Z}_2$.
    <2>2. **If $V \cong \mathbb{Z}_4$:**
        The automorphism group is $\operatorname{Aut}(\mathbb{Z}_4) \cong (\mathbb{Z}/4\mathbb{Z})^\times \cong \mathbb{Z}_2$.
        Because $\gcd(|P|, |\operatorname{Aut}(\mathbb{Z}_4)|) = \gcd(3, 2) = 1$, the only homomorphism $\theta: \mathbb{Z}_3 \to \mathbb{Z}_2$ is the trivial homomorphism.
        A trivial action implies $G \cong \mathbb{Z}_4 \times \mathbb{Z}_3 \cong \mathbb{Z}_{12}$, which is abelian.
    <2>3. Since $G$ is non-abelian, $V$ cannot be cyclic. Therefore:
        $$V \cong V_4 = \{e, a, b, c\} \cong \mathbb{Z}_2 \times \mathbb{Z}_2.$$

<1>3. Action of $P$ on $V_4$ and isomorphism with $A_4$:
    *Proof:*
    <2>1. The automorphism group of the Klein four-group is:
        $$\operatorname{Aut}(V_4) \cong \operatorname{GL}_2(\mathbb{F}_2) \cong S_3.$$
    <2>2. $S_3$ contains a unique subgroup of order $3$, namely $A_3 = \{\operatorname{id}, (a\,b\,c), (a\,c\,b)\}$.
    <2>3. Since $G$ is non-abelian, the action $\theta: \mathbb{Z}_3 \to S_3$ must be non-trivial, so $\operatorname{im}(\theta) = A_3 \le S_3$.
    <2>4. Up to group automorphism of $\mathbb{Z}_3$ (choosing the generator $y$ vs $y^2$), there is a unique non-trivial semidirect product $V_4 \rtimes \mathbb{Z}_3$.
    <2>5. In $A_4$, the Klein four-subgroup $V = \{e, (1\,2)(3\,4), (1\,3)(2\,4), (1\,4)(2\,3)\}$ is a normal subgroup of order $4$, and conjugation by the 3-cycle $(1\,2\,3)$ cyclically permutes the three non-identity elements of $V$.
    <2>6. Thus $A_4 \cong V_4 \rtimes \mathbb{Z}_3$.

<1>4. Conclusion:
    $G \cong V_4 \rtimes \mathbb{Z}_3 \cong A_4$. Q.E.D.
:::
