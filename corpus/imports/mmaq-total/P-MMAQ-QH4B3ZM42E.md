---
schema: qual/card@1
id: P-MMAQ-QH4B3ZM42E
kind: problem
title: "Let $E \\subset \\RR$ be measurable with $m(E) < \\infty$. Define $f(x)=m(E \\cap(E+x))$ Show that $f\\in L^1(\\RR)$. $f$ is\u2026"
classification:
  areas:
  - real-analysis
  topics:
  - uniform-continuity
  - measure-theory
  - l1
relations: []
review: draft
---

::: problem
Let $E \subset \RR$ be measurable with $m(E) < \infty$.
Define
$$
f(x)=m(E \cap(E+x)).
$$

Show that

1. $f\in L^1(\RR)$.

2. $f$ is uniformly continuous.

3. $\lim _{|x| \rightarrow \infty} f(x)=0$

> Hint:
> $$
> \chi_{E \cap(E+x)}(y)=\chi_{E}(y) \chi_{E}(y-x)
> $$
:::

::: {.solution}
> **AI-Generated Solution**

**Goal:** For measurable $E \subseteq \RR$ with $m(E) < \infty$, show $f(x) = m(E \cap (E+x))$ satisfies: (1) $f \in L^1$; (2) $f$ is uniformly continuous; (3) $\lim_{\abs{x} \to \infty} f(x) = 0$.

<1>1. Rewrite $f$ as a convolution of $L^1$ functions.
    <2>1. $f(x) = \int_\RR \chi_E(y) \chi_E(y-x) ~dy$.
        Proof: By the hint, $\chi_{E \cap (E+x)}(y) = \chi_E(y)\chi_E(y-x)$, and $f(x) = \int \chi_{E \cap (E+x)}(y) ~dy = m(E \cap (E+x))$.
    <2>2. Let $\tilde\chi_E(t) \definedas \chi_E(-t)$; then $f = \chi_E \ast \tilde\chi_E$, where $(\chi_E \ast \tilde\chi_E)(x) = \int \chi_E(y) \tilde\chi_E(x - y) ~dy = \int \chi_E(y) \chi_E(y - x) ~dy$.
        Proof: $\tilde\chi_E(x - y) = \chi_E(y - x)$, so the convolution equals the integral of <2>1.
    <2>3. $\chi_E \in L^1(\RR)$ and $\tilde\chi_E \in L^1(\RR)$.
        Proof: $\int \chi_E = m(E) < \infty$; reflection preserves the integral.
    <2>4. Q.E.D.
        Proof: $f$ is the convolution of two $L^1$ functions.

<1>2. Proof of (1): $f \in L^1(\RR)$.
    <2>1. By Tonelli's theorem,
        $$\int_\RR f(x) ~dx = \int_\RR \int_\RR \chi_E(y) \chi_E(y-x) ~dy ~dx = \int_\RR \chi_E(y) \left(\int_\RR \chi_E(y-x) ~dx\right) ~dy.$$
        Proof: The integrand is nonnegative, so Tonelli applies; both orders of integration are legitimate.
    <2>2. For each fixed $y$, $\int_\RR \chi_E(y-x) ~dx = m(E)$.
        Proof: Change of variables $u = y - x$ (Jacobian $1$).
    <2>3. Hence $\int_\RR f ~dx = \int_\RR \chi_E(y) \cdot m(E) ~dy = m(E) \cdot m(E) = m(E)^2 < \infty$.
        Proof: Combine <2>1 and <2>2.
    <2>4. Q.E.D.
        Proof: $f$ is nonnegative and has finite integral, so $f \in L^1$.

<1>3. Proof of (2): $f$ is uniformly continuous.
    <2>1. $f = \chi_E \ast \tilde\chi_E$ with both factors in $L^1$.
        Proof: By <1>1.
    <2>2. For $f_1, f_2 \in L^1$ with $f_2 \in L^\infty$ (in particular bounded), $f_1 \ast f_2$ is uniformly continuous.
        Proof: This is the standard theorem: $f_1 \ast f_2(x + h) - f_1 \ast f_2(x) = \int f_1(t)(f_2(x + h - t) - f_2(x - t)) ~dt$; one reduces to $f_1 \in C_c^0$ by density (the $\eps/3$ argument) and then uses uniform continuity of the compactly supported factor plus dominated convergence, exactly as in the proof that $f_1 \ast g$ is uniformly continuous for $f_1 \in L^1$, $g \in L^\infty$. Here $\tilde\chi_E$ is bounded by $1$, so the theorem applies.
    <2>3. Q.E.D.
        Proof: $\tilde\chi_E \in L^\infty$ (it takes values in $\{0, 1\}$), so <2>2 applies to $f = \chi_E \ast \tilde\chi_E$.

<1>4. Proof of (3): $f(x) \to 0$ as $\abs{x} \to \infty$.
    <2>1. Write $f(x) = \int_\RR \chi_E(y) \chi_E(y - x) ~dy$; the integrand vanishes unless $y \in E$ and $y - x \in E$, i.e. $y \in E \cap (E + x)$.
        Proof: By <1>1<2>1.
    <2>2. Reduce to bounded $E$: for $\eps > 0$, choose a bounded set $B \subseteq E$ (e.g. $B = E \cap [-R, R]$ for large $R$) with $m(E \setminus B) < \eps/2$.
        Proof: $E = \bigcup_{R} (E \cap [-R, R])$ is an increasing union with finite measure $m(E)$, so $m(E \setminus (E \cap [-R,R])) \to 0$ by continuity from below.
    <2>3. $f(x) \leq m(E \cap (E + x) \cap B \cap (B + x) \text{-related terms})$; more precisely, $f(x) = m(E \cap (E+x)) \leq m(B \cap (B+x)) + m((E\setminus B) \cap (E+x)) + m(E \cap ((E+x)\setminus(B+x)))$.
        Proof: Set-theoretic estimate: $E \cap (E+x) \subseteq (B \cap (B+x)) \cup ((E \setminus B) \cap (E+x)) \cup (E \cap ((E+x) \setminus (B+x)))$; subadditivity of $m$ gives the inequality.
    <2>4. The last two terms are each $\leq m(E \setminus B) < \eps/2$.
        Proof: $(E \setminus B) \cap (E + x) \subseteq E \setminus B$, and $E \cap ((E + x) \setminus (B + x)) \subseteq (E + x) \setminus (B + x) = (E \setminus B) + x$, a translate of $E \setminus B$ with the same measure.
    <2>5. So $f(x) \leq m(B \cap (B + x)) + \eps$ for every $x$.
        Proof: Combine <2>3 and <2>4.
    <2>6. For bounded $B$, $m(B \cap (B + x)) = 0$ once $\abs{x} > \diam(B)$ (with $B$ contained in an interval of length $L$, so $B$ and $B + x$ are disjoint when $\abs{x} > L$).
        Proof: $B \subseteq [-R, R]$ for some $R$; then $B + x \subseteq [-R + x, R + x]$, and these intervals are disjoint when $\abs{x} > 2R$, so the intersection is empty.
    <2>7. Hence $f(x) < \eps$ for all $\abs{x} > 2R$.
        Proof: By <2>5 (with $m(B \cap (B+x)) = 0$) and <2>6.
    <2>8. Q.E.D.
        Proof: $\eps > 0$ was arbitrary, so $f(x) \to 0$ as $\abs{x} \to \infty$.

<1>5. Conclusion.
    Proof: (1), (2), (3) were proved in <1>2, <1>3, <1>4 respectively.
:::
