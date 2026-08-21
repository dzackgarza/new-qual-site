---
schema: qual/card@1
id: P-TOIEK
kind: problem
title: Uniformly convergent sequences of bounded functions are uniformly bounded
classification:
  areas:
  - prelim
  topics:
  - Uniform Convergence
  - Sequences of Functions
relations: []
review: draft
solved: true
---

::: problem
  1. Suppose $f_n \rightrightarrows g$ with each $f_n$ bounded; we want to show that all of the $f_n$ are uniformly bounded by some $M$, i.e.
  $$
  \exists M \suchthat \forall x\in \RR, \forall n\in \NN, \quad \abs{f_n(x)} \leq M.
  $$
  - Since each $f_n$ is bounded, we can produce some $M_n$ such that $\abs{f_n(x)} \leq M < \infty$.
  - Since $f_n \rightrightarrows g$, we can give ourselves an epsilon of room and get an $N$ such that $n\geq N \implies \abs{f_n(x) - g(x)} < \varepsilon$. We then write
  $$
  f_n(x) = f_n(x) - g(x) + g(x) - f_N(x) + f_N(x) \\
  \implies \abs{f_n(x)} \leq \abs{f_n(x) - g(x)} + \abs{g(x) - f_N(x)} + \abs{f_N(x)} \\
  \leq \varepsilon + \varepsilon + M_N
  $$

  by the above two statements. But $N<\infty$, so we can choose $M = \max\theset{M_1, M_2, \cdots M_{N-1}, 2\varepsilon + M_N}$ as a uniform bound. Then just take $\varepsilon \to 0$. (Maybe not necessary?)
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Let $E$ be a set, and let $(f_n)_{n=1}^\infty$ be a sequence of functions $f_n: E \to \mathbb{R}$ such that each $f_n$ is bounded on $E$. Suppose $f_n \to g$ uniformly on $E$. Prove that the sequence $(f_n)_{n=1}^\infty$ is uniformly bounded on $E$, i.e., there exists a constant $M > 0$ such that $|f_n(x)| \le M$ for all $n \in \mathbb{N}$ and all $x \in E$.

<1>1. Definition of uniform convergence: There exists an integer $N \ge 1$ such that for all $n \ge N$ and all $x \in E$, $|f_n(x) - g(x)| < 1$.
    Proof: By the definition of uniform convergence with $\varepsilon = 1 > 0$.

<1>2. For all $n \ge N$ and all $x \in E$, $|f_n(x)| \le |f_N(x)| + 2$.
    Proof:
    <2>1. By the triangle inequality:
        $$|f_n(x) - f_N(x)| \le |f_n(x) - g(x)| + |g(x) - f_N(x)|.$$
    <2>2. For any $n \ge N$, applying <1>1 gives $|f_n(x) - g(x)| < 1$ and $|f_N(x) - g(x)| < 1$.
        Thus $|f_n(x) - f_N(x)| < 1 + 1 = 2$.
    <2>3. Again by the triangle inequality:
        $$|f_n(x)| \le |f_N(x)| + |f_n(x) - f_N(x)| < |f_N(x)| + 2.$$

<1>3. For each $k \in \{1, 2, \dots, N\}$, there exists a constant $M_k < \infty$ such that $|f_k(x)| \le M_k$ for all $x \in E$.
    Proof: By hypothesis, each function $f_k$ is bounded on $E$.

<1>4. Define $M = \max\{M_1, M_2, \dots, M_{N-1}, M_N + 2\}$. Then $|f_n(x)| \le M$ for all $n \in \mathbb{N}$ and all $x \in E$.
    Proof:
    <2>1. If $1 \le n < N$, then for all $x \in E$, $|f_n(x)| \le M_n \le M$ by <1>3 and definition of $M$.
    <2>2. If $n \ge N$, then by <1>2 and <1>3:
        $$|f_n(x)| < |f_N(x)| + 2 \le M_N + 2 \le M.$$
    <2>3. In all cases, $|f_n(x)| \le M$ for all $n \in \mathbb{N}$ and all $x \in E$.

<1>5. Conclusion: $(f_n)_{n=1}^\infty$ is uniformly bounded on $E$.
    Proof: Follows directly from <1>4. Q.E.D.
:::
