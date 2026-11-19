---
schema: qual/card@1
id: P-WESCA04-P1
kind: problem
title: "An entire function with real part bounded above is constant"
classification:
  areas: [complex-analysis]
  topics:
  - 'Liouville''s Theorem'
  - Entire Functions
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis section 1.3, problem 1 (August 2, 2004) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read the item on 2026-11-19 in the retained scan
    assets/attachments/analysis_2003-2007.pdf at PDF p. 34, printed page 2: section 1.3 item 1 of
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
Let $f$ be entire and suppose
$$
\operatorname{Re} f(z)\le 10
\qquad(z\in\CC).
$$
Show that $f$ is constant.
:::

::: {.solution}
The item is section 1.3 item 1 of the Preliminary Examination in Analysis, Wesleyan University,
August 2, 2004 (an entire function whose real part is bounded above is constant), on PDF p. 34 of the retained scan
assets/attachments/analysis_2003-2007.pdf, printed page 2.


::: pf

::: {.pf-step #s1-1}

Define
$$
g(z)
\coloneqq
e^{f(z)}.
$$
Then $g$ is entire.


::: pf-proof

The function $f$ is entire by hypothesis, and the exponential function is
entire on $\CC$. Therefore their composition
$$
g=\exp\circ f
$$
is entire.

:::

:::

::: {.pf-step #s1-2}

The function $g$ is bounded:
$$
\abs{g(z)}
\le
e^{10}
\qquad
(z\in\CC).
$$


::: pf-proof

For every complex number $w$,
$$
\abs{e^w}
=
e^{\operatorname{Re}w}.
$$
Hence
$$
\abs{g(z)}
=
\abs{e^{f(z)}}
=
e^{\operatorname{Re}f(z)}
\le
e^{10}
$$
by the hypothesis.

:::

:::

::: pf-step

Liouville's theorem implies that $g$ is constant.


::: pf-proof

Steps [](#s1-1){.pf-ref} through [](#s1-2){.pf-ref} show that $g$ is a bounded entire function. Liouville's
theorem therefore gives
$$
g(z)\equiv c
$$
for some constant $c\in\CC$.

:::

:::

::: {.pf-step #s1-4}

The constant $c$ is nonzero.


::: pf-proof

The exponential function never vanishes:
$$
e^w\ne0
\qquad
(w\in\CC).
$$
Thus
$$
g(z)=e^{f(z)}\ne0
$$
for every $z$, so its constant value is nonzero.

:::

:::

::: pf-step

One has
$$
f'(z)=0
\qquad
(z\in\CC).
$$


::: pf-proof

Differentiate the identity
$$
e^{f(z)}=c.
$$
The chain rule gives
$$
e^{f(z)}f'(z)=0.
$$
By step [](#s1-4){.pf-ref},
$$
e^{f(z)}=c\ne0.
$$
Therefore
$$
f'(z)=0
$$
for every $z$.

:::

:::

::: {.pf-step #s1-6}

Hence
$$
\boxed{f\text{ is constant}.}
$$


::: pf-proof

An entire function with identically zero derivative is constant on the
connected plane $\CC$.

:::

:::


:::

:::
