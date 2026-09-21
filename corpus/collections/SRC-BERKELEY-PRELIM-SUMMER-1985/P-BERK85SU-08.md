---
schema: qual/card@1
id: P-BERK85SU-08
kind: problem
title: Polynomial approximation with prescribed value and derivative at an endpoint
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Approximate g(y)=f(a+sqrt(y)) on [0,(b-a)^2] by a polynomial q,
    then correct its constant term so r(0)=g(0) without losing the
    prescribed uniform tolerance. The polynomial p(x)=r((x-a)^2)
    then has p(a)=f(a), p'(a)=0, and approximates f uniformly.
---

::: {.problem}
Let $f:[a,b]\to\mathbb R$ be continuous. Given $\varepsilon>0$, prove that there is a polynomial $p$ such that
\[
p(a)=f(a),\qquad p'(a)=0,
\]
and
\[
|p(x)-f(x)|<\varepsilon\qquad (x\in[a,b]).
\]
:::

::: {.solution}
If $a=b$, the constant polynomial $p(x)=f(a)$ has all the required
properties. Assume henceforth that $a<b$.

<1>1. Define
$$
g:[0,(b-a)^2]\to\RR,
\qquad
g(y)=f(a+\sqrt y).
$$
Then $g$ is continuous.

::: {.proof}
The map
$$
y\longmapsto a+\sqrt y
$$
is continuous from $[0,(b-a)^2]$ to $[a,b]$, and $f$ is continuous.
Therefore their composition $g$ is continuous.
:::

<1>2. There is a polynomial $q$ such that
$$
\abs{q(y)-g(y)}<\frac\varepsilon2
$$
for every $y\in[0,(b-a)^2]$.

::: {.proof}
This is the Weierstrass approximation theorem applied to the
continuous function $g$ from step <1>1.
:::

<1>3. The polynomial
$$
r(y)
\coloneqq
q(y)-q(0)+g(0)
$$
satisfies
$$
r(0)=g(0)
$$
and
$$
\abs{r(y)-g(y)}<\varepsilon
$$
for every $y\in[0,(b-a)^2]$.

::: {.proof}
The first identity is immediate. For the approximation estimate,
step <1>2 gives
$$
\begin{aligned}
\abs{r(y)-g(y)}
&\le
\abs{q(y)-g(y)}
+\abs{q(0)-g(0)}\\
&<
\frac\varepsilon2+\frac\varepsilon2
=
\varepsilon.
\end{aligned}
$$
:::

<1>4. Define
$$
p(x)=r((x-a)^2).
$$
Then $p$ is a polynomial satisfying
$$
p(a)=f(a)
$$
and
$$
p'(a)=0.
$$

::: {.proof}
Since $r$ is a polynomial, so is $p$. Moreover,
$$
p(a)=r(0)=g(0)=f(a)
$$
by step <1>3 and the definition of $g$. Differentiating gives
$$
p'(x)
=
2(x-a)r'((x-a)^2),
$$
so $p'(a)=0$.
:::

<1>5. For every $x\in[a,b]$,
$$
\boxed{\abs{p(x)-f(x)}<\varepsilon}.
$$

::: {.proof}
Since $x-a\ge0$,
$$
g((x-a)^2)
=
f\left(a+\sqrt{(x-a)^2}\right)
=
f(x).
$$
Therefore step <1>3 gives
$$
\abs{p(x)-f(x)}
=
\abs{r((x-a)^2)-g((x-a)^2)}
<
\varepsilon.
$$
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>4 gives the prescribed value and derivative at $a$, and
step <1>5 gives the required uniform approximation.
:::
:::
