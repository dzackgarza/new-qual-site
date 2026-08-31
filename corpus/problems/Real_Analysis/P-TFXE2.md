---
schema: qual/card@1
id: P-TFXE2
kind: problem
title: $Hf(x)\ge\frac{c}{(1+|x|)^n}$ for $0\neq f\in L^1(\RR^n)$
classification:
  areas:
  - real-analysis
  topics:
  - Maximal Functions
  - L¹
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: problem
Let $f\in L^1(\RR^n)$ with $f\neq 0$.

a. Prove that there exists a $c>0$ such that
\[
Hf(x) \geq {c \over (1 + \abs x)^n }
.\]
:::
::: {.solution}
<1>1. Since $f \neq 0$ in $L^1$, there is a ball $B(y,r)$ with $\int_{B(y,r)}|f| > 0$.
    ::: {.proof}
    if $\int_{B}|f| = 0$ for every ball, then by the Lebesgue differentiation theorem $f = 0$ a.e., contradicting $f \neq 0$ in $L^1$. (Equivalently: $\int|f| > 0$ forces a set of positive measure where $|f| > 0$, and a compact set of positive measure inside it is covered by finitely many balls where the integral is positive.)
    :::
<1>2. For every $x$, the ball $B(x, |x-y|+r)$ contains $B(y,r)$.
    ::: {.proof}
    $|z - x| \le |z-y| + |y-x| \le r + |x-y|$ for $z \in B(y,r)$, so $B(y,r) \subseteq B(x, |x-y|+r)$.
    :::
<1>3. Lower bound for $Hf(x)$ in terms of $|x|$.
    ::: {.proof}
    by <1>2,
    :::
    \[
    Hf(x) \ge \frac{1}{|B(x,|x-y|+r)|}\int_{B(x,|x-y|+r)} |f| \ge \frac{C}{\big(|x-y|+r\big)^n}
    \]
    with $C = \frac{\int_{B(y,r)}|f|}{\omega_n} > 0$, where $\omega_n$ is the volume of the unit ball.
<1>4. Conclude: $Hf(x) \ge c/(1+|x|)^n$ for a constant $c > 0$.
    ::: {.proof}
    from <1>3, $|x-y|+r \le |x| + |y| + r$, so
    :::
    \[
    Hf(x) \ge \frac{C}{(|x|+|y|+r)^n} \ge \frac{c}{(1+|x|)^n}
    \]
    with $c = C/(1+|y|+r)^n > 0$, since $1+|x| \le 1+|y|+r+|x| \le (1+|y|+r)(1+|x|)$.
<1>5. Q.E.D.
:::
