---
schema: qual/card@1
id: P-CAFA21D
kind: problem
title: "Sequence of holomorphic self-maps of the disk converging to 1"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
---

::: {.problem}
Let $a_n \in \Delta$ be a sequence such that $a_n \to 1$.
Let $f_n : \Delta \to \Delta$ be a sequence of holomorphic functions such that $f_n(0) = a_n$.
Show that $f_n \to 1$ uniformly on compact subsets of $\Delta$.
:::

::: {.solution}
Fix $0<r<1$. By Schwarz--Pick,
$$
\abs{\frac{f_n(z)-a_n}{1-\overline{a_n}f_n(z)}}\le \abs{z}\le r
\qquad (\abs{z}\le r).
$$
Thus there is some $\zeta_n(z)$ with $\abs{\zeta_n(z)}\le r$ such that
$$
f_n(z)=\frac{a_n+\zeta_n(z)}{1+\overline{a_n}\zeta_n(z)}.
$$
Hence
$$
f_n(z)-1
=\frac{(a_n-1)+\zeta_n(z)(1-\overline{a_n})}
{1+\overline{a_n}\zeta_n(z)}.
$$
Since $\abs{1+\overline{a_n}\zeta_n(z)}\ge1-r$,
$$
\sup_{\abs{z}\le r}\abs{f_n(z)-1}
\le \frac{\abs{a_n-1}+r\abs{1-\overline{a_n}}}{1-r}
\longrightarrow0.
$$
Every compact subset of $\Delta$ is contained in some $\abs{z}\le r<1$, so
$f_n\to1$ locally uniformly.
:::
