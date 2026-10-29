---
schema: qual/card@1
id: P-IPPKZ
kind: problem
title: Spring 2021
classification:
  areas:
  - algebra
  topics:
  - Polynomials
  - Rings
  - Integral Domains
relations: []
review: draft
---

::: {.problem}
Suppose that $f(x) \in (\ZZ/n\ZZ)[x]$ is a zero divisor.
Show that there is a nonzero $a\in \ZZ/n\ZZ$ with $af(x) = 0$.
:::

::: {.solution}

Write $R=\ZZ/n\ZZ$. Choose a nonzero polynomial $g=\sum_{j=0}^m b_jx^j\in R[x]$ of least degree among all nonzero polynomials satisfying $fg=0$, with $b_m\neq0$, and write $f=\sum_{i=0}^d a_ix^i$.

::: pf

::: {.pf-step #s1-1}

For every $0\leq i\leq d$, multiplication by $a_i$ annihilates $g$.


::: pf-proof

Proceed by descending induction on $i$. The coefficient of $x^{d+m}$ in $fg=0$ gives $a_db_m=0$. Thus $a_dg$ has degree less than $m$ if it is nonzero. But $f(a_dg)=a_d(fg)=0$, so minimality of $m$ forces $a_dg=0$.

Suppose $a_jg=0$ for all $j>i$. The coefficient of $x^{i+m}$ in $fg$ is
$$
a_ib_m+\sum_{j=i+1}^d a_jb_{i+m-j}=0,
$$
with terms involving out-of-range indices interpreted as zero. Every summand in the sum vanishes by the induction hypothesis, so $a_ib_m=0$. Again $a_ig$ is annihilated by $f$ and has degree less than $m$ if nonzero. Minimality implies $a_ig=0$, completing the induction.

:::

:::

::: {.pf-step #s1-2}

The nonzero scalar $b_m\in R$ annihilates $f$:
$$
\boxed{b_m f(x)=0}.
$$


::: pf-proof

Step [](#s1-1){.pf-ref} gives $a_ig=0$ for every $i$, so its leading coefficient is $a_ib_m=0$. Since $R$ is commutative,
$$
b_mf=\sum_{i=0}^d b_ma_ix^i=0.
$$
The choice of $g$ guarantees $b_m\neq0$.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} supplies the required nonzero scalar annihilator.

:::

:::

:::
