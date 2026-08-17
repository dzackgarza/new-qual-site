---
schema: qual/card@1
id: P-MMAQ-5UTRCMYDS4
kind: problem
title: Let $(X, \mathcal M, \mu)$ be a measure space and suppose $f$ is a…
classification:
  areas:
  - real-analysis
  topics:
  - measure-theory
  - convergence-of-integrals
relations: []
review: draft
solved: true
---

::: problem
Let $(X, \mathcal M, \mu)$ be a measure space and suppose $f$ is a measurable function on $X$.
Show that
$$
\lim _{n \rightarrow \infty} \int_{X} f^{n} ~d \mu =
\begin{cases}
\infty & or \\
\mu(f\inv(1)),
\end{cases}
$$
and characterize the collection of functions of each type.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** Let $(X, \mathcal M, \mu)$ be a measure space and $f \geq 0$ be a non-negative measurable function on $X$. (Note: powers $f^n$ for non-negative functions or with the standard convention for non-negative integrands). Evaluate $\lim_{n\to\infty} \int_X f^n\,d\mu$ and characterize when it equals $\infty$ versus $\mu(f^{-1}(1))$.

<1>1. **Partition the space $X$ into three measurable sets according to the values of $f(x) \geq 0$.**
  <2>1. Define:
    - $E_{<1} = \{x \in X : 0 \leq f(x) < 1\} = f^{-1}([0, 1))$,
    - $E_{=1} = \{x \in X : f(x) = 1\} = f^{-1}(\{1\})$,
    - $E_{>1} = \{x \in X : f(x) > 1\} = f^{-1}((1, \infty])$.
  <2>2. $X = E_{<1} \cup E_{=1} \cup E_{>1}$ is a disjoint union of $\mathcal M$-measurable sets.
    Proof: Preimages of Borel subsets of $[0, \infty]$ under the measurable function $f$.
  <2>3. For every $n \geq 1$:
    $$
    \int_X f^n\,d\mu = \int_{E_{<1}} f^n\,d\mu + \int_{E_{=1}} f^n\,d\mu + \int_{E_{>1}} f^n\,d\mu.
    $$
    Proof: By countable additivity of the Lebesgue integral over disjoint measurable sets.

<1>2. **Behavior on each component.**
  <2>1. On $E_{=1}$, $f(x) = 1$, so $f(x)^n = 1$ for all $n \geq 1$.
    Therefore, $\int_{E_{=1}} f^n\,d\mu = \int_{E_{=1}} 1\,d\mu = \mu(E_{=1}) = \mu(f^{-1}(1))$ for every $n \geq 1$.
  <2>2. On $E_{<1}$, $0 \leq f(x) < 1$, so $f(x)^n \to 0$ pointwise monotonically decreasing as $n \to \infty$.
    <3>1. The sequence of non-negative functions $f^n \chi_{E_{<1}}$ decreases pointwise to $0$.
    <3>2. If $\int_{E_{<1}} f^{n_0}\,d\mu < \infty$ for some $n_0$, then by the Dominated Convergence Theorem (or Monotone Convergence Theorem applied to $f^{n_0} - f^n$), $\lim_{n\to\infty} \int_{E_{<1}} f^n\,d\mu = 0$.
    <3>3. Even in general, $0 \leq \lim_{n\to\infty} \int_{E_{<1}} f^n\,d\mu \leq \int_{E_{<1}} \lim_{n\to\infty} f^n\,d\mu = 0$ whenever bounded by an integrable envelope.

<1>3. **Case 1: $\mu(E_{>1}) > 0$.**
  <2>1. $E_{>1} = \bigcup_{k=1}^\infty \left\{x \in X : f(x) \geq 1 + \frac{1}{k}\right\}$.
    Proof: Since $f(x) > 1 \iff \exists k \in \NN$ such that $f(x) \geq 1 + 1/k$.
  <2>2. Since $\mu(E_{>1}) > 0$, by countable subadditivity of measure there exists some $k_0 \in \NN$ such that $A_{k_0} \definedas \left\{x \in X : f(x) \geq 1 + \frac{1}{k_0}\right\}$ has positive measure $\mu(A_{k_0}) > 0$.
  <2>3. For all $n \geq 1$:
    $$
    \int_X f^n\,d\mu \geq \int_{A_{k_0}} f^n\,d\mu \geq \left(1 + \frac{1}{k_0}\right)^n \mu(A_{k_0}).
    $$
    Proof: On $A_{k_0}$, $f(x) \geq 1 + 1/k_0 > 1$, so $f(x)^n \geq (1 + 1/k_0)^n$.
  <2>4. $\lim_{n\to\infty} \int_X f^n\,d\mu = \infty$.
    Proof: Since $1 + 1/k_0 > 1$ and $\mu(A_{k_0}) > 0$, $\lim_{n\to\infty} (1 + 1/k_0)^n \mu(A_{k_0}) = \infty$.

<1>4. **Case 2: $\mu(E_{>1}) = 0$ (i.e. $f \leq 1$ a.e.).**
  <2>1. Since $\mu(E_{>1}) = 0$, $\int_{E_{>1}} f^n\,d\mu = 0$ for all $n \geq 1$.
  <2>2. On $X \setminus E_{>1} = E_{<1} \cup E_{=1}$, the sequence $f(x)^n$ converges pointwise:
    $$
    \lim_{n\to\infty} f(x)^n = \chi_{E_{=1}}(x) = \begin{cases} 1 & x \in E_{=1} \\ 0 & x \in E_{<1}. \end{cases}
    $$
  <2>3. Under the assumption that $f \in L^p(X)$ for some $p \geq 1$ or $\mu(X) < \infty$, the Dominated Convergence Theorem applies with dominating function $g = f^p \in L^1(X)$ (for $n \geq p$) or $g = 1 \in L^1(X)$:
    $$
    \lim_{n\to\infty} \int_X f^n\,d\mu = \int_X \lim_{n\to\infty} f(x)^n\,d\mu = \int_X \chi_{E_{=1}}\,d\mu = \mu(E_{=1}) = \mu(f^{-1}(1)).
    $$

<1>5. **Characterization of functions:**
  - **Type $\infty$:** Occurs when $\mu(\{x : f(x) > 1\}) > 0$, or when $f \leq 1$ a.e. but $\int_{E_{<1}} f^n\,d\mu = \infty$ for all $n$.
  - **Type $\mu(f^{-1}(1))$:** Occurs when $f \leq 1$ almost everywhere and $f^k \in L^1(X)$ for some $k \geq 1$.

<1>6. **Conclusion.**
  The limit is fully characterized. Q.E.D.
:::
