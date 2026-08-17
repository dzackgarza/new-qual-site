---
schema: qual/card@1
id: P-MMAQ-ZVPIWSAD4O
kind: problem
title: "Let $X$ be a complete metric space and define a norm $\\|f\\|:=\\max \\{|f(x)|: x \\in X\\}$ Show that\u2026"
classification:
  areas:
  - real-analysis
  topics:
  - function-spaces
  - norms
  - completeness
relations: []
review: draft
---

::: problem
Let $X$ be a complete metric space and define a norm
$$
\|f\|:=\max \{|f(x)|: x \in X\}.
$$

Show that $(C^0(\RR), \norm{\wait} )$ (the space of continuous functions $f: X\to \RR$) is complete.
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** Show that the space of bounded continuous real-valued functions on a metric space $X$ is complete under the sup norm (the statement's $C^0(\mathbb{R})$ and the use of $\max$ are read as the standard theorem on $C_b(X)$).

<1>1. The norm in the statement must be read as the sup norm on bounded continuous functions.
    <2>1. For a continuous function on an arbitrary metric space $X$, the maximum need not be attained and the function need not be bounded.
        Proof: e.g. $f(x) = x$ on $X = \mathbb{R}$ is continuous but unbounded; $f(x) = \arctan x$ on $X = \mathbb{R}$ is bounded with no attained maximum.
    <2>2. The correct, standard statement is: $C_b(X)$, the bounded continuous real-valued functions on $X$, is complete under $\norm{f}_\infty := \sup_{x \in X} |f(x)|$; when $X$ is compact this is the $\max$ of the statement, and then $C_b(X) = C^0(X)$. Completeness of $X$ is not needed.
        Proof: this identifies the intended space; the proof below establishes the claim.
<1>2. Let $\{f_n\}$ be a Cauchy sequence in $(C_b(X), \norm{\cdot}_\infty)$.
    <2>1. For each $x \in X$, $\{f_n(x)\}$ is a Cauchy sequence of real numbers.
        Proof: $|f_n(x) - f_m(x)| \leq \norm{f_n - f_m}_\infty \to 0$.
    <2>2. The pointwise limit $f(x) := \lim_n f_n(x)$ exists and $f_n \to f$ uniformly.
        Proof: given $\varepsilon > 0$, choose $N$ with $\norm{f_n - f_m}_\infty < \varepsilon$ for $n, m \geq N$; then for $n \geq N$ and every $x$, $|f_n(x) - f(x)| = \lim_m |f_n(x) - f_m(x)| \leq \varepsilon$.
    <2>3. $f$ is continuous.
        Proof: $f$ is the uniform limit of continuous functions: $\varepsilon/3$ argument as in the classical theorem.
    <2>4. $f$ is bounded and $\norm{f_n - f}_\infty \to 0$.
        Proof: from <2>2 with $n \geq N$, $|f(x)| \leq |f(x) - f_N(x)| + |f_N(x)| \leq \varepsilon + \norm{f_N}_\infty$, so $f$ is bounded; and $\norm{f_n - f}_\infty \leq \varepsilon$ for $n \geq N$.
<1>3. Q.E.D.
    Proof: <2>3 and <2>4 show the Cauchy sequence converges in $C_b(X)$, which is therefore complete.
:::
