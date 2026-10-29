---
schema: qual/card@1
id: P-UCLAB06W-05
kind: problem
title: Hessian determinant at a minimum
classification:
  areas: [prelim]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 5 of the official UCLA Basic Qual Winter 2006 PDF.
---

::: {.problem}
Let $f(x,y)$ be twice continuously differentiable and suppose that $f$ has its unique minimum at $(0,0)$.
Prove carefully that at $(0,0)$,
$$
\frac{\partial^2f}{\partial x^2}\frac{\partial^2f}{\partial y^2}
\geq
\left(\frac{\partial^2f}{\partial x\partial y}\right)^2.
$$

You may use without proof that the mixed partials are equal for $C^2$ functions.
:::

::: {.solution}

Write
$$
a=f_{xx}(0,0),
\qquad
b=f_{xy}(0,0)=f_{yx}(0,0),
\qquad
c=f_{yy}(0,0).
$$

::: pf

::: {.pf-step #s1-1}

For every $(u,v)\in\RR^2$,
$$
au^2+2buv+cv^2\ge0.
$$


::: pf-proof

Fix $(u,v)\in\RR^2$ and define the one-variable function
$$
\phi(t)=f(tu,tv).
$$
Since $(0,0)$ is a minimum of $f$, the point $t=0$ is a minimum of $\phi$. Because $f$ is $C^2$, the function $\phi$ is twice differentiable, and a twice differentiable function at a local minimum satisfies
$$
\phi''(0)\ge0.
$$
By the chain rule,
$$
\phi''(0)
=u^2f_{xx}(0,0)
+2uvf_{xy}(0,0)
+v^2f_{yy}(0,0),
$$
where equality of the mixed partials is used. This is exactly the displayed inequality.

:::

:::

::: {.pf-step #s1-2}

One has
$$
a\ge0
\qquad\text{and}\qquad
c\ge0.
$$


::: pf-proof

Apply step [](#s1-1){.pf-ref} first to $(u,v)=(1,0)$ and then to $(u,v)=(0,1)$.

:::

:::

::: {.pf-step #s1-3}

If $c>0$, then
$$
b^2\le ac.
$$


::: pf-proof

By step [](#s1-1){.pf-ref}, for every $t\in\RR$,
$$
a+2bt+ct^2\ge0.
$$
Since $c>0$, this quadratic polynomial has nonpositive discriminant; otherwise it would take negative values between two distinct real roots. Hence
$$
(2b)^2-4ac\le0,
$$
which is equivalent to $b^2\le ac$.

:::

:::

::: {.pf-step #s1-4}

If $c=0$, then $b=0$, and hence again
$$
b^2\le ac.
$$


::: pf-proof

With $c=0$, step [](#s1-1){.pf-ref} applied to $(u,v)=(1,t)$ gives
$$
a+2bt\ge0
$$
for every $t\in\RR$. If $b\ne0$, choosing $t$ with sufficiently large magnitude and sign opposite to $b$ makes the left-hand side negative. Therefore $b=0$. Since $c=0$, both sides of $b^2\le ac$ are then zero.

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{
f_{xx}(0,0)f_{yy}(0,0)
\ge
f_{xy}(0,0)^2
}.
$$


::: pf-proof

By step [](#s1-2){.pf-ref}, either $c>0$ or $c=0$. Step [](#s1-3){.pf-ref} handles the first case and step [](#s1-4){.pf-ref} the second. Substituting the definitions of $a,b,c$ gives the displayed inequality.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} is the required conclusion. The uniqueness of the minimum is stronger than needed; only the fact that $(0,0)$ is a local minimum enters the proof.

:::

:::

:::
