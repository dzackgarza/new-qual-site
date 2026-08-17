---
schema: qual/card@1
id: P-AMD-CTH7TM34
kind: problem
title: Let $(X, \mathcal B, \mu)$ be a measure space with $\mu(X) = 1$ and…
classification:
  areas:
  - real-analysis
  topics:
  - borel-cantelli
  - measure-theory
relations: []
review: draft
solved: true
---

::: {.problem}
Let $(X, \mathcal B, \mu)$ be a measure space with $\mu(X) = 1$ and $\{B_n\}_{n=1}^\infty$ be a sequence of $\mathcal B$-measurable subsets of $X$, and
$$
B \definedas \theset{x\in X \suchthat x\in B_n \text{ for infinitely many } n}.
$$

a. Argue that $B$ is also a $\mathcal{B} \dash$measurable subset of $X$.

b. Prove that if $\sum_{n=1}^\infty \mu(B_n) < \infty$ then $\mu(B)= 0$.

c. Prove that if  $\sum_{n=1}^\infty \mu(B_n) = \infty$ **and** the sequence of set complements $\theset{B_n^c}_{n=1}^\infty$ satisfies
$$
\mu\left(\bigcap_{n=k}^{K} B_{n}^{c}\right)=\prod_{n=k}^{K}\left(1-\mu\left(B_{n}\right)\right)
$$
for all positive integers $k$ and $K$ with $k < K$, then $\mu(B) = 1$.

> Hint: Use the fact that $1 - x \leq e^{-x}$ for all $x$.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Let $(X, \mathcal B, \mu)$ be a probability space ($\mu(X)=1$) and $\{B_n\}_{n=1}^\infty \subseteq \mathcal B$. Let $B = \{x\in X : x\in B_n \text{ for infinitely many } n\}$. Prove:
(a) $B \in \mathcal B$;
(b) If $\sum_{n=1}^\infty \mu(B_n) < \infty$, then $\mu(B) = 0$ (Borel-Cantelli Lemma I);
(c) If $\sum_{n=1}^\infty \mu(B_n) = \infty$ and $\mu(\bigcap_{n=k}^K B_n^c) = \prod_{n=k}^K (1 - \mu(B_n))$ for all $1 \leq k < K$, then $\mu(B) = 1$ (Borel-Cantelli Lemma II).

<1>1. **Part (a): $B \in \mathcal B$.**
  <2>1. $B = \bigcap_{k=1}^\infty \bigcup_{n=k}^\infty B_n = \limsup_{n\to\infty} B_n$.
    Proof: By definition, $x \in B$ if and only if for every positive integer $k$, there exists $n \geq k$ such that $x \in B_n$. This condition is equivalent to $x \in \bigcup_{n=k}^\infty B_n$ for every $k \geq 1$, which is precisely $x \in \bigcap_{k=1}^\infty \bigcup_{n=k}^\infty B_n$.
  <2>2. $B \in \mathcal B$.
    Proof: Since $\mathcal B$ is a $\sigma$-algebra and each $B_n \in \mathcal B$, the countable union $\bigcup_{n=k}^\infty B_n \in \mathcal B$ for each $k \geq 1$. Furthermore, the countable intersection of measurable sets $\bigcap_{k=1}^\infty \left(\bigcup_{n=k}^\infty B_n\right)$ belongs to $\mathcal B$. Thus $B \in \mathcal B$.

<1>2. **Part (b): If $\sum_{n=1}^\infty \mu(B_n) < \infty$, then $\mu(B) = 0$.**
  <2>1. For every $k \geq 1$, $B \subseteq \bigcup_{n=k}^\infty B_n$.
    Proof: Since $B = \bigcap_{j=1}^\infty \bigcup_{n=j}^\infty B_n$, it is an intersection over all $j \geq 1$, hence $B \subseteq \bigcup_{n=k}^\infty B_n$ for each specific index $k$.
  <2>2. For every $k \geq 1$, $\mu(B) \leq \sum_{n=k}^\infty \mu(B_n)$.
    Proof: By monotonicity and countable subadditivity of the measure $\mu$,
    $$
    \mu(B) \leq \mu\left(\bigcup_{n=k}^\infty B_n\right) \leq \sum_{n=k}^\infty \mu(B_n).
    $$
  <2>3. $\mu(B) = 0$.
    Proof: By hypothesis, the infinite series $\sum_{n=1}^\infty \mu(B_n)$ converges in $\mathbb{R}$. Therefore, its tail sum satisfies $\lim_{k\to\infty} \sum_{n=k}^\infty \mu(B_n) = 0$. Taking the limit as $k \to \infty$ in $\mu(B) \leq \sum_{n=k}^\infty \mu(B_n)$ yields $0 \leq \mu(B) \leq 0$, hence $\mu(B) = 0$.

<1>3. **Part (c): Under the independence condition and $\sum_{n=1}^\infty \mu(B_n) = \infty$, $\mu(B) = 1$.**
  <2>1. The complement of $B$ is $B^c = \bigcup_{k=1}^\infty \bigcap_{n=k}^\infty B_n^c$.
    Proof: By De Morgan's laws:
    $$
    B^c = \left(\bigcap_{k=1}^\infty \bigcup_{n=k}^\infty B_n\right)^c = \bigcup_{k=1}^\infty \left(\bigcup_{n=k}^\infty B_n\right)^c = \bigcup_{k=1}^\infty \bigcap_{n=k}^\infty B_n^c.
    $$
  <2>2. For each fixed $k \geq 1$, $\mu\left(\bigcap_{n=k}^\infty B_n^c\right) = 0$.
    <3>1. The sequence of sets $A_K \definedas \bigcap_{n=k}^K B_n^c$ is decreasing in $K$ for $K \geq k$, with $\bigcap_{K=k}^\infty A_K = \bigcap_{n=k}^\infty B_n^c$.
      Proof: For $K_1 \leq K_2$, $\bigcap_{n=k}^{K_2} B_n^c \subseteq \bigcap_{n=k}^{K_1} B_n^c$, and the countable intersection over all $K \geq k$ yields $\bigcap_{n=k}^\infty B_n^c$.
    <3>2. $\mu\left(\bigcap_{n=k}^\infty B_n^c\right) = \lim_{K\to\infty} \mu\left(\bigcap_{n=k}^K B_n^c\right)$.
      Proof: Since $\mu(X) = 1 < \infty$, the measure $\mu$ is finite. By continuity of measure from above (downward continuity), $\mu\left(\bigcap_{K=k}^\infty A_K\right) = \lim_{K\to\infty} \mu(A_K)$.
    <3>3. For every $K > k$, $\mu\left(\bigcap_{n=k}^K B_n^c\right) \leq \exp\left(-\sum_{n=k}^K \mu(B_n)\right)$.
      Proof: By the given hypothesis, $\mu\left(\bigcap_{n=k}^K B_n^c\right) = \prod_{n=k}^K (1 - \mu(B_n))$. Using the inequality $1 - x \leq e^{-x}$ (valid for all $x \in \mathbb{R}$, and here $\mu(B_n) \in [0, 1]$), we obtain
      $$
      \prod_{n=k}^K (1 - \mu(B_n)) \leq \prod_{n=k}^K e^{-\mu(B_n)} = \exp\left(-\sum_{n=k}^K \mu(B_n)\right).
      $$
    <3>4. $\lim_{K\to\infty} \exp\left(-\sum_{n=k}^K \mu(B_n)\right) = 0$.
      Proof: Since $\sum_{n=1}^\infty \mu(B_n) = \infty$ and the initial sum $\sum_{n=1}^{k-1} \mu(B_n)$ is finite, we have $\sum_{n=k}^\infty \mu(B_n) = \infty$, so $\lim_{K\to\infty} \sum_{n=k}^K \mu(B_n) = \infty$. Because $\lim_{t\to\infty} e^{-t} = 0$, the claim follows.
    <3>5. $\mu\left(\bigcap_{n=k}^\infty B_n^c\right) = 0$.
      Proof: By <3>2, <3>3, and <3>4, $0 \leq \mu\left(\bigcap_{n=k}^\infty B_n^c\right) \leq \lim_{K\to\infty} \exp\left(-\sum_{n=k}^K \mu(B_n)\right) = 0$.
  <2>3. $\mu(B^c) = 0$.
    Proof: By <2>1, $B^c = \bigcup_{k=1}^\infty \left(\bigcap_{n=k}^\infty B_n^c\right)$. By countable subadditivity of $\mu$:
    $$
    \mu(B^c) \leq \sum_{k=1}^\infty \mu\left(\bigcap_{n=k}^\infty B_n^c\right) = \sum_{k=1}^\infty 0 = 0.
    $$
    Since $\mu(B^c) \geq 0$, $\mu(B^c) = 0$.
  <2>4. $\mu(B) = 1$.
    Proof: Since $\mu(X) = 1$ and $B \in \mathcal B$, we have $\mu(B) = \mu(X) - \mu(B^c) = 1 - 0 = 1$.

<1>4. **Conclusion.**
  Claims (a), (b), and (c) are all verified. Q.E.D.
:::
