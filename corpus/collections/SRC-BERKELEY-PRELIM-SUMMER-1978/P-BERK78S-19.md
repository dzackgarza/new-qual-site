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

<1>1. The function $F$ is continuously differentiable on $\RR$ and
$$
F'(t)=f(t)
$$
for every $t\in\RR$.

::: {.proof}
The function $f$ is continuous on $\RR$. The fundamental theorem of
calculus therefore applies to the displayed integral and gives
$$
F'=f.
$$
In particular, $F$ is continuous.
:::

<1>2. The function $F$ is constant on
$$
\RR\sm S.
$$

::: {.proof}
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

<1>3. The complement
$$
\RR\sm S
$$
is dense in $\RR$.

::: {.proof}
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

<1>4. The function $F$ is constant on all of $\RR$.

::: {.proof}
By step <1>2, there is a real number $c$ such that
$$
F(t)=c
$$
for every $t\in\RR\sm S$.

Fix arbitrary $t\in\RR$. By step <1>3, choose a sequence
$$
t_n\in\RR\sm S
$$
with
$$
t_n\longrightarrow t.
$$
Continuity of $F$ from step <1>1 gives
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

<1>5. The function $f$ is identically zero:
$$
\boxed{
f(t)=0
\qquad
\text{for every }t\in\RR.
}
$$

::: {.proof}
By step <1>4, the derivative of $F$ is identically zero. Step <1>1 gives
$$
f=F',
$$
so $f\equiv0$.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 is the required conclusion.
:::
:::
