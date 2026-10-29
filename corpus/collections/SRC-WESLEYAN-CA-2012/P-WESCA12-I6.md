---
schema: qual/card@1
id: P-WESCA12-I6
kind: problem
title: 'State the Argument Principle'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Basic facts, item 6 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
State the Argument Principle.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

**Argument Principle.**

Let $f$ be meromorphic on a domain containing a positively oriented simple
closed contour
$$
\gamma
$$
and its interior.
Assume $f$ has no zero and no pole on $\gamma$.
Let
$$
N
$$
be the number of zeros of $f$ inside $\gamma$, counted with multiplicity,
and let
$$
P
$$
be the number of poles inside $\gamma$, counted with order.
Then
$$
\boxed{
\frac1{2\pi i}
\int_\gamma
\frac{f'(z)}{f(z)}
\,dz
=
N-P.
}
$$


::: pf-proof

At a zero $a$ of multiplicity $m$,
$$
f(z)
=
(z-a)^m g(z),
\qquad
g(a)\ne0,
$$
so
$$
\frac{f'(z)}{f(z)}
=
\frac{m}{z-a}
+
\frac{g'(z)}{g(z)}.
$$
Thus
$$
\operatorname{Res}_{z=a}
\frac{f'}f
=
m.
$$

At a pole $b$ of order $n$,
$$
f(z)
=
(z-b)^{-n}h(z),
\qquad
h(b)\ne0,
$$
so
$$
\operatorname{Res}_{z=b}
\frac{f'}f
=
-n.
$$

The residue theorem therefore gives
$$
\frac1{2\pi i}
\int_\gamma
\frac{f'}f
=
\sum \text{zero multiplicities}
-
\sum \text{pole orders}
=
N-P.
$$

:::

:::

::: {.pf-step #s1-2}

Equivalently,
$$
N-P
$$
is the winding number of the closed curve
$$
f\circ\gamma
$$
about the origin.


::: pf-proof

Along $\gamma$,
$$
w=f(z)
$$
gives
$$
dw=f'(z)\,dz.
$$
Hence
$$
\frac1{2\pi i}
\int_\gamma
\frac{f'(z)}{f(z)}
\,dz
=
\frac1{2\pi i}
\int_{f\circ\gamma}
\frac{dw}{w},
$$
which is precisely
$$
\operatorname{Ind}(f\circ\gamma,0).
$$

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} is the standard Argument Principle, and step [](#s1-2){.pf-ref} records its
winding-number interpretation.

:::

:::

:::
