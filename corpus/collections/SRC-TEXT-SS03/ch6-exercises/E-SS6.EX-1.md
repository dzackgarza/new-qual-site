---
schema: qual/card@1
id: E-SS6.EX-1
kind: exercise
title: "SS 6.1: Gauss's limit formula for the Gamma function"
classification:
  areas:
  - complex-analysis
  topics: ['Gamma Function', 'Zeta Function', 'Mellin Transform']
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: exercise
1. Prove that

$$
\Gamma (s) = \lim _ {n \to \infty} \frac {n ^ {s} n !}{s (s + 1) \cdots (s + n)}
$$

whenever $s \neq 0 , - 1 , - 2 , . . .$

[Hint: Use the product formula for $1 / \Gamma$ , and the definition of the Euler constant γ.]
:::

::: solution
**Goal:** Prove Gauss's limit formula for the Gamma function:
$$
\Gamma(s) = \lim_{n \to \infty} \frac{n^s n!}{s(s+1)(s+2)\cdots(s+n)} \qquad \text{for } s \in \mathbb{C} \setminus \{0, -1, -2, \dots\}.
$$

<1>1. The Weierstrass product formula for the reciprocal Gamma function:
    *Proof:*
    <2>1. For any $s \in \mathbb{C} \setminus \{0, -1, -2, \dots\}$, the reciprocal Gamma function is given by the entire product
    $$\frac{1}{\Gamma(s)} = s \, e^{\gamma s} \prod_{k=1}^\infty \left(1 + \frac{s}{k}\right) e^{-s/k},$$
    where $\gamma = \lim_{n \to \infty} \left( H_n - \log n \right)$ is the Euler–Mascheroni constant and $H_n = \sum_{k=1}^n \frac{1}{k}$.
    <2>2. Define the $n$-th partial product:
    $$P_n(s) = \prod_{k=1}^n \left(1 + \frac{s}{k}\right) e^{-s/k}.$$
    <2>3. By definition of the infinite product, $\lim_{n \to \infty} P_n(s) = \frac{e^{-\gamma s}}{s \Gamma(s)}$.

<1>2. Algebraic simplification of the partial product:
    *Proof:*
    <2>1. The product of linear factors simplifies to:
    $$\prod_{k=1}^n \left(1 + \frac{s}{k}\right) = \prod_{k=1}^n \frac{s + k}{k} = \frac{(s+1)(s+2)\cdots(s+n)}{n!} = \frac{s(s+1)(s+2)\cdots(s+n)}{s \cdot n!}.$$
    <2>2. The product of exponential factors simplifies to:
    $$\prod_{k=1}^n e^{-s/k} = \exp\left( -s \sum_{k=1}^n \frac{1}{k} \right) = e^{-s H_n}.$$
    <2>3. Combining these factors yields
    $$P_n(s) = \frac{s(s+1)\cdots(s+n)}{s \cdot n!} e^{-s H_n}.$$

<1>3. Introducing the sequence $\gamma_n = H_n - \log n$:
    *Proof:*
    <2>1. Multiply $P_n(s)$ by $s e^{s \gamma_n}$, where $\gamma_n = H_n - \log n$:
    $$s e^{s \gamma_n} P_n(s) = s e^{s(H_n - \log n)} \cdot \left[ \frac{s(s+1)\cdots(s+n)}{s \cdot n!} e^{-s H_n} \right].$$
    <2>2. The $s$ in the numerator and denominator cancel, and the $e^{s H_n}$ and $e^{-s H_n}$ cancel:
    $$s e^{s \gamma_n} P_n(s) = e^{-s \log n} \frac{s(s+1)\cdots(s+n)}{n!} = n^{-s} \frac{s(s+1)\cdots(s+n)}{n!} = \frac{s(s+1)\cdots(s+n)}{n^s n!}.$$

<1>4. Passing to the limit $n \to \infty$:
    *Proof:*
    <2>1. Since $\gamma_n \to \gamma$ as $n \to \infty$, continuity of the exponential function implies $\lim_{n \to \infty} e^{s \gamma_n} = e^{s \gamma}$.
    <2>2. Using step 1.3 for $\lim_{n \to \infty} P_n(s)$:
    $$\lim_{n \to \infty} \frac{s(s+1)\cdots(s+n)}{n^s n!} = \lim_{n \to \infty} \left[ s e^{s \gamma_n} P_n(s) \right] = s e^{\gamma s} \left( \frac{e^{-\gamma s}}{s \Gamma(s)} \right) = \frac{1}{\Gamma(s)}.$$
    <2>3. Since $\Gamma(s) \neq 0$ and $s \notin \{0, -1, -2, \dots\}$, taking the reciprocal of both sides gives:
    $$\Gamma(s) = \lim_{n \to \infty} \frac{n^s n!}{s(s+1)(s+2)\cdots(s+n)}.$$
:::
