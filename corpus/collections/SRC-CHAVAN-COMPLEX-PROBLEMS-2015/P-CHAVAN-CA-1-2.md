---
schema: qual/card@1
id: P-CHAVAN-CA-1-2
kind: problem
title: Maximum modulus for polynomials from circular mean squares
classification: {areas: [complex-analysis], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problem 1.2 in the deterministic extraction; f/p and z/z_0 inconsistencies are normalized to the polynomial and center defined by the problem.
---

::: {.problem}
Let $p(z)=a_0+a_1z+\cdots+a_nz^n$ and suppose $z_0\in\mathbb C$, $|z_0|<1$, is such that
\[
|p(z)|\le |p(z_0)|\qquad(|z|\le1).
\]
Write
\[
p(z)=b_0+b_1(z-z_0)+\cdots+b_n(z-z_0)^n.
\]
For $0<r<1-|z_0|$, verify
\[
\frac1{2\pi}\int_{-\pi}^{\pi}|p(z_0+re^{i\theta})|^2\,d\theta
=|b_0|^2+|b_1|^2r^2+\cdots+|b_n|^2r^{2n},
\]
and
\[
\frac1{2\pi}\int_{-\pi}^{\pi}|p(z_0+re^{i\theta})|^2\,d\theta\le |b_0|^2.
\]
Conclude that a nonconstant polynomial cannot attain its maximum modulus in the open unit disk, and hence
\[
\max_{|z|\le1}|p(z)|=\max_{|z|=1}|p(z)|.
\]
:::

::: {.solution}
<1>1. For every $0<r<1-|z_0|$,
$$
\frac1{2\pi}\int_{-\pi}^{\pi}|p(z_0+re^{i\theta})|^2\,d\theta
=\sum_{k=0}^n |b_k|^2r^{2k}.
$$

::: {.proof}
From the expansion of $p$ about $z_0$,
$$
p(z_0+re^{i\theta})
=\sum_{k=0}^n b_kr^ke^{ik\theta}.
$$
Hence
$$
|p(z_0+re^{i\theta})|^2
=\sum_{j=0}^n\sum_{k=0}^n
b_j\overline{b_k}\,r^{j+k}e^{i(j-k)\theta}.
$$
For integers $j,k$,
$$
\frac1{2\pi}\int_{-\pi}^{\pi}e^{i(j-k)\theta}\,d\theta
=
\begin{cases}
1,&j=k,\\
0,&j\ne k.
\end{cases}
$$
Termwise integration of the finite double sum therefore leaves only
the diagonal terms, giving
$$
\frac1{2\pi}\int_{-\pi}^{\pi}|p(z_0+re^{i\theta})|^2\,d\theta
=|b_0|^2+|b_1|^2r^2+\cdots+|b_n|^2r^{2n}.
$$
:::

<1>2. For every $0<r<1-|z_0|$,
$$
\frac1{2\pi}\int_{-\pi}^{\pi}|p(z_0+re^{i\theta})|^2\,d\theta
\le |b_0|^2.
$$

::: {.proof}
For every $\theta$,
$$
|z_0+re^{i\theta}|
\le |z_0|+r
<1.
$$
Thus the hypothesis that $|p(z)|\le |p(z_0)|$ on the closed unit disk
gives
$$
|p(z_0+re^{i\theta})|^2\le |p(z_0)|^2.
$$
Since $b_0=p(z_0)$, integrating this pointwise inequality and dividing
by $2\pi$ gives the claim.
:::

<1>3. If $p$ attains its maximum modulus at a point $z_0$ with $|z_0|<1$, then $p$ is constant.

::: {.proof}
Combining steps <1>1 and <1>2 yields
$$
|b_0|^2+\sum_{k=1}^n|b_k|^2r^{2k}\le |b_0|^2.
$$
Therefore
$$
\sum_{k=1}^n|b_k|^2r^{2k}\le0.
$$
Every summand is nonnegative and $r>0$, so
$$
b_1=b_2=\cdots=b_n=0.
$$
Hence $p(z)=b_0$ for all $z$, so $p$ is constant.
:::

<1>4. A nonconstant polynomial cannot attain its maximum modulus in the open unit disk.

::: {.proof}
If a nonconstant polynomial attained its maximum modulus at an interior
point $z_0$, step <1>3 would force it to be constant, a contradiction.
:::

<1>5. One has
$$
\boxed{\max_{|z|\le1}|p(z)|=\max_{|z|=1}|p(z)|}.
$$

::: {.proof}
The polynomial $p$ is continuous, so $|p|$ attains a maximum on the
compact closed unit disk. If $p$ is nonconstant, step <1>4 shows that
no maximizing point lies in the open unit disk, hence some maximizing
point lies on the unit circle. If $p$ is constant, the equality is
immediate. Thus in all cases the two maxima are equal.
:::

<1>6. Q.E.D.

::: {.proof}
Steps <1>1 and <1>2 establish the requested integral identities, step
<1>4 gives the nonconstant case, and step <1>5 gives the final
maximum-modulus equality.
:::
:::
