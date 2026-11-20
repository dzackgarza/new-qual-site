---
schema: qual/card@1
id: P-WESCA04-P5
kind: problem
title: "Uniform convergence on the boundary controls a holomorphic sequence inside"
classification:
  areas: [complex-analysis]
  topics:
  - Uniform Convergence
  - Holomorphic Functions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis section 1.3, problem 5 (August 2, 2004) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md. Flash drops the closure bar from the continuity domain, while the same sentence requires boundary values on $\partial D$; the card normalizes that concrete extraction defect to $\overline D$.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read the item on 2026-11-19 in the retained scan
    assets/attachments/analysis_2003-2007.pdf at PDF p. 34, printed page 2: section 1.3 item 5 of
    the Preliminary Examination in Analysis, Wesleyan University, August 2, 2004. The
    page had cited only the extraction; it now names the examination, its item and the
    page of the scan. The statement is unchanged.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    The proof ended with a pf-qed that only announced that an earlier step had answered
    the question, which STYLE-08 forbids; it is dropped, and the step that carries the
    result is now the QED step. No argument or statement changes.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    Read at 200 dpi on 2026-11-19, the printed item 5 concludes uniform convergence on D, not on
    the closure, while its continuity hypothesis is on the closure. The card had carried the
    stronger conclusion on the closure as if it were the printed one; the statement now reads as
    printed, and the solution records that its maximum-modulus step yields the stronger
    conclusion on the closure.

---

::: {.problem}
Let $D\subset\CC$ be a bounded domain.
Suppose each $f_n$ is continuous on $\overline D$ and analytic on $D$.
If $(f_n)$ converges uniformly on $\partial D$, prove that it converges uniformly on $D$.
:::

::: {.solution}
The item is section 1.3 item 5 of the Preliminary Examination in Analysis, Wesleyan University,
August 2, 2004 (uniform convergence on the boundary of a bounded domain gives uniform convergence on the domain), on PDF p. 34 of the retained scan
assets/attachments/analysis_2003-2007.pdf, printed page 2.
The printed conclusion is uniform convergence on $D$; the maximum-modulus step below gives it on
$\overline D$, which is the stronger statement, so the printed conclusion follows.

::: pf

::: {.pf-step #s1-1}

Since
$$
f_n\restrict_{\partial D}
$$
converges uniformly, the sequence is uniformly Cauchy on
$$
\partial D.
$$


::: pf-proof

Uniform convergence in the supremum norm implies the Cauchy property:
for every
$$
\varepsilon>0
$$
there exists
$$
N
$$
such that for
$$
m,n\ge N,
$$
$$
\sup_{z\in\partial D}
\abs{f_n(z)-f_m(z)}
<
\varepsilon.
$$

:::

:::

::: {.pf-step #s1-2}

For fixed $m,n$, define
$$
h_{m,n}
\coloneqq
f_n-f_m.
$$
Then $h_{m,n}$ is continuous on
$$
\overline D
$$
and holomorphic on $D$.


::: pf-proof

Both properties are preserved under subtraction.

:::

:::

::: {.pf-step #s1-3}

For every $m,n$,
$$
\boxed{
\sup_{z\in\overline D}
\abs{h_{m,n}(z)}
\le
\sup_{z\in\partial D}
\abs{h_{m,n}(z)}.
}
$$


::: pf-proof

Because $D$ is bounded,
$$
\overline D
$$
is compact.
Since $h_{m,n}$ is continuous on $\overline D$,
$$
\abs{h_{m,n}}
$$
attains its maximum there.

If a positive strict maximum occurred at a point of the interior $D$, the
maximum modulus principle would force $h_{m,n}$ to be constant on the
connected domain $D$.
In that constant case the same modulus occurs on the boundary as well.

Thus in all cases the supremum on the closure is bounded by the supremum on
the boundary.

:::

:::

::: {.pf-step #s1-4}

The sequence
$$
(f_n)
$$
is uniformly Cauchy on
$$
\overline D.
$$


::: pf-proof

Fix
$$
\varepsilon>0.
$$
Choose
$$
N
$$
from step [](#s1-1){.pf-ref}.
For
$$
m,n\ge N,
$$
step [](#s1-3){.pf-ref} gives
$$
\begin{aligned}
\sup_{z\in\overline D}
\abs{f_n(z)-f_m(z)}
&=
\sup_{z\in\overline D}
\abs{h_{m,n}(z)}\\
&\le
\sup_{z\in\partial D}
\abs{h_{m,n}(z)}\\
&<
\varepsilon.
\end{aligned}
$$

:::

:::

::: {.pf-step #s1-5}

There exists a continuous function
$$
f:\overline D\to\CC
$$
such that
$$
f_n\longrightarrow f
$$
uniformly on
$$
\overline D.
$$


::: pf-proof

The compact space
$$
\overline D
$$
has a complete supremum-norm function space
$$
C(\overline D).
$$
Step [](#s1-4){.pf-ref} says
$$
(f_n)
$$
is Cauchy in this Banach space.
Hence it converges in the supremum norm to some
$$
f\in C(\overline D).
$$

:::

:::

::: pf-step

Moreover, the limit $f$ is holomorphic on $D$.


::: pf-proof

Uniform convergence on
$$
\overline D
$$
implies locally uniform convergence on $D$.
By the Weierstrass theorem on locally uniform limits of holomorphic
functions,
$$
f\restrict_D
$$
is holomorphic.
This extra conclusion is not required for the uniform-convergence claim.

:::

:::


:::

:::
