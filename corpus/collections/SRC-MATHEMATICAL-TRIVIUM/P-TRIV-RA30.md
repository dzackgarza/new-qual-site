---
schema: qual/card@1
id: P-TRIV-RA30
kind: problem
title: Asymptotic approximation of the cosine integral $\operatorname{Ci}x$
classification:
  areas: [real-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Real Analysis, Problem 30, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Show that the cosine integral $\operatorname{Ci} x \equiv -\int_x^{\infty} \frac{\cos t}{t}\, dt$ for large enough $x$ can be approximated as $\operatorname{Ci} x \approx \frac{\sin x}{x}$. Find the region of $x$ for which the relative error of this approximation is less than $10^{-4}$.
:::

::: {.remark}
There is no single tail interval $(X,\infty)$ on which the relative error is
uniformly small: at every $x=n\pi$ the approximation $\sin x/x$ vanishes while
$\operatorname{Ci}(x)$ does not. Thus the requested “region” is necessarily a
union of intervals excluding neighborhoods of the zeros of $\sin x$.
:::

::: {.solution}

Let
$$
A(x)=\frac{\sin x}{x}.
$$

::: pf

::: {.pf-step #s1-1}

Integration by parts gives
$$
\operatorname{Ci}(x)
=
\frac{\sin x}{x}
-
\int_x^\infty\frac{\sin t}{t^2}\,dt.
$$


::: pf-proof

Starting from
$$
\operatorname{Ci}(x)
=
-\int_x^\infty\frac{\cos t}{t}\,dt,
$$
integrate the integral on the right by parts with
$$
u=\frac1t,
\qquad
dv=\cos t\,dt.
$$
Then
$$
du=-\frac{dt}{t^2},
\qquad
v=\sin t,
$$
and the boundary term at infinity vanishes. Hence
$$
\int_x^\infty\frac{\cos t}{t}\,dt
=
-\frac{\sin x}{x}
+
\int_x^\infty\frac{\sin t}{t^2}\,dt.
$$
Negating gives the formula.

:::

:::

::: {.pf-step #s1-2}

Therefore
$$
\operatorname{Ci}(x)-A(x)
=
-\int_x^\infty\frac{\sin t}{t^2}\,dt.
$$


::: pf-proof

Subtract $A(x)=\sin x/x$ from step [](#s1-1){.pf-ref}.

:::

:::

::: {.pf-step #s1-3}

For $x>0$,
$$
\abs{
\int_x^\infty\frac{\sin t}{t^2}\,dt
}
\leq
\frac{2}{x^2}.
$$


::: pf-proof

Let
$$
F(T)=\int_x^T\sin t\,dt
=
\cos x-\cos T.
$$
Then $\abs{F(T)}\leq2$. Integration by parts in the Dirichlet form gives
$$
\int_x^R\frac{\sin t}{t^2}\,dt
=
\frac{F(R)}{R^2}
+
2\int_x^R\frac{F(t)}{t^3}\,dt.
$$
Letting $R\to\infty$ and using $\abs{F}\leq2$ gives
$$
\abs{
\int_x^\infty\frac{\sin t}{t^2}\,dt
}
\leq
4\int_x^\infty t^{-3}\,dt
=
\frac{2}{x^2}.
$$

:::

:::

::: {.pf-step #s1-4}

Hence, whenever $\sin x\neq0$,
$$
\frac{\abs{\operatorname{Ci}(x)-A(x)}}{\abs{A(x)}}
\leq
\frac{2}{x\abs{\sin x}}.
$$


::: pf-proof

Combine steps [](#s1-2){.pf-ref} through [](#s1-3){.pf-ref} and divide by
$$
\abs{A(x)}
=
\frac{\abs{\sin x}}{x}.
$$

:::

:::

::: {.pf-step #s1-5}

Put
$$
q(x)=\frac{2}{x\abs{\sin x}}.
$$
If $q(x)<1$, then
$$
\frac{\abs{\operatorname{Ci}(x)-A(x)}}{\abs{\operatorname{Ci}(x)}}
\leq
\frac{q(x)}{1-q(x)}.
$$


::: pf-proof

Step [](#s1-4){.pf-ref} gives
$$
\abs{\operatorname{Ci}(x)-A(x)}
\leq
q(x)\abs{A(x)}.
$$
The reverse triangle inequality then gives
$$
\abs{\operatorname{Ci}(x)}
\geq
\abs{A(x)}-\abs{\operatorname{Ci}(x)-A(x)}
\geq
(1-q(x))\abs{A(x)}.
$$
Divide the two estimates.

:::

:::

::: {.pf-step #s1-6}

A sufficient condition for true relative error below $10^{-4}$ is
$$
\boxed{x\abs{\sin x}>20002}.
$$


::: pf-proof

Let
$$
\varepsilon=10^{-4}.
$$
By step [](#s1-5){.pf-ref}, it suffices to require
$$
\frac{q}{1-q}<\varepsilon.
$$
This is equivalent to
$$
q<\frac{\varepsilon}{1+\varepsilon}.
$$
Since
$$
q=\frac{2}{x\abs{\sin x}},
$$
it suffices that
$$
x\abs{\sin x}
>
\frac{2(1+\varepsilon)}{\varepsilon}
=
20002.
$$

:::

:::

::: {.pf-step #s1-7}

The large-$x$ asymptotic expansion begins
$$
\operatorname{Ci}(x)
=
\frac{\sin x}{x}
-
\frac{\cos x}{x^2}
+
O(x^{-3}).
$$


::: pf-proof

Integrate the remainder in step [](#s1-1){.pf-ref} once more by parts:
$$
\int_x^\infty\frac{\sin t}{t^2}\,dt
=
\frac{\cos x}{x^2}
-
2\int_x^\infty\frac{\cos t}{t^3}\,dt.
$$
The last integral is $O(x^{-3})$ by the same Dirichlet estimate used in step
[](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

Away from zeros of $\sin x$, the pointwise relative error therefore has
the asymptotic form
$$
\boxed{
\frac{\abs{\operatorname{Ci}(x)-\sin x/x}}{\abs{\sin x/x}}
=
\frac{\abs{\cot x}}{x}
+
O(x^{-2}).
}
$$


::: pf-proof

Subtract the leading approximation from step [](#s1-7){.pf-ref} and divide by
$\abs{\sin x}/x$.

:::

:::

::: {.pf-step #s1-9}

No condition of the form $x>X$ alone can guarantee relative error below
$10^{-4}$.


::: pf-proof

For every $X$ there is an integer $n$ with $n\pi>X$. At $x=n\pi$,
$$
A(x)=\frac{\sin(n\pi)}{n\pi}=0,
$$
whereas step [](#s1-7){.pf-ref} gives
$$
\operatorname{Ci}(n\pi)
=
-\frac{(-1)^n}{(n\pi)^2}
+
O(n^{-3}),
$$
which is nonzero for all sufficiently large $n$. Thus the approximation cannot
have small relative error on an entire tail interval.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} proves the leading approximation, step [](#s1-6){.pf-ref} gives a rigorous region
with relative error below $10^{-4}$, and steps [](#s1-8){.pf-ref} through [](#s1-9){.pf-ref} describe the
asymptotically sharp pointwise behavior and the unavoidable exclusions near
zeros of $\sin x$.

:::

:::

:::
