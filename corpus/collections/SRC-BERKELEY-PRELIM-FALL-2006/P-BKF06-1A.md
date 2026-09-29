---
schema: qual/card@1
id: P-BKF06-1A
kind: problem
title: Fourth derivative of $x/\sin x$ at $0$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against Problem 1A of the retained Berkeley Fall 2006 preliminary-exam solution packet f06solution.pdf.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Taylor coefficient 7/360. The proof
    below makes the removable analytic extension at zero explicit, so the
    fourth-derivative limit follows from the Taylor coefficient rather than
    from differentiating an asymptotic remainder.
---

::: {.problem}
Compute
\[
\lim_{x\to0}\frac{d^4}{dx^4}\left(\frac{x}{\sin x}\right).
\]
:::

::: {.solution}

::: pf

::: {.pf-step #g-analytic-extension}
The function
$$
g(x)=\frac{x}{\sin x}
$$
for $x\ne0$ extends to a real-analytic function near $0$ by setting
$g(0)=1$.

::: pf-proof
The function
$$
h(x)=
\begin{cases}
\dfrac{\sin x}{x},&x\ne0,\\
1,&x=0
\end{cases}
$$
is real analytic near $0$, with power series
$$
h(x)=1-\frac{x^2}{6}+\frac{x^4}{120}+O(x^6).
$$
Since $h(0)=1$, it is nonzero on some neighborhood of $0$. Hence
$g=1/h$ is real analytic there and agrees with $x/\sin x$ away from
$0$.
:::

:::

::: {.pf-step #taylor-expansion-g}
The Taylor expansion of $g$ at $0$ begins
$$
g(x)
=
1+\frac{x^2}{6}+\frac{7x^4}{360}+O(x^6).
$$

::: pf-proof
Since $h$ is even, its reciprocal $g=1/h$ is even on the
neighborhood from step [](#g-analytic-extension){.pf-ref}. Thus its Taylor series has only even
powers. Write
$$
g(x)=1+ax^2+bx^4+O(x^6).
$$
Multiplying this by the expansion for $h$ from step [](#g-analytic-extension){.pf-ref} gives
$$
\begin{aligned}
1
&=
g(x)h(x)
\\
&=
\left(1+ax^2+bx^4+O(x^6)\right)
\left(1-\frac{x^2}{6}+\frac{x^4}{120}+O(x^6)\right).
\end{aligned}
$$
Comparing the $x^2$ coefficient yields
$$
a=\frac16.
$$
Comparing the $x^4$ coefficient then yields
$$
b-\frac{a}{6}+\frac1{120}=0,
$$
so
$$
b
=
\frac1{36}-\frac1{120}
=
\frac7{360}.
$$
:::

:::

::: {.pf-step #g4-value}
One has
$$
g^{(4)}(0)=\boxed{\frac7{15}}.
$$

::: pf-proof
Because $g$ is analytic by step [](#g-analytic-extension){.pf-ref}, the coefficient of $x^4$ in its
Taylor series is $g^{(4)}(0)/4!$. Step [](#taylor-expansion-g){.pf-ref} therefore gives
$$
g^{(4)}(0)
=
4!\frac7{360}
=
\frac7{15}.
$$
:::

:::

::: {.pf-step #limit-equals-g4}
Therefore
$$
\lim_{x\to0}\frac{d^4}{dx^4}\left(\frac{x}{\sin x}\right)
=
\frac7{15}.
$$

::: pf-proof
The analytic extension $g$ from step [](#g-analytic-extension){.pf-ref} agrees with $x/\sin x$ for
$x\ne0$, and $g^{(4)}$ is continuous at $0$. Hence
$$
\lim_{x\to0}g^{(4)}(x)=g^{(4)}(0),
$$
which step [](#g4-value){.pf-ref} evaluates.
:::

:::

::: pf-qed
Step [](#limit-equals-g4){.pf-ref} is the requested limit.
:::

:::

:::
