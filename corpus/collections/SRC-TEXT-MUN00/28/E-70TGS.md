---
schema: qual/card@1
id: E-70TGS
kind: problem
title: Shrinking maps and contractions on compact metric spaces
classification:
  areas:
  - topology
  topics:
  - Compactness
  - Metric Spaces
relations: []
review: draft
audit:
- event: solution-written
  by: Gemini 3.7 Flash
  date: 2026-08-29
---

::: {.exercise}

Let $(X, d)$ be a metric space.
If $f$ satisfies the condition

$$
d(f(x), f(y)) < d(x, y)
$$

for all $x, y \in X$ with $x \neq y$, then $f$ is called a shrinking map.
If there is a number $\alpha < 1$ such that

$$
d(f(x), f(y)) \leq \alpha d(x, y)
$$

for all $x, y \in X$, then $f$ is called a contraction.
A fixed point of $f$ is a point $x$ such that $f(x) = x$.

(a) If $f$ is a contraction and $X$ is compact, show $f$ has a unique fixed point.
[Hint: Define $f^1 = f$ and $f^{n+1} = f \circ f^n$. Consider the intersection $A$ of the sets $A_n = f^n(X)$.]

(b) Show more generally that if $f$ is a shrinking map and $X$ is compact, then $f$ has a unique fixed point.
[Hint: Let $A$ be as before. Given $x \in A$, choose $x_n$ so that $x = f^{n+1}(x_n)$. If $a$ is the limit of some subsequence of the sequence $y_n = f^n(x_n)$, show that $a \in A$ and $f(a) = x$. Conclude that $A = f(A)$, so that $\operatorname{diam} A = 0$.]

(c) Let $X = [0, 1]$.
Show that $f(x) = x - x^2/2$ maps $X$ into $X$ and is a shrinking map that is not a contraction.
[Hint: Use the mean-value theorem of calculus.]

(d) The result in (a) holds if $X$ is a complete metric space, such as $\mathbb{R}$; see the exercises of §43. The result in (b) does not: show that the map $f: \mathbb{R} \to \mathbb{R}$ given by $f(x) = [x + (x^2 + 1)^{1/2}]/2$ is a shrinking map that is not a contraction and has no fixed point.
:::

::: solution
**Goal:** Prove the existence and uniqueness of fixed points for contractions and shrinking maps on compact metric spaces, and analyze explicit counterexamples on non-compact and non-contraction spaces.

<1>1. Part (a): Contractions on compact metric spaces have a unique fixed point.
    *Proof:*
    <2>1. Define $A_n = f^n(X)$ for each $n \ge 1$. Since $X$ is compact and $f$ is continuous, each $A_n$ is a non-empty compact set, and $A_{n+1} = f(A_n) \subseteq A_n$.
    <2>2. The intersection $A = \bigcap_{n=1}^\infty A_n$ is non-empty by the finite intersection property of compact spaces.
    <2>3. For any $n \ge 1$, the contraction bound gives $\operatorname{diam}(A_n) \le \alpha^n \operatorname{diam}(X)$. Since $\alpha < 1$, $\operatorname{diam}(A_n) \to 0$ as $n \to \infty$.
    <2>4. Hence $\operatorname{diam}(A) = 0$, so $A = \{x_0\}$ is a singleton.
    <2>5. Since $f(A) \subseteq \bigcap_{n=1}^\infty f(A_n) = \bigcap_{n=1}^\infty A_{n+1} = A$, $f(x_0) \in A$, which forces $f(x_0) = x_0$.
    <2>6. If $x \neq y$ were two distinct fixed points, $d(x, y) = d(f(x), f(y)) \le \alpha d(x, y) < d(x, y)$, a contradiction. Thus the fixed point is unique.

<1>2. Part (b): Shrinking maps on compact metric spaces have a unique fixed point (Edelstein's Theorem).
    *Proof:*
    <2>1. Consider the function $g: X \to \mathbb{R}$ defined by $g(x) = d(x, f(x))$.
    <2>2. Since $f$ is continuous and the metric $d$ is continuous, $g$ is continuous.
    <2>3. Because $X$ is compact, by the Extreme Value Theorem there exists a point $x_0 \in X$ at which $g$ attains its absolute minimum: $g(x_0) \le g(x)$ for all $x \in X$.
    <2>4. Suppose for contradiction that $x_0 \neq f(x_0)$. Let $y_0 = f(x_0)$.
    <2>5. Because $f$ is a shrinking map and $x_0 \neq y_0$:
        $$g(y_0) = d(y_0, f(y_0)) = d(f(x_0), f(y_0)) < d(x_0, y_0) = d(x_0, f(x_0)) = g(x_0).$$
    <2>6. This contradicts the minimality of $g(x_0)$, so $x_0 = f(x_0)$.
    <2>7. Uniqueness follows because if $x \neq y$ were two fixed points, $d(x, y) = d(f(x), f(y)) < d(x, y)$, impossible.

<1>3. Part (c): $f(x) = x - x^2/2$ on $[0, 1]$ is a shrinking map but not a contraction.
    *Proof:*
    <2>1. The derivative is $f'(x) = 1 - x$. For $x \in [0, 1]$, $0 \le f'(x) \le 1$, and $f(0) = 0, f(1) = 1/2$, so $f([0, 1]) = [0, 1/2] \subseteq [0, 1]$.
    <2>2. For distinct $x, y \in [0, 1]$ with $x < y$, the Mean Value Theorem gives:
        $$|f(y) - f(x)| = f'(c)|y - x| = (1 - c)|y - x|$$
        for some $c \in (x, y)$. Since $c > x \ge 0$, $1 - c < 1$, so $|f(y) - f(x)| < |y - x|$. Thus $f$ is a shrinking map.
    <2>3. Since $\lim_{x \to 0^+} \frac{f(x) - f(0)}{x - 0} = f'(0) = 1$, $\sup_{x \neq y} \frac{|f(x) - f(y)|}{|x - y|} = 1$, so no constant $\alpha < 1$ exists. Thus $f$ is not a contraction.

<1>4. Part (d): $f(x) = \frac{x + \sqrt{x^2+1}}{2}$ on $\mathbb{R}$ is a shrinking map without fixed points.
    *Proof:*
    <2>1. The derivative is $f'(x) = \frac{1}{2}\left(1 + \frac{x}{\sqrt{x^2+1}}\right)$.
    <2>2. Since $|x| < \sqrt{x^2+1}$, we have $-1 < \frac{x}{\sqrt{x^2+1}} < 1$, which implies $0 < f'(x) < 1$ for all $x \in \mathbb{R}$.
    <2>3. By the Mean Value Theorem, $|f(x) - f(y)| = f'(c)|x - y| < |x - y|$ for all $x \neq y$, so $f$ is a shrinking map.
    <2>4. Since $\lim_{x \to \infty} f'(x) = 1$, $f$ is not a contraction.
    <2>5. Setting $f(x) = x$ gives $\frac{x + \sqrt{x^2+1}}{2} = x \iff \sqrt{x^2+1} = x$, which has no real solutions (since $x^2 + 1 > x^2 \ge 0$). Thus $f$ has no fixed point. Q.E.D.
:::
