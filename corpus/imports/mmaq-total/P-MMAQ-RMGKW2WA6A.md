---
schema: qual/card@1
id: P-MMAQ-RMGKW2WA6A
kind: problem
title: Let $\{u_n\}_{n=1}^\infty$ be an orthonormal sequence in a Hilbert…
classification:
  areas:
  - real-analysis
  topics:
  - functional-analysis
  - hilbert-spaces
  - norms
relations: []
review: draft
---

::: problem
Let $\{u_n\}_{n=1}^\infty$ be an orthonormal sequence in a Hilbert space $\mathcal{H}$.

a.  Prove that for every $x \in \mathcal H$ one has
    $$
    \displaystyle\sum_{n=1}^{\infty}\left|\left\langle x, u_{n}\right\rangle\right|^{2} \leq\|x\|^{2}
    $$

b.  Prove that for any sequence $\{a_n\}_{n=1}^\infty \in \ell^2(\NN)$ there exists an element $x\in\mathcal H$ such that
    $$
    a_n = \inner{x}{u_n} \text{ for all } n\in \NN
    $$
    and
    $$
    \norm{x}^2 = \sum_{n=1}^{\infty}\left|\left\langle x, u_{n}\right\rangle\right|^{2}
    $$
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** For an orthonormal sequence $\{u_n\}$ in a Hilbert space $\mathcal H$: (a) prove Bessel's inequality $\sum_n |\inner{x}{u_n}|^2 \leq \norm{x}^2$; (b) for every $\{a_n\} \in \ell^2(\NN)$, construct $x \in \mathcal H$ with $\inner{x}{u_n} = a_n$ for all $n$ and $\norm{x}^2 = \sum_n |a_n|^2$.

<1>1. Proof of (a): Bessel's inequality.
    <2>1. For each finite $N$, consider $y_N \definedas x - \sum_{n=1}^{N} \inner{x}{u_n} u_n$; then $y_N \perp u_m$ for all $m \leq N$.
        Proof: $\inner{y_N}{u_m} = \inner{x}{u_m} - \sum_{n=1}^N \inner{x}{u_n} \inner{u_n}{u_m} = \inner{x}{u_m} - \inner{x}{u_m} = 0$, using $\inner{u_n}{u_m} = \delta_{nm}$.
    <2>2. Pythagoras: $\norm{x}^2 = \norm{y_N}^2 + \sum_{n=1}^N |\inner{x}{u_n}|^2 \geq \sum_{n=1}^N |\inner{x}{u_n}|^2$.
        Proof: $x = y_N + \sum_{n \leq N} \inner{x}{u_n} u_n$ with $y_N$ orthogonal to the (mutually orthogonal) $u_n$'s; Pythagoras gives the identity, and $\norm{y_N}^2 \geq 0$.
    <2>3. The partial sums $\sum_{n=1}^N |\inner{x}{u_n}|^2$ are bounded above by $\norm{x}^2$, hence the series converges and $\sum_{n=1}^\infty |\inner{x}{u_n}|^2 \leq \norm{x}^2$.
        Proof: By <2>2, the monotone sequence of partial sums is bounded by $\norm{x}^2$; its limit is the sum of the series, bounded by $\norm{x}^2$.
    <2>4. Q.E.D.
        Proof: This proves (a).

<1>2. Proof of (b): the Riesz–Fischer construction.
    <2>1. The series $\sum_{n=1}^\infty a_n u_n$ converges in $\mathcal H$.
        Proof: Since $\{a_n\} \in \ell^2$, the partial sums $S_N = \sum_{n \leq N} a_n u_n$ form a Cauchy sequence: for $M > N$, $\norm{S_M - S_N}^2 = \sum_{n=N+1}^{M} |a_n|^2 \to 0$ as $N \to \infty$ (orthonormality, Pythagoras); $\mathcal H$ is complete.
    <2>2. Define $x \definedas \sum_{n=1}^\infty a_n u_n$; then $\inner{x}{u_m} = a_m$ for every $m$.
        Proof: By continuity of the inner product, $\inner{x}{u_m} = \lim_N \sum_{n=1}^N a_n \inner{u_n}{u_m} = a_m$, since $\inner{u_n}{u_m} = \delta_{nm}$.
    <2>3. $\norm{x}^2 = \sum_{n=1}^\infty |a_n|^2$.
        Proof: By continuity of the norm, $\norm{x}^2 = \lim_N \norm{S_N}^2 = \lim_N \sum_{n=1}^N |a_n|^2 = \sum_n |a_n|^2$ (Pythagoras for the mutually orthogonal $a_n u_n$'s).
    <2>4. Q.E.D.
        Proof: By <2>2 and <2>3, $x$ has the two required properties.
:::
