---
schema: qual/card@1
id: P-WESCA05-II1
kind: problem
title: "Laurent series of $e^{1/z^2}$ on the punctured plane"
classification:
  areas: [complex-analysis]
  topics:
  - Laurent Series
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis section 2, problem 1 (Summer 2005) in the deterministic MinerU Flash extraction assets/attachments/analysis_2003-2007_extracted.md.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read the item on 2026-11-19 in the retained scan
    assets/attachments/analysis_2003-2007.pdf at PDF p. 27: the Complex Analysis Section of
    the Analysis Qualifier, Wesleyan University, Summer 2005, Section 2 item 1. The page had cited
    only the extraction; it now names the examination, its item and the page of the
    scan. The statement is unchanged.

- event: source-corrected
  by: claude
  date: 2026-11-19
  note: >-
    The proof ended with a pf-qed that only announced that an earlier step had
    answered the question, which STYLE-08 forbids; it is dropped, and the step that
    carries the result is now the QED step. No argument or statement changes.

---

::: {.problem}
Expand
$$
f(z)=e^{1/z^2}
$$
in a Laurent series on the annulus $0<\abs{z}<\infty$.
:::

::: {.solution}
The item is Section 2 item 1 of the Complex Analysis Section of the Analysis Qualifier, Wesleyan
University, Summer 2005 (Laurent series of e^{1/z^2} on 0<|z|<infty), on PDF p. 27 of the retained scan
assets/attachments/analysis_2003-2007.pdf.


::: pf

::: {.pf-step #s1-1}

The exponential power series gives
$$
e^w=\sum_{n=0}^{\infty}\frac{w^n}{n!}
$$
for every $w\in\CC$.


::: pf-proof

The exponential function is entire, and its Taylor series about $0$ has infinite radius of convergence.

:::

:::

::: {.pf-step #s1-2}

For every $z\ne0$, substituting
$$
w=\frac1{z^2}
$$
into step [](#s1-1){.pf-ref} gives
$$
e^{1/z^2}
=
\sum_{n=0}^{\infty}\frac{1}{n!z^{2n}}.
$$


::: pf-proof

If $z\ne0$, then $w=1/z^2$ is a well-defined complex number. Since the series in step [](#s1-1){.pf-ref} converges for every complex $w$, this substitution is valid.

:::

:::

::: {.pf-step #s1-3}

Hence the Laurent expansion on $0<\abs{z}<\infty$ is
$$
\boxed{
e^{1/z^2}
=
1+\frac1{z^2}+\frac1{2!z^4}
+\frac1{3!z^6}+\cdots
=
\sum_{n=0}^{\infty}\frac{z^{-2n}}{n!}.}
$$


::: pf-proof

Step [](#s1-2){.pf-ref} gives the Laurent series. Its convergence domain is exactly the punctured plane: for every $z\ne0$, it is the convergent exponential series evaluated at $1/z^2$, while the expression is not defined at $z=0$.

:::

:::


:::

:::
