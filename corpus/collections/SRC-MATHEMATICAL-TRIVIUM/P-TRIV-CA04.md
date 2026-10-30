---
schema: qual/card@1
id: P-TRIV-CA04
kind: problem
title: Laurent series of $e^z/(z-1)^2$ about $z=1$
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis, Problem 4, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
Compute the Laurent series of $f(z) = \frac{e^z}{(z - 1)^2}$ around $z_0 = 1$; give the region of convergence.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Write
$$
e^z
=
e\,e^{z-1}.
$$


::: pf-proof

Since
$$
z=1+(z-1),
$$
one has
$$
e^z
=
e^{1+(z-1)}
=
e\,e^{z-1}.
$$

:::

:::

::: {.pf-step #s1-2}

The Taylor series of $e^{z-1}$ is
$$
e^{z-1}
=
\sum_{n=0}^{\infty}
\frac{(z-1)^n}{n!},
$$
with infinite radius of convergence.


::: pf-proof

This is the standard exponential power series centered at $0$, applied to
$z-1$.

:::

:::

::: {.pf-step #s1-3}

Therefore
$$
\boxed{
\frac{e^z}{(z-1)^2}
=
e
\sum_{n=0}^{\infty}
\frac{(z-1)^{n-2}}{n!}.
}
$$


::: pf-proof

Substitute step [](#s1-2){.pf-ref} into step [](#s1-1){.pf-ref} and divide termwise by $(z-1)^2$.

:::

:::

::: {.pf-step #s1-4}

In expanded form,
$$
\boxed{
\frac{e^z}{(z-1)^2}
=
\frac{e}{(z-1)^2}
+
\frac{e}{z-1}
+
\frac e{2!}
+
\frac e{3!}(z-1)
+
\frac e{4!}(z-1)^2
+\cdots.
}
$$


::: pf-proof

Write out the first terms of the series in step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-5}

The region of convergence is
$$
\boxed{
0<\abs{z-1}<\infty.
}
$$


::: pf-proof

The exponential series has infinite radius of convergence, so the shifted
series in step [](#s1-3){.pf-ref} converges for every finite $z$. The only excluded point is
$z=1$, where the original function has a pole of order $2$.

:::

:::

::: pf-qed

Steps [](#s1-4){.pf-ref} and [](#s1-5){.pf-ref} give the Laurent series and its region of convergence.

:::

:::

:::
