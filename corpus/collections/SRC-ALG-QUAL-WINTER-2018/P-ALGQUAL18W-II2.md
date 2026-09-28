---
schema: qual/card@1
id: P-ALGQUAL18W-II2
kind: problem
title: Vanishing trace on an induced representation
classification: {areas: [algebra], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Part II, Problem 2 in the deterministic MinerU Flash extraction assets/attachments/qual18wintersol_extracted.md.
- event: solution-written
  by: chatgpt
  date: 2026-09-21
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-21
  note: >-
    Independently proved the trace vanishing from the coset-summand
    decomposition of the induced module, then compared the argument with the
    worked source solution. A fixed coset would give a conjugate of g in H;
    hence g has no diagonal block, so every diagonal matrix coefficient is
    zero over an arbitrary field.
---

::: {.problem}
Let $G$ be a finite group, $H\subseteq G$ a subgroup, and $g\in G$ an element such that no conjugate of $g$ lies in $H$.
Prove that for every finite-dimensional $H$-module $V$ over an arbitrary field, the trace of $g$ on $\operatorname{Ind}_H^G V$ is zero.
:::

::: {.solution}
Let $k$ be the ground field. Choose representatives
$$
x_1,\ldots,x_r
$$
for the left cosets in $G/H$, and choose a basis
$$
v_1,\ldots,v_m
$$
of $V$ over $k$.

<1>1. The vectors
$$
x_i\otimes v_j,
\qquad
1\leq i\leq r,
\quad
1\leq j\leq m,
$$
form a basis of
$$
\Ind_H^G V
=
k[G]\otimes_{k[H]}V.
$$

::: {.proof}
As a right $k[H]$-module,
$$
k[G]
=
\bigoplus_{i=1}^r x_i k[H].
$$
Tensoring this decomposition with $V$ over $k[H]$ gives
$$
k[G]\otimes_{k[H]}V
\cong
\bigoplus_{i=1}^r x_i\otimes V.
$$
The chosen basis of $V$ therefore gives the displayed basis of the induced
module.
:::

<1>2. For each $i$ there are unique
$$
\sigma(i)\in\{1,\ldots,r\}
\qquad\text{and}\qquad
h_i\in H
$$
such that
$$
g x_i=x_{\sigma(i)}h_i,
$$
and $\sigma$ is the permutation of $G/H$ induced by left multiplication by
$g$.

::: {.proof}
The element $g x_i$ lies in a unique left coset $x_{\sigma(i)}H$, so it has
a unique expression
$$
g x_i=x_{\sigma(i)}h_i
$$
with $h_i\in H$. Since left multiplication by $g$ is a bijection of $G/H$,
the resulting map $i\mapsto\sigma(i)$ is a permutation.
:::

<1>3. The permutation $\sigma$ has no fixed point.

::: {.proof}
If $\sigma(i)=i$, then step <1>2 gives
$$
g x_i=x_i h_i
$$
for some $h_i\in H$. Hence
$$
x_i^{-1}g x_i=h_i\in H,
$$
so a conjugate of $g$ lies in $H$, contrary to the hypothesis. Therefore
$$
\sigma(i)\neq i
$$
for every $i$.
:::

<1>4. The trace of $g$ on the induced module is
$$
\trace\!\left(g\mid\Ind_H^G V\right)=\boxed{0}.
$$

::: {.proof}
By step <1>2,
$$
g(x_i\otimes v_j)
=
g x_i\otimes v_j
=
x_{\sigma(i)}h_i\otimes v_j
=
x_{\sigma(i)}\otimes h_i v_j.
$$
Thus $g$ maps the entire summand
$$
x_i\otimes V
$$
into
$$
x_{\sigma(i)}\otimes V.
$$
By step <1>3 these are distinct summands. Consequently the coefficient of
$x_i\otimes v_j$ in $g(x_i\otimes v_j)$ is zero for every basis vector from
step <1>1. Every diagonal entry of the matrix of $g$ in that basis is
therefore zero, and so its trace is zero.
:::

<1>5. Q.E.D.

::: {.proof}
Step <1>4 is the required trace identity.
:::
:::
