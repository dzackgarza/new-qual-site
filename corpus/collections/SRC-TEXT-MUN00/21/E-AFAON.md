---
schema: qual/card@1
id: E-AFAON
kind: problem
title: Arithmetic of convergent sequences
classification:
  areas:
  - topology
  topics:
  - Convergence
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Theorem.
Let $x_n \to x$ and $y_n \to y$ in the space $\mathbb{R}$.
Then

$$
\begin{array}{c}
x_n + y_n \to x + y, \\
x_n - y_n \to x - y, \\
x_n y_n \to xy,
\end{array}
$$

and provided that each $y_n \neq 0$ and $y \neq 0$,

$$
x_n / y_n \to x/y.
$$

[Hint: Apply Lemma 21.4; recall from the exercises of §19 that if $x_n \to x$ and $y_n \to y$, then $x_n \times y_n \to x \times y$.]
:::

::: solution
**Goal:** Prove the algebraic limit theorems for convergent sequences in $\mathbb{R}$ using product convergence and the continuity of arithmetic operations.

<1>1. Product sequence convergence:
    *Proof:*
    <2>1. By the definition of the product topology on $\mathbb{R} \times \mathbb{R}$, a sequence of pairs $(x_n, y_n)_{n=1}^\infty$ converges to $(x, y)$ in $\mathbb{R} \times \mathbb{R}$ if and only if each coordinate sequence converges: $x_n \to x$ and $y_n \to y$ in $\mathbb{R}$.
    <2>2. Hence $(x_n, y_n) \to (x, y)$ in $\mathbb{R}^2$.

<1>2. Sequence Lemma for continuous maps (Lemma 21.4):
    If $F: X \to Y$ is a continuous map between topological spaces and $z_n \to z$ in $X$, then $F(z_n) \to F(z)$ in $Y$.

<1>3. Continuity of arithmetic operations and limit conclusions:
    *Proof:*
    <2>1. **Sum:** The addition map $S: \mathbb{R} \times \mathbb{R} \to \mathbb{R}$ given by $S(u, v) = u + v$ is continuous (for any $\varepsilon > 0$, choosing $\delta = \varepsilon/2$ ensures $|(u+v) - (x+y)| \le |u-x| + |v-y| < \varepsilon$).
        Applying Lemma 21.4 to $S$ yields $x_n + y_n = S(x_n, y_n) \to S(x, y) = x + y$.
    <2>2. **Difference:** The subtraction map $D: \mathbb{R} \times \mathbb{R} \to \mathbb{R}$ given by $D(u, v) = u - v$ is continuous.
        Applying Lemma 21.4 yields $x_n - y_n = D(x_n, y_n) \to D(x, y) = x - y$.
    <2>3. **Product:** The multiplication map $M: \mathbb{R} \times \mathbb{R} \to \mathbb{R}$ given by $M(u, v) = u v$ is continuous (since $|uv - xy| \le |u||v-y| + |y||u-x|$).
        Applying Lemma 21.4 yields $x_n y_n = M(x_n, y_n) \to M(x, y) = xy$.
    <2>4. **Quotient:** The division map $Q: \mathbb{R} \times (\mathbb{R} \setminus \{0\}) \to \mathbb{R}$ given by $Q(u, v) = u / v$ is continuous on the open subset $\mathbb{R} \times (\mathbb{R} \setminus \{0\}) \subset \mathbb{R}^2$.
        Because $y \neq 0$ and each $y_n \neq 0$, the sequence $(x_n, y_n)$ lies in the domain of $Q$ and converges to $(x, y)$.
        Applying Lemma 21.4 yields $x_n / y_n = Q(x_n, y_n) \to Q(x, y) = x / y$.

<1>4. Conclusion:
    All four arithmetic limits hold as stated. Q.E.D.
:::
