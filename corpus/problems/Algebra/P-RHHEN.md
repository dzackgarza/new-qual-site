---
schema: qual/card@1
id: P-RHHEN
kind: problem
title: Hilbert's Nullstellensatz
classification:
  areas:
  - algebra
  topics:
  - Geometry
  - Maximal Ideals
  - Commutative Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
(1) State the **Weak** and **Strong** forms of **Hilbert's Nullstellensatz** over an algebraically closed field $k$.
(2) State the geometric bijection between radical ideals in $k[x_1, \dots, x_n]$ and algebraic sets in $\mathbb{A}^n(k)$.
(3) Sketch the proof of the Nullstellensatz (Zariski's Lemma / Noether Normalization, and the Rabinowitsch trick).
:::

::: solution
**Goal:** Formulate Hilbert's Nullstellensatz and sketch its proof via Zariski's Lemma and the Rabinowitsch trick.

<1>1. Statements of Hilbert's Nullstellensatz:
    *Proof:*
    <2>1. Let $k$ be an **algebraically closed field**, and let $R = k[x_1, x_2, \dots, x_n]$ be the polynomial ring in $n$ variables.
    <2>2. **Weak Nullstellensatz (Maximal Ideals):**
        Every maximal ideal $\mathfrak{m} \subset k[x_1, \dots, x_n]$ is of the form:
        $$\mathfrak{m} = (x_1 - a_1, x_2 - a_2, \dots, x_n - a_n) \quad \text{for some point } (a_1, \dots, a_n) \in k^n = \mathbb{A}^n(k).$$
    <2>3. **Weak Nullstellensatz (Geometric Form):**
        If $I \subsetneq k[x_1, \dots, x_n]$ is a proper ideal ($1 \notin I$), then the algebraic zero set is non-empty:
        $$V(I) = \{a \in k^n \mid f(a) = 0 \ \forall f \in I\} \ne \varnothing.$$
    <2>4. **Strong Nullstellensatz (Ideal of the Variety):**
        For any ideal $I \subseteq k[x_1, \dots, x_n]$, the ideal of all polynomials vanishing on $V(I)$ is precisely the **radical** of $I$:
        $$I(V(I)) = \sqrt{I} \coloneqq \{f \in R \mid \exists m \ge 1 \text{ with } f^m \in I\}.$$

<1>2. Galois Connection and Ideal-Variety Correspondence:
    *Proof:*
    <2>1. There is an inclusion-reversing bijection:
        $$\left\{ \text{Radical ideals } I \subseteq k[x_1, \dots, x_n] \right\} \xleftrightarrow{\quad 1:1 \quad} \left\{ \text{Algebraic subsets } X \subseteq \mathbb{A}^n(k) \right\}$$
        given by $I \mapsto V(I)$ and $X \mapsto I(X)$.
    <2>2. Under this correspondence, maximal ideals correspond to points, and prime ideals correspond to **irreducible algebraic varieties**.

<1>3. Proof Sketch:
    *Proof:*
    <2>1. **Step A: Zariski's Lemma (Weak Nullstellensatz):**
        - *Lemma:* If a field extension $K/k$ is finitely generated as a $k$-algebra, then $K/k$ is an **algebraic extension** of fields. (Proved via Noether Normalization or Zariski's lemma on integral domains).
        - For a maximal ideal $\mathfrak{m}$, the residue field $K = k[x_1, \dots, x_n]/\mathfrak{m}$ is a finitely generated $k$-algebra.
        - By Zariski's Lemma, $K/k$ is algebraic. Since $k$ is algebraically closed, $K = k$.
        - Let $a_i = x_i \pmod{\mathfrak{m}} \in k$. Then $x_i - a_i \in \mathfrak{m}$, forcing $\mathfrak{m} = (x_1 - a_1, \dots, x_n - a_n)$.
    <2>2. **Step B: Rabinowitsch Trick (Strong from Weak):**
        - Let $g \in I(V(I))$ vanish everywhere on $V(I) \subset k^n$.
        - Introduce an auxiliary variable $y$, and consider the polynomial ring $k[x_1, \dots, x_n, y]$.
        - Consider the ideal $J = (I, 1 - y g(x)) \subseteq k[x_1, \dots, x_n, y]$.
        - A point $(a, b) \in k^{n+1}$ is in $V(J) \iff a \in V(I)$ and $1 - b g(a) = 0$.
        - But since $g \in I(V(I))$, $a \in V(I) \implies g(a) = 0$, so $1 - b \cdot 0 = 1 = 0$, which has no solutions.
        - Thus $V(J) = \varnothing$.
        - By the Weak Nullstellensatz, $J = k[x_1, \dots, x_n, y]$, so $1 \in J$:
          $$1 = \sum_{i=1}^m h_i(x, y) f_i(x) + h_0(x, y) (1 - y g(x)) \quad (f_i \in I).$$
        - Substitute $y = 1/g(x)$ in the function field $k(x_1, \dots, x_n)$:
          $$1 = \sum_{i=1}^m h_i(x, 1/g(x)) f_i(x) + 0.$$
        - Clearing denominators by multiplying by $g(x)^N$ for large $N$:
          $$g(x)^N = \sum_{i=1}^m \tilde{h}_i(x) f_i(x) \in I.$$
        - Thus $g \in \sqrt{I}$, proving $I(V(I)) = \sqrt{I}$.

<1>4. Conclusion:
    The Nullstellensatz establishes $I(V(I)) = \sqrt{I}$ via Zariski's Lemma and the Rabinowitsch trick. Q.E.D.
:::
