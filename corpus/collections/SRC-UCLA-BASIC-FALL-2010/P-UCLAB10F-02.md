---
schema: qual/card@1
id: P-UCLAB10F-02
kind: problem
title: Riemann integrability directly from the definition
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
  note: Checked against Problem 2 of the retained UCLA Basic Examination, Fall 2010.
---

::: {.problem}
Problem 2. Suppose $f$ is bounded on $[a,b]$.

(a) Define what it means for $f$ to be Riemann integrable on $[a,b]$.

(b) Prove directly from the definition that every continuous $f$ is Riemann integrable.
:::

::: pf

::: pf-step

Let
\[
P:\quad a=x_0<x_1<\cdots<x_m=b
\]
be a partition of $[a,b]$. For each subinterval
\[
I_i=[x_{i-1},x_i],
\]
define
\[
M_i=\sup_{x\in I_i}f(x),
\qquad
m_i=\inf_{x\in I_i}f(x),
\]
and define the upper and lower Darboux sums
\[
U(f,P)=\sum_{i=1}^mM_i(x_i-x_{i-1}),
\]
\[
L(f,P)=\sum_{i=1}^m m_i(x_i-x_{i-1}).
\]


::: pf-proof

Because $f$ is bounded on $[a,b]$, the suprema and infima are finite, so the sums are well-defined.

:::

:::

::: pf-step

The upper and lower Riemann integrals are
\[
\overline{\int_a^b}f
=
\inf_P U(f,P)
\]
and
\[
\underline{\int_a^b}f
=
\sup_P L(f,P).
\]
The function $f$ is Riemann integrable if these two numbers are equal; their common value is denoted
\[
\boxed{\int_a^b f(x)\,dx}.
\]


::: pf-proof

This is the Darboux definition of Riemann integrability.

:::

:::

::: pf-step

Equivalently, $f$ is Riemann integrable if for every $\varepsilon>0$ there exists a partition $P$ such that
\[
U(f,P)-L(f,P)<\varepsilon.
\]


::: pf-proof

For every partition $P$,
\[
L(f,P)
\le
\underline{\int_a^b}f
\le
\overline{\int_a^b}f
\le
U(f,P).
\]
Thus if such partitions exist for every $\varepsilon>0$, the difference between upper and lower integrals is bounded by every positive $\varepsilon$, hence is zero.

Conversely, if the upper and lower integrals are equal, choose partitions whose upper sum is within $\varepsilon/2$ of the upper integral and whose lower sum is within $\varepsilon/2$ of the lower integral. Passing to a common refinement can only decrease the upper sum and increase the lower sum, giving a partition with gap less than $\varepsilon$.

:::

:::

::: pf-step

Suppose now that $f$ is continuous on $[a,b]$. Then $f$ is uniformly continuous there.


::: pf-proof

The interval $[a,b]$ is compact. The Heine--Cantor theorem states that every continuous function on a compact metric space is uniformly continuous.

:::

:::

::: pf-step

Given $\varepsilon>0$, there exists $\delta>0$ such that
\[
|x-y|<\delta
\quad\Longrightarrow\quad
|f(x)-f(y)|
<
\frac{\varepsilon}{b-a}
\]
for all $x,y\in[a,b]$.


::: pf-proof

Apply uniform continuity from step <1>4 with tolerance
\[
\frac{\varepsilon}{b-a}.
\]
If $a=b$, the integral is trivial; assume $a<b$.

:::

:::

::: pf-step

Choose a partition $P$ whose mesh satisfies
\[
\max_i(x_i-x_{i-1})<\delta.
\]
Then
\[
U(f,P)-L(f,P)<\varepsilon.
\]


::: pf-proof

On each subinterval $I_i$, any two points are less than $\delta$ apart. Hence step <1>5 gives
\[
M_i-m_i
\le
\frac{\varepsilon}{b-a}.
\]
Therefore
\[
\begin{aligned}
U(f,P)-L(f,P)
&=
\sum_{i=1}^m(M_i-m_i)(x_i-x_{i-1})\\
&\le
\frac{\varepsilon}{b-a}
\sum_{i=1}^m(x_i-x_{i-1})\\
&=
\varepsilon.
\end{aligned}
\]
If strict inequality is desired, use $\varepsilon/(2(b-a))$ in step <1>5.

:::

:::

::: pf-step

Every continuous function on $[a,b]$ is Riemann integrable.


::: pf-proof

By step <1>6, for every $\varepsilon>0$ there is a partition with upper-minus-lower sum less than $\varepsilon$. Step <1>3 therefore implies that $f$ is Riemann integrable.

:::

:::

::: pf-qed

Steps <1>1--<1>3 give the definition, and steps <1>4--<1>7 prove part (b) directly from it.

:::

:::
