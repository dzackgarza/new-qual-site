---
schema: qual/card@1
id: P-MMAQ-MZ6ONVPBKI
kind: problem
title: A summable family of positive terms has countable index, and $f(x)=\sum_{q\leq x}a(q)$ is continuous precisely off $\QQ$
classification:
  areas:
  - real-analysis
  topics:
  - series-of-numbers
  - continuity
relations: []
review: draft
solved: true
---

::: problem
Let $I$ be an index set and $\alpha: I \to (0, \infty)$.

1. Show that
   $$
   \sum_{i \in I} a(i):=\sup _{\substack{ J \subset I \\ J \text { finite }}} \sum_{i \in J} a(i)<\infty \implies I \text{ is countable.}
   $$

2. Suppose $I = \QQ$ and $\sum_{q \in \mathbb{Q}} a(q)<\infty$.
   Define
   $$
   f(x):=\sum_{\substack{q \in \mathbb{Q}\\ q \leq x}} a(q).
   $$
   Show that $f$ is continuous at $x \iff x\not\in \QQ$.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** (1) Show $\sup_{J \text{ finite}} \sum_{i \in J} a(i) < \infty \implies I$ countable, for $a: I \to (0,\infty)$.
(2) For $I = \QQ$ with $\sum_q a(q) < \infty$, show $f(x) = \sum_{q \leq x} a(q)$ is continuous at $x$ iff $x \notin \QQ$.

<1>1. Proof of (1): if the sup over finite subsets is finite, then $I$ is countable.
<2>1. Let $S \definedas \sum_{i \in I} a(i) < \infty$.
For each $n \geq 1$, define $I_n \definedas \theset{i \in I \suchthat a(i) > 1/n}$.
Proof: Definition.
<2>2. Each $I_n$ is finite, with $\abs{I_n} < n S$.
Proof: If $I_n$ contained $k$ elements, then $\sum_{i \in I_n} a(i) > k/n$; since $I_n$ is a finite subset of $I$, this sum is $\leq S$, so $k < nS$.
<2>3. $I = \bigcup_{n=1}^\infty I_n$.
Proof: For each $i \in I$, $a(i) > 0$, so $a(i) > 1/n$ for some $n$; hence $i \in I_n$.
<2>4. $I$ is a countable union of finite sets, hence countable.
Proof: By <2>2 each $I_n$ is finite and by <2>3 their union is all of $I$.
<2>5. Q.E.D. Proof: This proves (1).

<1>2. Preparation for (2): $f$ is well-defined and nondecreasing, and its jumps occur exactly at rationals.
<2>1. $f(x) = \sum_{q \in \QQ, q \leq x} a(q)$ converges absolutely, and $0 \leq f(x) \leq \sum_{q \in \QQ} a(q) < \infty$.
Proof: The partial sums over finite subsets are bounded by the total sum $S$ (a finite subset of $\{q \leq x\}$ is a finite subset of $\QQ$), so the sum over the countable set $\{q \in \QQ : q \leq x\}$ converges and is $\leq S$.
<2>2. $f$ is nondecreasing.
Proof: If $x < y$, the set $\{q \leq x\}$ is contained in $\{q \leq y\}$, and all $a(q) > 0$.
<2>3. For $q_0 \in \QQ$, the jump of $f$ at $q_0$ is $f(q_0) - f(q_0^-) = a(q_0) > 0$, where $f(q_0^-) = \sum_{q < q_0} a(q)$.
Proof: $\sum_{q \leq q_0} a(q) - \sum_{q < q_0} a(q) = a(q_0)$, both series being absolutely convergent.

<1>3. If $x \in \QQ$, then $f$ is discontinuous at $x$.
<2>1. $f(x) - f(x^-) = a(x) > 0$.
Proof: By <1>2<2>3, the jump at $x$ is $a(x) > 0$.
<2>2. Hence $f$ is not continuous at $x$.
Proof: A function continuous at $x$ satisfies $f(x) = \lim_{y \to x^-} f(y) = f(x^-)$; here the left limit differs from the value by $a(x) > 0$.
<2>3. Q.E.D. Proof: This proves the "only if" direction.

<1>4. If $x \notin \QQ$, then $f$ is continuous at $x$.
<2>1. Fix $x \notin \QQ$ and $\eps > 0$.
Since $\sum_{q \in \QQ} a(q) = S < \infty$, there is a finite set $F \subset \QQ$ such that $\sum_{q \in \QQ \setminus F} a(q) < \eps$.
Proof: This is Cauchy's criterion for the absolutely convergent series over the countable set $\QQ$ (sum over all but finitely many terms is small).
<2>2. Let $d \definedas \min\theset{\abs{x - q} \suchthat q \in F} > 0$, since $x \notin \QQ$ and $F$ is finite.
Proof: The minimum is attained on the finite set $F$ and is strictly positive because no element of $F$ equals $x$.
<2>3. For any $y$ with $\abs{y - x} < d$, every $q \in \QQ$ with $\min(x,y) < q \leq \max(x,y)$ satisfies $\abs{q - x} < \abs{y - x} < d$, hence $q \notin F$: the rationals between $x$ and $y$ all avoid the finite set $F$.
Proof: If $q$ lies strictly between $x$ and $y$, then $\abs{q - x} < \abs{y - x} < d = \min_{q' \in F} \abs{q' - x}$, so $q$ is closer to $x$ than every element of $F$ is; in particular $q \notin F$.
(If $F = \emptyset$, the conclusion is trivial.)
<2>4. Therefore $\abs{f(y) - f(x)} = \sum_{q \in \QQ,\ \min(x,y) < q \leq \max(x,y)} a(q) \leq \sum_{q \in \QQ \setminus F} a(q) < \eps$.
Proof: The difference of the two sums is the sum of $a(q)$ over rationals strictly between $x$ and $y$ (by absolute convergence); by <2>3 all such $q$ lie in $\QQ \setminus F$, so this sub-sum is bounded by the total mass outside $F$, which is $< \eps$ by <2>1. <2>5. Q.E.D. Proof: $\eps > 0$ was arbitrary, so $f$ is continuous at $x$.

<1>5. Conclusion.
Proof: (1) by <1>1. For (2), $x \in \QQ \implies$ discontinuous by <1>3, and $x \notin \QQ \implies$ continuous by <1>4; these give both directions.
:::
