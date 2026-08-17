---
schema: qual/card@1
id: P-MMAQ-4WROQBJVCP
kind: problem
title: "Let $\\mathcal B$ denote the set of all Borel subsets of $\\RR$ and $\\mu : \\mathcal B \\to [0, \\infty)$ denote a\u2026"
classification:
  areas:
  - real-analysis
  topics:
  - measure-theory
relations: []
review: draft
solved: true
---

::: problem
Let $\mathcal B$ denote the set of all Borel subsets of $\RR$ and $\mu : \mathcal B \to [0, \infty)$ denote a finite Borel measure on $\RR$.

a.  Prove that if $\{F_k\}$ is a sequence of Borel sets for which $F_k \supseteq  F_{k+1}$ for all $k$, then
    $$
    \lim _{k \rightarrow \infty} \mu\left(F_{k}\right)=\mu\left(\bigcap_{k=1}^{\infty} F_{k}\right)
    $$

b.  Suppose $mu$ has the property that $mu(E) = 0$ for every $E \in \mathcal B$ with Lebesgue measure $m(E) = 0$.
    Prove that for every $\eps > 0$ there exists $\delta > 0$ so that if $E \in \mathcal B$ with $m(E) < \delta$, then $mu(E) < \eps$.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Let $\mu$ be a finite Borel measure on $\RR$. Prove:
(a) Continuity of measure from above: $F_k \supseteq F_{k+1} \implies \lim_{k\to\infty} \mu(F_k) = \mu(\bigcap_{k=1}^\infty F_k)$;
(b) Absolute continuity $(\mu \ll m) \implies \eps$-$\delta$ absolute continuity: $\forall \eps > 0, \exists \delta > 0$ such that $m(E) < \delta \implies \mu(E) < \eps$.

<1>1. **Part (a): Continuity from above for a finite measure.**
  <2>1. Let $F = \bigcap_{k=1}^\infty F_k$. Define disjoint sets $E_k = F_k \setminus F_{k+1}$ for all $k \geq 1$.
    Proof: For $j < k$, $F_{j+1} \supseteq F_k \supseteq F_k \setminus F_{k+1} = E_k$, while $E_j = F_j \setminus F_{j+1}$ is disjoint from $F_{j+1}$. Thus $E_j \cap E_k = \emptyset$ for $j \neq k$.
  <2>2. For every $n \geq 1$, $F_1 \setminus F_n = \bigcup_{k=1}^{n-1} E_k$ (disjoint union), and $F_1 \setminus F = \bigcup_{k=1}^\infty E_k$ (disjoint union).
    Proof: By telescoping differences: $F_1 \setminus F_n = \bigcup_{k=1}^{n-1} (F_k \setminus F_{k+1}) = \bigcup_{k=1}^{n-1} E_k$. Taking the countable union over all $n \geq 1$ yields $\bigcup_{k=1}^\infty E_k = \bigcup_{n=1}^\infty (F_1 \setminus F_n) = F_1 \setminus (\bigcap_{n=1}^\infty F_n) = F_1 \setminus F$.
  <2>3. $\mu(F_1 \setminus F) = \sum_{k=1}^\infty \mu(E_k) = \lim_{n\to\infty} \sum_{k=1}^{n-1} \mu(E_k) = \lim_{n\to\infty} \mu(F_1 \setminus F_n)$.
    Proof: By countable additivity of $\mu$ on the pairwise disjoint collection $\{E_k\}_{k=1}^\infty$.
  <2>4. $\mu(F_1 \setminus F) = \mu(F_1) - \mu(F)$ and $\mu(F_1 \setminus F_n) = \mu(F_1) - \mu(F_n)$.
    Proof: Since $F \subseteq F_1$, $F_n \subseteq F_1$, and $\mu(F_1) \leq \mu(\RR) < \infty$, the subtraction property of finite measures gives $\mu(A \setminus B) = \mu(A) - \mu(B)$ whenever $B \subseteq A$ and $\mu(B) < \infty$.
  <2>5. $\lim_{n\to\infty} \mu(F_n) = \mu(F) = \mu\left(\bigcap_{k=1}^\infty F_k\right)$.
    Proof: By <2>3 and <2>4:
    $$
    \mu(F_1) - \mu(F) = \lim_{n\to\infty} (\mu(F_1) - \mu(F_n)) = \mu(F_1) - \lim_{n\to\infty} \mu(F_n).
    $$
    Subtracting the finite quantity $\mu(F_1)$ from both sides and multiplying by $-1$ yields $\lim_{n\to\infty} \mu(F_n) = \mu(F)$.

<1>2. **Part (b): $\eps$-$\delta$ characterization of absolute continuity.**
  <2>1. Suppose for contradiction that there exists $\eps_0 > 0$ such that for every $\delta > 0$, there exists a Borel set $E \in \mathcal B$ with $m(E) < \delta$ but $\mu(E) \geq \eps_0$.
  <2>2. For each $k \in \NN$, choose $\delta = 2^{-k}$. There exists $E_k \in \mathcal B$ such that $m(E_k) < 2^{-k}$ and $\mu(E_k) \geq \eps_0$.
    Proof: By the contradiction assumption <2>1.
  <2>3. Define $A_n = \bigcup_{k=n}^\infty E_k$ and $A = \limsup_{k\to\infty} E_k = \bigcap_{n=1}^\infty A_n$.
    Proof: Standard definition of the limsup of a sequence of sets.
  <2>4. $m(A) = 0$.
    Proof: For each $n \geq 1$, $A \subseteq A_n = \bigcup_{k=n}^\infty E_k$. By countable subadditivity of Lebesgue measure $m$:
    $$
    m(A) \leq m(A_n) \leq \sum_{k=n}^\infty m(E_k) < \sum_{k=n}^\infty 2^{-k} = 2^{1-n}.
    $$
    Taking $n \to \infty$ gives $m(A) \leq 0$, so $m(A) = 0$.
  <2>5. $\mu(A_n) \geq \eps_0$ for all $n \geq 1$.
    Proof: For each $n \geq 1$, $E_n \subseteq A_n$, so by monotonicity of $\mu$, $\mu(A_n) \geq \mu(E_n) \geq \eps_0$.
  <2>6. The sequence $\{A_n\}$ is decreasing ($A_n \supseteq A_{n+1}$), so $\mu(A) = \lim_{n\to\infty} \mu(A_n) \geq \eps_0 > 0$.
    Proof: By Part (a) (<1>1), since $\mu$ is a finite Borel measure and $A = \bigcap_{n=1}^\infty A_n$, $\mu(A) = \lim_{n\to\infty} \mu(A_n) \geq \eps_0 > 0$.
  <2>7. Contradiction: $m(A) = 0$ but $\mu(A) > 0$, violating the hypothesis $\mu \ll m$.
    Proof: Hypothesis states that $\mu(E) = 0$ whenever $m(E) = 0$. But <2>4 gives $m(A) = 0$ while <2>6 gives $\mu(A) \geq \eps_0 > 0$, a contradiction.
  <2>8. The claim holds: for every $\eps > 0$ there exists $\delta > 0$ such that $m(E) < \delta \implies \mu(E) < \eps$.

<1>3. **Conclusion.**
  Both statements (a) and (b) are proved rigorously. Q.E.D.
:::
