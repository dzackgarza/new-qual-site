---
schema: qual/card@1
id: P-BKS04-9A
kind: problem
title: $(f(x)-f(y)).(x-y)\le L|x-y|^2$ for all $x,y$ iff $Df(x)v.v\le L|v|^2$ for all $x,v$
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against the retained UC Berkeley Spring 2004 preliminary exam and its companion solution packet.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Compared the authored solution with the retained `s04solution.pdf` solution packet.
---

::: {.problem}
Let $f\colon\RR^n\to\RR^n$ be a differentiable function, and let $L$ be a nonnegative real number.
Prove that the following are equivalent:

(i) For every $x,y\in\RR^n$,

$$
(f(x)-f(y)).(x-y)\leq L\abs{x-y}^2
$$

(ii) For every $x,v\in\RR^n$,

$$
Df(x)v.v\leq L\abs{v}^2,
$$

where $Df(x)$ is the derivative of $f$ at $x$, and $.$ denotes the standard inner product of vectors in $\RR^n$.
:::

::: {.solution}
(i) $\Longrightarrow$ (ii): Let $x=y+tv$. Then (i) says

$$
t(f(y+tv)-f(y)).v\leq Lt^2\abs{v}^2.
$$

Divide by $t^2$ and take the limit as $t\to0$ to deduce $Df(y)v.v\leq L\abs{v}^2$.

(ii) $\Longrightarrow$ (i): Let $\phi(t)=f(y+t(x-y))$ for $t\in\RR$. Then

$$
\begin{aligned}
f(x)-f(y)&=\phi(1)-\phi(0)\\
&=\int_0^1\phi'(t)\,dt\\
&=\int_0^1Df(y+t(x-y))(x-y)\,dt&&\text{(by the chain rule)},
\end{aligned}
$$

so

$$
\begin{aligned}
(f(x)-f(y)).(x-y)&=\int_0^1Df(y+t(x-y))(x-y).(x-y)\,dt\\
&\leq\int_0^1L\abs{x-y}^2\,dt&&\text{(by (ii))}\\
&=L\abs{x-y}^2.
\end{aligned}
$$
:::
