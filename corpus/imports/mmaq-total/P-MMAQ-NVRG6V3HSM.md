---
schema: qual/card@1
id: P-MMAQ-NVRG6V3HSM
kind: problem
title: Let $(X, \mathcal B, mu)$ be a measure space with $mu(X) = 1$ and…
classification:
  areas:
  - real-analysis
  topics:
  - measure-theory
  - borel-cantelli
relations: []
review: draft
solved: true
---

::: problem
Let $(X, \mathcal B, mu)$ be a measure space with $mu(X) = 1$ and $\{B_n\}_{n=1}^\infty$ be a sequence of $\mathcal B$-measurable subsets of $X$, and
$$
B \definedas \theset{x\in X \suchthat x\in B_n \text{ for infinitely many } n}.
$$

a.  Argue that $B$ is also a $\mathcal{B} \dash$measurable subset of $X$.

b.  Prove that if $\sum_{n=1}^\infty \mu(B_n) < \infty$ then $\mu(B)= 0$.

c.  Prove that if $\sum_{n=1}^\infty \mu(B_n) = \infty$ **and** the sequence of set complements $\theset{B_n^c}_{n=1}^\infty$ satisfies
    $$
    \mu\left(\bigcap_{n=k}^{K} B_{n}^{c}\right)=\prod_{n=k}^{K}\left(1-\mu\left(B_{n}\right)\right)
    $$
    for all positive integers $k$ and $K$ with $k < K$, then $mu(B) = 1$.

> Hint: Use the fact that $1 - x \leq e^{-x}$ for all $x$.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** With $\mu(X) = 1$ and $B = \limsup_n B_n$: (a) show $B$ is measurable; (b) $\sum_n \mu(B_n) < \infty \implies \mu(B) = 0$; (c) $\sum_n \mu(B_n) = \infty$ and the stated independence-like product identity $\implies \mu(B) = 1$.

<1>1. Proof of (a): $B$ is measurable.
    <2>1. $B = \bigcap_{k=1}^\infty \bigcup_{n=k}^\infty B_n$.
        Proof: $x$ belongs to infinitely many $B_n$ iff for every $k$ there is some $n \geq k$ with $x \in B_n$, i.e. $x \in \bigcup_{n=k}^\infty B_n$ for all $k$.
    <2>2. Each $\bigcup_{n=k}^\infty B_n$ is measurable, and so is their countable intersection.
        Proof: A countable union of measurable sets is measurable, and a countable intersection of measurable sets is measurable; $\mathcal B$ is a $\sigma$-algebra.
    <2>3. Q.E.D.
        Proof: By <2>1 and <2>2.

<1>2. Proof of (b): if $\sum_n \mu(B_n) < \infty$, then $\mu(B) = 0$.
    <2>1. For each $k$, $B \subseteq \bigcup_{n=k}^\infty B_n$.
        Proof: If $x \in B$, then $x \in B_n$ for infinitely many $n$, in particular for some $n \geq k$.
    <2>2. $\mu(B) \leq \mu\left(\bigcup_{n=k}^\infty B_n\right) \leq \sum_{n=k}^\infty \mu(B_n)$.
        Proof: Monotonicity of $\mu$ (from <2>1), then countable subadditivity.
    <2>3. $\sum_{n=k}^\infty \mu(B_n) \to 0$ as $k \to \infty$.
        Proof: The tail of the convergent series $\sum_n \mu(B_n)$ tends to $0$.
    <2>4. Hence $\mu(B) = 0$.
        Proof: From <2>2, $\mu(B) \leq \sum_{n=k}^\infty \mu(B_n)$ for every $k$; let $k \to \infty$ and use <2>3.
    <2>5. Q.E.D.
        Proof: This proves (b).

<1>3. Proof of (c): if $\sum_n \mu(B_n) = \infty$ and $\mu\left(\bigcap_{n=k}^K B_n^c\right) = \prod_{n=k}^K (1 - \mu(B_n))$ for all $k < K$, then $\mu(B) = 1$.
    <2>1. $B^c = \bigcup_{k=1}^\infty \bigcap_{n=k}^\infty B_n^c$.
        Proof: Complement of $\bigcap_k \bigcup_{n \geq k} B_n$ is $\bigcup_k \bigcap_{n \geq k} B_n^c$ (de Morgan's laws).
    <2>2. For each $k$, $\bigcap_{n=k}^\infty B_n^c \subseteq \bigcap_{n=k}^K B_n^c$ for every $K > k$, so $\mu\left(\bigcap_{n=k}^\infty B_n^c\right) \leq \prod_{n=k}^K (1 - \mu(B_n))$ for every $K > k$.
        Proof: Monotonicity plus the hypothesis applied to the finite intersection.
    <2>3. $\prod_{n=k}^K (1 - \mu(B_n)) \leq \exp\left(-\sum_{n=k}^K \mu(B_n)\right)$.
        Proof: The hint: $1 - x \leq e^{-x}$ for all $x$, applied to each factor $x = \mu(B_n)$; all factors are in $[0,1]$.
    <2>4. For fixed $k$, $\exp\left(-\sum_{n=k}^K \mu(B_n)\right) \to 0$ as $K \to \infty$.
        Proof: $\sum_{n=k}^\infty \mu(B_n) = \infty$ since $\sum_n \mu(B_n) = \infty$ (removing the first $k-1$ terms does not change divergence).
    <2>5. Hence $\mu\left(\bigcap_{n=k}^\infty B_n^c\right) = 0$ for every $k$.
        Proof: From <2>2 the measure is $\leq$ the product for all $K$, and by <2>3, <2>4 the product tends to $0$; a nonnegative number $\leq 0$ is $0$.
    <2>6. $\mu(B^c) = 0$.
        Proof: $B^c = \bigcup_k C_k$ with $C_k \definedas \bigcap_{n=k}^\infty B_n^c$; the sets $C_k$ increase with $k$, so by continuity from below, $\mu(B^c) = \lim_k \mu(C_k) = 0$ by <2>5. (Alternatively, subadditivity over the union.)
    <2>7. Hence $\mu(B) = 1$.
        Proof: $\mu(B) = \mu(X) - \mu(B^c) = 1 - 0$, since $\mu(X) = 1$.
    <2>8. Q.E.D.
        Proof: This proves (c).
:::
