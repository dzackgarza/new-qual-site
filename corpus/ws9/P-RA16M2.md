---
schema: qual/card@1
id: P-RA16M2
kind: problem
title: 'UGA analysis qualifying exam, May 2016, problem 2'
classification:
  areas:
  - real-analysis
  topics:
  - sequences-of-numbers
  - limits
relations: []
review: draft
solved: true
---

::: {.problem title="?"}
Let $\{a_k\}_{k=1}^{\infty}$ be a bounded sequence of real numbers and let $$E:=\left\{s\in\mathbb R:\text{ the set }\{k\in\mathbb N:a_k\ge s\}\text{ has at most finitely many elements}\right\}.$$ Prove that $$\limsup_{k\to\infty}a_k=\inf E.$$
:::

:::: {.solution}
> **AI-Generated Solution** **Goal:** Prove $\limsup_{k\to\infty} a_k = \inf E$ where $E = \{s \in \mathbb R : \{k : a_k \ge s\} \text{ is finite}\}$ and $\{a_k\}$ is bounded.

<1>1. $E$ is nonempty and bounded below.
Proof: boundedness gives $a_k \le M$ for all $k$; then $s = M+1$ satisfies $\{k : a_k \ge s\} = \emptyset$, so $M + 1 \in E$.
If $a_k \ge m$ for all $k$, then any $s < m$ has $\{k : a_k \ge s\} = \mathbb N$, infinite, so $s \notin E$; hence $E \subseteq [m, \infty)$, bounded below.

<1>2. Let $L := \limsup_k a_k$.
Then $L$ is a lower bound for $E$.
<2>1. For $s \in E$, the set $\{k : a_k \ge s\}$ is finite.
<2>2. $a_k < s$ for all sufficiently large $k$.
Proof: <2>1: only finitely many exceptions.
<2>3. $L \le s$.
Proof: $L = \limsup a_k = \inf_n \sup_{k\ge n} a_k$, and <2>2 gives $\sup_{k \ge n} a_k \le s$ for large $n$; hence the inf over $n$ is $\le s$.
<2>4. $L \le \inf E$.
Proof: <2>3 holds for every $s \in E$, so $L$ is a lower bound of $E$.

<1>3. $\inf E \le L$.
<2>1. For every $\varepsilon > 0$, the set $\{k : a_k \ge L + \varepsilon\}$ is finite.
Proof: by the characterization of limsup, only finitely many terms exceed $L + \varepsilon$ (a subsequence with $a_{k_j} \ge L + \varepsilon$ for infinitely many $j$ would have a subsequential limit $\ge L + \varepsilon > L$, contradicting $L = \limsup a_k$). <2>2. $L + \varepsilon \in E$ for every $\varepsilon > 0$.
Proof: <2>1 is exactly the defining property of membership in $E$.
<2>3. $\inf E \le L + \varepsilon$ for all $\varepsilon > 0$, so $\inf E \le L$.
Proof: <2>2 gives elements of $E$ arbitrarily close to $L$ from above.

<1>4. Q.E.D. Proof: <1>2 gives $L \le \inf E$ and <1>3 gives $\inf E \le L$; hence $\limsup_k a_k = L = \inf E$.
:::
