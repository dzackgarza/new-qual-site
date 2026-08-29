---
schema: qual/card@1
id: E-AMD-JFCWSOUA
kind: exercise
title: $[A_4,A_4]\cong\ZZ_2^2$
classification:
  areas:
  - algebra
  topics:
  - Commutators
  - Permutations
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}
Show that $[A_4, A_4] \cong \mathbb{Z}_2^2$.
:::

::: solution
**Goal:** Prove that the derived (commutator) subgroup $[A_4, A_4]$ of the alternating group $A_4$ is the Klein four-group $V_4 \cong \mathbb{Z}_2^2$.

<1>1. Klein four-group and quotient abelianity:
    *Proof:*
    <2>1. Let $V = \{e, (1\,2)(3\,4), (1\,3)(2\,4), (1\,4)(2\,3)\} \le A_4$.
    <2>2. $V$ is a normal subgroup of $A_4$ ($V \trianglelefteq A_4$) of order $|V| = 4$.
    <2>3. The quotient group $A_4 / V$ has order $\frac{|A_4|}{|V|} = \frac{12}{4} = 3$.
    <2>4. Since the order is prime, $A_4 / V \cong \mathbb{Z}_3$, which is abelian.
    <2>5. By the universal property of the commutator subgroup, $G/N$ is abelian if and only if $[G, G] \le N$.
    <2>6. Thus $[A_4, A_4] \le V$.

<1>2. Direct generation of non-identity elements of $V$ via commutators:
    *Proof:*
    <2>1. Compute the commutator of the 3-cycles $\sigma = (1\,2\,3)$ and $\tau = (1\,2\,4)$ in $A_4$:
        $$[\sigma, \tau] = \sigma \tau \sigma^{-1} \tau^{-1} = (1\,2\,3)(1\,2\,4)(1\,3\,2)(1\,4\,2) = (1\,2)(3\,4) \in [A_4, A_4].$$
    <2>2. Conjugating $(1\,2)(3\,4) \in [A_4, A_4]$ by the 3-cycle $(1\,2\,3) \in A_4$ gives:
        $$(1\,2\,3)(1\,2)(3\,4)(1\,3\,2) = (2\,3)(1\,4) = (1\,4)(2\,3) \in [A_4, A_4].$$
    <2>3. Multiplying these two elements:
        $$(1\,2)(3\,4)(1\,4)(2\,3) = (1\,3)(2\,4) \in [A_4, A_4].$$
    <2>4. Hence $[A_4, A_4]$ contains all elements of $V$, so $V \le [A_4, A_4]$.

<1>3. Conclusion:
    Combining <1>1 and <1>2 yields $[A_4, A_4] = V \cong \mathbb{Z}_2^2$. Q.E.D.
:::
