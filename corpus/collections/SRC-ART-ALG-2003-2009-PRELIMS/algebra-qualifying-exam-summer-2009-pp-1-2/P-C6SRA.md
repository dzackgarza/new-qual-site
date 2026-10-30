---
schema: qual/card@1
id: P-C6SRA
kind: problem
title: Examples of vanishing tensors over $\ZZ$ and $\QQ$, torsion-free
  nonfree modules, maximal nonprime ideals, non-Noetherian rings, and non-ideal centers
classification:
  areas:
  - algebra
  topics:
  - Tensor Products
  - Modules
  - Counterexamples
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
- event: source-checked
  by: claude-opus-5.5
  date: 2026-10-31
  note: 'Part (d) answer corrected: in a ring with 1 every maximal two-sided ideal is prime, so no example exists; the previous answer M_2(Q) used the integral-domain criterion, under which the simple ring M_2(Q) has 0 maximal and prime.'
---
::: {.problem}
For each of the following, either give an example or indicate that none exists.
You do not need to supply proofs.
(a) Two non-zero $\ZZ$-modules $A$ and $B$ such that $A\otimes_{\ZZ} B=0$.
(b) Two non-zero $\QQ$-modules $V$ and $W$ such that $V\otimes_{\QQ} W=0$.
(c) A ring $R$ and a module $M$ over $R$ which is torsion free but is not free.
(d) A ring $R$ and an ideal $I$ of $R$ that is maximal but not prime.
(e) A ring which is not Noetherian.
(f) A ring whose center is not an ideal.
:::

::: {.solution}

::: pf

::: {.pf-step #s1}

For part (a), take
$$
A=\ZZ/2\ZZ,
\qquad
B=\ZZ/3\ZZ.
$$
Then $A\otimes_{\ZZ}B=0$.

::: pf-proof

Using $(\ZZ/m)\otimes_{\ZZ}B\cong B/mB$,
$$
(\ZZ/2)\otimes_{\ZZ}(\ZZ/3)
\cong (\ZZ/3)/2(\ZZ/3)=0,
$$
because multiplication by $2$ is an automorphism of $\ZZ/3$.

:::

:::

::: {.pf-step #s2}

For part (b), no such nonzero $\QQ$-modules exist.

::: pf-proof

A $\QQ$-module is a vector space. If $0\ne v\in V$ and $0\ne w\in W$, choose linear functionals $\lambda:V\to\QQ$ and $\mu:W\to\QQ$ with $\lambda(v)=\mu(w)=1$. The induced map
$$
\lambda\otimes\mu:V\otimes_{\QQ}W\to\QQ
$$
sends $v\otimes w$ to $1$, so $V\otimes_{\QQ}W\ne0$.

:::

:::

::: {.pf-step #s3}

For part (c), take $R=\ZZ$ and $M=\QQ$.

::: pf-proof

The $\ZZ$-module $\QQ$ is torsion-free. It is not free: $\QQ$ is divisible, whereas a nonzero free abelian group is not divisible.

:::

:::

::: {.pf-step #s4}

For part (d), no such example exists: in a ring with $1$, every maximal two-sided ideal is prime.

::: pf-proof

Recall that a two-sided ideal $I\ne R$ is prime when $aRb\subseteq I$ implies $a\in I$ or $b\in I$; for commutative $R$ this is the usual condition $ab\in I\Rightarrow a\in I$ or $b\in I$.
Let $I$ be maximal, and suppose $aRb\subseteq I$ with $a,b\notin I$.
By maximality, $I+RaR=R$ and $I+RbR=R$. Then
$$
R=R\cdot R=(I+RaR)(I+RbR)\subseteq I+RaRbR\subseteq I,
$$
because $aRb\subseteq I$ and $I$ is a two-sided ideal. This contradicts $I\ne R$.

:::

:::

::: {.pf-step #s5}

For part (e), take
$$
R=k[x_1,x_2,x_3,\dots]
$$
for any field $k$.

::: pf-proof

The ascending chain
$$
(x_1)\subsetneq(x_1,x_2)\subsetneq(x_1,x_2,x_3)\subsetneq\cdots
$$
does not stabilize, so $R$ is not Noetherian.

:::

:::

::: {.pf-step #s6}

For part (f), again take $R=M_2(\QQ)$.

::: pf-proof

Its center is
$$
Z(R)=\{aI_2:a\in\QQ\}.
$$
This is a proper subset of $R$ but contains the identity matrix. Any two-sided ideal containing $1$ is all of $R$, so $Z(R)$ is not an ideal.

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref}, [](#s2){.pf-ref}, [](#s3){.pf-ref}, [](#s4){.pf-ref}, [](#s5){.pf-ref} and [](#s6){.pf-ref} answer parts (a)--(f), respectively.

:::

:::

:::
