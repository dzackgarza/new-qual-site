---
schema: qual/card@1
id: E-SS10.EX-3
kind: exercise
title: "More generally, consider the diference equation given by the initial values u<su"
classification:
  areas:
  - complex-analysis
  topics: ['Theta Functions', 'Modular Forms', 'Partitions']
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-30
---

::: exercise
3. More generally, consider the diference equation given by the initial values u<sub>0</sub> and $u _ { 1 }$ , and the recurrence relation $u _ { n } = a u _ { n - 1 } + b u _ { n - 2 }$ for $n \geq 2$ . Define the generating function associated to $\{ u _ { n } \} _ { n = 0 } ^ { \infty }$ by $\textstyle U ( x ) = \sum _ { n = 0 } ^ { \infty } u _ { n } x ^ { n }$ . The recurrence relation implies that $U ( x ) ( 1 - a x - b x ^ { 2 } ) = u _ { 0 } + ( u _ { 1 } - a u _ { 0 } ) x$ in a neighborhood of the origin.
   If α and $\beta$ denote the roots of the polynomial $p ( x ) = x ^ { 2 } - a x - b ;$ then we may write

Figure 2. Appearance of the golden mean

$$
U (x) = \frac {u _ {0} + (u _ {1} - a u _ {0}) x}{(1 - \alpha x) (1 - \beta x)} = \frac {A}{1 - \alpha x} + \frac {B}{(1 - \beta x)} = A \sum_ {n = 0} ^ {\infty} \alpha^ {n} x ^ {n} + B \sum_ {n = 0} ^ {\infty} \beta^ {n} x ^ {n},
$$

where it is an easy matter to solve for A and B. Finally, this gives $u _ { n } = A \alpha ^ { n } +$ $B \beta ^ { n }$ . Note that this approach yields a solution to our problem if the roots of $p$ are distinct, namely $\alpha \neq \beta$ . A variant of the formula holds if $\alpha = \beta$
:::

::: {.solution}
<1>1. The recurrence $u_n = a u_{n-1} + b u_{n-2}$ gives, for the generating function $U(x) = \sum_{n \ge 0} u_n x^n$,
$$U(x)(1 - ax - bx^2) = u_0 + (u_1 - a u_0)x.$$
::: {.proof}
multiply the recurrence by $x^n$ and sum over $n \ge 2$, then rearrange.
:::

<1>2. Hence $U(x) = \frac{u_0 + (u_1 - a u_0)x}{1 - ax - bx^2}$.
::: {.proof}
<1>1.
:::

<1>3. The denominator factors as $1 - ax - bx^2 = (1 - \alpha x)(1 - \beta x)$, where $\alpha, \beta$ are the roots of $x^2 - ax - b$.
::: {.proof}
$x^2 - ax - b = (x - \alpha)(x - \beta)$, so $1 - ax - bx^2 = (1 - \alpha x)(1 - \beta x)$.
:::

<1>4. If $\alpha \neq \beta$, partial fractions give $U(x) = \frac{A}{1 - \alpha x} + \frac{B}{1 - \beta x}$ for constants $A, B$.
::: {.proof}
<1>2 and <1>3.
:::

<1>5. Expanding, $U(x) = A \sum_{n \ge 0} \alpha^n x^n + B \sum_{n \ge 0} \beta^n x^n$, so $u_n = A \alpha^n + B \beta^n$.
::: {.proof}
<1>4 and comparing coefficients.
:::

<1>6. If $\alpha = \beta$, then $U(x) = \frac{A}{1 - \alpha x} + \frac{B}{(1 - \alpha x)^2}$, giving $u_n = (A + B(n+1))\alpha^n$.
::: {.proof}
the repeated-root partial fraction decomposition.
:::

<1>7. Q.E.D.
::: {.proof}
<1>5 and <1>6.
:::
:::
