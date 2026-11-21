---
schema: qual/card@1
id: E-HAT-3.2-18
kind: problem
title: Cup product nondegenerality on surfaces
classification:
  areas:
  - topology
  topics:
  - Cohomology
  - Cup Product
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-29
- event: source-checked
  by: claude
  date: 2026-10-31
  note: Statement compared with Hatcher, Algebraic Topology, Section 3.2, Exercise 18; it matches the printed text.
- event: solution-reviewed
  by: claude
  date: 2026-10-31
  note: >-
    Read both halves. For $M_g$ the symplectic basis gives a nondegenerate pairing on $H^1$, so
    each nonzero class pairs nontrivially with something. If $M_g\simeq X\vee Y$ then one factor,
    say $X$, has $H_2=0$ and nonzero $H_1$, hence $H^2(X;\ZZ)=0$ by the universal coefficient
    theorem, and a nonzero class from that summand pairs trivially with everything. The
    nonorientable case repeats the argument over $\ZZ_2$, where the pairing on $H^1(N_g;\ZZ_2)$ is
    nondegenerate in the dual crosscap basis.
- event: solution-reviewed
  by: claude
  date: 2026-11-07
  note: >-
    Statement matches Exercise 18 (p.230) with all three sentences. Rechecked: the symplectic basis of Exercise 1 p.228 makes the cup product on H^1(M_g;Z) nondegenerate, so every nonzero class pairs nontrivially; a splitting M_g = X v Y with both reduced homologies nontrivial forces one factor to have H_2 = 0 and H_1 nonzero free, hence H^1 != 0 and H^2 = 0 by Theorem 3.2 p.195, and a class from that factor is in the radical; for N_g over Z_2 the intersection form is the identity, and the same splitting argument works since H^2(N_g;Z_2) is one-dimensional and splits, so one factor has zero second cohomology. The wedge vanishing is now attributed to the relative cup product of p.209. Not covered: nothing about the case g with both factors having trivial reduced homology, excluded by the hypothesis.
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Lamport structure for the two parts and their deductions, which is what Queue D asks for on this card. The symplectic basis and its products are a step; the zero-radical statement for orientable surfaces is a step with both coefficient cases (some p_i nonzero, or all zero and some q_i nonzero); the wedge argument is a step in which the choice of the factor with vanishing H_2, the vanishing of H^2 of that factor and the two kinds of product are separated; and the nonorientable case gets the same two steps over Z_2, with the identity form and the observation that a nonzero subgroup of Z^{g-1} + Z_2 maps nontrivially to Z_2. No retained set covers this exercise; the card now says so. Locators checked: Exercise 1 of the section on printed p. 228, the relative cup product on p. 209, Theorem 3.2 on p. 195, the exercise on p. 230. No statement repair.
---

::: {.problem}
For the closed orientable surface $M$ of genus $g \geq 1$, show that for each nonzero $\alpha \in H^1(M; \ZZ)$ there exists $\beta \in H^1(M; \ZZ)$ with $\alpha \beta \neq 0$.
Deduce that $M$ is not homotopy equivalent to a wedge sum $X \vee Y$ of CW complexes with nontrivial reduced homology.
Do the same for closed nonorientable surfaces using cohomology with $\ZZ_2$ coefficients.
:::

::: {.solution}
No retained solution set covers this exercise: the Hatcher sets in the checkout reach §3.2 in Li (exercises 1, 2, 3, 4, 6, 11) and Sam (1, 4, 11), and neither holds exercise 18. The argument is the card's own, checked against Hatcher, *Algebraic Topology* (2002), §3.2 Exercise 18, printed p. 230.

::: pf

::: {.pf-step #symplectic}
For the closed orientable surface $M_g$ of genus $g\ge1$ there is a basis $a_1,b_1,\dots,a_g,b_g$ of $H^1(M_g;\ZZ)$, with $u$ generating $H^2(M_g;\ZZ)$, such that
$$
a_i\smile b_j=\delta_{ij}u,\qquad b_i\smile a_j=-\delta_{ij}u,\qquad a_i\smile a_j=b_i\smile b_j=0 .
$$

::: pf-proof
This is the computation of Exercise 1 of the section, printed p. 228: the basis is the one dual to the standard symplectic basis of $H_1(M_g;\ZZ)$, the cup product is the intersection form, and the intersection form of a closed orientable surface in that basis is the standard symplectic one with $u$ the orientation class.
:::

:::

::: {.pf-step #zero-radical}
For every nonzero $\alpha\in H^1(M_g;\ZZ)$ there is $\beta\in H^1(M_g;\ZZ)$ with $\alpha\smile\beta\ne0$.

::: pf-proof
Write $\alpha=\sum_i(p_ia_i+q_ib_i)$. If some $p_i\ne0$, then $\alpha\smile b_i=p_iu\ne0$ by step [](#symplectic){.pf-ref}. If every $p_i=0$ then $\alpha=\sum_iq_ib_i$ is nonzero, so some $q_i\ne0$, and $\alpha\smile a_i=q_i(b_i\smile a_i)=-q_iu\ne0$. So the pairing has zero radical.
:::

:::

::: {.pf-step #wedge-orientable}
$M_g$ is not homotopy equivalent to $X\vee Y$ with both factors having nontrivial reduced integral homology.

::: pf-proof
Suppose $M_g\simeq X\vee Y$ with both reduced homologies nontrivial. Reduced homology is additive over a wedge, and $\widetilde H_*(M_g)$ is $\ZZ^{2g}$ in degree $1$ and $\ZZ$ in degree $2$ and nothing else; so $H_2$ lies entirely in one factor and the other, call it $X$, has $H_2(X)=0$ together with $\widetilde H_1(X)\ne0$. As a direct summand of $H_1(M_g)$, the group $H_1(X)$ is a nonzero free abelian group, so $H^1(X;\ZZ)\ne0$, and the universal coefficient theorem, Theorem 3.2 printed p. 195, gives $H^2(X;\ZZ)\cong\operatorname{Hom}(H_2(X),\ZZ)\oplus\operatorname{Ext}(H_1(X),\ZZ)=0$ because $H_2(X)=0$ and $H_1(X)$ is free. Cohomology is additive over a wedge, so $H^1(X)\subset H^1(M_g)$: choose nonzero $\alpha$ in this summand, with $\alpha=p^*\alpha_X$. For $\beta$ coming from $Y$, $\alpha\smile\beta=0$ because cup products of classes from different wedge summands vanish, by the relative cup product of printed p. 209; for $\beta=p^*\beta_X$ from $X$, $\alpha\smile\beta=p^*(\alpha_X\smile\beta_X)=0$ because $\alpha_X\smile\beta_X\in H^2(X;\ZZ)=0$. So $\alpha\smile\beta=0$ for every $\beta$, contradicting step [](#zero-radical){.pf-ref}.
:::

:::

::: {.pf-step #nonorientable-pairing}
For the closed nonorientable surface $N_g$ and coefficients $\ZZ_2$, the pairing $H^1(N_g;\ZZ_2)\times H^1(N_g;\ZZ_2)\to H^2(N_g;\ZZ_2)\cong\ZZ_2$ has zero radical.

::: pf-proof
Take the basis of $H^1(N_g;\ZZ_2)$ dual to the $g$ crosscap loops. A crosscap loop has mod $2$ self-intersection $1$ and distinct crosscaps are disjoint, so the intersection form is the identity matrix, and by Exercise 1 of the section, printed p. 228, the cup product is the intersection form; thus $\alpha_i\smile\alpha_j=\delta_{ij}v$ for a generator $v$ of $H^2(N_g;\ZZ_2)$. For a nonzero $\alpha=\sum_{i\in S}\alpha_i$ over $\ZZ_2$, pairing with $\alpha_i$ for $i\in S$ gives $v\ne0$.
:::

:::

::: {.pf-step #wedge-nonorientable}
$N_g$ is not homotopy equivalent to a wedge $X\vee Y$ with both factors having nontrivial reduced integral homology.

::: pf-proof
Suppose $N_g\simeq X\vee Y$ with both factors nontrivial. The reduced integral homology of $N_g$ is confined to $H_1(N_g;\ZZ)\cong\ZZ^{g-1}\oplus\ZZ_2$, so each factor has $H_i=0$ for $i\ge2$ and its reduced homology sits in degree $1$; since $H_1(N_g)\cong H_1(X)\oplus H_1(Y)$, each of $H_1(X)$, $H_1(Y)$ is a nonzero subgroup of $\ZZ^{g-1}\oplus\ZZ_2$, hence maps nontrivially to $\ZZ_2$ — a nonzero subgroup either contains a free summand, which maps onto $\ZZ_2$, or is $\ZZ_2$ itself — so $H^1(X;\ZZ_2)$ and $H^1(Y;\ZZ_2)$ are both nonzero. Also $H^2(N_g;\ZZ_2)\cong\ZZ_2$ is one-dimensional and equals $H^2(X;\ZZ_2)\oplus H^2(Y;\ZZ_2)$, so one factor, say $X$, has $H^2(X;\ZZ_2)=0$. Take nonzero $\alpha=p^*\alpha_X\in H^1(N_g;\ZZ_2)$. For $\beta$ from $Y$ the product vanishes by the wedge argument of step [](#wedge-orientable){.pf-ref}, and for $\beta=p^*\beta_X$ it is $p^*(\alpha_X\smile\beta_X)=0$ because $\alpha_X\smile\beta_X\in H^2(X;\ZZ_2)=0$. So $\alpha$ is in the radical, contradicting step [](#nonorientable-pairing){.pf-ref}: the same conclusion holds for closed nonorientable surfaces with $\ZZ_2$ coefficients.
:::

:::

:::
:::
