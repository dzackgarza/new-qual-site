---
schema: qual/card@1
id: P-CALCPT3-32
kind: problem
title: "Which of four subsets of $\\RR$ are subfields"
classification:
  areas: [prelim]
  topics: [Fields]
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-10-30
  note: "Transcribed from Question 32 of assets/attachments/calculus_practice_test3.pdf and checked against its MinerU Flash extraction; they agree. The source names the reals, rationals and integers R, Q, Z."
---

::: {.problem}
Which of the following subsets $F_i$ of $\RR$, $1\le i\le 4$, are subfields of $\RR$?
$$
\begin{aligned}
F_1&=\{a/b : a,b\in\ZZ \text{ and } b \text{ is odd}\}\\
F_2&=\{a+b\sqrt2 : a,b\in\ZZ\}\\
F_3&=\{a+b\sqrt2 : a,b\in\QQ\}\\
F_4&=\{a+b\sqrt[4]{2} : a,b\in\QQ\}
\end{aligned}
$$

(A) No $F_i$ is a subfield of $\RR$.
(B) $F_3$ only
(C) $F_2$ and $F_3$ only
(D) $F_1$, $F_2$, and $F_3$ only
(E) $F_1$, $F_2$, $F_3$, and $F_4$
:::

::: {.solution}
A subfield of $\RR$ must contain the multiplicative inverse of each of its nonzero elements.

::: pf

::: {.pf-step #F1}
$F_1$ is not a subfield.

::: pf-proof
$2=2/1\in F_1$. If $\frac12=a/b$ with $b$ odd, then $b=2a$ is even, a contradiction. So $\frac12\notin F_1$.
:::

:::

::: {.pf-step #F2}
$F_2$ is not a subfield.

::: pf-proof
$2\in F_2$. If $\frac12=a+b\sqrt2$ with $a,b\in\ZZ$, then $b=0$ because $\sqrt2$ is irrational, so $a=\frac12\notin\ZZ$, a contradiction.
:::

:::

::: {.pf-step #F3}
$F_3$ is a subfield.

::: pf-proof
$F_3$ contains $0$ and $1$ and is closed under addition, negation, and multiplication, since $(a+b\sqrt2)(c+d\sqrt2)=(ac+2bd)+(ad+bc)\sqrt2$. For $a+b\sqrt2\ne0$ with $a,b\in\QQ$, the rational number $a^2-2b^2$ is nonzero because $\sqrt2$ is irrational, and
$$\frac1{a+b\sqrt2}=\frac{a}{a^2-2b^2}-\frac{b}{a^2-2b^2}\sqrt2\in F_3.$$
:::

:::

::: {.pf-step #F4}
$F_4$ is not a subfield.

::: pf-proof
$\sqrt[4]2\in F_4$, but $(\sqrt[4]2)^2=\sqrt2\notin F_4$. Indeed, $x^4-2$ is irreducible over $\QQ$ by Eisenstein at $2$, so $1,\sqrt[4]2,\sqrt2$ are linearly independent over $\QQ$, and $\sqrt2=a+b\sqrt[4]2$ has no solution with $a,b\in\QQ$. So $F_4$ is not closed under multiplication.
:::

:::

::: pf-step
The answer is $\boxed{F_3\text{ only}}$, choice (B).

::: pf-proof
By steps [](#F1){.pf-ref} through [](#F4){.pf-ref}, exactly $F_3$ is a subfield. This rules out (A), which excludes $F_3$, and (C), (D), (E), which include $F_2$.
:::

:::

:::

:::
