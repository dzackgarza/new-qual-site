---
schema: qual/card@1
id: P-AMD-WFUONDWI
kind: problem
title: Bessel's inequality and the Riesz–Fischer theorem
classification:
  areas:
  - real-analysis
  topics:
  - hilbert-spaces
  - l2
relations: []
review: draft
solved: true
---

::: {.problem}
Let $\{u_n\}_{n=1}^∞$ be an orthonormal sequence in a Hilbert space $\mathcal{H}$.

a. Prove that for every $x ∈ \mathcal H$ one has 
$$
\displaystyle\sum_{n=1}^{\infty}\left|\left\langle x, u_{n}\right\rangle\right|^{2} \leq\|x\|^{2}
$$

b. Prove that for any sequence $\{a_n\}_{n=1}^\infty \in \ell^2(\NN)$ there exists an element $x\in\mathcal H$ such that 
  $$
  a_n = \inner{x}{u_n} \text{ for all } n\in \NN
  $$
  and
  $$
  \norm{x}^2 = \sum_{n=1}^{\infty}\left|\left\langle x, u_{n}\right\rangle\right|^{2}
  $$
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Let $\{u_n\}_{n=1}^\infty$ be an orthonormal sequence in a Hilbert space $\mathcal H$. Prove:
(a) Bessel's inequality: $\sum_{n=1}^\infty |\langle x, u_n \rangle|^2 \leq \|x\|^2$ for all $x \in \mathcal H$;
(b) Riesz-Fischer Theorem: For any $\{a_n\}_{n=1}^\infty \in \ell^2(\NN)$, there exists $x \in \mathcal H$ such that $\langle x, u_n \rangle = a_n$ for all $n \in \NN$ and $\|x\|^2 = \sum_{n=1}^\infty |a_n|^2$.

<1>1. **Part (a): Bessel's Inequality $\sum_{n=1}^\infty |\langle x, u_n \rangle|^2 \leq \|x\|^2$.**
  <2>1. For any $N \in \NN$, define $x_N = \sum_{n=1}^N \langle x, u_n \rangle u_n$.
  <2>2. $\langle x - x_N, u_k \rangle = 0$ for all $k \in \{1, \dots, N\}$.
    Proof: By linearity of the inner product and orthonormality $\langle u_n, u_k \rangle = \delta_{nk}$:
    $$
    \langle x_N, u_k \rangle = \left\langle \sum_{n=1}^N \langle x, u_n \rangle u_n, u_k \right\rangle = \sum_{n=1}^N \langle x, u_n \rangle \langle u_n, u_k \rangle = \langle x, u_k \rangle.
    $$
    Thus $\langle x - x_N, u_k \rangle = \langle x, u_k \rangle - \langle x_N, u_k \rangle = 0$.
  <2>3. $\langle x - x_N, x_N \rangle = 0$.
    Proof: Since $x_N$ is a linear combination of $\{u_1, \dots, u_N\}$ and $x - x_N$ is orthogonal to each $u_k$ by <2>2, $\langle x - x_N, x_N \rangle = \sum_{k=1}^N \overline{\langle x, u_k \rangle} \langle x - x_N, u_k \rangle = 0$.
  <2>4. $\|x\|^2 = \|x - x_N\|^2 + \|x_N\|^2$.
    Proof: By the Pythagorean Theorem for inner product spaces, since $\langle x - x_N, x_N \rangle = 0$:
    $$
    \|x\|^2 = \|(x - x_N) + x_N\|^2 = \|x - x_N\|^2 + \|x_N\|^2 + 2\operatorname{Re}\langle x - x_N, x_N \rangle = \|x - x_N\|^2 + \|x_N\|^2.
    $$
  <2>5. $\|x_N\|^2 = \sum_{n=1}^N |\langle x, u_n \rangle|^2$.
    Proof: By orthonormality of $\{u_n\}$:
    $$
    \|x_N\|^2 = \left\langle \sum_{n=1}^N \langle x, u_n \rangle u_n, \sum_{m=1}^N \langle x, u_m \rangle u_m \right\rangle = \sum_{n=1}^N \sum_{m=1}^N \langle x, u_n \rangle \overline{\langle x, u_m \rangle} \langle u_n, u_m \rangle = \sum_{n=1}^N |\langle x, u_n \rangle|^2.
    $$
  <2>6. For all $N \in \NN$, $\sum_{n=1}^N |\langle x, u_n \rangle|^2 \leq \|x\|^2$.
    Proof: From <2>4 and <2>5, $\|x\|^2 - \sum_{n=1}^N |\langle x, u_n \rangle|^2 = \|x - x_N\|^2 \geq 0$.
  <2>7. $\sum_{n=1}^\infty |\langle x, u_n \rangle|^2 \leq \|x\|^2$.
    Proof: The partial sums are monotonically increasing and bounded above by $\|x\|^2$. Taking $N \to \infty$ yields the result.

<1>2. **Part (b): Existence of $x \in \mathcal H$ for given $\{a_n\} \in \ell^2(\NN)$.**
  <2>1. Define the partial sums $S_N = \sum_{n=1}^N a_n u_n$ for $N \in \NN$.
  <2>2. $\{S_N\}_{N=1}^\infty$ is a Cauchy sequence in $\mathcal H$.
    Proof: For $M > N \geq 1$:
    $$
    \|S_M - S_N\|^2 = \left\| \sum_{n=N+1}^M a_n u_n \right\|^2 = \sum_{n=N+1}^M |a_n|^2.
    $$
    Since $\{a_n\} \in \ell^2(\NN)$, the series $\sum_{n=1}^\infty |a_n|^2$ converges in $\mathbb R$, so its tail sum $\sum_{n=N+1}^M |a_n|^2 \to 0$ as $N, M \to \infty$. Thus $\{S_N\}$ is Cauchy.
  <2>3. There exists $x \in \mathcal H$ such that $S_N \to x$ in $\mathcal H$ as $N \to \infty$.
    Proof: $\mathcal H$ is a Hilbert space, hence complete. Every Cauchy sequence converges to a limit $x \in \mathcal H$.
  <2>4. $\langle x, u_k \rangle = a_k$ for all $k \in \NN$.
    Proof: By continuity of the inner product on $\mathcal H$:
    $$
    \langle x, u_k \rangle = \left\langle \lim_{N\to\infty} S_N, u_k \right\rangle = \lim_{N\to\infty} \langle S_N, u_k \rangle.
    $$
    For any $N \geq k$, $\langle S_N, u_k \rangle = \left\langle \sum_{n=1}^N a_n u_n, u_k \right\rangle = \sum_{n=1}^N a_n \langle u_n, u_k \rangle = a_k$.
    Therefore, $\lim_{N\to\infty} \langle S_N, u_k \rangle = a_k$, which gives $\langle x, u_k \rangle = a_k$.
  <2>5. $\|x\|^2 = \sum_{n=1}^\infty |\langle x, u_n \rangle|^2 = \sum_{n=1}^\infty |a_n|^2$.
    Proof: By continuity of the norm on $\mathcal H$:
    $$
    \|x\|^2 = \lim_{N\to\infty} \|S_N\|^2 = \lim_{N\to\infty} \sum_{n=1}^N |a_n|^2 = \sum_{n=1}^\infty |a_n|^2.
    $$
    Since $a_n = \langle x, u_n \rangle$ by <2>4, this is precisely $\|x\|^2 = \sum_{n=1}^\infty |\langle x, u_n \rangle|^2$.

<1>3. **Conclusion.**
  Both Part (a) and Part (b) are proved rigorously. Q.E.D.
:::
