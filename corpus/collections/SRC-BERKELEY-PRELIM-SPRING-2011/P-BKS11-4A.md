---
schema: qual/card@1
id: P-BKS11-4A
kind: problem
title: Linear functionals on $M_n(k)$ with $f(AB)=f(BA)$ are multiples of the trace
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-25
  note: Compared the authored statement with page 2 of the retained Spring 2011 solution PDF and independently reviewed the commutator argument.
- event: solution-written
  by: chatgpt
  date: 2026-09-25
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-25
  note: Independently checked the matrix-unit commutators, equality of diagonal values, and the converse cyclicity of trace over an arbitrary field.
---

::: {.problem}
Let $M _ { n } ( k )$ be the n by n matrices over a field k. Find (with proof) all linear maps f from $M _ { n } ( k )$ to k such that $f ( A B ) = f ( B A )$ for all matrices A and B.
:::

::: {.solution}
For $1\leq i,j\leq n$, let $E_{ij}$ denote the standard matrix unit.

::: pf

::: {.pf-step #f-vanishes-on-commutators}
Every admissible linear map $f$ vanishes on every commutator:
$$
f([A,B])=0
$$
for all $A,B\in M_n(k)$.

::: pf-proof
By linearity and the hypothesis,
$$
f([A,B])
=
f(AB-BA)
=
f(AB)-f(BA)
=
0.
$$
:::

:::

::: {.pf-step #f-off-diagonal-zero}
If $i\neq j$, then
$$
f(E_{ij})=0.
$$

::: pf-proof
For $i\neq j$,
$$
[E_{ii},E_{ij}]
=
E_{ii}E_{ij}-E_{ij}E_{ii}
=
E_{ij}-0
=
E_{ij}.
$$
Apply step [](#f-vanishes-on-commutators){.pf-ref}.
:::

:::

::: {.pf-step #f-diagonal-equal}
If $i\neq j$, then
$$
f(E_{ii})=f(E_{jj}).
$$

::: pf-proof
One has
$$
[E_{ij},E_{ji}]
=
E_{ii}-E_{jj}.
$$
Step [](#f-vanishes-on-commutators){.pf-ref} therefore gives
$$
0
=
f(E_{ii}-E_{jj})
=
f(E_{ii})-f(E_{jj}).
$$
:::

:::

::: {.pf-step #f-necessity}
There is a scalar $c\in k$ such that
$$
f(A)=c\operatorname{tr}(A)
$$
for every $A\in M_n(k)$.

::: pf-proof
If $n=1$, every linear map $M_1(k)=k\to k$ is multiplication by a scalar,
so the conclusion is immediate.

Assume $n\geq2$ and set
$$
c\coloneqq f(E_{11}).
$$
By step [](#f-diagonal-equal){.pf-ref},
$$
f(E_{ii})=c
$$
for every $i$, and step [](#f-off-diagonal-zero){.pf-ref} gives
$$
f(E_{ij})=0
$$
when $i\neq j$. Thus for
$$
A=(a_{ij}),
$$
linearity gives
$$
f(A)
=
\sum_{i,j}a_{ij}f(E_{ij})
=
c\sum_i a_{ii}
=
c\operatorname{tr}(A).
$$
:::

:::

::: {.pf-step #f-sufficiency}
Conversely, every scalar multiple of the trace satisfies the required
identity.

::: pf-proof
For arbitrary matrices $A=(a_{ij})$ and $B=(b_{ij})$,
$$
\begin{aligned}
\operatorname{tr}(AB)
&=
\sum_i\sum_j a_{ij}b_{ji}\\
&=
\sum_j\sum_i b_{ji}a_{ij}\\
&=
\operatorname{tr}(BA),
\end{aligned}
$$
using commutativity of the field $k$. Multiplication by any scalar
$c\in k$ preserves the equality.
:::

:::

::: {.pf-step #complete-family}
The complete family is
$$
\boxed{
f=c\operatorname{tr},
\qquad
c\in k
}.
$$

::: pf-proof
Step [](#f-necessity){.pf-ref} proves necessity, and step [](#f-sufficiency){.pf-ref} proves sufficiency.
:::

:::

::: pf-qed
Step [](#complete-family){.pf-ref} is the required classification.
:::

:::

:::
