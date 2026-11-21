---
schema: qual/card@1
id: P-K6CAP
kind: problem
title: $\lim_{n\to\infty}\int_{\RR}f(x)g(x+n)\,dx=0$ for $f,g\in L^2(\RR)$
classification:
  areas:
  - real-analysis
  topics:
  - L²
  - Small Tails
  - Convergence of Integrals
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 6 of the official UGA August 2016 real-analysis qualifying exam; replaced the legacy tail estimate by a rigorous compact-support approximation argument.
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Restructured into a structured proof under #2. Re-checked: compactly supported functions are
    dense in $L^2$, by dominated convergence applied to the truncations; Cauchy--Schwarz with
    translation invariance bounds the $(g-h)$ term by $\varepsilon/2$ uniformly in $n$; for
    compactly supported $h$ the integral runs over $[-n-R,-n+R]$, whose $L^2$ mass is a tail and
    tends to $0$; and the two pieces give the limit. Added: the density statement with its
    justification, the translation invariance of $\norm{(g-h)(\cdot+n)}_2$, and the explicit
    description of the intervals as tails, all of which the earlier solution invoked in one clause.
    The statement is Problem 6 of the UGA August 2016 real-analysis qualifying examination; the
    collection's provenance is that paper, so no retained solution set covers it and the argument is
    the card's own. One presentation repair: the opening definition wrote `:=`, which STYLE-04
    spells `\coloneqq`, and the step no longer needs the abbreviation.
- event: source-checked
  by: claude
  date: 2026-11-19
  note: >-
    Read in the retained examination `assets/attachments/Real_Analysis_Fall_2016.docx`, converted with
    Pandoc: the item is the sixth and last problem, and its printed words are the card's. The document
    numbers its problems automatically and that numbering does not survive the conversion, so the
    position and the opening words are the locator rather than a number. Both are now named in the
    solution's opening sentence. Not checked: the argument, which the edit does not touch.
---

::: {.problem}
Let $f, g \in L^2(\RR)$. Show that
$$
\lim _{n \to \infty} \int _{\RR} f(x) g(x+n) \,dx = 0
$$
:::

::: {.concept}
\envlist
- Cauchy Schwarz: $\norm{fg}_1 \leq \norm{f}_1 \norm{g}_1$.
- Small tails in $L^p$.
:::

::: {.solution}
This is the last of the six problems of the Fall 2016 real analysis examination, retained in this repository as `assets/attachments/Real_Analysis_Fall_2016.docx`; the conversion loses the document's automatic numbering, so the position and the opening words locate it.
The collection's provenance is the examination paper, so no retained solution set covers the problem and the argument is the card's own: approximate $g$ by a compactly supported $L^2$ function, and use that $f$ has small $L^2$ tails.

::: pf

::: {.pf-step #approximation}
For $\varepsilon>0$ there is $h\in L^2(\RR)$ vanishing a.e. outside some $[-R,R]$ with $\norm{g-h}_2<\varepsilon/(2(1+\norm{f}_2))$.

::: pf-proof
Compact support is dense in $L^2(\RR)$: the truncations $g\mathbf{1}_{[-R,R]}$ converge to $g$ in $L^2$ by dominated convergence with dominating function $\abs{g}^2$. Choose $h$ among them within the stated distance.
:::

:::

::: {.pf-step #smooth-part}
$\abs{\int_\RR f(x)(g-h)(x+n)\,dx}<\varepsilon/2$ for every $n$.

::: pf-proof
Cauchy--Schwarz gives $\abs{\int f(x)(g-h)(x+n)\,dx}\le\norm{f}_2\norm{(g-h)(\cdot+n)}_2$, and $\norm{(g-h)(\cdot+n)}_2=\norm{g-h}_2$ because Lebesgue measure is translation invariant; by step [](#approximation){.pf-ref} the product is less than $\varepsilon/2$.
:::

:::

::: {.pf-step #compact-part}
With $h$ supported in $[-R,R]$, the integral $\int_\RR f(x)h(x+n)\,dx$ equals $\int_{-n-R}^{-n+R}f(x)h(x+n)\,dx$ and is bounded by $\norm{h}_2\bigl(\int_{-n-R}^{-n+R}\abs{f}^2\bigr)^{1/2}$, which tends to $0$ as $n\to\infty$.

::: pf-proof
$h(x+n)$ vanishes unless $x+n\in[-R,R]$, that is unless $x\in[-n-R,-n+R]$, which gives the identity. Cauchy--Schwarz on that interval gives the bound, $\abs{h(x+n)}$ having $L^2$ norm $\norm{h}_2$ by translation invariance. The sets $[-n-R,-n+R]$ shrink to the empty set as $n\to\infty$ in the sense that they lie in $\RR\setminus[-M,M]$ for $n>M+R$, so the integrals are tails of the integrable function $\abs{f}^2$ and tend to $0$.
:::

:::

::: {.pf-step}
$\boxed{\lim_{n\to\infty}\int_\RR f(x)g(x+n)\,dx=0}$.

::: pf-proof
Write $\int f(x)g(x+n)\,dx=\int f(x)(g-h)(x+n)\,dx+\int f(x)h(x+n)\,dx$. The first term is below $\varepsilon/2$ in modulus for every $n$ by step [](#smooth-part){.pf-ref}, and the second is below $\varepsilon/2$ for all large $n$ by step [](#compact-part){.pf-ref}. So the integral is below $\varepsilon$ in modulus eventually, and $\varepsilon>0$ was arbitrary.
:::

:::

:::
:::
