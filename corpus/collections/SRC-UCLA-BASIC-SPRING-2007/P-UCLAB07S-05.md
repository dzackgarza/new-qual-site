---
schema: qual/card@1
id: P-UCLAB07S-05
kind: problem
title: An eigenvector of a normal operator is an eigenvector of its adjoint
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
  note: Checked against Problem 5 of the retained UCLA Basic Examination, Spring 2007.
---

::: {.problem}
Let $T$ be a normal linear operator on a finite-dimensional complex inner-product space $V$.
Prove that if $v$ is an eigenvector of $T$, then $v$ is also an eigenvector of $T^*$.
:::

::: {.solution}

Suppose
$$
Tv=\lambda v
$$
with
$$
v\ne0.
$$

::: pf

::: {.pf-step #s1-1}

The operator
$$
S=T-\lambda I
$$
is normal.


::: pf-proof

Since $T$ is normal,
$$
T^*T=TT^*.
$$
Now
$$
S^*=T^*-\overline{\lambda}I.
$$
Hence
$$
\begin{aligned}
S^*S
&=
(T^*-\overline{\lambda}I)(T-\lambda I)\\
&=
T^*T-\lambda T^*-\overline{\lambda}T+\abs{\lambda}^2I,
\end{aligned}
$$
while
$$
\begin{aligned}
SS^*
&=
(T-\lambda I)(T^*-\overline{\lambda}I)\\
&=
TT^*-\overline{\lambda}T-\lambda T^*+\abs{\lambda}^2I.
\end{aligned}
$$
These are equal because
$$
T^*T=TT^*.
$$
Thus $S$ is normal.

:::

:::

::: {.pf-step #s1-2}

For every normal operator $N$ on a finite-dimensional complex inner-product space,
$$
\norm{Nx}=\norm{N^*x}
$$
for all $x$.


::: pf-proof

Normality gives
$$
N^*N=NN^*.
$$
Therefore
$$
\begin{aligned}
\norm{Nx}^2
&=
\langle Nx,Nx\rangle\\
&=
\langle N^*Nx,x\rangle\\
&=
\langle NN^*x,x\rangle\\
&=
\langle N^*x,N^*x\rangle\\
&=
\norm{N^*x}^2.
\end{aligned}
$$
Taking nonnegative square roots gives the claim.

:::

:::

::: {.pf-step #s1-3}

One has
$$
Sv=0.
$$


::: pf-proof

By definition,
$$
Sv
=(T-\lambda I)v
=Tv-\lambda v
=0.
$$

:::

:::

::: {.pf-step #s1-4}

One has
$$
S^*v=0.
$$


::: pf-proof

By step [](#s1-1){.pf-ref}, $S$ is normal.
Therefore step [](#s1-2){.pf-ref} gives
$$
\norm{S^*v}
=
\norm{Sv}.
$$
By step [](#s1-3){.pf-ref},
$$
\norm{Sv}=0.
$$
Hence
$$
\norm{S^*v}=0,
$$
so
$$
S^*v=0.
$$

:::

:::

::: {.pf-step #s1-5}

Therefore
$$
\boxed{T^*v=\overline{\lambda}v}.
$$


::: pf-proof

Since
$$
S^*=T^*-\overline{\lambda}I,
$$
step [](#s1-4){.pf-ref} says
$$
(T^*-\overline{\lambda}I)v=0.
$$
Thus
$$
T^*v=\overline{\lambda}v.
$$

:::

:::

::: {.pf-step #s1-6}

Hence $v$ is an eigenvector of $T^*$.


::: pf-proof

The vector $v$ is nonzero by hypothesis, and step [](#s1-5){.pf-ref} shows that it is taken to a scalar multiple of itself by $T^*$.
Therefore $v$ is an eigenvector of $T^*$, with eigenvalue $\overline{\lambda}$.

:::

:::

::: pf-qed

Step [](#s1-6){.pf-ref} is the required conclusion.

:::

:::

:::
