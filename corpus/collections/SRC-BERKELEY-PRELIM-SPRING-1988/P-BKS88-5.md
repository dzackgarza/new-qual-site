---
schema: qual/card@1
id: P-BKS88-5
kind: problem
title: Groups of order $2n$ with an inverting subgroup of index 2
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UC Berkeley Spring 1988 preliminary examination.
---

::: {.problem}
Let $D$ be a group of order $2n$, where $n$ is odd, with a subgroup $H$ of order $n$ satisfying $xhx^{-1}=h^{-1}$ for all $h$ in $H$ and all $x$ in $D\setminus H$. Prove that $H$ is commutative and that every element of $D\setminus H$ is of order $2$.
:::

::: {.solution}
::: pf

::: {.pf-step #normal-index-two}
$H$ is a normal subgroup of $D$ of index $2$.

::: pf-proof
Since $|D|=2n$ and $|H|=n$, the index $[D:H]$ is $2$. Every subgroup of index $2$ is normal, so $H\triangleleft D$.
:::

:::

::: pf-step
$H$ is commutative.

::: pf-proof
Choose $x\in D\setminus H$. For arbitrary $h_1,h_2\in H$, the hypothesis applied to $h_1$, $h_2$, and $h_1h_2$ gives
$$
x h_1x^{-1}=h_1^{-1},
\qquad
x h_2x^{-1}=h_2^{-1},
\qquad
x(h_1h_2)x^{-1}=(h_1h_2)^{-1}.
$$
On the other hand,
$$
x(h_1h_2)x^{-1}
=(xh_1x^{-1})(xh_2x^{-1})
=h_1^{-1}h_2^{-1}.
$$
Hence
$$
h_1^{-1}h_2^{-1}
=(h_1h_2)^{-1}
=h_2^{-1}h_1^{-1}.
$$
Taking inverses yields $h_1h_2=h_2h_1$. Thus $H$ is commutative.
:::

:::

::: pf-step
Every $x\in D\setminus H$ satisfies $x^2=e$.

::: pf-proof
By [](#normal-index-two){.pf-ref}, the quotient $D/H$ has order $2$. Thus the nontrivial coset $xH$ has square $H$, so $x^2\in H$. Applying the hypothesis to $h=x^2$ gives
$$
x x^2 x^{-1}=(x^2)^{-1}.
$$
The left-hand side is $x^2$, hence $(x^2)^2=e$. Therefore the order of $x^2$ divides $2$. But $x^2\in H$ and $|H|=n$ is odd, so Lagrange's theorem forces $x^2=e$.
:::

:::

:::

:::
