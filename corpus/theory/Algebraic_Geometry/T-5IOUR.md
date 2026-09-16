---
schema: qual/card@1
id: T-5IOUR
kind: theorem
title: Serre's cohomological criterion for affineness
classification:
  areas:
  - algebraic-geometry
  topics:
  - Serre Criterion
  - Affine Schemes
  - Cohomology
relations:
- kind: uses
  target: T-SK599
- kind: uses
  target: D-PTIW0
review: draft
prompts:
- State and prove Serre's criterion for affineness.
- Can the Noetherian hypothesis be weakened?
- What fails without quasicompactness?
---

::: {.theorem}
Let $X$ be a Noetherian scheme.
The following are equivalent:

(i) $X$ is affine.

(ii) $H^p(X, \mcf) = 0$ for all quasicoherent $\mcf$ and all $p > 0$.

(iii) $H^1(X, \mci) = 0$ for every coherent sheaf of ideals $\mci$.
:::

::: {.proof}
1. (i) $\Rightarrow$ (ii) is vanishing of higher cohomology of quasicoherent sheaves on affine schemes, and (ii) $\Rightarrow$ (iii) is immediate. Assume (iii) and put $A = \OO_X(X)$.

2. For $f \in A$ write $X_f = \{x \in X : f(x) \neq 0\}$. If $f_1, \ldots, f_r \in A$ generate the unit ideal of $A$ and every $X_{f_i}$ is affine, then $X \cong \Spec A$: the morphism $X \to \Spec A$ restricts over each $D(f_i)$ to $X_{f_i} \to \Spec A_{f_i}$, which is an isomorphism because $\OO_X(X_{f_i}) = A_{f_i}$ for $X$ Noetherian, and the $D(f_i)$ cover $\Spec A$.

3. Every closed point $p \in X$ lies in some affine $X_f$. Let $U$ be an affine open neighbourhood of $p$ and $Z = X \setminus U$ with the reduced structure. The sequence of coherent ideal sheaves
   $$0 \to \mci_{Z \cup \{p\}} \to \mci_Z \to \kappa(p) \to 0$$
   is exact because $p \notin Z$, and $H^1(X, \mci_{Z \cup \{p\}}) = 0$ by (iii), so $H^0(X, \mci_Z) \to \kappa(p)$ is surjective and some $f \in \mci_Z(X) \subseteq A$ has $f(p) \neq 0$.
   Then $X_f \subseteq U$ and $X_f = U_{f|_U}$ is affine.

4. The sets $X_f$ of step 3 cover every closed point, hence $X$, since a Noetherian scheme has a closed point in every nonempty closed subset. By quasicompactness finitely many $X_{f_1}, \ldots, X_{f_r}$ cover $X$.

5. The $f_i$ generate the unit ideal of $A$. The morphism $\varphi \colon \OO_X^{r} \to \OO_X$, $(a_i) \mapsto \sum_i a_i f_i$, is surjective as a map of sheaves, since on $X_{f_i}$ the section $f_i$ is a unit. Let $\mcf = \ker \varphi$, a coherent sheaf, and filter it by $\mcf_j = \mcf \cap (\OO_X^{j} \oplus 0)$ for $0 \leq j \leq r$. The projection to the $j$-th coordinate embeds $\mcf_j / \mcf_{j-1}$ into $\OO_X$, so each quotient is isomorphic to a coherent sheaf of ideals and has $H^1 = 0$ by (iii). Induction on $j$ along $0 \to \mcf_{j-1} \to \mcf_j \to \mcf_j/\mcf_{j-1} \to 0$ gives $H^1(X, \mcf) = H^1(X, \mcf_r) = 0$, so $\varphi$ is surjective on global sections and $1 = \sum_i a_i f_i$ with $a_i \in A$.

6. Steps 2, 4 and 5 give $X \cong \Spec A$.
:::

::: {.remark title="The two follow-ups"}
*Weakening Noetherian.* The criterion holds for quasicompact quasi-separated schemes, with $\mci$ ranging over quasicoherent ideals rather than coherent ones.
Noetherian is used only to have coherent ideals available and to extract finite subcovers, and both can be arranged directly.

*Dropping quasicompactness.* The conclusion fails.
An infinite disjoint union of affine schemes has vanishing higher cohomology for every quasicoherent sheaf, being a disjoint union of affines, but it is not affine: its ring of global sections is an infinite product, and the comparison map is not an isomorphism.
The finite subcover in the proof is where quasicompactness enters, and without it the $f_i$ need not be finite in number.
:::
