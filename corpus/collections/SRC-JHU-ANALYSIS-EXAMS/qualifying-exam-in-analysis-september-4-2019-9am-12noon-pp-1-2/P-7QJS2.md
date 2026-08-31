---
schema: qual/card@1
id: P-7QJS2
kind: problem
title: "A holomorphic function on the punctured disk dominated by a power of the logarithm"
classification:
  areas:
  - complex-analysis
  topics:
  - Isolated Singularities
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

4. Let f be a holomorphic function in the punctured disk $\{ z : 0 < | z | < 2 \}$ satisfying

$$
| f ( z ) | \leq ( \log { \frac { 1 } { | z | } } ) ^ { 1 0 0 } \mathrm { { i n } } \left\{ | z | \leq 1 / 2 \right\} ,
$$

$$
| f ( z ) | = 1 \ \mathrm { o n } \ | z | = 1 .
$$

a. Show that f has a removable singularity at the origin.

b. Show that if $f ( z ) \neq 0$ in $| z | < 1$ , then f is constant.

c. (Extra credit) True or false, explain.

$f = \alpha z ^ { n }$ for $\alpha \in \mathbb { C } , | \alpha | = 1$ and an integer $n \geq 0$

::: {.solution}
**(a).**

<1>1. On $|z| \le 1/2$, $|f(z)| \le (\log \frac{1}{|z|})^{100}$.
::: {.proof}
hypothesis.
:::

<1>2. $\lim_{z \to 0} |z| \cdot |f(z)| \le \lim_{z \to 0} |z| (\log \frac{1}{|z|})^{100} = 0$.
::: {.proof}
<1>1 and the fact that $|z|(\log(1/|z|))^{100} \to 0$ as $|z| \to 0$ (the logarithm grows slower than any negative power).
:::

<1>3. Hence $|z f(z)| \to 0$ as $z \to 0$, so $f$ has a removable singularity at $0$ (by Riemann's removable singularity theorem, since $f$ is bounded by $o(1/|z|)$).
::: {.proof}
<1>2; a function with $|f(z)| = o(1/|z|)$ has a removable singularity.
:::

**(b).**

<1>1. By (a), $f$ extends to a holomorphic function on $|z| < 2$, still denoted $f$.
::: {.proof}
(a).
:::

<1>2. $|f(z)| = 1$ on $|z| = 1$, and $f$ is holomorphic on $|z| \le 1$.
::: {.proof}
hypothesis and <1>1.
:::

<1>3. If $f(z) \neq 0$ in $|z| < 1$, then $1/f$ is holomorphic on $|z| < 1$ and $|1/f(z)| = 1$ on $|z| = 1$.
::: {.proof}
<1>2 and the nonvanishing hypothesis.
:::

<1>4. By the maximum modulus principle, $|f(z)| \le 1$ and $|1/f(z)| \le 1$ on $|z| < 1$, so $|f(z)| = 1$ on $|z| < 1$.
::: {.proof}
<1>2 and <1>3 (both $f$ and $1/f$ attain their maximum modulus on the boundary, where it is $1$).
:::

<1>5. Hence $f$ has constant modulus $1$ on the connected domain $|z| < 1$, so $f$ is constant.
::: {.proof}
<1>4 (a holomorphic function with constant modulus is constant).
:::

**(c).**

<1>1. The statement is **true**.
::: {.proof}
by (b), if $f(z) \neq 0$ in $|z| < 1$ then $f$ is constant.
:::

<1>2. Hence $f = \alpha$ for some $\alpha \in \mathbb{C}$ with $|\alpha| = 1$ (since $|f| = 1$ on $|z| = 1$).
::: {.proof}
<1>1 and the boundary condition.
:::

<1>3. This is exactly $f = \alpha z^n$ with $n = 0$.
::: {.proof}
<1>2.
:::

<1>4. Q.E.D.
::: {.proof}
<1>3 (a), <1>5 (b), <1>3 (c).
:::
:::
