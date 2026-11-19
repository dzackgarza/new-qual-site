---
schema: qual/card@1
id: P-WESCA04-E1
kind: problem
title: "Examples of removable, pole, and essential singularities at the origin"
classification:
  areas: [complex-analysis]
  topics:
  - Singularities
  - Poles
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis section 1.2, item 1 (August 2, 2004) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read the item on 2026-11-19 in the retained scan
    assets/attachments/analysis_2003-2007.pdf at PDF p. 33, printed page 1: section 1.2 item 1 of
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

---

::: {.problem}
Give an example each of an analytic function having at the origin:

1. a removable singularity;

2. a pole;

3. an essential singularity.
:::

::: {.solution}
The item is section 1.2 item 1 of the Preliminary Examination in Analysis, Wesleyan University,
August 2, 2004 (examples of a removable singularity, a pole and an essential singularity at the origin), on PDF p. 33 of the retained scan
assets/attachments/analysis_2003-2007.pdf, printed page 1.


::: pf

::: {.pf-step #s1-1}

A removable singularity at the origin is given by
$$
f_1(z)
\coloneqq
\frac{\sin z}{z},
\qquad
z\ne0.
$$


::: pf-proof

The Taylor series for sine is
$$
\sin z
=
z-\frac{z^3}{3!}
+\frac{z^5}{5!}
-\cdots.
$$
Therefore, for $z\ne0$,
$$
\frac{\sin z}{z}
=
1-\frac{z^2}{3!}
+\frac{z^4}{5!}
-\cdots.
$$
The right-hand side is a power series convergent at $z=0$, so defining
$$
f_1(0)=1
$$
extends $f_1$ holomorphically across the origin. Hence the singularity is
removable.

:::

:::

::: {.pf-step #s1-2}

A pole at the origin is given by
$$
f_2(z)
\coloneqq
\frac1z.
$$


::: pf-proof

The Laurent expansion of $f_2$ at $0$ is simply
$$
f_2(z)=z^{-1}.
$$
Thus the principal part has one nonzero term and the coefficient of
$z^{-1}$ is nonzero. Equivalently,
$$
z f_2(z)=1
$$
extends holomorphically and nonvanishingly across $0$. Hence $0$ is a pole
of order $1$.

:::

:::

::: {.pf-step #s1-3}

An essential singularity at the origin is given by
$$
f_3(z)
\coloneqq
e^{1/z},
\qquad
z\ne0.
$$


::: pf-proof

Substitute $1/z$ into the exponential series:
$$
e^{1/z}
=
\sum_{n=0}^{\infty}
\frac1{n!z^n}
=
1
+\frac1z
+\frac1{2!z^2}
+\frac1{3!z^3}
+\cdots.
$$
Its Laurent series has infinitely many nonzero negative-power terms.

A removable singularity has no negative-power terms, while a pole has only
finitely many. Therefore the singularity of $e^{1/z}$ at $0$ is essential.

:::

:::

::: {.pf-step #s1-4}

Thus one valid list is
$$
\boxed{
\frac{\sin z}{z},
\qquad
\frac1z,
\qquad
e^{1/z},
}
$$
for removable, pole, and essential singularities respectively.


::: pf-proof

This is exactly the content of steps [](#s1-1){.pf-ref} through [](#s1-3){.pf-ref}.

:::

:::


:::

:::
