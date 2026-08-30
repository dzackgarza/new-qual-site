---
schema: qual/card@1
id: P-RASP13D
kind: problem
title: "Pointwise limit of bounded linear operators between Banach spaces is bounded"
classification:
  areas:
  - real-analysis
  topics:
  - Banach Spaces
  - Bounded Operators
  - Uniform Boundedness Principle
relations: []
review: draft
audit:
- event: solution-written
  by: muse-spark-1.2
  date: 2026-08-30
---

::: problem
Let $X$ and $Y$ be two Banach spaces and denote by $L(X, Y)$ the space of all continuous linear operators from $X$ to $Y$.
Let $A_n \in L(X, Y)$ ($n = 1, 2, \ldots$). Assume that $\lim_{n \to \infty} A_n(x)$ exists for each $x \in X$.
Define $A(x) = \lim_{n \to \infty} A_n(x)$.
Prove that $A \in L(X, Y)$.
:::

::: {.solution}
<1>1. Linearity of the limit operator $A$:
<2>1. For any $x_1, x_2 \in X$ and scalars $\alpha, \beta \in \mathbb{C}$ (or $\mathbb{R}$):
\[
\begin{aligned}
A(\alpha x_1 + \beta x_2) &= \lim_{n \to \infty} A_n(\alpha x_1 + \beta x_2) \\
&= \lim_{n \to \infty} \big( \alpha A_n(x_1) + \beta A_n(x_2) \big) \\
&= \alpha \lim_{n \to \infty} A_n(x_1) + \beta \lim_{n \to \infty} A_n(x_2) \\
&= \alpha A(x_1) + \beta A(x_2).
\end{aligned}
\]
Thus $A: X \to Y$ is linear.
Proof: linearity of each $A_n$ and linearity of limits in $Y$.

<1>2. Uniform bound via Banach–Steinhaus Theorem:
<2>1. For each fixed $x \in X$, the sequence $(A_n(x))_{n=1}^\infty$ converges in $Y$.
Every convergent sequence in a normed space is bounded:
\[
\sup_{n \ge 1} \|A_n(x)\|_Y < \infty \quad \text{for each } x \in X.
\]
Proof: convergent sequences in metric spaces are bounded.
<2>2. Since $X$ is a Banach space and $Y$ is a normed space, by the Uniform Boundedness Principle (Banach–Steinhaus Theorem), pointwise boundedness implies uniform boundedness in operator norm:
\[
M := \sup_{n \ge 1} \|A_n\|_{L(X, Y)} < \infty.
\]
Proof: Uniform Boundedness Principle.

<1>3. Continuity of $A$:
<2>1. For any $x \in X$, by continuity of the norm $\|\cdot\|_Y$:
\[
\|A(x)\|_Y = \left\| \lim_{n \to \infty} A_n(x) \right\|_Y = \lim_{n \to \infty} \|A_n(x)\|_Y \le \limsup_{n \to \infty} \|A_n\|_{L(X, Y)} \|x\|_X \le M \|x\|_X.
\]
Proof: continuity of norm and definition of operator norm.
<2>2. Thus $\|A\|_{L(X, Y)} = \sup_{\|x\|_X \le 1} \|A(x)\|_Y \le M < \infty$.
Hence $A$ is a bounded (continuous) linear operator.
Proof: characterization of continuous linear operators.

<1>4. Conclusion:
$A \in L(X, Y)$. Q.E.D.
Proof: <1>1 and <1>3.
:::
