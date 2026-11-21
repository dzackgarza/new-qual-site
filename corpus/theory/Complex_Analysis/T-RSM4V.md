---
schema: qual/card@1
id: T-RSM4V
kind: theorem
title: Summing series by residues
slogan: 'A meromorphic $f$ vanishing like $z^{-2}$ has its sums over $\ZZ$ and over the half-integers equal to minus the residues of $\pi\cot\pi z\,f$ and its three companion kernels.'
prompts:
- How does one sum $\sum_{n\in\ZZ}f(n)$ by residues?
- Which kernel sums a series over the half-integers with alternating signs?
classification:
  areas:
  - complex-analysis
  topics:
  - Residues
  - Series of Numbers
relations: []
review: draft
---

::: {.theorem}
Let $f$ be [[D-7DFVJ|meromorphic]] on $\CC$ with finitely many poles, and suppose there are $R>0$ and $C>0$ with
$$
\abs{f(z)}\le \frac{C}{\abs z^2}\qquad\text{for } \abs z\ge R .
$$
Suppose also that no pole of $f$ is one of the points $\ZZ$ or $\tfrac12+\ZZ$, that is, no pole of $f$ is a pole of any of the four kernels below.
Then, each sum on the right being taken over the poles of $f$,
$$
\begin{aligned}
\sum_{n=-\infty}^{\infty} f(n) &= -\sum \Res\qty{\pi \cot (\pi z) f(z)}, \\
\sum_{n=-\infty}^{\infty}(-1)^{n} f(n) &= -\sum \Res\qty{\pi \csc (\pi z) f(z)}, \\
\sum_{n=-\infty}^{\infty} f\qty{\frac{2 n+1}{2}} &= \sum \Res\qty{\pi \tan (\pi z) f(z)}, \\
\sum_{n=-\infty}^{\infty}(-1)^{n} f\qty{\frac{2 n+1}{2}} &= \sum \Res\qty{\pi \sec (\pi z) f(z)}.
\end{aligned}
$$
:::

::: {.proof}
Each of the four series converges absolutely, since $\abs{f}=O\qty{\abs z^{-2}}$ at infinity; so each left-hand side is a limit of its partial sums over the sampled points inside a large square, and it is that limit the argument computes.

**The kernels are bounded on the contours.** Let $\pi\cot(\pi z)$, $\pi\csc(\pi z)$, $\pi\tan(\pi z)$ and $\pi\sec(\pi z)$ be the four kernels. On the square $Q_N$ with vertices $\pm\qty{N+\tfrac12}\pm i\qty{N+\tfrac12}$, whose boundary misses $\ZZ$: on the horizontal sides $\abs{\Im z}=N+\tfrac12\ge\tfrac12$ gives $\abs{\cot\pi z}\le\coth\qty{\pi/2}$ and $\abs{\csc\pi z}\le 1/\sinh\qty{\pi/2}$; on the vertical sides $z=\pm\qty{N+\tfrac12}+iy$ one has $\cot\pi z=-i\tanh(\pi y)$ and $\abs{\sin\pi z}=\cosh(\pi y)$, so $\abs{\cot\pi z}<1$ and $\abs{\csc\pi z}\le1$. On the square $R_N$ with vertices $\pm N\pm iN$, whose boundary misses $\tfrac12+\ZZ$: on the vertical sides $z=\pm N+iy$ one has $\tan\pi z=i\tanh(\pi y)$ and $\abs{\cos\pi z}=\cosh(\pi y)$, so $\abs{\tan\pi z}<1$ and $\abs{\sec\pi z}\le1$; on the horizontal sides $\abs{\tan\pi z}\le\coth\pi$ and $\abs{\sec\pi z}\le1/\sinh(\pi N)$. So on each contour the corresponding kernel is bounded by a constant independent of $N$.

**The contour integrals vanish in the limit.** On $Q_N$ or $R_N$ the integrand $\text{kernel}\cdot f$ is $O\qty{N^{-2}}$, the side lengths are $2N+1$ or $2N$, and the boundary misses the poles of both factors, so the integral over the boundary is $O\qty{N^{-1}}$ and tends to $0$.

**Residues.** The residue theorem ([[T-HRPNO]]) gives, for $N$ large enough that every pole of $f$ lies inside the contour,
$$
0=\lim_{N\to\infty}\frac{1}{2\pi i}\oint_{\bd Q_N}\pi\cot(\pi z)f(z)\dz=\sum_{n\in\ZZ}f(n)+\sum_{\text{poles }p}\Res_{z=p}\qty{\pi\cot(\pi z)f(z)},
$$
because $\pi\cot(\pi z)$ has a simple pole of residue $1$ at each integer; this is the first display. The same computation with the other three kernels uses their residues at the sampled points: $\pi\csc(\pi z)$ has residue $(-1)^n$ at $n$, since $\sin(\pi z)$ has derivative $\pi(-1)^n$ there; $\pi\tan(\pi z)$ has residue $-1$ at $\tfrac{2n+1}{2}$; and $\pi\sec(\pi z)$ has residue $(-1)^{n+1}$ at $\tfrac{2n+1}{2}$, because $\cos(\pi z)$ has derivative $-\pi(-1)^n$ there. Substituting these four residues and moving the sum over the sampled points to the other side gives the four displays, the signs of the last two being the signs of those residues.
:::

::: {.remark}
The three companion kernels are the first two at a shifted argument: $\tan(\pi z)=-\cot\qty{\pi\qty{z+\tfrac12}}$ and $\sec(\pi z)=\csc\qty{\pi\qty{z+\tfrac12}}$, which is why the half-integer sums carry kernels of their own.
:::
