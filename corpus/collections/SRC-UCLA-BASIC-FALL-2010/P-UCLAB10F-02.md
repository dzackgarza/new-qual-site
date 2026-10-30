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
Suppose $f$ is bounded on $[a,b]$.

(a) Define what it means for $f$ to be Riemann integrable on $[a,b]$.

(b) Prove directly from the definition that every continuous $f$ is Riemann integrable.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Let
$$
P:\quad a=x_0<x_1<\cdots<x_m=b
$$
be a partition of $[a,b]$. For each subinterval
$$
I_i=[x_{i-1},x_i],
$$
define
$$
M_i=\sup_{x\in I_i}f(x),
\qquad
m_i=\inf_{x\in I_i}f(x),
$$
and define the upper and lower Darboux sums
$$
U(f,P)=\sum_{i=1}^mM_i(x_i-x_{i-1}),
$$
$$
L(f,P)=\sum_{i=1}^m m_i(x_i-x_{i-1}).
$$


::: pf-proof

Because $f$ is bounded on $[a,b]$, the suprema and infima are finite, so the sums are well-defined.

:::

:::

::: {.pf-step #s1-2}

The upper and lower Riemann integrals are
$$
\overline{\int_a^b}f
=
\inf_P U(f,P)
$$
and
$$
\underline{\int_a^b}f
=
\sup_P L(f,P).
$$
The function $f$ is Riemann integrable if these two numbers are equal; their common value is denoted
$$
\boxed{\int_a^b f(x)\,dx}.
$$


::: pf-proof

This is the Darboux definition of Riemann integrability.

:::

:::

::: {.pf-step #s1-3}

Equivalently, $f$ is Riemann integrable if for every $\varepsilon>0$ there exists a partition $P$ such that
$$
U(f,P)-L(f,P)<\varepsilon.
$$


::: pf-proof

For every partition $P$,
$$
L(f,P)
\le
\underline{\int_a^b}f
\le
\overline{\int_a^b}f
\le
U(f,P).
$$
Thus if such partitions exist for every $\varepsilon>0$, the difference between upper and lower integrals is bounded by every positive $\varepsilon$, hence is zero.

Conversely, if the upper and lower integrals are equal, choose partitions whose upper sum is within $\varepsilon/2$ of the upper integral and whose lower sum is within $\varepsilon/2$ of the lower integral. Passing to a common refinement can only decrease the upper sum and increase the lower sum, giving a partition with gap less than $\varepsilon$.

:::

:::

::: {.pf-step #s1-4}

Suppose now that $f$ is continuous on $[a,b]$. Then $f$ is uniformly continuous there.


::: pf-proof

The interval $[a,b]$ is compact. The Heine--Cantor theorem states that every continuous function on a compact metric space is uniformly continuous.

:::

:::

::: {.pf-step #s1-5}

Given $\varepsilon>0$, there exists $\delta>0$ such that
$$
\abs{x-y}<\delta
\quad\Longrightarrow\quad
\abs{f(x)-f(y)}
<
\frac{\varepsilon}{b-a}
$$
for all $x,y\in[a,b]$.


::: pf-proof

Apply uniform continuity from step [](#s1-4){.pf-ref} with tolerance
$$
\frac{\varepsilon}{b-a}.
$$
If $a=b$, the integral is trivial; assume $a<b$.

:::

:::

::: {.pf-step #s1-6}

Choose a partition $P$ whose mesh satisfies
$$
\max_i(x_i-x_{i-1})<\delta.
$$
Then
$$
U(f,P)-L(f,P)<\varepsilon.
$$


::: pf-proof

On each subinterval $I_i$, any two points are less than $\delta$ apart. Hence step [](#s1-5){.pf-ref} gives
$$
M_i-m_i
\le
\frac{\varepsilon}{b-a}.
$$
Therefore
$$
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
$$
If strict inequality is desired, use $\varepsilon/(2(b-a))$ in step [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

Every continuous function on $[a,b]$ is Riemann integrable.


::: pf-proof

By step [](#s1-6){.pf-ref}, for every $\varepsilon>0$ there is a partition with upper-minus-lower sum less than $\varepsilon$. Step [](#s1-3){.pf-ref} therefore implies that $f$ is Riemann integrable.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref} give the definition, and steps [](#s1-4){.pf-ref} through [](#s1-7){.pf-ref} prove part (b) directly from it.

:::

:::

:::
