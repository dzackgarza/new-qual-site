---
schema: qual/card@1
id: P-BKF80-1
kind: problem
title: Differentiate an integral with moving endpoints and parameter-dependent integrand
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Define
$$
F(x)=\int_{\sin x}^{\cos x} e^{t^2+xt}\,dt.
$$
Compute $F'(0)$.
:::

::: {.solution}
Set
$$
a(x)\coloneqq\sin x,
\qquad
b(x)\coloneqq\cos x,
\qquad
f(x,t)\coloneqq e^{t^2+xt}.
$$

<1>1. For every $x$,
$$
F'(x)
=-\sin x\,e^{\cos^2x+x\cos x}
-\cos x\,e^{\sin^2x+x\sin x}
+\int_{\sin x}^{\cos x} t e^{t^2+xt}\,dt.
$$

::: {.proof}
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

<1>2. $F'(0)=\boxed{\dfrac{e-3}{2}}$.

::: {.proof}
Substituting $x=0$ into step <1>1 gives
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

<1>3. Q.E.D.

::: {.proof}
Step <1>2 gives the requested value.
:::
:::
