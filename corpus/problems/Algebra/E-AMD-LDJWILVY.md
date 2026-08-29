---
schema: qual/card@1
id: E-AMD-LDJWILVY
kind: exercise
title: If $H\le N_G(K)$ then $HK$ is a subgroup
classification:
  areas:
  - algebra
  topics:
  - Subgroups
  - Centralizers and Normalizers
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: Claude Opus 5
  date: 2026-08-30
---

::: {.exercise}
Show that if $H \leq N_G(K)$ then $HK \leq G$, and give a counterexample showing that this condition is necessary.
:::

::: solution
**Goal:** Show that $H \le N_G(K)$ forces the product set $HK = \{hk : h \in H, k \in K\}$ to be a subgroup of $G$, and exhibit $H, K \le S_3$ with $H \not\le N_G(K)$ and $HK$ not a subgroup.

<1>1. Setup and the normalizing hypothesis: *Proof:* <2>1. Let $H, K \le G$ and assume $H \le N_G(K) = \{g \in G : gKg^{-1} = K\}$.
<2>2. Thus $hKh^{-1} = K$ for every $h \in H$; equivalently $h^{-1}Kh = K$ for every $h \in H$.

<1>2. $HK$ is nonempty: *Proof:* <2>1. $1 = 1 \cdot 1 \in HK$ since $1 \in H$ and $1 \in K$.

<1>3. $HK$ is closed under multiplication: *Proof:* <2>1. Let $h_1 k_1, h_2 k_2 \in HK$ with $h_i \in H$ and $k_i \in K$.
<2>2. Insert $h_2^{-1} h_2$ and regroup: $$(h_1 k_1)(h_2 k_2) = (h_1 h_2)\bigl(h_2^{-1} k_1 h_2\bigr) k_2.$$ <2>3. By Step 1.2, $h_2^{-1} k_1 h_2 \in K$, and $K$ is closed, so $\bigl(h_2^{-1} k_1 h_2\bigr) k_2 \in K$.
<2>4. Since $h_1 h_2 \in H$, the product lies in $HK$.

<1>4. $HK$ is closed under inverses: *Proof:* <2>1. Let $hk \in HK$.
Then $(hk)^{-1} = k^{-1} h^{-1} = h^{-1}\bigl(h k^{-1} h^{-1}\bigr)$.
<2>2. By Step 1.2, $h k^{-1} h^{-1} \in K$, and $h^{-1} \in H$, so $(hk)^{-1} \in HK$.

<1>5. Conclusion of the positive part: *Proof:* <2>1. $HK$ is a nonempty subset of $G$ closed under products and inverses, hence $HK \le G$ by the subgroup criterion.

<1>6. The hypothesis is necessary: a counterexample in $S_3$: *Proof:* <2>1. Take $G = S_3$, $H = \langle (1\,2) \rangle$, and $K = \langle (1\,3) \rangle$, both of order $2$.
<2>2. $H \cap K = \{1\}$, so the product set has $$|HK| = \frac{|H|\,|K|}{|H \cap K|} = \frac{2 \cdot 2}{1} = 4.$$ <2>3. By Lagrange's theorem every subgroup of $S_3$ has order dividing $|S_3| = 6$, and $4 \nmid 6$.
<2>4. Therefore $HK$ is not a subgroup of $S_3$.
<2>5. Consistently with the hypothesis failing: $K$ has index $3$ in $S_3$ and is not normal, and $N_{S_3}(K) = K$ because $K$ is its own normalizer among the order-$2$ subgroups; since $(1\,2) \notin K$, we have $H \not\le N_G(K)$.

<1>7. Conclusion: If $H \le N_G(K)$ then $HK \le G$, and the example $H = \langle (1\,2)\rangle$, $K = \langle (1\,3)\rangle$ in $S_3$ shows the hypothesis cannot be dropped.
Q.E.D.
:::
