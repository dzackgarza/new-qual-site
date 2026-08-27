---
schema: qual/card@1
id: E-AMD-2OEGAZBX
kind: exercise
title: $\Out(A_4)$ is nontrivial
classification:
  areas:
  - algebra
  topics:
  - Automorphisms
  - Permutations
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
---

::: {.exercise}
Show that $\Out(A_4)$ is nontrivial.
:::

::: {.solution}
Recall that the outer automorphism group is defined as the quotient:
$$
\Out(A_4) = \Aut(A_4) / \Inn(A_4).
$$
To show $\Out(A_4)$ is nontrivial, we show that $|\Aut(A_4)| > |\Inn(A_4)|$ (specifically $\Aut(A_4) \cong S_4$ while $\Inn(A_4) \cong A_4$, so $\Out(A_4) \cong \ZZ_2$).

1. **Inner Automorphisms of $A_4$:** Since $A_4$ has trivial center ($Z(A_4) = 1$):
   $$
   \Inn(A_4) \cong A_4 / Z(A_4) \cong A_4.
   $$
   Thus $|\Inn(A_4)| = |A_4| = 12$.

2. **Constructing an Outer Automorphism via Conjugation in $S_4$:** $A_4$ is a normal subgroup of the symmetric group $S_4$.
   For any odd permutation $\tau \in S_4 \setminus A_4$, conjugation by $\tau$, defined by:
   $$
   \phi_\tau(\sigma) = \tau \sigma \tau^{-1} \quad \text{for } \sigma \in A_4,
   $$
   maps $A_4$ to $A_4$ and is an automorphism $\phi_\tau \in \Aut(A_4)$.

3. **Showing $\phi_\tau \notin \Inn(A_4)$:** Consider the transposition $\tau = (12) \in S_4 \setminus A_4$.

   - The action of $\phi_{(12)}$ on the 3-cycle $(123) \in A_4$ is:
     $$
     \phi_{(12)}((123)) = (12)(123)(12) = (213) = (132).
     $$

   - Suppose towards a contradiction that $\phi_{(12)}$ were an inner automorphism.
     Then there would exist some $g \in A_4$ such that $g \sigma g^{-1} = (12) \sigma (12)$ for all $\sigma \in A_4$.
     This would mean $g^{-1}(12)$ commutes with every element of $A_4$.
     Since the centralizer of $A_4$ in $S_4$ is trivial ($C_{S_4}(A_4) = 1$), we would have $g^{-1}(12) = e \implies (12) = g \in A_4$, which is impossible because $(12)$ is an odd permutation.

4. **Conclusion:** The automorphism $\phi_{(12)}$ is an outer automorphism of $A_4$.
   Therefore, $\Out(A_4) = \Aut(A_4)/\Inn(A_4)$ contains a non-identity coset, so:
   $$
   \Out(A_4) \cong S_4 / A_4 \cong \ZZ_2 \neq 1.
   $$
:::
