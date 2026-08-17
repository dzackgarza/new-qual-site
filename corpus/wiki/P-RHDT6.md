---
schema: qual/card@1
id: P-RHDT6
kind: problem
title: A summable family of positive terms has countable index set; $f(x)=\sum_{q\le x}a(q)$ is continuous precisely at irrationals
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
Let $I$ be an index set and $\alpha: I \to (0, \infty)$.

a.
Show that
\[
\sum_{i \in I} a(i):=\sup _{\substack{ J \subset I \\ J \text { finite }}} \sum_{i \in J} a(i)<\infty \implies I \text{ is countable.}
\]

b.
Suppose $I = \QQ$ and $\sum_{q \in \mathbb{Q}} a(q)<\infty$.
Define
\[
f(x):=\sum_{\substack{q \in \mathbb{Q}\\ q \leq x}} a(q).
\]
Show that $f$ is continuous at $x \iff x\not\in \QQ$.

:::{.concept}
\envlist

- Can always filter sets $X$ with a function $X\to \RR$.
- Countable union of countable sets is still countable.
- Continuity: $\lim_{y\to x} f(y) = f(x)$ from either side.
- Trick: pick enumerations of countable sets and reindex sums
:::

:::{.solution}
\envlist

:::{.proof title="of a"}
\envlist

- Set $S \definedas \sum_{i\in I} \alpha(i)$, we will show that $S<\infty \implies I$ is countable.
- Write 
\[
I = \Union_{n\geq 0} S_n, &&
S_n \definedas \theset{i\in I \suchthat \alpha(i) \geq {1\over n}}
.\]
  - Note that $S_n \subseteq S$ for all $n$, so $\sum_{i\in I}\alpha(i) \geq \sum_{i\in S_n} \alpha(i)$ for all $n$.
  - It suffices to show that $S_n$ is countable, since $I$ is a countable union of $S_n$.
- There is an inequality
\[  
\infty 
&> S \da \sum_{i\in I} \alpha(i) \\
&\geq \sum_{i\in S_n} \alpha(i) \\
&\geq \sum_{i\in S_n} {1\over n} \\
&= {1\over n} \sum_{i\in S_n} 1 \\
&= \qty{1\over n} \# S_n \\ \\
\implies \infty &> n S \geq \# S_n
.\]
:::

:::{.proof title="of b"}
\envlist

- We'll prove something more general: let $Q = \ts{q_k}$ be countable and $\ts{\alpha_k \da \alpha(q_k)}$ be summable, and define
\[
f(x) \da \sum_{q_k\leq x} \alpha_k
.\]
  
  - $f$ is always discontinuous precisely on the countable set $Q$ and continuous on $\RR\sm Q$.

  - $f$ is always left-continuous, is right-continuous at $x\in\RR\sm Q$, and *not* right-continuous at $x\in Q$

  - $f$ has jump discontinuities at every $q_m$, where the jump is precisely $\alpha_m$.

- This follows from computing the left and right limits:
\[
f(x^+) &= \lim_{h\to 0} \sum_{q_k \leq x+h} \alpha_k = \sum_{q_k\leq x} \alpha_k = \sum_{q_k < x} \alpha_k + \sum_{q_k = x} \alpha_k \\
f(x^-) &= \lim_{h\to 0} \sum_{q_k \leq x-h} \alpha_k = \sum_{q_k < x} \alpha_k
,\]
  where we've used that $\ts{q_k \leq x} = \ts{q_k < x} \disjoint \ts{x}$ in the first equality.

- Then if $x=q_m$ for some $m$,
\[
f(x^+) &= f(q_m^+) = \sum_{q_k < q_m} \alpha_k + \alpha_m \\
f(x^-) &= f(a_m^-) = \sum_{q_k< q_m} \alpha_k
,\]
which clearly differ if $\alpha_m \neq 0$.

- Taking $x\not\in Q$, we have $\ts{q_k \leq x} = \ts{q_k < x}$, since $\ts{q_k=x} = \emptyset$, so
\[
f(x^+) &= \sum_{q_k\leq x} \alpha_k = \sum_{q_k < x} \alpha_k \\
f(x^-) &= \sum_{q_k< x} \alpha_k
,\]
  so the limits agree.

- To recover the result in the problem, let $\QQ = \ts{q_k}$ be any enumeration of the rationals.

:::

:::
