---
schema: qual/card@1
id: P-BERK78S-19
kind: problem
title: Vanishing integrals between points outside a countable set force a continuous function to vanish
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
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Introduced the antiderivative F(t)=int_0^t f. The hypothesis makes F
    constant on R\S. Since a countable subset cannot contain any nonempty
    interval, R\S is dense; continuity therefore makes F constant on all
    of R. The fundamental theorem of calculus then gives f=F'=0.
---

::: {.problem}
Let $f:\mathbb R\to\mathbb R$ be continuous. Suppose $\mathbb R$ contains a countably infinite subset $S$ such that
\[
\int_p^q f(x)\,dx=0
\]
whenever $p,q\notin S$. Prove that $f$ is identically zero.
:::

::: {.solution}
Define
$$
F(t)=\int_0^t f(x)\,dx.
$$

::: pf

::: {.pf-step #s1}

The function $F$ is continuously differentiable on $\RR$ and
$$
F'(t)=f(t)
$$
for every $t\in\RR$.

::: pf-proof

The function $f$ is continuous on $\RR$. The fundamental theorem of
calculus therefore applies to the displayed integral and gives
$$
F'=f.
$$
In particular, $F$ is continuous.

:::

:::

::: {.pf-step #s2}

The function $F$ is constant on
$$
\RR\sm S.
$$

::: pf-proof

Let
$$
p,q\in\RR\sm S.
$$
Then
$$
\begin{aligned}
F(q)-F(p)
&=
\int_0^q f(x)\,dx
-
\int_0^p f(x)\,dx\\
&=
\int_p^q f(x)\,dx\\
&=
0
\end{aligned}
$$
by the hypothesis. Hence
$$
F(p)=F(q)
$$
for every pair $p,q\notin S$.

:::

:::

::: {.pf-step #s3}

The complement
$$
\RR\sm S
$$
is dense in $\RR$.

::: pf-proof

Let
$$
(a,b)
$$
be any nonempty open interval. Every nonempty real interval is
uncountable, whereas $S$ is countable. Therefore
$$
(a,b)\not\subseteq S.
$$
Thus every nonempty open interval contains a point of $\RR\sm S$, which
is exactly density of the complement.

:::

:::

::: {.pf-step #s4}

The function $F$ is constant on all of $\RR$.

::: pf-proof

By step [](#s2){.pf-ref}, there is a real number $c$ such that
$$
F(t)=c
$$
for every $t\in\RR\sm S$.

Fix arbitrary $t\in\RR$. By step [](#s3){.pf-ref}, choose a sequence
$$
t_n\in\RR\sm S
$$
with
$$
t_n\longrightarrow t.
$$
Continuity of $F$ from step [](#s1){.pf-ref} gives
$$
F(t)
=
\lim_{n\to\infty}F(t_n)
=
\lim_{n\to\infty}c
=
c.
$$
Thus $F\equiv c$ on $\RR$.

:::

:::

::: {.pf-step #s5}

The function $f$ is identically zero:
$$
\boxed{
f(t)=0
\qquad
\text{for every }t\in\RR.
}
$$

::: pf-proof

By step [](#s4){.pf-ref}, the derivative of $F$ is identically zero. Step [](#s1){.pf-ref} gives
$$
f=F',
$$
so $f\equiv0$.

:::

:::

::: pf-qed

Step [](#s5){.pf-ref} is the required conclusion.

:::

:::

:::
