---
schema: qual/card@1
id: P-DQQUE
kind: problem
title: $\limsup a_k=\inf\{s:\text{only finitely many }a_k\ge s\}$
classification:
  areas:
  - real-analysis
  topics:
  - Sequences of Numbers
  - Limits
relations: []
review: draft
solved: true
---

Let $\{a_k\}_{k=1}^\infty$ be a bounded sequence of real numbers and $E$ given by: $$E:= \bigg\{s \in \mathbb{R}\, \colon \, \text{ the set } \{k \in \mathbb{N}\, \colon \, a_k \geq s\} \text{ has at most finitely many elements}\bigg\}.$$ Prove that $\limsup_{k \to \infty} a_k = \inf E$.

::: {.proof}
*Proof.* Let $e \in E$.
As there are only finitely many $a_k \geq s$, there exists some $N \in \mathbb{N}$ such that $a_k < e$ for all $k \geq N$.
Define $T_k := \{a_k : k \geq n\}$.
It is clear that $e$ is thus an upper bound for $T_N$.
So, $$e \geq \sup T_N \geq \limsup a_k.$$ Thus, $\limsup a_k$ is a lower bound for $E$, meaning $\inf E \geq \limsup a_n$.\
Conversely, suppose $k \in \mathbb{N}$.
$$T_k = \{a_n : n \geq k \}.$$ So, $\sup T_k \geq a_n$ for all $a_n \in T_k$.
Then, $\{a_k : a_k \geq \sup T_k\}$ must be finite, so $\{k \in \mathbb{N} : a_k \geq \sup T_k\}$ is finite.
So, $\sup T_k \in E$ for all $k \in \mathbb{N}$.
Since $\inf E$ is a lower bound for $E$, $\inf E \leq \sup T_k$ for all $k \in \mathbb{N}$.
Thus, $$\inf E \leq \lim (\sup T_k) = \limsup a_k.$$ We have both inequalities, therefore $\limsup a_k = \inf E$.
◻
:::
::: {.solution}
> **AI-Generated Solution**

<1>1. Notation: $E = \{s \in \RR : \text{only finitely many } k \text{ have } a_k \ge s\}$; $(a_k)$ is bounded.
Proof: given.

<1>2. For every $s \in E$: $s \ge \limsup_{k \to \infty} a_k$.
<2>1. Since only finitely many $a_k \ge s$, there is $N$ with $a_k < s$ for all $k \ge N$.
Proof: definition of $E$.
<2>2. $\sup_{k \ge N} a_k \le s$.
Proof: <2>1 says $s$ is an upper bound for $\{a_k : k \ge N\}$.
<2>3. $\limsup a_k = \inf_N \sup_{k \ge N} a_k \le \sup_{k \ge N} a_k \le s$.
Proof: <2>2 and the definition of $\limsup$ as the decreasing limit of the tails.
<2>4. Q.E.D. Proof: $s \in E$ arbitrary.

<1>3. Hence $\limsup a_k \le \inf E$.
Proof: <1>2 shows $\limsup a_k$ is a lower bound for $E$.

<1>4. For every $k$: $\sup_{j \ge k} a_j \in E$.
Proof: the set $\{j : a_j \ge \sup_{j \ge k} a_j\}$ is contained in $\{1, \ldots, k-1\}$ (every $j \ge k$ has $a_j \le \sup_{j \ge k} a_j$), hence finite.

<1>5. $\inf E \le \sup_{j \ge k} a_j$ for every $k$; letting $k \to \infty$ gives $\inf E \le \limsup a_k$.
Proof: <1>4 and the definition of $\inf$; the tails $\sup_{j \ge k} a_j$ decrease to $\limsup a_k$.

<1>6. Q.E.D.: $\limsup a_k = \inf E$.
Proof: <1>3 and <1>5 give both inequalities.
:::
