---
schema: qual/card@1
id: P-BERK85S-17
kind: problem
title: Comparison theorem for scalar autonomous differential equations
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-written
  by: chatgpt
  date: 2026-09-22
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-22
  note: >-
    Used a first-contact argument for h=phi_2-phi_1. At every contact point
    h'=v_2-v_1 is strictly positive, which rules out a first return to zero
    after the solutions separate to the right of t_0; no uniqueness or
    Lipschitz hypothesis is used.
---

::: {.problem}
Let $v_1,v_2:\mathbb R\to\mathbb R$ be continuous and satisfy
\[
v_1(x)<v_2(x)
\]
for every $x$. Let $\varphi_1,\varphi_2$ solve
\[
x'=v_1(x)
\qquad\text{and}\qquad
x'=v_2(x),
\]
respectively, on an interval $(a,b)$. If
\[
\varphi_1(t_0)=\varphi_2(t_0)
\]
for some $t_0\in(a,b)$, prove that
\[
\varphi_1(t)\le\varphi_2(t)
\]
for every $t\in(t_0,b)$.
:::

::: {.solution}
Define
$$
h(t)\coloneqq\varphi_2(t)-\varphi_1(t).
$$

<1>1. At every $t\in(a,b)$ for which $h(t)=0$, one has
$$
h'(t)>0.
$$

::: {.proof}
If $h(t)=0$, then
$$
\varphi_1(t)=\varphi_2(t)=x
$$
for some $x\in\RR$. Using the two differential equations,
$$
\begin{aligned}
h'(t)
&=
\varphi_2'(t)-\varphi_1'(t)\\
&=
v_2(x)-v_1(x)
>0.
\end{aligned}
$$
:::

<1>2. There is $\delta>0$ such that
$$
h(t)>0
$$
for every $t\in(t_0,t_0+\delta)$.

::: {.proof}
The hypothesis gives $h(t_0)=0$, and step <1>1 gives $h'(t_0)>0$.
Hence
$$
\lim_{t\downarrow t_0}
\frac{h(t)-h(t_0)}{t-t_0}
=
h'(t_0)
>0.
$$
For all sufficiently small $t-t_0>0$, the quotient is positive, and
therefore $h(t)>0$.
:::

<1>3. In fact,
$$
h(t)>0
$$
for every $t\in(t_0,b)$.

::: {.proof}
Suppose otherwise. Then there is $s\in(t_0,b)$ with $h(s)\leq0$.
Choose $\delta>0$ as in step <1>2 with $t_0+\delta<s$. By continuity of
$h$, there is at least one zero of $h$ in $[t_0+\delta,s]$. Let
$$
\tau
\coloneqq
\min\{t\in[t_0+\delta,s]:h(t)=0\}.
$$
Then
$$
h(t)>0
\qquad
(t_0+\delta\leq t<\tau),
$$
while $h(\tau)=0$. Since $h$ is differentiable at $\tau$,
$$
h'(\tau)
=
\lim_{t\uparrow\tau}
\frac{h(\tau)-h(t)}{\tau-t}
\leq0.
$$
But step <1>1 applies at the contact point $\tau$ and gives
$h'(\tau)>0$, a contradiction.
:::

<1>4. Therefore, for every $t\in(t_0,b)$,
$$
\boxed{\varphi_1(t)<\varphi_2(t)}.
$$

::: {.proof}
By the definition of $h$, step <1>3 says
$$
\varphi_2(t)-\varphi_1(t)>0.
$$
This is stronger than the required inequality
$\varphi_1(t)\leq\varphi_2(t)$.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 proves the desired comparison.
:::
:::
