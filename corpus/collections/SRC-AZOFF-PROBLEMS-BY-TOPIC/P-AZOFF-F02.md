---
schema: qual/card@1
id: P-AZOFF-F02
kind: problem
title: Laurent expansions of $e^{1/z}$ and $\cos(1/z)$
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Laurent expansions and singularities, Problem 2, in the deterministic MinerU Flash extraction assets/attachments/Azoff Problems by Topic_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Substituted w=1/z into the globally convergent Taylor series for the
    exponential and cosine. The resulting Laurent series converge for every
    z nonzero, which is the maximal punctured-plane annulus about the origin.
---

::: {.problem}
Find the Laurent expansions of $\exp ( \textstyle { \frac { 1 } { z } } )$ and $\cos { \left( { \frac { 1 } { z } } \right) }$ about the origin.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

The Laurent expansion of $e^{1/z}$ about the origin is
$$
\boxed{
e^{1/z}
=
\sum_{n=0}^{\infty}\frac{z^{-n}}{n!}.
}
$$
It converges on the maximal annulus
$$
0<\abs{z}<\infty.
$$

::: pf-proof

The exponential Taylor series
$$
e^w
=
\sum_{n=0}^{\infty}\frac{w^n}{n!}
$$
converges for every $w\in\CC$. For $z\neq0$, substitute
$$
w=\frac1z.
$$
This gives
$$
e^{1/z}
=
\sum_{n=0}^{\infty}\frac{z^{-n}}{n!}.
$$
Since the Taylor series converges for every finite value of $w=1/z$, the
Laurent series converges for every $z\neq0$. Thus its annulus of convergence
about the origin is $0<\abs{z}<\infty$.

:::

:::

::: {.pf-step #s2}

The Laurent expansion of $\cos(1/z)$ about the origin is
$$
\boxed{
\cos(1/z)
=
\sum_{n=0}^{\infty}
\frac{(-1)^n z^{-2n}}{(2n)!}.
}
$$
It also converges on
$$
0<\abs{z}<\infty.
$$

::: pf-proof

The cosine Taylor series
$$
\cos w
=
\sum_{n=0}^{\infty}
\frac{(-1)^n w^{2n}}{(2n)!}
$$
converges for every $w\in\CC$. Substituting $w=1/z$ for $z\neq0$ gives
$$
\cos(1/z)
=
\sum_{n=0}^{\infty}
\frac{(-1)^n z^{-2n}}{(2n)!}.
$$
Again, global convergence in the variable $w$ shows that this Laurent series
converges for every $z\neq0$, hence on the maximal annulus
$0<\abs{z}<\infty$.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} give both requested Laurent expansions and their maximal
annuli of convergence.

:::

:::

:::
