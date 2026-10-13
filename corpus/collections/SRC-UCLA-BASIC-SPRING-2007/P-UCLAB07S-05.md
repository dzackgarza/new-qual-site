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
\[
Tv=\lambda v
\]
with
\[
v\ne0.
\]

<1>1. The operator
\[
S=T-\lambda I
\]
is normal.

::: {.proof}
Since $T$ is normal,
\[
T^*T=TT^*.
\]
Now
\[
S^*=T^*-\overline{\lambda}I.
\]
Hence
\[
\begin{aligned}
S^*S
&=
(T^*-\overline{\lambda}I)(T-\lambda I)\\
&=
T^*T-\lambda T^*-\overline{\lambda}T+|\lambda|^2I,
\end{aligned}
\]
while
\[
\begin{aligned}
SS^*
&=
(T-\lambda I)(T^*-\overline{\lambda}I)\\
&=
TT^*-\overline{\lambda}T-\lambda T^*+|\lambda|^2I.
\end{aligned}
\]
These are equal because
\[
T^*T=TT^*.
\]
Thus $S$ is normal.
:::

<1>2. For every normal operator $N$ on a finite-dimensional complex inner-product space,
\[
\|Nx\|=\|N^*x\|
\]
for all $x$.

::: {.proof}
Normality gives
\[
N^*N=NN^*.
\]
Therefore
\[
\begin{aligned}
\|Nx\|^2
&=
\langle Nx,Nx\rangle\\
&=
\langle N^*Nx,x\rangle\\
&=
\langle NN^*x,x\rangle\\
&=
\langle N^*x,N^*x\rangle\\
&=
\|N^*x\|^2.
\end{aligned}
\]
Taking nonnegative square roots gives the claim.
:::

<1>3. One has
\[
Sv=0.
\]

::: {.proof}
By definition,
\[
Sv
=(T-\lambda I)v
=Tv-\lambda v
=0.
\]
:::

<1>4. One has
\[
S^*v=0.
\]

::: {.proof}
By step <1>1, $S$ is normal.
Therefore step <1>2 gives
\[
\|S^*v\|
=
\|Sv\|.
\]
By step <1>3,
\[
\|Sv\|=0.
\]
Hence
\[
\|S^*v\|=0,
\]
so
\[
S^*v=0.
\]
:::

<1>5. Therefore
\[
\boxed{T^*v=\overline{\lambda}v}.
\]

::: {.proof}
Since
\[
S^*=T^*-\overline{\lambda}I,
\]
step <1>4 says
\[
(T^*-\overline{\lambda}I)v=0.
\]
Thus
\[
T^*v=\overline{\lambda}v.
\]
:::

<1>6. Hence $v$ is an eigenvector of $T^*$.

::: {.proof}
The vector $v$ is nonzero by hypothesis, and step <1>5 shows that it is taken to a scalar multiple of itself by $T^*$.
Therefore $v$ is an eigenvector of $T^*$, with eigenvalue $\overline{\lambda}$.
:::

<1>7. Q.E.D.

::: {.proof}
Step <1>6 is the required conclusion.
:::
:::
