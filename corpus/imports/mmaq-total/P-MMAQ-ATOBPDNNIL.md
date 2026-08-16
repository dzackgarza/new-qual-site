---
schema: qual/card@1
id: P-MMAQ-ATOBPDNNIL
kind: problem
title: "For $n\\in \\NN$, define $e_{n}=\\left(1+\\frac{1}{n}\\right)^{n} \\quad \\text { and } \\quad E_{n}=\\left(1+\\frac{1}{n}\\right)^{n+1}$"
classification:
  areas:
  - real-analysis
  topics:
  - bernoulli
  - sequences-of-numbers
relations: []
review: draft
---

::: problem
For $n\in \NN$, define
$$
e_{n}=\left(1+\frac{1}{n}\right)^{n} 
\quad \text { and } \quad 
E_{n}=\left(1+\frac{1}{n}\right)^{n+1}
$$

Show that $e_n < E_n$, and prove Bernoulli's inequality:
$$
(1+x)^{n} \geq 1+n x \text { for }-1<x<\infty \text { and } n \in \mathbb{N}
$$

Use this to show the following:

1. The sequence $e_n$ is increasing.

2. The sequence $E_n$ is decreasing.

3. $2 < e_n < E_n < 4$.

4. $\lim _{n \rightarrow \infty} e_{n}=\lim _{n \rightarrow \infty} E_{n}$.
:::

::: {.solution}
> **AI-Generated Solution** (Gemini 3.7 Flash)

**Goal:** For $e_n = (1 + 1/n)^n$ and $E_n = (1 + 1/n)^{n+1}$ ($n \in \NN$):
1. Prove $e_n < E_n$ and Bernoulli's inequality $(1+x)^n \geq 1+nx$ for $x > -1, n \in \NN$.
2. Show $e_n$ is strictly increasing.
3. Show $E_n$ is strictly decreasing.
4. Show $2 \leq e_n < E_n \leq 4$ (and $2 < e_n < E_n < 4$ for $n \geq 2$).
5. Show $\lim_{n\to\infty} e_n = \lim_{n\to\infty} E_n = e$.

<1>1. **$e_n < E_n$ and Bernoulli's Inequality.**
  <2>1. $e_n < E_n$ for all $n \in \NN$.
    Proof: $E_n = e_n \left(1 + \frac{1}{n}\right)$. Since $1 + \frac{1}{n} > 1$ and $e_n > 0$, we have $E_n > e_n$.
  <2>2. Bernoulli's Inequality: $(1+x)^n \geq 1+nx$ for all $x > -1$ and $n \in \NN$.
    Proof by induction on $n$:
    - **Base case $n=1$:** $(1+x)^1 = 1+1x = 1+x$, which holds with equality.
    - **Inductive step:** Assume $(1+x)^k \geq 1+kx$ for some $k \geq 1$. Since $x > -1$, $1+x > 0$. Multiplying both sides by $1+x$:
      $$
      (1+x)^{k+1} \geq (1+kx)(1+x) = 1 + (k+1)x + kx^2 \geq 1 + (k+1)x,
      $$
      since $kx^2 \geq 0$. Thus the statement holds for $k+1$. By mathematical induction, it holds for all $n \in \NN$.

<1>2. **Part 1: The sequence $e_n$ is strictly increasing.**
  <2>1. Consider the ratio $\frac{e_{n+1}}{e_n}$:
    $$
    \frac{e_{n+1}}{e_n} = \frac{\left(1 + \frac{1}{n+1}\right)^{n+1}}{\left(1 + \frac{1}{n}\right)^n} = \left(1 + \frac{1}{n+1}\right) \left( \frac{1 + \frac{1}{n+1}}{1 + \frac{1}{n}} \right)^n = \left(\frac{n+2}{n+1}\right) \left( \frac{\frac{n+2}{n+1}}{\frac{n+1}{n}} \right)^n
    $$
    $$
    = \left(\frac{n+2}{n+1}\right) \left( \frac{n(n+2)}{(n+1)^2} \right)^n = \left(\frac{n+2}{n+1}\right) \left( 1 - \frac{1}{(n+1)^2} \right)^n.
    $$
  <2>2. Apply Bernoulli's inequality with $x = -\frac{1}{(n+1)^2} > -1$:
    $$
    \left( 1 - \frac{1}{(n+1)^2} \right)^n > 1 - \frac{n}{(n+1)^2} = \frac{(n+1)^2 - n}{(n+1)^2} = \frac{n^2 + n + 1}{(n+1)^2}.
    $$
    (Strict inequality holds since $x \neq 0$ and $n \geq 2$, and for $n=1$, $e_2 = 9/4 = 2.25 > 2 = e_1$).
  <2>3. Multiply the factors:
    $$
    \frac{e_{n+1}}{e_n} > \left(\frac{n+2}{n+1}\right) \left(\frac{n^2+n+1}{(n+1)^2}\right) = \frac{n^3 + 3n^2 + 3n + 2}{(n+1)^3} = \frac{(n+1)^3 + 1}{(n+1)^3} = 1 + \frac{1}{(n+1)^3} > 1.
    $$
  <2>4. Thus $e_{n+1} > e_n$ for all $n \in \NN$, so $\{e_n\}$ is strictly increasing.

<1>3. **Part 2: The sequence $E_n$ is strictly decreasing.**
  <2>1. Consider the ratio $\frac{E_{n-1}}{E_n}$ for $n \geq 2$:
    $$
    \frac{E_{n-1}}{E_n} = \frac{\left(1 + \frac{1}{n-1}\right)^n}{\left(1 + \frac{1}{n}\right)^{n+1}} = \left(\frac{n}{n-1}\right)^n \left(\frac{n}{n+1}\right)^{n+1} = \left(\frac{n}{n+1}\right) \left( \frac{n^2}{n^2-1} \right)^n = \left(\frac{n}{n+1}\right) \left( 1 + \frac{1}{n^2-1} \right)^n.
    $$
  <2>2. Apply Bernoulli's inequality with $x = \frac{1}{n^2-1} > 0$:
    $$
    \left(1 + \frac{1}{n^2-1}\right)^n > 1 + \frac{n}{n^2-1}.
    $$
  <2>3. Multiply the factors:
    $$
    \frac{E_{n-1}}{E_n} > \left(\frac{n}{n+1}\right) \left( 1 + \frac{n}{n^2-1} \right) = \left(\frac{n}{n+1}\right) \left(\frac{n^2+n-1}{n^2-1}\right) = \frac{n^3 + n^2 - n}{(n+1)(n^2-1)} = \frac{n^3 + n^2 - n}{n^3 + n^2 - n - 1} > 1.
    $$
  <2>4. Thus $E_{n-1} > E_n$ for all $n \geq 2$, so $\{E_n\}$ is strictly decreasing.

<1>4. **Part 3: Bounds $2 \leq e_1 < e_n < E_n < E_1 = 4$.**
  <2>1. $e_1 = (1 + 1)^1 = 2$ and $E_1 = (1 + 1)^2 = 4$.
  <2>2. For any $n \geq 2$, by strict monotonicity:
    $$
    2 = e_1 < e_n < E_n < E_1 = 4.
    $$
    Proof: By <1>2, $e_n > e_1 = 2$. By <1>1, $e_n < E_n$. By <1>3, $E_n < E_1 = 4$.

<1>5. **Part 4: $\lim_{n\to\infty} e_n = \lim_{n\to\infty} E_n$.**
  <2>1. The sequence $\{e_n\}$ is increasing and bounded above by $4$, so by the Monotone Convergence Theorem for real sequences, $\lim_{n\to\infty} e_n = L$ exists and is finite.
  <2>2. $E_n = e_n \left(1 + \frac{1}{n}\right)$.
  <2>3. Taking limits as $n \to \infty$:
    $$
    \lim_{n\to\infty} E_n = \lim_{n\to\infty} \left[ e_n \left(1 + \frac{1}{n}\right) \right] = \left(\lim_{n\to\infty} e_n\right) \left(\lim_{n\to\infty} \left(1 + \frac{1}{n}\right)\right) = L \cdot 1 = L.
    $$
    Proof: By algebraic limit laws for products of convergent sequences.

<1>6. **Conclusion.**
  All parts 1 through 4 are proved rigorously. Q.E.D.
:::
