---
schema: qual/card@1
id: P-WESCA07-III2
kind: problem
title: "A quadratic Schwarz-type estimate from a derivative bound"
classification:
  areas: [complex-analysis]
  topics:
  - Schwarz Lemma
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis Section III, problem 2 (Summer 2007) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read the item on 2026-11-19 in the retained scan
    assets/attachments/analysis_2003-2007.pdf at PDF p. 11 (printed p. 4 of the 2007 complex-analysis paper). The card had cited neither the
    examination nor a page; it now names both, and the statement was compared with the
    printed item and left unchanged.
- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    The proof ended with a pf-qed that only announced that an earlier step had answered
    the question, which STYLE-08 forbids; it is dropped, and the step that carries the
    result is now the QED step. No argument or statement changes.

---

::: {.problem}
Let $f$ be analytic on the unit disk $D$, with
$$
f(0)=f'(0)=0,
\qquad
\abs{f'(z)}<1\quad(z\in D).
$$
Show that
$$
\abs{f(z)}\le\frac{\abs{z}^2}{2}
\qquad(z\in D).
$$

Hint: represent $f(z)$ as a path integral along a convenient path.
:::

::: {.solution}
The item is Section 3 item 2 of the Complex Analysis section of the Analysis Qualifier, Wesleyan University, Summer 2007 ($\abs{f'(z)}<1$ with $f(0)=f'(0)=0$ forces $\abs{f(z)}\le\abs{z}^2/2$), in the retained scan
assets/attachments/analysis_2003-2007.pdf.


::: pf

::: {.pf-step #s1-1}

The derivative $f'$ maps $D$ into the unit disk and satisfies
$$
f'(0)=0.
$$


::: pf-proof

This is exactly the given hypothesis
$$
\abs{f'(z)}<1
$$
for $z\in D$, together with $f'(0)=0$.

:::

:::

::: {.pf-step #s1-2}

For every $w\in D$,
$$
\abs{f'(w)}\le \abs{w}.
$$


::: pf-proof

The function $f'$ is holomorphic on $D$, maps $D$ into itself by step [](#s1-1){.pf-ref}, and vanishes at $0$. Schwarz's lemma therefore gives
$$
\abs{f'(w)}\le\abs{w}.
$$

:::

:::

::: {.pf-step #s1-3}

For every $z\in D$,
$$
f(z)=\int_0^1 f'(tz)\,z\,dt.
$$


::: pf-proof

Integrate $f'$ along the straight-line path
$$
\gamma(t)=tz,
\qquad 0\le t\le1.
$$
Since $f(0)=0$,
$$
f(z)-f(0)
=\int_\gamma f'(w)\,dw
=\int_0^1 f'(tz)\,z\,dt.
$$

:::

:::

::: {.pf-step #s1-4}

One has
$$
\boxed{\abs{f(z)}\le\frac{\abs{z}^2}{2}}
$$
for every $z\in D$.


::: pf-proof

By steps [](#s1-2){.pf-ref} and [](#s1-3){.pf-ref},
$$
\begin{aligned}
\abs{f(z)}
&\le\int_0^1 \abs{f'(tz)}\,\abs{z}\,dt\\
&\le\int_0^1 t\abs{z}^2\,dt\\
&=\frac{\abs{z}^2}{2}.
\end{aligned}
$$

:::

:::


:::

:::
