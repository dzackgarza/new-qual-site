---
schema: qual/card@1
id: P-GREPT-49
kind: problem
title: "Limit of the recursion $x_{n+1}=\\frac12(x_n+2/x_n)$"
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 49 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
The value of the first term, $x_1$, of a sequence $(x_n)$ of real numbers is unknown, but it is known that $x_1$ is not zero. Furthermore, for every integer $n \ge 1$, the following recursion relation holds true:

$$x_{n+1} = \frac{1}{2} \left( x_n + \frac{2}{x_n} \right)$$

Which of the following statements is true about this sequence?

(A) The sequence diverges if $x_1 < 0$ and converges to $1$ if $x_1 > 0$.
(B) The sequence diverges if $x_1 < 0$ and converges to $\sqrt{2}$ if $x_1 > 0$.
(C) The sequence converges to $-1$ if $x_1 < 0$ and converges to $\sqrt{2}$ if $x_1 > 0$.
(D) The sequence converges to $-\sqrt{2}$ if $x_1 < 0$ and converges to $\sqrt{2}$ if $x_1 > 0$.
(E) The sequence diverges for any $x_1 \neq 0$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

If $x_1>0$, then every $x_n>0$ and
$$
x_n\ge\sqrt2
$$
for every $n\ge2$.


::: pf-proof

If $x_n>0$, then both $x_n$ and $2/x_n$ are positive, so $x_{n+1}>0$.
Thus positivity is preserved. Moreover, for positive $t$,
$$
\frac12\left(t+\frac2t\right)\ge\sqrt{t\cdot\frac2t}=\sqrt2
$$
by the arithmetic--geometric mean inequality. Applying this with $t=x_n$
gives the bound for every $n\ge2$.

:::

:::

::: {.pf-step #s1-2}

If $x_1>0$, the tail $(x_n)_{n\ge2}$ is nonincreasing.


::: pf-proof

For $n\ge2$, step [](#s1-1){.pf-ref} gives $x_n\ge\sqrt2$. Hence
$$
x_{n+1}-x_n
=\frac12\left(x_n+\frac2{x_n}\right)-x_n
=\frac{2-x_n^2}{2x_n}
\le0.
$$

:::

:::

::: {.pf-step #s1-3}

If $x_1>0$, then
$$
x_n\longrightarrow\sqrt2.
$$


::: pf-proof

By steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref}, the tail is decreasing and bounded below by $\sqrt2$,
so it converges to some $L\ge\sqrt2$. Passing to the limit in the continuous
recursion gives
$$
L=\frac12\left(L+\frac2L\right),
$$
so $L^2=2$. Since $L>0$, one has $L=\sqrt2$.

:::

:::

::: {.pf-step #s1-4}

If $x_1<0$, then
$$
x_n\longrightarrow-\sqrt2.
$$


::: pf-proof

Set $y_n=-x_n$. Since $x_1<0$, one has $y_1>0$. Directly from the recursion,
$$
y_{n+1}
=-x_{n+1}
=\frac12\left(y_n+\frac2{y_n}\right).
$$
Thus $(y_n)$ satisfies the positive recursion treated in step [](#s1-3){.pf-ref}, so
$y_n\to\sqrt2$ and therefore $x_n=-y_n\to-\sqrt2$.

:::

:::

::: {.pf-step #s1-5}

Therefore the true statement is
$$
\boxed{\text{(D)}}.
$$


::: pf-proof

Steps [](#s1-3){.pf-ref} through [](#s1-4){.pf-ref} give exactly the two sign-dependent limits stated in choice
(D).

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} gives the required choice.

:::

:::

:::
