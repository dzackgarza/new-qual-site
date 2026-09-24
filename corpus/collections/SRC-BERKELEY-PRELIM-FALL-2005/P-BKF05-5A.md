---
schema: qual/card@1
id: P-BKF05-5A
kind: problem
title: A differential inequality forcing finite-time blowup
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
  note: Checked against the vendored UC Berkeley Fall 2005 preliminary-exam solution packet, which reproduces the problem statement with its solution.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained comparison argument and replaced its
    integration step by the mean value theorem applied to 1/f+x, requiring
    only the stated differentiability.
---

::: {.problem}
Does there exist a differentiable function \(f:\mathbb R\to\mathbb R\) such that
\[
f(0)=1
\qquad\text{and}\qquad
f'(x)\ge f(x)^2
\]
for every \(x\in\mathbb R\)? Prove your answer.
:::

::: {.solution}
<1>1. Any function satisfying the stated differential inequality would
be nondecreasing on $\RR$.

::: {.proof}
For every $x\in\RR$,
$$
f'(x)\ge f(x)^2\ge0.
$$
Hence $f'\ge0$ everywhere, so the mean value theorem implies that $f$
is nondecreasing.
:::

<1>2. Such a function would satisfy
$$
f(x)\ge1
$$
for every $x\ge0$.

::: {.proof}
By step <1>1, $f$ is nondecreasing, and the hypothesis gives
$f(0)=1$. Therefore $f(x)\ge f(0)=1$ whenever $x\ge0$.
:::

<1>3. On $[0,1]$, define
$$
g(x)=\frac1{f(x)}+x.
$$
Then $g'(x)\le0$ for every $x\in[0,1]$.

::: {.proof}
Step <1>2 gives $f(x)>0$ on $[0,1]$, so $g$ is differentiable there.
Using the assumed inequality,
$$
\begin{aligned}
g'(x)
&=
-\frac{f'(x)}{f(x)^2}+1
\\
&\le
-1+1
\\
&=
0.
\end{aligned}
$$
:::

<1>4. The conclusions of steps <1>2 and <1>3 are contradictory.

::: {.proof}
By step <1>3 and the mean value theorem, $g$ is nonincreasing on
$[0,1]$. Hence
$$
g(1)\le g(0)=1.
$$
But step <1>2 gives $f(1)\ge1$, so
$$
g(1)
=
\frac1{f(1)}+1
>
1.
$$
This is a contradiction.
:::

<1>5. Therefore
$$
\boxed{\text{no such differentiable function exists}}.
$$

::: {.proof}
Assuming that such a function existed led to the contradiction in step
<1>4. Hence no function can satisfy all the stated conditions.
:::

<1>6. Q.E.D.

::: {.proof}
Step <1>5 answers the question and proves the answer.
:::
:::
