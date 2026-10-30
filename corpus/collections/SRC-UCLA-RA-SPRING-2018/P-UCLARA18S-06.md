---
schema: qual/card@1
id: P-UCLARA18S-06
kind: problem
title: Existence of optimal couplings on the circle
classification:
  areas:
  - real-analysis
  topics:
  - Weak Convergence
  - Borel Measures
  - Compactness
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2018, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Problem 6. Let $\circlegroup$ denote the unit circle in the complex plane, let $\mathcal P(\circlegroup)$ denote the space of Borel probability measures on $\circlegroup$, and let $\mathcal P(\circlegroup\times\circlegroup)$ denote the space of Borel probability measures on $\circlegroup\times\circlegroup$. Fix $\mu,\nu\in\mathcal P(\circlegroup)$ and define
$$
\mathcal M=\left\{\gamma\in\mathcal P(\circlegroup\times\circlegroup):
\iint_{\circlegroup\times\circlegroup}f(x)g(y)\,d\gamma(x,y)
=\int_{\circlegroup}f(x)\,d\mu(x)\int_{\circlegroup}g(y)\,d\nu(y)
\text{ for all }f,g\in C(\circlegroup)\right\}.
$$
Show that $F:\mathcal M\to\RR$ defined by
$$
F(\gamma)=\iint_{\circlegroup\times\circlegroup}
\sin^2\!\left(\frac{\theta-\phi}{2}\right)
\,d\gamma(e^{i\theta},e^{i\phi})
$$
achieves its minimum on $\mathcal M$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

The set $\mathcal M$ is nonempty.


::: pf-proof

The product probability measure
$$
\mu\times\nu
$$
belongs to $\mathcal P(\circlegroup\times\circlegroup)$. For every
$$
f,g\in C(\circlegroup),
$$
Fubini's theorem gives
$$
\iint f(x)g(y)\,d(\mu\times\nu)(x,y)
=
\left(\int f\,d\mu\right)
\left(\int g\,d\nu\right).
$$
Thus
$$
\mu\times\nu\in\mathcal M.
$$

:::

:::

::: {.pf-step #s1-2}

For
$$
x=e^{i\theta},
\qquad
y=e^{i\phi},
$$
the cost satisfies
$$
\boxed{
\sin^2\!\left(\frac{\theta-\phi}{2}\right)
=
\frac12
\left(
1
-
\operatorname{Re}(x)\operatorname{Re}(y)
-
\operatorname{Im}(x)\operatorname{Im}(y)
\right)}.
$$


::: pf-proof

Use
$$
\sin^2\frac{\alpha}{2}
=
\frac{1-\cos\alpha}{2}
$$
and
$$
\cos(\theta-\phi)
=
\cos\theta\cos\phi
+
\sin\theta\sin\phi.
$$
Since
$$
\operatorname{Re}(e^{i\theta})=\cos\theta,
\qquad
\operatorname{Im}(e^{i\theta})=\sin\theta,
$$
the displayed identity follows.

:::

:::

::: {.pf-step #s1-3}

For every $\gamma\in\mathcal M$,
$$
\begin{aligned}
F(\gamma)
=
\frac12
\Bigg[
1
&-
\left(\int_{\circlegroup}\operatorname{Re}(x)\,d\mu(x)\right)
\left(\int_{\circlegroup}\operatorname{Re}(y)\,d\nu(y)\right)\\
&-
\left(\int_{\circlegroup}\operatorname{Im}(x)\,d\mu(x)\right)
\left(\int_{\circlegroup}\operatorname{Im}(y)\,d\nu(y)\right)
\Bigg].
\end{aligned}
$$


::: pf-proof

The functions
$$
1,\qquad
\operatorname{Re},\qquad
\operatorname{Im}
$$
are continuous on $\circlegroup$. Apply the defining identity of
$\mathcal M$ to the three product functions
$$
1\cdot1,\qquad
\operatorname{Re}(x)\operatorname{Re}(y),\qquad
\operatorname{Im}(x)\operatorname{Im}(y),
$$
and then use the cost decomposition from step [](#s1-2){.pf-ref}.

:::

:::

::: {.pf-step #s1-4}

The value in step [](#s1-3){.pf-ref} is independent of $\gamma$.


::: pf-proof

Every quantity on the right-hand side depends only on the fixed measures
$$
\mu
\qquad\text{and}\qquad
\nu.
$$
Thus the same value is obtained for every $\gamma\in\mathcal M$.

:::

:::

::: {.pf-step #s1-5}

Therefore $F$ attains its minimum on $\mathcal M$.


::: pf-proof

By step [](#s1-1){.pf-ref}, $\mathcal M\ne\varnothing$. By step [](#s1-4){.pf-ref}, $F$ is constant
on $\mathcal M$. Hence every $\gamma\in\mathcal M$, in particular
$\mu\times\nu$, is a minimizer.

:::

:::

::: pf-qed

Step [](#s1-5){.pf-ref} proves the claim.

:::

:::

:::
