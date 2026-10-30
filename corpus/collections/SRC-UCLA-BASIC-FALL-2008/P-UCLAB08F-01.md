---
schema: qual/card@1
id: P-UCLAB08F-01
kind: problem
title: Uniform continuity of power functions on the nonnegative ray
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against Problem 1 of the retained UCLA Basic Examination, Fall 2008.
---

::: {.problem}
For each $a\in\{0,1,2\}$, determine whether
$$
f(t)=t^a
$$
is uniformly continuous on $[0,\infty)$.
Prove each assertion.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For $a=0$, the function
$$
f(t)=1
$$
is uniformly continuous on $[0,\infty)$.


::: pf-proof

For all $s,t\ge0$,
$$
\abs{f(t)-f(s)}=0.
$$
Thus for every $\varepsilon>0$, any $\delta>0$ satisfies the definition of uniform continuity.

:::

:::

::: {.pf-step #s1-2}

For $a=1$, the function
$$
f(t)=t
$$
is uniformly continuous on $[0,\infty)$.


::: pf-proof

For all $s,t\ge0$,
$$
\abs{f(t)-f(s)}=\abs{t-s}.
$$
Given $\varepsilon>0$, choose
$$
\delta=\varepsilon.
$$
Then
$$
\abs{t-s}<\delta
$$
implies
$$
\abs{f(t)-f(s)}<\varepsilon.
$$

:::

:::

::: {.pf-step #s1-3}

For $a=2$, the function
$$
f(t)=t^2
$$
is not uniformly continuous on $[0,\infty)$.


::: pf-proof

For each positive integer $n$, set
$$
x_n=n,
\qquad
y_n=n+\frac1n.
$$
Then
$$
\abs{x_n-y_n}=\frac1n\longrightarrow0,
$$
but
$$
\begin{aligned}
\abs{f(y_n)-f(x_n)}
&=
\left(n+\frac1n\right)^2-n^2\\
&=
2+\frac1{n^2}
>
1.
\end{aligned}
$$
If $f$ were uniformly continuous, taking $\varepsilon=1$ would give some $\delta>0$ such that
$$
\abs{s-t}<\delta
$$
implies
$$
\abs{f(s)-f(t)}<1.
$$
For sufficiently large $n$, one has $1/n<\delta$, contradicting the displayed inequality above.

:::

:::

::: {.pf-step #s1-4}

Therefore the uniformly continuous cases are exactly
$$
\boxed{a=0\text{ and }a=1}.
$$


::: pf-proof

Steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref} prove uniform continuity for $a=0,1$, and step [](#s1-3){.pf-ref} rules it out for $a=2$.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} gives the complete classification.

:::

:::

:::
