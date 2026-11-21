---
schema: qual/card@1
id: P-BKF80-1
kind: problem
title: Differentiate an integral with moving endpoints and parameter-dependent integrand
classification: {areas: [prelim], topics: [Differentiation Under the Integral Sign, Leibniz Rule]}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read in the retained sheet `assets/attachments/Fall80.pdf`: the statement is its Problem 1, and the printed words
    are the card's. The exam, the problem number and the file are now named in the solution's
    opening sentence. Not checked in this pass: the solution, which the edit does not touch.
---

::: {.problem}
Define
$$
F(x)=\int_{\sin x}^{\cos x} e^{t^2+xt}\,dt.
$$
Compute $F'(0)$.
:::

::: {.solution}
This is Problem 1 of the Preliminary Exam, Fall 1980, retained in this repository as `assets/attachments/Fall80.pdf`; the statement below is its wording.
Set
$$
a(x)\coloneqq\sin x,
\qquad
b(x)\coloneqq\cos x,
\qquad
f(x,t)\coloneqq e^{t^2+xt}.
$$

::: pf

::: {.pf-step #f-prime-formula}
For every $x$,
$$
F'(x)
=-\sin x\,e^{\cos^2x+x\cos x}
-\cos x\,e^{\sin^2x+x\sin x}
+\int_{\sin x}^{\cos x} t e^{t^2+xt}\,dt.
$$

::: pf-proof
The functions $a$, $b$, and $f$ are smooth, so the Leibniz rule gives
$$
F'(x)
=f(x,b(x))b'(x)-f(x,a(x))a'(x)
+\int_{a(x)}^{b(x)}\frac{\partial f}{\partial x}(x,t)\,dt.
$$
Here $b'(x)=-\sin x$, $a'(x)=\cos x$, and
$$
\frac{\partial f}{\partial x}(x,t)=t e^{t^2+xt},
$$
which yields the stated formula.
:::

:::

::: {.pf-step #f-prime-value}
$F'(0)=\boxed{\dfrac{e-3}{2}}$.

::: pf-proof
Substituting $x=0$ into step [](#f-prime-formula){.pf-ref} gives
$$
F'(0)=-1+\int_0^1 t e^{t^2}\,dt.
$$
With $u=t^2$, this integral is
$$
\int_0^1 t e^{t^2}\,dt
=\frac12\int_0^1 e^u\,du
=\frac{e-1}{2}.
$$
Therefore
$$
F'(0)=-1+\frac{e-1}{2}=\frac{e-3}{2}.
$$
:::

:::

::: pf-qed
Step [](#f-prime-value){.pf-ref} gives the requested value.
:::

:::
:::
