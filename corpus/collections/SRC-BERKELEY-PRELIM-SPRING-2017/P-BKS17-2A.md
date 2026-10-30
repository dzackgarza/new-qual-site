---
schema: qual/card@1
id: P-BKS17-2A
kind: problem
title: Solutions of $f(2x)=2f(x)$ differentiable at the origin are linear
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored spaces around inline math and normalized LaTeX against Sp17_Exam_0.pdf page 3 problem 2A.
- event: source-checked
  by: chatgpt
  date: 2026-10-02
  note: Independently reviewed the supplied Berkeley Spring 2017 solution. Its displayed example uses $\log_2(x)$ for all $x\ne0$; the solution below uses $\log_2\abs{x}$ so the example is defined on all of $\RR$.
- event: solution-written
  by: chatgpt
  date: 2026-10-02
- event: solution-reviewed
  by: chatgpt
  date: 2026-10-02
  note: Verified the dyadic scaling argument at the origin and the continuity, functional equation, and nonlinearity of the explicit example.
---

::: {.problem}
Suppose $f$ is a function from the reals to the reals satisfying $2f(x) = f(2x)$ for all $x$.

(a) Prove that if $f$ is differentiable at $0$ then $f$ is linear.

(b) Give an example of such a function $f$ that is continuous but not linear.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

One has $f(0)=0$.


::: pf-proof

Substitute $x=0$ into
$$
2f(x)=f(2x).
$$
This gives $2f(0)=f(0)$, hence $f(0)=0$.

:::

:::

::: {.pf-step #s1-2}

If $f$ is differentiable at $0$ with derivative $c$, then
$$
f(x)=cx
$$
for every $x\in\RR$.


::: pf-proof

Fix $x\ne0$. Iterating the functional equation gives
$$
f\!\left(\frac{x}{2^n}\right)=\frac{f(x)}{2^n}
$$
for every $n\geq0$. By step [](#s1-1){.pf-ref},
$$
\frac{f(x/2^n)-f(0)}{x/2^n}
=
\frac{f(x)}{x}.
$$
As $n\to\infty$, the points $x/2^n$ tend to $0$. Differentiability at $0$ therefore gives
$$
c=f'(0)=\frac{f(x)}{x}.
$$
Thus $f(x)=cx$ for every nonzero $x$, and step [](#s1-1){.pf-ref} gives the same formula at $x=0$.

:::

:::

::: {.pf-step #s1-3}

A continuous non-linear example is
$$
f(x)
=
\begin{cases}
x\sin\!\bigl(2\pi\log_2\abs{x}\bigr),&x\ne0,\\
0,&x=0.
\end{cases}
$$


::: pf-proof

For $x\ne0$,
$$
\begin{aligned}
f(2x)
&=2x\sin\!\bigl(2\pi\log_2\abs{2x}\bigr)\\
&=2x\sin\!\bigl(2\pi(1+\log_2\abs{x})\bigr)\\
&=2f(x).
\end{aligned}
$$
The same identity holds at $x=0$. The function is continuous away from $0$, and
$$
\abs{f(x)}\leq\abs{x}
$$
shows that $f(x)\to0=f(0)$ as $x\to0$, so it is continuous everywhere.

It is not linear: $f(1)=0$, while for $x=2^{1/4}$,
$$
f(2^{1/4})
=
2^{1/4}\sin(\pi/2)
=
2^{1/4}\ne0.
$$

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} proves part (a), and step [](#s1-3){.pf-ref} supplies the example required in part (b).

:::

:::

:::

::: {.remark}
The vendored source solution writes $xg(\log_2 x)$ for $x\ne0$. Since the problem asks for a function on all of $\RR$, replacing $\log_2x$ by $\log_2\abs{x}$ gives the intended construction on negative inputs as well.
:::
