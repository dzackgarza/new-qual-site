---
schema: qual/card@1
id: P-BKS82-4
kind: problem
title: Directional derivatives in every direction need not imply differentiability
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the retained PDF; the extracted markdown contains a different Problem 4.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: Checked every directional derivative and the failure of the Fréchet remainder along the diagonal.
---

::: {.problem}
Let $f:\mathbb R^2\to\mathbb R$ have directional derivatives in every direction at the origin. Must $f$ be differentiable at the origin? Prove your answer or give a counterexample.
:::

::: {.solution}
::: pf

::: {.pf-step #counterexample-function}
The answer is no. Consider
$$
\boxed{
f(x,y)
=
\begin{cases}
\dfrac{x^3}{x^2+y^2},&(x,y)\ne(0,0),\\
0,&(x,y)=(0,0).
\end{cases}
}
$$

::: pf-proof
This defines a real-valued function on all of $\RR^2$.
:::

:::

::: {.pf-step #directional-derivatives-exist}
The function $f$ has a directional derivative at the origin in every
nonzero direction $v=(a,b)$, namely
$$
D_vf(0,0)
=
\frac{a^3}{a^2+b^2}.
$$

::: pf-proof
For $t\ne0$,
$$
f(ta,tb)
=
\frac{t^3a^3}{t^2(a^2+b^2)}
=
t\frac{a^3}{a^2+b^2}.
$$
Therefore
$$
D_vf(0,0)
=
\lim_{t\to0}
\frac{f(ta,tb)-f(0,0)}{t}
=
\frac{a^3}{a^2+b^2}.
$$
Thus every directional derivative exists.
:::

:::

::: {.pf-step #candidate-derivative}
If $f$ were differentiable at the origin, its derivative would have
to be the linear map
$$
L(h,k)=h.
$$

::: pf-proof
Differentiability implies that the directional derivative in each direction
$v$ equals the derivative applied to $v$. Step [](#directional-derivatives-exist){.pf-ref} gives
$$
D_{(1,0)}f(0,0)=1,
\qquad
D_{(0,1)}f(0,0)=0.
$$
Hence a putative derivative $L:\RR^2\to\RR$ would satisfy
$$
L(1,0)=1,
\qquad
L(0,1)=0.
$$
By linearity, $L(h,k)=h$.
:::

:::

::: {.pf-step #remainder-not-vanishing}
The differentiability remainder for the map $L$ in step [](#candidate-derivative){.pf-ref} does
not tend to zero.

::: pf-proof
Along the diagonal $(h,k)=(t,t)$ with $t\ne0$,
$$
f(t,t)=\frac{t^3}{2t^2}=\frac t2
$$
and
$$
L(t,t)=t.
$$
Consequently
$$
\frac{
\abs{f(t,t)-f(0,0)-L(t,t)}
}{
\norm{(t,t)}
}
=
\frac{\abs{-t/2}}{\sqrt2\abs t}
=
\frac1{2\sqrt2}.
$$
This does not tend to $0$ as $t\to0$.
:::

:::

::: {.pf-step #not-differentiable-conclusion}
Therefore $f$ is not differentiable at the origin although all of
its directional derivatives there exist.

::: pf-proof
If $f$ were differentiable, step [](#candidate-derivative){.pf-ref} would identify its derivative with
$L$, but step [](#remainder-not-vanishing){.pf-ref} contradicts the defining remainder estimate for
differentiability.
:::

:::

::: pf-qed
Steps [](#counterexample-function){.pf-ref}, [](#directional-derivatives-exist){.pf-ref}, [](#candidate-derivative){.pf-ref}, [](#remainder-not-vanishing){.pf-ref}, and [](#not-differentiable-conclusion){.pf-ref} give the required counterexample.
:::

:::
:::
