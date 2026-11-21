---
schema: qual/card@1
id: P-CAF06F
kind: problem
title: "Uniform convergence of Taylor series on compact subsets of the unit disk"
classification:
  areas:
  - complex-analysis
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-18
  note: >-
    Rewritten as a Lamport structured proof of the argument already on the card, correct as it
    stood. Added: the existence of r and rho with the inclusion of the Cauchy circle in the disk
    of radius 2, which the prose asserted; the finiteness of M; and the derivation of the
    closed form f(z+1) - f(z) from the convergence of the Taylor series about z on a disk of
    radius rho > 1, where the prose stated it as an aside. Not claimed: a retained solution
    set; the provenance names the examination paper.
---

::: {.problem}
Let $f(z)$ be a holomorphic function in the disk $\abs{z} < 2$.
Show that $\sum_{n=1}^{\infty} \frac{f^{(n)}(z)}{n!}$ converges uniformly in any compact subset of the unit disk $\abs{z} < 1$.
:::

::: {.solution}
No retained solution set covers this problem: the collection's `provenance` names `assets/attachments/FA06_220_Complex_Analysis_Qual.pdf`, the examination paper, which carries no solutions. The argument below is the card's own and follows the card's previous prose.

Throughout $f$ is holomorphic on $\abs z<2$.

::: pf

::: {.pf-step #setup}
For a compact $K\subset\DD$ there are $r<1$ and $\rho>1$ with $K\subseteq\theset{\abs z\le r}$ and $\abs{\zeta-z}=\rho$ contained in $\abs\zeta<2$ for every $z\in K$.

::: pf-proof
$\abs\cdot$ is continuous and $K$ is compact, so $r'\coloneqq\max_{z\in K}\abs z<1$ because $K$ lies in the open unit disk; take $r$ with $r'<r<1$. Then $2-r>1$, so there is $\rho$ with $1<\rho<2-r$. For $z\in K$ and $\abs{\zeta-z}=\rho$ one has $\abs\zeta\le\abs z+\rho\le r+\rho<2$, and $r+\rho$ is still less than $2$ by the choice of $\rho$.

:::

:::

::: {.pf-step #estimates}
With $M=\max_{\abs\zeta\le r+\rho}\abs{f(\zeta)}$, one has $\abs{f^{(n)}(z)}/n!\le M/\rho^n$ for all $z\in K$ and $n\ge0$.

::: pf-proof
For fixed $z\in K$ the closed disk $\overline{B(z,\rho)}$ lies in $\theset{\abs\zeta\le r+\rho}\subset\theset{\abs\zeta<2}$, where $f$ is holomorphic and bounded by $M$. Cauchy's estimates for the derivatives on a disk of radius $\rho$ give $\abs{f^{(n)}(z)}\le n!M\rho^{-n}$; dividing by $n!$ gives the claim. Note $M<\infty$ since $\abs\zeta\le r+\rho$ is compact and $f$ continuous there.

:::

:::

::: {.pf-step #uniform}
$\sum_n f^{(n)}(z)/n!$ converges uniformly on $K$.

::: pf-proof
By step [](#estimates){.pf-ref}, $\abs{f^{(n)}(z)/n!}\le M\rho^{-n}$ for all $z\in K$, and $\sum_nM\rho^{-n}=M/(\rho-1)<\infty$ because $\rho>1$. The Weierstrass $M$-test then gives uniform convergence on $K$.

:::

:::

::: {.pf-step #conclusion}
The series converges uniformly on every compact subset of $\DD$, and its sum is $f(z+1)-f(z)$.

::: pf-proof
Given a compact $K\subset\DD$, step [](#uniform){.pf-ref} gives uniform convergence there, and $K$ was arbitrary. For the sum: fix $z\in K$; the Taylor series of $f$ about $z$ converges on the disk $\abs{w-z}<\rho$ with $\rho>1$, so at $w=z+1$ it gives $f(z+1)=\sum_{n\ge0}f^{(n)}(z)/n!$, and the term $n=0$ is $f(z)$. Hence $\sum_{n\ge1}f^{(n)}(z)/n!=f(z+1)-f(z)$.

:::

:::

:::
:::
