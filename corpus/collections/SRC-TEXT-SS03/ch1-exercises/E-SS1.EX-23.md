---
schema: qual/card@1
id: E-SS1.EX-23
kind: problem
title: A smooth function whose Taylor series at $0$ vanishes identically
classification:
  areas:
    - complex-analysis
  topics: [Taylor Series, Counterexamples]
relations: []
review: draft
audit:
  - event: solution-written
    by: gpt-5.6-sol
    date: 2026-09-10
  - event: solution-written
    by: claude
    date: 2026-11-18
    note: >-
      Restructured as a Lamport proof of the argument already on the card, whose three
      ingredients (the form P_n(1/x)e^{-1/x^2}, the exponential decay of every power, and the
      induction at the origin) are correct. Added: the recursion P_{n+1}(t) = -t^2 P_n'(t) +
      2t^3 P_n(t) written explicitly; the series inequality that gives t^m e^{-t^2} -> 0; the
      statement that the derivatives are identically zero on the negative axis, which the
      induction uses for the left-hand difference quotient; and the reason a convergent power
      series has coefficients f^{(n)}(0)/n!. Not claimed: a retained solution set; the
      collection's provenance is the Stein--Shakarchi textbook, and the argument is the card's
      own.
---

::: {.exercise}
Consider the function $f$ defined on $\RR$ by
$$
f(x) = \begin{cases} 0 & \text{if } x \leq 0, \\ e^{-1/x^2} & \text{if } x > 0. \end{cases}
$$
Prove that $f$ is indefinitely differentiable on $\RR$, and that $f^{(n)}(0) = 0$ for all $n \geq 1$. Conclude that $f$ does not have a converging power series expansion $\sum_{n=0}^{\infty} a_n x^n$ for $x$ near the origin.
:::

::: {.solution}
Throughout $f(x) = 0$ for $x \le 0$ and $f(x) = e^{-1/x^{2}}$ for $x > 0$. The exercise is Exercise 23 of Stein--Shakarchi, *Complex Analysis*, Chapter 1.

::: pf

::: {.pf-step #form}
For every $n \ge 0$ and every $x > 0$ there is a polynomial $P_{n}$ with $f^{(n)}(x) = P_{n}(1/x)e^{-1/x^{2}}$.

::: pf-proof
Induction on $n$. For $n = 0$ take $P_{0} = 1$. If $f^{(n)}(x) = P_{n}(1/x)e^{-1/x^{2}}$, the product and chain rules give $f^{(n+1)}(x) = \bigl[-x^{-2}P_{n}'(1/x) + 2x^{-3}P_{n}(1/x)\bigr]e^{-1/x^{2}}$, and with $t = 1/x$ the bracket is $-t^{2}P_{n}'(t) + 2t^{3}P_{n}(t)$, a polynomial in $t$; so $P_{n+1}(t) = -t^{2}P_{n}'(t) + 2t^{3}P_{n}(t)$ serves.

:::

:::

::: {.pf-step #decay}
For every integer $m \ge 0$, $\lim_{x \downarrow 0}x^{-m}e^{-1/x^{2}} = 0$.

::: pf-proof
With $t = 1/x \to +\infty$ the expression is $t^{m}e^{-t^{2}}$, and the exponential dominates every power: $t^{m}e^{-t^{2}} \le t^{m}\big/\bigl(t^{m+2}/(m+2)!\bigr) \to 0$, using $e^{t^{2}} \ge t^{m+2}/(m+2)!$ from the series of the exponential.

:::

:::

::: {.pf-step #right}
For every $n \ge 0$, $f^{(n)}(x) \to 0$ as $x \downarrow 0$, and $f$ is $C^{\infty}$ on $(0,\infty)$ with $f^{(n)} = 0$ on $(-\infty,0)$.

::: pf-proof
The first assertion is steps [](#form){.pf-ref} and [](#decay){.pf-ref}: $P_{n}(1/x)$ is a finite sum of terms $c_{k}x^{-k}$, each of which tends to $0$ after multiplication by $e^{-1/x^{2}}$. The second is that $e^{-1/x^{2}}$ is a composition of smooth functions on $(0,\infty)$, and that the constant $0$ is smooth on $(-\infty,0)$.

:::

:::

::: {.pf-step #at-zero}
$f$ is $C^{\infty}$ on $\RR$ with $f^{(n)}(0) = 0$ for every $n \ge 0$.

::: pf-proof
Induction on $n$, the assertion at stage $n$ being that $f^{(n)}$ exists everywhere and is continuous at $0$ with $f^{(n)}(0) = 0$. For $n = 0$ this is step [](#right){.pf-ref}. Assume it for $n$. On $(-\infty,0)$ the difference quotient of $f^{(n)}$ at $0$ from the left is $0$, since $f^{(n)} = 0$ there. From the right, using step [](#form){.pf-ref}, $\frac{f^{(n)}(h) - f^{(n)}(0)}{h} = h^{-1}P_{n}(1/h)e^{-1/h^{2}} \to 0$ by step [](#decay){.pf-ref} applied to the polynomial $t \mapsto tP_{n}(t)$ in the variable $t = 1/h$. So $f^{(n+1)}(0)$ exists and equals $0$, and step [](#right){.pf-ref} gives continuity of $f^{(n+1)}$ at $0$.

:::

:::

::: pf-step
$f$ has no converging power series expansion about the origin: no $\sum_{n \ge 0}a_{n}x^{n}$ converges to $f$ on a neighbourhood of $0$.

::: pf-proof
Suppose $\sum_{n}a_{n}x^{n}$ converges to $f(x)$ for $\abs{x} < r$. A function represented by a convergent power series is $C^{\infty}$ there, with $a_{n} = f^{(n)}(0)/n!$; by step [](#at-zero){.pf-ref} every $a_{n} = 0$. Then the sum is the zero function on $(-r,r)$, while $f(x) = e^{-1/x^{2}} > 0$ for $0 < x < r$, a contradiction.

:::

:::

:::
:::
