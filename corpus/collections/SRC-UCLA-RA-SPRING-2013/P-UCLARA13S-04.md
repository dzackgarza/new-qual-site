---
schema: qual/card@1
id: P-UCLARA13S-04
kind: problem
title: Existence of an equilibrium measure for Newtonian energy
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Transcribed from the UCLA Analysis Qualifying Exam Solutions compendium, Spring 2013 section.
---

::: {.problem}
Let $K\subset\RR^3$ be nonempty and compact.
For every Borel probability measure $\mu$ on $K$, define
$$
I(\mu)=\int_K\int_K \frac{1}{\norm{x-y}}\,d\mu(x)\,d\mu(y)\in(0,\infty],
$$
and let
$$
R_K=\inf\{I(\mu):\mu\text{ is a Borel probability measure on }K\}.
$$
Show that there exists a Borel probability measure $\mu$ on $K$ such that $I(\mu)=R_K$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

If
$$
R_K=\infty,
$$
then every Borel probability measure on $K$ minimizes the energy.


::: pf-proof

By definition,
$$
R_K
=
\inf\{I(\mu):\mu\text{ is a Borel probability measure on }K\}.
$$
If this infimum is $\infty$, then no probability measure can have finite energy. Hence
$$
I(\mu)=\infty=R_K
$$
for every probability measure $\mu$ on $K$. Such measures exist because $K$ is nonempty; for example, any Dirac mass $\delta_x$ with $x\in K$ is a probability measure.

:::

:::

::: {.pf-step #s1-2}

Assume henceforth that
$$
R_K<\infty.
$$
There is a sequence of Borel probability measures $(\mu_n)$ on $K$ such that
$$
I(\mu_n)\longrightarrow R_K.
$$


::: pf-proof

This is the definition of the infimum. For each $n$, choose $\mu_n$ with
$$
I(\mu_n)<R_K+\frac1n.
$$
Since always $I(\mu_n)\ge R_K$, the energies converge to $R_K$.

:::

:::

::: {.pf-step #s1-3}

After passing to a subsequence, there is a bounded linear functional
$$
L\in C(K)^*
$$
such that
$$
\int_K\varphi\,d\mu_n
\longrightarrow
L(\varphi)
\qquad
(\varphi\in C(K)).
$$


::: pf-proof

Each probability measure $\mu_n$ defines a positive functional on $C(K)$ of norm
$$
\norm{\mu_n}
=
\mu_n(K)
=1.
$$
Thus $(\mu_n)$ lies in the closed unit ball of $C(K)^*$.

By Banach--Alaoglu, this unit ball is weak-* compact. Since $K$ is compact metric, $C(K)$ is separable, so the weak-* topology on the dual unit ball is metrizable and hence sequentially compact. Therefore a subsequence converges weak-* to some $L\in C(K)^*$.

:::

:::

::: {.pf-step #s1-4}

The functional $L$ is integration against a Borel probability measure $\mu$ on $K$.


::: pf-proof

If $\varphi\in C(K)$ and $\varphi\ge0$, then
$$
L(\varphi)
=
\lim_{n\to\infty}
\int_K\varphi\,d\mu_n
\ge0.
$$
Thus $L$ is positive. Also,
$$
L(1)
=
\lim_{n\to\infty}\mu_n(K)
=1.
$$
By the Riesz representation theorem for positive linear functionals on $C(K)$, there is a unique finite positive Borel measure $\mu$ on $K$ such that
$$
L(\varphi)
=
\int_K\varphi\,d\mu
\qquad
(\varphi\in C(K)).
$$
The identity $L(1)=1$ gives
$$
\mu(K)=1,
$$
so $\mu$ is a probability measure.

:::

:::

::: {.pf-step #s1-5}

One has
$$
\mu_n\otimes\mu_n
\overset{*}{\rightharpoonup}
\mu\otimes\mu
$$
as Borel probability measures on $K\times K$.


::: pf-proof

For functions of the form
$$
\Phi(x,y)=g(x)h(y),
\qquad
g,h\in C(K),
$$
weak-* convergence gives
$$
\begin{aligned}
\int_{K\times K}\Phi\,d(\mu_n\otimes\mu_n)
&=
\left(\int_Kg\,d\mu_n\right)
\left(\int_Kh\,d\mu_n\right)\\
&\longrightarrow
\left(\int_Kg\,d\mu\right)
\left(\int_Kh\,d\mu\right)\\
&=
\int_{K\times K}\Phi\,d(\mu\otimes\mu).
\end{aligned}
$$

Finite linear combinations of product functions form a subalgebra of $C(K\times K)$ that contains the constants and separates points. By the Stone--Weierstrass theorem, this subalgebra is uniformly dense in $C(K\times K)$.

All the product measures involved have total mass $1$. Therefore uniform approximation transfers the convergence from that dense subalgebra to every
$$
\Phi\in C(K\times K).
$$
This is exactly weak-* convergence of the product measures.

:::

:::

::: {.pf-step #s1-6}

For $M>0$, define
$$
k_M(x,y)
\coloneqq
\min\left\{
M,\frac1{\norm{x-y}}
\right\},
$$
with
$$
k_M(x,x)=M.
$$
Then $k_M\in C(K\times K)$ and
$$
k_M(x,y)\uparrow \frac1{\norm{x-y}}
$$
in the extended-real sense as $M\to\infty$.


::: pf-proof

Away from the diagonal $x=y$, continuity is immediate. If $(x_j,y_j)\to(x,x)$, then
$$
\norm{x_j-y_j}\to0,
$$
so
$$
\frac1{\norm{x_j-y_j}}\to\infty
$$
whenever $x_j\ne y_j$. Hence for all sufficiently large $j$,
$$
k_M(x_j,y_j)=M=k_M(x,x),
$$
which proves continuity at the diagonal.

For fixed $(x,y)$ with $x\ne y$, the sequence $k_M(x,y)$ increases to $\norm{x-y}^{-1}$. On the diagonal it increases to $\infty$, which is the prescribed extended value of the Newtonian kernel.

:::

:::

::: {.pf-step #s1-7}

For every $M>0$,
$$
\int_{K\times K}k_M\,d(\mu\otimes\mu)
\le
R_K.
$$


::: pf-proof

By steps [](#s1-5){.pf-ref} and [](#s1-6){.pf-ref},
$$
\int k_M\,d(\mu\otimes\mu)
=
\lim_{n\to\infty}
\int k_M\,d(\mu_n\otimes\mu_n).
$$
Since
$$
k_M(x,y)
\le
\frac1{\norm{x-y}}
$$
in the extended-real sense,
$$
\int k_M\,d(\mu_n\otimes\mu_n)
\le
I(\mu_n).
$$
Taking the limit and using step [](#s1-2){.pf-ref} gives
$$
\int k_M\,d(\mu\otimes\mu)
\le
R_K.
$$

:::

:::

::: {.pf-step #s1-8}

The weak-* limit measure satisfies
$$
I(\mu)\le R_K.
$$


::: pf-proof

By step [](#s1-6){.pf-ref}, the kernels $k_M$ increase pointwise to the Newtonian kernel. The monotone convergence theorem therefore gives
$$
I(\mu)
=
\lim_{M\to\infty}
\int_{K\times K}k_M\,d(\mu\otimes\mu).
$$
Every term on the right is at most $R_K$ by step [](#s1-7){.pf-ref}, so the limit is at most $R_K$.

:::

:::

::: {.pf-step #s1-9}

One has
$$
\boxed{I(\mu)=R_K}.
$$


::: pf-proof

Since $\mu$ is a Borel probability measure on $K$ by step [](#s1-4){.pf-ref}, the definition of $R_K$ gives
$$
R_K\le I(\mu).
$$
Step [](#s1-8){.pf-ref} gives the reverse inequality. Hence equality holds.

:::

:::

::: pf-qed

Step [](#s1-1){.pf-ref} handles the case $R_K=\infty$, while steps [](#s1-2){.pf-ref} through [](#s1-9){.pf-ref} produce a minimizing probability measure when $R_K<\infty$.

:::

:::

:::
