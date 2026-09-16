---
schema: qual/card@1
id: P-JHQKZ
kind: problem
title: $(R/I)\otimes_R M\cong M/IM$
classification:
  areas:
  - algebra
  topics:
  - Modules
  - Ideals
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the two-sided ideal and left-module hypotheses with Summer 2014 problem 4 in the retained extraction; no commutativity is assumed."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Checked the bimodule structure, representative independence, balancing, left linearity, vanishing on IM, and both inverse identities; preserved the source hint separately."
---

::: {.problem}
Let $R$ be a ring with 1, and let $I$ be a two sided ideal of $R$.
Let $M$ be a left $R$-module.
Recall that $IM$ is the submodule $$IM = \{a_1 m_1 + \cdots + a_n m_n : a_i \in I, m_i \in M\}.$$ Prove that $(R/I) \otimes_R M \cong M/IM$ as $R$-modules.
:::

::: {.hint}
Construct an $R$-balanced map from $(R/I)\times M$ to $M/IM$
and use the universal mapping property of tensor products.
:::

::: {.solution}
The isomorphism and its inverse are
$$
\begin{aligned}
\Phi:(R/I)\otimes_R M&\longrightarrow M/IM,
& (a+I)\otimes m&\longmapsto am+IM,\\
\Psi:M/IM&\longrightarrow(R/I)\otimes_R M,
&m+IM&\longmapsto(1+I)\otimes m.
\end{aligned}
$$
We verify these maps without assuming that $R$ is commutative.

<1>1. The tensor product and quotient have the required left
$R$-module structures.

::: {.proof}
Because $I$ is two-sided, $R/I$ is an $(R,R)$-bimodule by
left and right multiplication. Put $T=(R/I)\otimes_R M$, using
the right $R$-action on $R/I$ and the given left action on $M$.
For $r\in R$, left multiplication on $R/I$ is a right-linear
map: $r(ab)=(ra)b$. It therefore induces an additive map on
$T$, with
$$
r\big((a+I)\otimes m\big)=(ra+I)\otimes m.
$$
The module identities follow on elementary tensors from the
ring identities, and elementary tensors generate $T$ additively.
Thus this defines a left $R$-module structure [@DF04].

The set $IM$ is an additive subgroup, since sums concatenate
the finite expressions and negatives can be absorbed in the
coefficients. For $r\in R$, each $ra_i$ lies in $I$, so
$r\sum_i a_im_i=\sum_i(ra_i)m_i\in IM$. Hence $IM$ is a
left submodule, and $M/IM$ is a left quotient module.
:::

<1>2. The displayed rule defines a left $R$-linear map $\Phi$.

::: {.proof}
Define $\beta:(R/I)\times M\to M/IM$ by
$\beta(a+I,m)=am+IM$. If $a$ is replaced by $a+i$ with
$i\in I$, the value changes by $im\in IM$, so it is
independent of the representative. It is additive in each
variable. For $r\in R$,
$$
\beta((a+I)r,m)=(ar)m+IM
=a(rm)+IM=\beta(a+I,rm).
$$
Thus $\beta$ is balanced, and the universal property of the
tensor product gives an additive map $\Phi:T\to M/IM$
with the asserted rule [@DF04]. It is left $R$-linear since
$$
\Phi\big(r((a+I)\otimes m)\big)
=(ra)m+IM=r(am+IM).
$$
:::

<1>3. The map $\Psi$ is well defined and left $R$-linear,
and is inverse to $\Phi$.

::: {.proof}
Define $\eta:M\to T$ by $\eta(m)=(1+I)\otimes m$.
It is additive, and balancing gives
$$
\eta(rm)=(1+I)\otimes rm=(r+I)\otimes m
=r\eta(m).
$$
For $i\in I$ and $m\in M$,
$\eta(im)=(i+I)\otimes m=0$. It follows by additivity that
$\eta$ vanishes on all of $IM$. It therefore descends to a
left-linear map $\Psi:M/IM\to T$ with the displayed formula.

For every $m+IM$, one has $\Phi\Psi(m+IM)=m+IM$.
For every elementary tensor, balancing gives
$$
\Psi\Phi((a+I)\otimes m)
=(1+I)\otimes am=(a+I)\otimes m.
$$
Since elementary tensors generate $T$, these identities prove
that both composites are the identity. Thus $\Phi$ is the
claimed left $R$-module isomorphism.
:::
:::
