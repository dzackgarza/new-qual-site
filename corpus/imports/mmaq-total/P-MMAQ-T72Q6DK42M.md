---
schema: qual/card@1
id: P-MMAQ-T72Q6DK42M
kind: problem
title: "Let $\\{f_k\\}$ be any sequence of functions in $L^2([0, 1])$ satisfying $\\norm{f_k}_2 \\leq M$ for all $k \\in \\NN$."
classification:
  areas:
  - real-analysis
  topics:
  - lp-spaces
  - convergence-of-functions
  - fatou
  - egorov
relations: []
review: draft
solved: true
---

::: problem
Let $\{f_k\}$ be any sequence of functions in $L^2([0, 1])$ satisfying $\norm{f_k}_2 \leq M$ for all $k \in \NN$.

Prove that if $f_k \to f$ almost everywhere, then $f \in L^2([0, 1])$ with $\norm{f}_2 \leq M$ and
$$
\lim _{k \rightarrow \infty} \int_{0}^{1} f_{k}(x) dx = \int_{0}^{1} f(x) d x
$$

> Hint: Try using Fatou's Lemma to show that $\norm{f}_2 \leq M$ and then try applying Egorov's Theorem.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** If $\{f_k\} \subseteq L^2([0,1])$ with $\norm{f_k}_2 \leq M$ and $f_k \to f$ a.e., prove $f \in L^2([0,1])$, $\norm{f}_2 \leq M$, and $\int_0^1 f_k \to \int_0^1 f$.

<1>1. Proof that $f \in L^2([0,1])$ and $\norm{f}_2 \leq M$.
<2>1. $|f|^2 = \liminf_k |f_k|^2$ almost everywhere.
Proof: $f_k \to f$ a.e. implies $|f_k|^2 \to |f|^2$ a.e., so the pointwise limit (hence liminf) is $|f|^2$.
<2>2. Fatou's lemma: $\int |f|^2 = \int \liminf_k |f_k|^2 \leq \liminf_k \int |f_k|^2$.
Proof: Fatou's lemma applied to the nonnegative measurable functions $|f_k|^2$.
<2>3. $\liminf_k \int |f_k|^2 \leq M^2$, since $\int |f_k|^2 = \norm{f_k}_2^2 \leq M^2$ for all $k$.
Proof: $\int |f_k|^2 \leq M^2$ for every $k$, so the liminf is $\leq M^2$.
<2>4. Hence $\int |f|^2 \leq M^2 < \infty$, so $f \in L^2([0,1])$ with $\norm{f}_2 \leq M$.
Proof: Combine <2>2 and <2>3. <2>5. Q.E.D. Proof: This proves the first two claims.

<1>2. Proof that $\int_0^1 f_k \to \int_0^1 f$.
<2>1. $f, f_k \in L^1([0,1])$ (since $L^2([0,1]) \subseteq L^1([0,1])$), with $\norm{f}_1, \norm{f_k}_1 \leq M$.
Proof: Hölder: $\int |g| \leq (\int |g|^2)^{1/2} (\int 1)^{1/2} = \norm{g}_2$ on the probability space $[0,1]$; apply to $f$ (by <1>1) and $f_k$.
<2>2. Egorov's theorem: fix $\eps > 0$; there is a measurable $A \subseteq [0,1]$ with $m(A) < \eps$ such that $f_k \to f$ uniformly on $[0,1] \setminus A$.
Proof: Egorov's theorem applies since $m([0,1]) < \infty$ and $f_k \to f$ a.e. (a.e. convergence can be achieved on a set of full measure, then Egorov on $[0,1]$ up to a null set).
<2>3. $\int_{[0,1]\setminus A} |f_k - f| \to 0$ as $k \to \infty$.
Proof: Uniform convergence on $[0,1] \setminus A$ (<2>2) gives $\sup_{[0,1]\setminus A} |f_k - f| \to 0$, and the set has measure $\leq 1$.
<2>4. $\int_A |f_k - f| \leq \int_A |f_k| + \int_A |f| \leq m(A)^{1/2}\norm{f_k}_2 + m(A)^{1/2}\norm{f}_2 \leq 2M\eps^{1/2}$.
Proof: Cauchy–Schwarz applied to $|f_k| \chi_A$ and to $|f| \chi_A$, then $\norm{f_k}_2, \norm{f}_2 \leq M$ (<1>1, hypothesis) and $m(A) < \eps$.
<2>5. Hence $\abs{\int f_k - \int f} \leq \int |f_k - f| = \int_{[0,1]\setminus A}|f_k - f| + \int_A |f_k - f|$, whose limsup as $k \to \infty$ is $\leq 0 + 2M\eps^{1/2}$.
Proof: Triangle inequality, <2>3 and <2>4. <2>6. Q.E.D. Proof: $\eps > 0$ was arbitrary, so $\lim_k \int f_k = \int f$.
:::
