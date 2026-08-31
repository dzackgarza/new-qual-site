---
schema: qual/card@1
id: P-APAF25I
kind: problem
title: Finite-dimensionality of $k[x,y]/I$ for a two-point variety; must $\dim<100$?
classification:
  areas:
  - applied-algebra
  topics:
  - Gröbner Bases
  - Ideals
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: problem
Let $k$ be an algebraically closed field and let $I\subseteq k[x,y]$ be an ideal.
Suppose that the variety of $I$ is $V(I)=\{(1,0),(0,1)\}\subseteq k^2$.

(a) Prove that $k[x,y]/I$ is a finite-dimensional $k$-vector space.

(b) Do we necessarily have $\dim_k(k[x,y]/I)<100$?
:::

::: solution
**Goal:** Prove finite-dimensionality of $k[x,y]/I$ for a two-point variety in (a), and construct an ideal with $\dim_k(k[x,y]/I) \ge 100$ in (b).

<1>1. Part (a): Finite-dimensionality of $k[x,y]/I$.
    *Proof:*
    <2>1. Let $p_1 = (1, 0)$ and $p_2 = (0, 1)$ in $k^2$, with corresponding maximal ideals $\mathfrak{m}_1 = (x - 1, y)$ and $\mathfrak{m}_2 = (x, y - 1)$ in $k[x, y]$.
    <2>2. By Hilbert's Nullstellensatz, since $k$ is algebraically closed, the radical of $I$ is
    $$\sqrt{I} = I(V(I)) = I(\{p_1, p_2\}) = \mathfrak{m}_1 \cap \mathfrak{m}_2.$$
    <2>3. Since the polynomial ring $k[x, y]$ is Noetherian, the ideal $\sqrt{I}$ is finitely generated, so there exists an integer $N \ge 1$ such that $(\sqrt{I})^N \subseteq I$.
    <2>4. Note that $\mathfrak{m}_1 + \mathfrak{m}_2 = k[x, y]$ because $-(x - 1) + x = 1 \in \mathfrak{m}_1 + \mathfrak{m}_2$.
    <2>5. Comaximality implies that for any integer $N \ge 1$, the power ideals $\mathfrak{m}_1^N$ and $\mathfrak{m}_2^N$ are comaximal: $\mathfrak{m}_1^N + \mathfrak{m}_2^N = k[x, y]$.
    <2>6. Therefore $\mathfrak{m}_1^N \cap \mathfrak{m}_2^N = \mathfrak{m}_1^N \mathfrak{m}_2^N \subseteq (\mathfrak{m}_1 \cap \mathfrak{m}_2)^N \subseteq I$.
    <2>7. By the Chinese Remainder Theorem:
    $$k[x, y] / (\mathfrak{m}_1^N \cap \mathfrak{m}_2^N) \cong k[x, y] / \mathfrak{m}_1^N \oplus k[x, y] / \mathfrak{m}_2^N.$$
    <2>8. Translating coordinates to the origin shows that $k[x, y]/\mathfrak{m}_1^N \cong k[u, v]/(u, v)^N$, which has a $k$-basis given by the monomials $\{u^i v^j : i + j < N\}$ of dimension $\binom{N+1}{2} < \infty$.
    <2>9. Thus $k[x, y] / (\mathfrak{m}_1^N \cap \mathfrak{m}_2^N)$ is a finite-dimensional $k$-vector space of dimension $2 \binom{N+1}{2} = N(N+1)$.
    <2>10. Since $k[x, y]/I$ is a vector space quotient of $k[x, y] / (\mathfrak{m}_1^N \cap \mathfrak{m}_2^N)$, we have $\dim_k(k[x, y]/I) \le N(N+1) < \infty$.

<1>2. Part (b): Arbitrarily large vector space dimension.
    *Proof:*
    <2>1. For any positive integer $N \ge 1$, define the ideal $I_N = \mathfrak{m}_1^N \cap \mathfrak{m}_2^N = \mathfrak{m}_1^N \mathfrak{m}_2^N$.
    <2>2. The variety of $I_N$ is $V(I_N) = V(\mathfrak{m}_1^N) \cup V(\mathfrak{m}_2^N) = V(\mathfrak{m}_1) \cup V(\mathfrak{m}_2) = \{(1, 0), (0, 1)\} = V(I)$.
    <2>3. By step 1.9, the dimension of the quotient ring is exactly
    $$\dim_k(k[x, y]/I_N) = N(N + 1).$$
    <2>4. Setting $N = 10$ yields $\dim_k(k[x, y]/I_{10}) = 10(11) = 110 \ge 100$.
    <2>5. Therefore it is not necessarily true that $\dim_k(k[x,y]/I) < 100$.

<1>3. Conclusion:
    *Proof:*
    $k[x, y]/I$ is always finite-dimensional over $k$, but its dimension can be arbitrarily large (so $\dim_k(k[x, y]/I) < 100$ does not necessarily hold).
:::
