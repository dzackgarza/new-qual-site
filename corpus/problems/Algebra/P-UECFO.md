---
schema: qual/card@1
id: P-UECFO
kind: problem
title: Every irreducible representation of $G$ appears in a tensor power of a faithful
  finite-dimensional representation
classification:
  areas:
  - algebra
  topics:
  - Representation Theory
  - Tensor Products
  - Semisimplicity
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-30
---

::: problem
Let $(\pi, V)$ be a faithful finite-dimensional representation of a finite group $G$ over $\mathbb{C}$.
Show that, given any irreducible representation $W$ of $G$, the $n$-th tensor power $V^{\otimes n}$ (or tensor algebra $T(V \oplus V^*)$) contains an isomorphic copy of $W$ for some integer $n \ge 0$.
:::

::: solution
**Goal:** Prove Burnside's Theorem on generation of representations: every irreducible character $\chi$ of a finite group $G$ appears as a constituent of $\chi_V^n$ for some $n \ge 0$, when $\chi_V$ is faithful (or in $\chi_{V \oplus V^*}^n$).

<1>1. Character formulation of subrepresentation containment:
    *Proof:*
    <2>1. By character theory for finite groups over $\mathbb{C}$, an irreducible representation $W$ with character $\chi_W$ is contained in $V^{\otimes n}$ (which has character $\chi_V^n$) if and only if the inner product of characters is strictly positive:
        $$\langle \chi_W, \chi_V^n \rangle = \frac{1}{|G|} \sum_{g \in G} \chi_V(g)^n \overline{\chi_W(g)} > 0.$$

<1>2. Properties of the faithful character $\chi_V$:
    *Proof:*
    <2>1. Let $d = \dim V = \chi_V(e)$.
    <2>2. For any $g \in G$, $\pi(g)$ is diagonalizable with eigenvalues that are roots of unity $\lambda_1, \dots, \lambda_d$.
    <2>3. By the triangle inequality:
        $$|\chi_V(g)| = |\lambda_1 + \cdots + \lambda_d| \le |\lambda_1| + \cdots + |\lambda_d| = d = \chi_V(e).$$
    <2>4. Equality $|\chi_V(g)| = d$ holds if and only if all $\lambda_j$ are equal: $\lambda_1 = \cdots = \lambda_d = \zeta$, so $\pi(g) = \zeta I$.
    <2>5. Furthermore, $\chi_V(g) = d$ (without absolute values) holds if and only if $\lambda_1 = \cdots = \lambda_d = 1$, so $\pi(g) = I$.
    <2>6. Because $(\pi, V)$ is a **faithful** representation, $\pi(g) = I \iff g = e$.
    <2>7. Thus $\chi_V(g) = d$ if and only if $g = e$.
    <2>8. In particular, for all $g \ne e$, $|\chi_V(g)| \le d$, and if we consider the self-dual character $\psi(g) = \chi_V(g) + \overline{\chi_V(g)} + 1 = \chi_{V \oplus V^* \oplus \mathbb{C}}(g)$, then $\psi(e) = 2d + 1 > 0$ and $\operatorname{Re}(\psi(g)) < \psi(e)$ for all $g \ne e$.

<1>3. Asymptotic domination of the identity term as $n \to \infty$:
    *Proof:*
    <2>1. Consider the sum $S(n) = \sum_{g \in G} \psi(g)^n \overline{\chi_W(g)}$ where $\psi(g) = \chi_{V \oplus V^*}(g) + 1 \ge 0$.
    <2>2. The term at $g = e$ is $\psi(e)^n \overline{\chi_W(e)} = (2d + 1)^n \dim W > 0$.
    <2>3. For every $g \ne e$, $|\psi(g)| < 2d + 1$, so:
        $$\left| \frac{\psi(g)}{\psi(e)} \right| \le r < 1 \quad \text{for some constant } r \in [0, 1).$$
    <2>4. Dividing the inner product by $(2d+1)^n$:
        $$\frac{|G|}{(2d+1)^n} \langle \chi_W, \psi^n \rangle = \dim W + \sum_{g \ne e} \left(\frac{\psi(g)}{2d+1}\right)^n \overline{\chi_W(g)}.$$
    <2>5. As $n \to \infty$, the sum $\sum_{g \ne e} \left(\frac{\psi(g)}{2d+1}\right)^n \overline{\chi_W(g)} \to 0$.
    <2>6. Since $\dim W \ge 1 > 0$, for all sufficiently large $n$, we have:
        $$\frac{|G|}{(2d+1)^n} \langle \chi_W, \psi^n \rangle > \frac{1}{2} \dim W > 0.$$
    <2>7. Therefore, $\langle \chi_W, \psi^n \rangle > 0$ for all sufficiently large $n$.

<1>4. Extracting powers of $V$:
    *Proof:*
    <2>1. Since $\psi = \chi_V + \chi_{V^*} + 1$, $\psi^n$ is a sum of characters of tensor products of the form $V^{\otimes a} \otimes (V^*)^{\otimes b}$.
    <2>2. Since $G$ is finite, $V^* \cong V^{\otimes k}$ for some $k$ (since $g^{-1} = g^{|G|-1}$, $\chi_{V^*}(g) = \chi_V(g^{-1})$).
    <2>3. Thus, every term in $\psi^n$ is a subrepresentation of $V^{\otimes N}$ for some $N$.
    <2>4. Therefore, $\langle \chi_W, \chi_V^N \rangle > 0$ for some integer $N \ge 1$.

<1>5. Conclusion:
    Every irreducible representation of $G$ is contained in $V^{\otimes N}$ (or $T(V \oplus V^*)$) for sufficiently large $N$. Q.E.D.
:::
