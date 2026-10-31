---
schema: qual/card@1
id: P-TRIV-RA03
kind: problem
title: Derivatives of $e^{-1/x^2}$ at $0$
classification:
  areas: [real-analysis]
  topics:
  - Derivatives
  - Smooth Non-Analytic Functions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 3, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Find $f^{(n)}(0)$, if $f(x) = e^{-\frac{1}{x^2}}$, $x \in \RR$, $n > 0$.
:::

::: {.remark}
The printed formula is undefined at $x=0$. The standard intended function is
the smooth extension
$$
f(x)=
\begin{cases}
e^{-1/x^2},&x\neq0,\\
0,&x=0.
\end{cases}
$$
The solution uses this intended definition.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

For every integer $m\geq0$,
$$
\lim_{x\to0}
\abs{x}^{-m}e^{-1/x^2}
=0.
$$


::: pf-proof

Put
$$
t=\frac1{x^2}.
$$
Then as $x\to0$, one has $t\to\infty$, and
$$
\abs{x}^{-m}e^{-1/x^2}
=
t^{m/2}e^{-t}.
$$
Exponential decay dominates every power, so
$$
t^{m/2}e^{-t}\longrightarrow0.
$$

:::

:::

::: {.pf-step #s1-2}

For every $n\geq0$, there is a polynomial $P_n$ such that for $x\neq0$,
$$
f^{(n)}(x)
=
P_n(1/x)e^{-1/x^2}.
$$


::: pf-proof

Proceed by induction. For $n=0$, take $P_0=1$.

Suppose
$$
f^{(n)}(x)=P_n(1/x)e^{-1/x^2}.
$$
Differentiating for $x\neq0$ gives
$$
\begin{aligned}
f^{(n+1)}(x)
&=
-\frac1{x^2}P_n'(1/x)e^{-1/x^2}
+
\frac{2}{x^3}P_n(1/x)e^{-1/x^2}.
\end{aligned}
$$
The coefficient is again a polynomial in $1/x$, so the claim follows.

:::

:::

::: pf-step

For every $n\geq0$,
$$
\lim_{x\to0}f^{(n)}(x)=0
$$
when the derivative is taken on $x\neq0$.


::: pf-proof

By step [](#s1-2){.pf-ref}, $f^{(n)}(x)$ is a finite sum of terms
$$
c_m x^{-m}e^{-1/x^2}.
$$
Each term tends to $0$ by step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

The function $f$ is differentiable at $0$ and
$$
f'(0)=0.
$$


::: pf-proof

Since $f(0)=0$,
$$
\frac{f(h)-f(0)}h
=
\frac{e^{-1/h^2}}h.
$$
Its absolute value tends to $0$ by step [](#s1-1){.pf-ref} with $m=1$.

:::

:::

::: {.pf-step #s1-5}

Suppose $f^{(n)}(0)=0$. Then $f^{(n+1)}(0)$ exists and equals $0$.


::: pf-proof

For $h\neq0$,
$$
\frac{f^{(n)}(h)-f^{(n)}(0)}h
=
\frac{f^{(n)}(h)}h.
$$
By step [](#s1-2){.pf-ref}, this is again a finite sum of terms of the form
$$
c_m h^{-m}e^{-1/h^2},
$$
after increasing the exponents by one. Step [](#s1-1){.pf-ref} shows that every such term
tends to $0$. Hence the derivative at $0$ exists and is $0$.

:::

:::

::: {.pf-step #s1-6}

Therefore, for every integer $n>0$,
$$
\boxed{f^{(n)}(0)=0}.
$$


::: pf-proof

Step [](#s1-4){.pf-ref} is the base case, and step [](#s1-5){.pf-ref} gives the induction step.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required value of every derivative at the origin.

:::

:::

:::
