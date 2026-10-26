---
schema: qual/card@1
id: P-WESCA10-II3
kind: problem
title: 'Possible contour integrals of $1/(1+z^2)$'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problems, problem 3 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md.
---

::: {.problem}
Find all possible values of
\[
\int_\gamma\frac{dz}{1+z^2},
\]
where $\gamma$ is any closed piecewise smooth path in $\mathbb C$ avoiding $\pm i$.
:::

::: pf

::: pf-step

The residues of $1/(1+z^2)$ at its two poles are
\[
\operatorname{Res}\left(i,\frac1{1+z^2}\right)=\frac1{2i},
\qquad
\operatorname{Res}\left(-i,\frac1{1+z^2}\right)=-\frac1{2i}.
\]


::: pf-proof

Since
\[
1+z^2=(z-i)(z+i),
\]
both poles are simple. Hence
\[
\operatorname{Res}\left(i,\frac1{1+z^2}\right)
=\frac1{i+i}=\frac1{2i},
\]
and
\[
\operatorname{Res}\left(-i,\frac1{1+z^2}\right)
=\frac1{-i-i}=-\frac1{2i}.
\]

:::

:::

::: pf-step

For every admissible path $\gamma$,
\[
\int_\gamma\frac{dz}{1+z^2}
=\pi\bigl(n(\gamma,i)-n(\gamma,-i)\bigr).
\]


::: pf-proof

The residue theorem and step <1>1 give
\[
\int_\gamma\frac{dz}{1+z^2}
=2\pi i\left(
n(\gamma,i)\frac1{2i}
-n(\gamma,-i)\frac1{2i}
\right),
\]
which simplifies to the stated formula.

:::

:::

::: pf-step

The set of all possible values is
\[
\boxed{\pi\mathbb Z}.
\]


::: pf-proof

By step <1>2, every value is an integer multiple of $\pi$, because winding
numbers are integers. Conversely, let $m\in\mathbb Z$. Choose a sufficiently
small positively oriented circle about $i$ that does not enclose $-i$, and
traverse it $|m|$ times, reversing its orientation when $m<0$; for $m=0$ take
any contractible closed path avoiding $\pm i$. The resulting path has
\[
n(\gamma,i)=m,
\qquad
n(\gamma,-i)=0.
\]
Step <1>2 then gives the value $m\pi$.

:::

:::

::: pf-qed

Step <1>3 identifies exactly all possible values.

:::

:::
