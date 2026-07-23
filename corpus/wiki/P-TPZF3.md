---
schema: qual/card@1
id: P-TPZF3
kind: problem
title: "Let $K$ be the set of numbers in $[0, 1]$ whose decimal expansions do\u2026"
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
---
Let $K$ be the set of numbers in $[0, 1]$ whose decimal expansions do not use the digit $4$.

> We use the convention that when a decimal number ends with 4 but all other digits are
different from 4, we replace the digit $4$ with $399\cdots$. For example, $0.8754 = 0.8753999\cdots$.

Show that $K$ is a compact, nowhere dense set without isolated points, and find the
Lebesgue measure $m(K)$.

:::{.concept}
\envlist
- Definition: $A$ is *nowhere dense* $\iff$ every interval $I$ contains a subinterval $S \subseteq A^c$.
  - Equivalently, the interior of the closure is empty, $\qty{\bar K}^\circ = \emptyset$.
:::

:::{.solution}
\envlist

Claim: **$K$ is compact**.

- It suffices to show that $K^c \definedas [0, 1]\setminus K$ is open; 
  Then $K$ will be a closed and bounded subset of $\RR$ and thus compact by Heine-Borel.

- Strategy: write $K^c$ as the union of open balls (since these form a basis for the Euclidean topology on $\RR$).
  
  - Do this by showing every point $x\in K^c$ is an interior point, i.e. $x$ admits a neighborhood $N_x$ such that $N_x \subseteq K^c$.

- Identify $K^c$ as the set of real numbers in $[0, 1]$ whose decimal expansion **does** contain a 4.
  
  - We will show that there exists a neighborhood small enough such that all points in it contain a $4$ in their decimal expansions.

- Let $x\in K^c$, suppose a 4 occurs as the $k$th digit, and write
\[  
x = 0.d_1 d_2 \cdots d_{k-1}~ 4 ~d_{k+1}\cdots 
= \qty{\sum_{j=1}^k d_j 10^{-j}} + \qty{4\cdot 10^{-k}} + \qty{\sum_{j=k+1}^\infty d_j 10^{-j}}
.\]

- Set $r_x < 10^{-k}$ and let $y \in [0, 1] \Intersect B_{r_x}(x)$ be arbitrary and write 
\[  
y = \sum_{j=1}^\infty c_j 10^{-j}
.\]

- Thus $\abs{x-y} < r_x < 10^{-k}$, and the first $k$ digits of $x$ and $y$ must agree:

  - We first compute the difference:
\[  
x - y &= \sum_{i=1}^\infty d_j 10^{-j} - \sum_{i=1}^\infty c_j 10^{-j} = \sum_{i=1}^\infty \qty{d_j - c_j} 10^{-j} \\
\]
  - Thus (claim)
\[
\abs{x-y} &\leq \sum_{j=1}^\infty \abs{d_j - c_j} 10^j < 10^{-k} \iff \abs{d_j - c_j} = 0 \quad \forall j\leq k
.\]
  - Otherwise we can note that any term $\abs{d_j - c_j}\geq 1$ and there is a contribution to $\abs{x-y}$ of at least $1\cdot 10^{-j}$ for some $j < k$, whereas
\[  
j < k \iff 10^{-j} > 10^{-k}
,\]
  a contradiction.
  
- This means that for all $j \leq k$ we have $d_j = c_j$, and in particular $d_k = 4 = c_k$, so $y$ has a 4 in its decimal expansion.

- But then $K^c = \Union_x B_{r_x}(x)$ is a union of open sets and thus open.


Claim: **$K$ is nowhere dense and $m(K) = 0$:**

- Strategy: Show $\qty{\bar K}^\circ = \emptyset$.
- Since $K$ is closed, $\bar K = K$, so it suffices to show that $K$ does not properly contain any interval.
- It suffices to show $m(K^c) = 1$, since this implies $m(K) = 0$ and since any interval has strictly positive measure, this will mean $K$ can not contain an interval.

- As in the construction of the Cantor set, let 

  - $K_0$ denote $[0, 1]$ with 1 interval $\left({4 \over 10}, {5 \over 10} \right)$ of length $1 \over 10$ deleted, so 
  \[m(K_0^c) = {1\over 10}.\]
  - $K_1$ denote $K_0$ with 9 intervals $\left({1 \over 100}, {5\over 100}\right), ~\left({14 \over 100}, {15 \over 100}\right), \cdots \left({94\over 100}, {95 \over 100}\right)$ of length ${1 \over 100}$ deleted, so 
  \[m(K_1^c) = {1\over 10} + {9 \over 100}.\]
  - $K_n$ denote $K_{n-1}$ with $9^{n}$ such intervals of length $1 \over 10^{n+1}$ deleted, so 
  \[m(K_n^c) = {1\over 10} + {9 \over 100} + \cdots + {9^{n} \over 10^{n+1}}.\]

- Then compute 
\[
m(K^c) 
= \sum_{j=0}^\infty {9^n \over 10^{n+1} } 
= {1\over 10} \sum_{j=0}^\infty \qty{9\over 10}^n 
= {1 \over 10} \qty{ {1 \over 1 - {9 \over 10 } } } 
= 1.
\]

Claim: **$K$ has no isolated points**:

- A point $x\in K$ is isolated iff there there is an open ball $B_r(x)$ containing $x$ such that $B_r(x) \subsetneq K^c$.
  - So every point in this ball **should** have a 4 in its decimal expansion.

- Strategy: show that if $x\in K$, every neighborhood of $x$ intersects $K$.

- Note that $m(K_n) = \left( \frac 9 {10} \right)^n \converges{n\to\infty}\to 0$ 
- Also note that we deleted open intervals, and the endpoints of these intervals are never deleted.
  - Thus endpoints of deleted intervals are elements of $K$.

- Fix $x$. Then for every $\varepsilon$, by the Archimedean property of $\RR$, choose $n$ such that $\left( \frac 9 {10} \right)^n < \varepsilon$.

- Then there is an endpoint $x_n$ of some deleted interval $I_n$ satisfying \[\abs{x - x_n} \leq  \left( \frac 9 {10} \right)^n < \eps.\]

- So every ball containing $x$ contains some endpoint of a removed interval, and thus an element of $K$.
:::

