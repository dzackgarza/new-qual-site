---
schema: qual/card@1
id: P-SBKCW
kind: problem
title: Derivatives of a normal family form a normal family
classification:
  areas:
  - complex-analysis
  topics:
  - Normal Families
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Read September 2019 Complex Analysis 3 in the retained extraction."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the finite holomorphic-limit normality convention on arbitrary domains and the uniform derivative estimate on each compact set."
---

::: {.problem}
(a) Define a normal family of holomorphic functions on an open,
possibly unbounded, domain $U$.

(b) If $\mathcal F$ is normal on the open unit disk $D$, prove
that $\mathcal F'=\{f':f\in\mathcal F\}$ is normal on $D$.
:::

::: {.solution}
::: pf

::: {.pf-step #s1}
Normality requires a locally uniformly convergent subsequence
with finite holomorphic limit from every sequence in the family.

::: pf-proof
Precisely, a family $\mathcal F\subseteq\mathcal O(U)$
is normal if every sequence $(f_n)$ in it has a subsequence
$(f_{n_j})$ converging uniformly on every compact subset
of $U$ to a holomorphic function $f:U\to\CC$.
The limit need not belong to $\mathcal F$, and $U$ may be
unbounded [@SS03].
:::

:::

::: pf-step
The family of derivatives is normal.

::: pf-proof
Given a sequence $(g_n)$ in $\mathcal F'$, choose
$f_n\in\mathcal F$ with $g_n=f_n'$. Normality supplies
a subsequence $f_{n_j}\to f$ locally uniformly on $D$,
where $f$ is holomorphic. Let $K\subset D$ be a nonempty
compact set. Choose $\delta>0$ such that the compact set
$$
L=\{z+w:z\in K,\ \abs{w}\leq\delta\}
$$
is contained in $D$. For instance, take
$\delta=(1-\max_{z\in K}\abs{z})/2$.
For $z\in K$, the differentiated Cauchy formula gives
$$
g_{n_j}(z)-f'(z)=\frac{1}{2\pi i}
\int_{\abs{\zeta-z}=\delta}
\frac{f_{n_j}(\zeta)-f(\zeta)}{(\zeta-z)^2}\,d\zeta.
$$
Consequently
$$
\sup_{z\in K}\abs{g_{n_j}(z)-f'(z)}
\leq\delta^{-1}\sup_{\zeta\in L}\abs{f_{n_j}(\zeta)-f(\zeta)}
\longrightarrow0.
$$
Thus the same
subsequence converges locally uniformly to the holomorphic
function $f'$, exactly as required by step [](#s1){.pf-ref}.
:::

:::

:::
:::
