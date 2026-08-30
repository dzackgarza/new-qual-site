---
schema: qual/card@1
id: P-PAQ4K
kind: problem
title: Convergence of positive continuous functions and Fatou-type inequality
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
  - Convergence
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

Assume that $f_1, f_2, \ldots$ is a sequence of positive continuous functions defined on $[0,1]$ with

$$f(x) = \lim_{n \to \infty} f_n(x) \text{ for every } x \in [0,1]$$

and

$$\int_0^1 f_n(x) \, dx = 1.$$

(a) Is it always true that $\int_0^1 f(x) \, dx \leq 1$?
Provide a proof if it is true or provide a counterexample if it is false.

(b) Is it always true that $\int_0^1 f(x) \, dx \geq 1$?
Provide a proof if it is true or provide a counterexample if it is false.

::: {.solution}
<1>1. Part (a): **Yes**, it is always true that $\int_0^1 f(x)\,dx \le 1$: <2>1. Each $f_n$ is positive and continuous on $[0, 1]$, hence non-negative and Lebesgue measurable.
Proof: continuous functions on compact intervals are Borel measurable.
<2>2. The pointwise limit $f(x) = \lim_{n \to \infty} f_n(x)$ is non-negative and measurable on $[0, 1]$, with $f(x) = \liminf_{n \to \infty} f_n(x)$.
Proof: pointwise limits of measurable functions are measurable.
<2>3. By Fatou’s Lemma:
\[
\int_0^1 f(x)\,dx = \int_0^1 \liminf_{n \to \infty} f_n(x)\,dx \le \liminf_{n \to \infty} \int_0^1 f_n(x)\,dx.
\]
Proof: Fatou's Lemma for non-negative measurable functions.
<2>4. Since $\int_0^1 f_n(x)\,dx = 1$ for all $n$, the right-hand side is $\liminf_{n \to \infty} 1 = 1$.
Proof: limit of a constant sequence.
<2>5. Therefore $\int_0^1 f(x)\,dx \le 1$.
Proof: <2>3 and <2>4.

<1>2. Part (b): **No**, it is not always true that $\int_0^1 f(x)\,dx \ge 1$: <2>1. We construct a counterexample of strictly positive continuous functions $g_n$ on $[0, 1]$ whose integral is $1$ but whose pointwise limit is $0$.
Proof: counterexample strategy (mass escaping to zero width).
<2>2. For each $n \ge 2$, define the continuous tent function $T_n: [0, 1] \to [0, \infty)$ by:
\[
T_n(x) = \begin{cases} 4n^2 x & 0 \le x \le \frac{1}{2n} \\ 4n - 4n^2 x & \frac{1}{2n} < x \le \frac{1}{n} \\ 0 & \frac{1}{n} < x \le 1. \end{cases}
\]
The area under $T_n$ is the area of a triangle with base $1/n$ and height $2n$: $\int_0^1 T_n(x)\,dx = \frac{1}{2} \cdot \frac{1}{n} \cdot 2n = 1$.
Proof: piecewise linear integration.
<2>3. To ensure strict positivity, define $g_n(x) = \left(1 - \frac{1}{n}\right) T_n(x) + \frac{1}{n}$ for all $x \in [0, 1]$.
Proof: $g_n(x) \ge 1/n > 0$ for all $x \in [0, 1]$.
<2>4. Each $g_n$ is continuous and strictly positive on $[0, 1]$, and its integral is:
\[
\int_0^1 g_n(x)\,dx = \left(1 - \frac{1}{n}\right) \int_0^1 T_n(x)\,dx + \int_0^1 \frac{1}{n}\,dx = \left(1 - \frac{1}{n}\right)(1) + \frac{1}{n} = 1.
\]
Proof: linearity of integration.
<2>5. Determine the pointwise limit $f(x) = \lim_{n \to \infty} g_n(x)$ for every $x \in [0, 1]$:

- For $x = 0$: $T_n(0) = 0$, so $g_n(0) = 1/n \to 0$.

- For any $x \in (0, 1]$: choose $N > 1/x$.
  For all $n \ge N$, $1/n \le 1/N < x$, so $T_n(x) = 0$.
  Thus $g_n(x) = 1/n \to 0$ as $n \to \infty$.
  Proof: evaluation of $T_n(x)$ for large $n$.
  <2>6. Thus $f(x) = 0$ for all $x \in [0, 1]$, which gives:
\[
\int_0^1 f(x)\,dx = \int_0^1 0\,dx = 0 < 1.
\]
Proof: integral of the zero function.
<2>7. This disproves the claim that $\int_0^1 f(x)\,dx \ge 1$.
Proof: $0 \not\ge 1$.

<1>3. Conclusion: (a) True by Fatou’s Lemma.
(b) False: standard escaping spike sequence yields $\int_0^1 f(x)\,dx = 0 < 1$.
Q.E.D. Proof: <1>1 and <1>2.
:::
