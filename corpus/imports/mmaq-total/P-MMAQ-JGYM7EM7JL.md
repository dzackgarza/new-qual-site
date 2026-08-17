---
schema: qual/card@1
id: P-MMAQ-JGYM7EM7JL
kind: problem
title: Let $(X, \mathcal M, \mu)$ be a measure space and suppose…
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
Let $(X, \mathcal M, \mu)$ be a measure space and suppose $\theset{E_n} \subset \mathcal M$ satisfies
$$
\lim _{n \rightarrow \infty} \mu\left(X \backslash E_{n}\right)=0.
$$

Define
$$
G \definedas \theset{x\in X \suchthat x\in E_n \text{ for only finitely many  } n}.
$$

Show that $G \in \mathcal M$ and $\mu(G) = 0$.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Let $(X, \mathcal M, \mu)$ be a measure space with $E_n \in \mathcal M$ and $\mu(X \setminus E_n) \to 0$.
Let $G$ be the set of points belonging to only finitely many $E_n$.
Show $G \in \mathcal M$ and $\mu(G) = 0$.

<1>1. Rewrite $G$ in terms of the complements.
<2>1. A point $x$ belongs to only finitely many $E_n$ iff there exists $N$ with $x \in X \setminus E_n$ for all $n \geq N$.
Proof: If $x \in E_n$ for finitely many $n$, let $N$ exceed the largest such index; conversely, if $x \in X\setminus E_n$ for all $n \geq N$, then $x$ lies in at most the finitely many $E_1, \ldots, E_{N-1}$.
<2>2. Hence $G = \union_{N=1}^\infty \intersect_{n \geq N} (X \setminus E_n)$.
Proof: By <2>1, $G$ is the countable union over $N$ of the sets $\intersect_{n\geq N}(X \setminus E_n)$.
<2>3. $G \in \mathcal M$.
Proof: Each $X \setminus E_n \in \mathcal M$ (complement of a measurable set), each countable intersection $\intersect_{n \geq N}(X\setminus E_n) \in \mathcal M$, and $G$ is a countable union of such sets by <2>2.

<1>2. Bound $\mu(G)$.
<2>1. For each fixed $N$, $\mu(\intersect_{n \geq N} (X \setminus E_n)) \leq \mu(X \setminus E_N)$.
Proof: $\intersect_{n\geq N}(X\setminus E_n) \subseteq X \setminus E_N$; monotonicity of $\mu$.
<2>2. Let $F_N \definedas \intersect_{n \geq N}(X \setminus E_n)$; then $F_1 \subseteq F_2 \subseteq \cdots$ and $G = \union_N F_N$.
Proof: As $N$ grows the intersection shrinks, so the sets increase; the union is $G$ by <1>2.<2>2. <2>3. By continuity from below, $\mu(G) = \lim_{N \to \infty} \mu(F_N)$.
Proof: <2>2 gives an increasing sequence of measurable sets exhausting $G$.
<2>4. $\lim_N \mu(F_N) \leq \lim_N \mu(X \setminus E_N) = 0$.
Proof: By <2>1, $\mu(F_N) \leq \mu(X \setminus E_N)$ for each $N$, and the latter tends to $0$ by hypothesis.
<2>5. Q.E.D. Proof: By <2>3 and <2>4, $\mu(G) = 0$.

<1>3. Conclusion: $G \in \mathcal M$ and $\mu(G) = 0$.
Proof: Measurability by <1>2.<2>3; measure zero by <1>2.<2>5.
:::
