---
schema: qual/card@1
id: P-GREPT-41
kind: problem
title: "Sharp bound on $f(1)$ from bounds on the Taylor coefficients at $0$"
classification:
  areas: [prelim]
  topics:
  - Taylor Series
  - Estimates
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: "Transcribed from Question 41 of the Practice Test (Chapter 9) in assets/attachments/extracted/Cracking_the_GRE_Mathematics_Subject.md (Mistral OCR)."
---

::: {.problem}
Let $f(x)$ be a function that has derivatives of all orders at every real $x$, such that $f(0) = 0$. Assume the following about the values of the derivatives of $f$ at $x = 0$:

I. $f'(0) = 1$

II. $f''(0) = 2$

III. $f^{(n)}(0) \leq \frac{n!}{2^{n-3}}$ for every integer $n \geq 3$

What is the smallest number $m$ that makes the statement $f(1) \leq m$ true?

(A) $2$
(B) $3$
(C) $4$
(D) $6$
(E) $8$
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Define
$$
h(x)=
\begin{cases}
e^{-1/x^2}, & x\ne0,\\
0, & x=0.
\end{cases}
$$
Then $h$ is infinitely differentiable on $\RR$ and
$$
h^{(n)}(0)=0
$$
for every $n\ge0$.


::: pf-proof

For $x\ne0$, repeated differentiation shows that each derivative has the
form
$$
h^{(n)}(x)=P_n(1/x)e^{-1/x^2}
$$
for a polynomial $P_n$. For every integer $N\ge0$,
$$
\lim_{x\to0}\abs{x}^{-N}e^{-1/x^2}=0,
$$
because with $t=1/x^2$ this becomes a constant power of $t$ times $e^{-t}$
as $t\to\infty$. Hence every such derivative tends to $0$ at the origin.
The same estimate, with one additional factor $\abs{x}^{-1}$, shows that the
difference quotient of each extended derivative at $0$ also tends to $0$.
Inductively, each derivative therefore extends differentiably across $0$ with
derivative $0$, proving that $h$ is smooth and flat at $0$.

:::

:::

::: {.pf-step #s1-2}

For every $M>0$, the function
$$
f_M(x)=x+x^2+Mh(x)
$$
satisfies all three hypotheses of the problem.


::: pf-proof

By step [](#s1-1){.pf-ref}, $h^{(n)}(0)=0$ for every $n$. Therefore
$$
f_M(0)=0,
\qquad
f_M'(0)=1,
\qquad
f_M''(0)=2,
$$
and for every $n\ge3$,
$$
f_M^{(n)}(0)=0
\le\frac{n!}{2^{n-3}}.
$$

:::

:::

::: {.pf-step #s1-3}

The values $f_M(1)$ are unbounded above as $M$ varies.


::: pf-proof

Since $h(1)=e^{-1}$,
$$
f_M(1)=1+1+Me^{-1}=2+\frac{M}{e}.
$$
This tends to $+\infty$ as $M\to\infty$.

:::

:::

::: {.pf-step #s1-4}

Therefore
$$
\boxed{\text{no finite number }m\text{ makes }f(1)\le m\text{ follow from the stated hypotheses}},
$$
so none of choices (A)--(E) is correct as written.


::: pf-proof

Given any proposed finite $m$, choose $M>e(m-2)$. Then the function $f_M$
from step [](#s1-2){.pf-ref} satisfies every printed hypothesis, while step [](#s1-3){.pf-ref} gives
$f_M(1)>m$.

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} proves the literal conclusion.

:::

:::

:::

::: {.remark}
The source selects (C) by replacing $f$ with its Taylor series at $0$. If one
adds a hypothesis guaranteeing that this Taylor series represents $f$ at
$x=1$, then the stated coefficient bounds give
$$
f(1)\le1+1+\sum_{n=3}^{\infty}2^{-(n-3)}=4,
$$
which is the source-intended answer.
:::
