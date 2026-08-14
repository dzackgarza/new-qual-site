---
schema: qual/card@1
id: P-DQQUE
kind: problem
title: "Let $\\{a_k\\}_{k=1}^\\infty$ be a bounded sequence of real numbers and"
classification:
  areas:
  - real-analysis
  topics:
  - sequences-of-numbers
  - limits
relations: []
review: draft
---
Let $\{a_k\}_{k=1}^\infty$ be a bounded sequence of real numbers and
$E$ given by:
$$E:= \bigg\{s \in \mathbb{R}\, \colon \, \text{ the set } \{k \in \mathbb{N}\, \colon \, a_k \geq s\} \text{ has at most finitely many elements}\bigg\}.$$
Prove that $\limsup_{k \to \infty} a_k = \inf E$.

:::{.proof}
*Proof.* Let $e \in E$. As there are only finitely many
$a_k \geq s$, there exists some $N \in \mathbb{N}$ such that
$a_k < e$ for all $k \geq N$. Define $T_k := \{a_k : k \geq n\}$. It
is clear that $e$ is thus an upper bound for $T_N$. So,
$$e \geq \sup T_N \geq \limsup a_k.$$ Thus, $\limsup a_k$ is a lower
bound for $E$, meaning $\inf E \geq \limsup a_n$.\
Conversely, suppose $k \in \mathbb{N}$.
$$T_k = \{a_n : n \geq k \}.$$ So, $\sup T_k \geq a_n$ for all
$a_n \in T_k$. Then, $\{a_k : a_k \geq \sup T_k\}$ must be finite,
so $\{k \in \mathbb{N} : a_k \geq \sup T_k\}$ is finite. So,
$\sup T_k \in E$ for all $k \in \mathbb{N}$. Since $\inf E$ is a
lower bound for $E$, $\inf E \leq \sup T_k$ for all
$k \in \mathbb{N}$. Thus,
$$\inf E \leq \lim (\sup T_k) = \limsup a_k.$$ We have both
inequalities, therefore $\limsup a_k = \inf E$. ◻
:::
