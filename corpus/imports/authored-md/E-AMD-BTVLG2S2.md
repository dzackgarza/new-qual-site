---
schema: qual/card@1
id: E-AMD-BTVLG2S2
kind: exercise
title: $|HK|=|H||K|/|H\cap K|$
classification:
  areas:
  - algebra
  topics:
  - Cosets and Lagrange
  - Subgroups
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-16
---

::: {.exercise}
Let $H, K \leq G$ a finite group, and without using the normalizers of $H$ or $K$, show that $\abs{HK} = \abs{H} \abs{K}/\abs{H\intersect K}$.
:::

::: {.solution}
**Goal:** Let $G$ be a finite group, and let $H, K \le G$ be subgroups.
Prove directly via fibers of the product map (without using normalizers) that $|HK| = \frac{|H| \cdot |K|}{|H \cap K|}$, where $HK = \{h k \mid h \in H, k \in K\}$.

<1>1. Definition of the product map and its image: <2>1. Define the Cartesian product $H \times K = \{(h, k) \mid h \in H, k \in K\}$.
Proof: Standard Cartesian product of two finite sets.
<2>2. The cardinality of the Cartesian product is $|H \times K| = |H| \cdot |K|$.
Proof: Basic counting principle for Cartesian products of finite sets.
<2>3. Define the multiplication map $\phi: H \times K \to HK$ by $\phi(h, k) = h k$.
Proof: Well-defined map since $HK$ is defined precisely as the set $\{h k \mid (h, k) \in H \times K\}$.
<2>4. The map $\phi$ is surjective onto $HK$.
Proof: Every element $x \in HK$ is of the form $x = h k = \phi(h, k)$ for some $(h, k) \in H \times K$.

<1>2. Fiber analysis of the map $\phi$: <2>1. Let $x \in HK$ be arbitrary, and fix a representation $(h_0, k_0) \in H \times K$ such that $\phi(h_0, k_0) = h_0 k_0 = x$.
Proof: By surjectivity of $\phi$ (<1>1.<2>4). <2>2. The fiber over $x$ is defined as $\phi^{-1}(x) = \{(h, k) \in H \times K \mid h k = x\}$.
Proof: Definition of preimage/fiber of a map.
<2>3. $(h, k) \in \phi^{-1}(x)$ if and only if there exists $d \in H \cap K$ such that $h = h_0 d$ and $k = d^{-1} k_0$.
<3>1. Direction $\impliedby$: If $d \in H \cap K$, then $h = h_0 d \in H$ (since $h_0 \in H, d \in H$) and $k = d^{-1} k_0 \in K$ (since $d \in K \implies d^{-1} \in K, k_0 \in K$). Moreover, $\phi(h, k) = h k = (h_0 d)(d^{-1} k_0) = h_0 (d d^{-1}) k_0 = h_0 k_0 = x$.
Thus $(h, k) \in \phi^{-1}(x)$.
Proof: Group axioms and subgroup closure under multiplication and inverses.
<3>2. Direction $\implies$: Let $(h, k) \in \phi^{-1}(x)$, so $h k = h_0 k_0 = x$.
Then $h_0^{-1} h = k_0 k^{-1}$.
Define $d = h_0^{-1} h = k_0 k^{-1} \in G$.
Since $h_0, h \in H$, $d = h_0^{-1} h \in H$.
Since $k_0, k \in K$, $d = k_0 k^{-1} \in K$.
Therefore, $d \in H \cap K$.
From $d = h_0^{-1} h$, we obtain $h = h_0 d$.
From $d = k_0 k^{-1}$, we take inverses $d^{-1} = k k_0^{-1}$, so $k = d^{-1} k_0$.
Proof: Algebraic manipulation in the group $G$.
<3>3. Q.E.D. Proof: Equivalence established by <3>1 and <3>2. <2>4. The map $\psi: H \cap K \to \phi^{-1}(x)$ given by $\psi(d) = (h_0 d, d^{-1} k_0)$ is a bijection.
<3>1. $\psi$ is injective: If $\psi(d_1) = \psi(d_2)$, then $(h_0 d_1, d_1^{-1} k_0) = (h_0 d_2, d_2^{-1} k_0)$, so $h_0 d_1 = h_0 d_2$, which gives $d_1 = d_2$ by left cancellation.
Proof: Left cancellation in groups.
<3>2. $\psi$ is surjective: By <2>3, every $(h, k) \in \phi^{-1}(x)$ is of the form $(h_0 d, d^{-1} k_0) = \psi(d)$ for some $d \in H \cap K$.
Proof: Direct consequence of <2>3. <3>3. Q.E.D. Proof: $\psi$ is both injective and surjective.
<2>5. Consequently, for every $x \in HK$, the size of the fiber is $|\phi^{-1}(x)| = |H \cap K|$.
Proof: Since $\psi$ is a bijection between the finite set $H \cap K$ and $\phi^{-1}(x)$.

<1>3. Counting the cardinality $|HK|$: <2>1. By the Fiber Counting Theorem (partitioning the domain $H \times K$ by the fibers of $\phi$): $$|H \times K| = \sum_{x \in HK} |\phi^{-1}(x)|.$$ Proof: The preimages $\phi^{-1}(x)$ for $x \in HK$ form a partition of the domain $H \times K$.
<2>2. Since each fiber has constant size $|\phi^{-1}(x)| = |H \cap K|$ (<1>2.<2>5): $$|H \times K| = \sum_{x \in HK} |H \cap K| = |HK| \cdot |H \cap K|.$$ Proof: Summing the constant value $|H \cap K|$ over all $|HK|$ elements of $HK$.
<2>3. Substituting $|H \times K| = |H| \cdot |K|$ (<1>1.<2>2) gives: $$|H| \cdot |K| = |HK| \cdot |H \cap K|.$$ Proof: Equating the two expressions for $|H \times K|$.
<2>4. Since $|H \cap K| \ge 1$ (as $e \in H \cap K$), dividing by $|H \cap K|$ gives: $$|HK| = \frac{|H| \cdot |K|}{|H \cap K|}.$$ Proof: Division by non-zero integer $|H \cap K|$.

<1>4. Conclusion: $|HK| = \frac{|H| |K|}{|H \cap K|}$.
Proof: By <1>3.
:::
