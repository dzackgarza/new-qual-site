---
schema: qual/card@1
id: E-SS3.EX-12
kind: problem
title: $\sum_{n\in\ZZ}(u+n)^{-2}=\pi^2/\sin^2\pi u$ by residues
classification:
  areas:
    - complex-analysis
  topics: [Residue Theorem, Series Summation, Cotangent]
relations: []
review: draft
audit:
  - event: solution-written
    by: gpt-5.6-sol
    date: 2026-09-11
---

::: {.exercise}
Suppose $u$ is not an integer. Prove that
$$
\sum_{n=-\infty}^{\infty} \frac{1}{(u + n)^2} = \frac{\pi^2}{(\sin\pi u)^2}
$$
by integrating
$$
f(z) = \frac{\pi\cot\pi z}{(u + z)^2}
$$
over the circle $\abs{z} = R_N = N + 1/2$ ($N$ integral, $N \geq \abs{u}$), adding the residues of $f$ inside the circle, and letting $N$ tend to infinity.

Note. Two other derivations of this identity, using Fourier series, were given in Book I.
:::

::: {.solution}
Let
$$
f(z)=\frac{\pi\cot(\pi z)}{(u+z)^2},\qquad u\notin\ZZ,
$$
and let $C_N$ be $\abs{z}=R_N=N+\tfrac12$, with $N\ge \abs{u}$.

At each integer $n$ with $\abs{n}\le N$, $\pi\cot(\pi z)$ has residue $1$, so
$$
\operatorname{Res}_{z=n}f(z)=\frac1{(u+n)^2}.
$$
At $z=-u$ there is a double pole. If $g(z)=\pi\cot(\pi z)$, then
$$
\operatorname{Res}_{z=-u}\frac{g(z)}{(z+u)^2}=g'(-u)
=-\pi^2\csc^2(\pi u).
$$
Therefore the residue theorem gives
$$
\int_{C_N}f(z)\,dz
=2\pi i\left(
\sum_{n=-N}^N\frac1{(u+n)^2}
-\frac{\pi^2}{\sin^2(\pi u)}
\right).
\tag{1}
$$

It remains to show the contour integral tends to $0$. The standard formula
$$
\cot(x+iy)=\frac{\sin 2x-i\sinh 2y}{\cosh 2y-\cos 2x}
$$
gives $\abs{\cot(\pi(x+iy))}^2=\frac{\cosh 2\pi y+\cos 2\pi x}{\cosh 2\pi y-\cos 2\pi x}$. Hence $\abs{\cot(\pi z)}\le\coth\frac{\pi}{2}$ when $\abs{y}\ge\frac12$, since then $\cosh2\pi y-\cos2\pi x\ge\cosh\pi-1$. If $z=x+iy$ lies on $\abs{z}=N+\tfrac12$ with $\abs{y}<\frac12$, then $\sqrt{N^2+N}<\abs{x}\le N+\frac12$, so $\abs{x}$ lies within $\frac18$ of $N+\frac12$ (as $N+\frac12-\sqrt{N^2+N}=\frac{1/4}{N+\frac12+\sqrt{N^2+N}}\le\frac18$), and $\cos2\pi x\le\cos\frac{3\pi}{4}<0$; then $\abs{\cot(\pi z)}\le1$. Thus $\abs{\cot(\pi z)}\le C$ on all these circles, with $C=\coth\frac{\pi}{2}$. Also $\abs{z+u}\ge R_N-\abs{u}$. Hence
$$
\abs{\int_{C_N}f(z)\,dz}
\le 2\pi R_N\,\frac{C}{(R_N-\abs{u})^2}\longrightarrow0.
$$
Letting $N\to\infty$ in (1) yields
$$
\sum_{n=-\infty}^{\infty}\frac1{(u+n)^2}
=\frac{\pi^2}{\sin^2(\pi u)}.
$$
:::

::: {.remark title="Variations"}
$$
\sum_{k\in \ZZ} \frac{1}{\qty{k - \frac12}^2} = \pi^2.
$$
This is the main identity at $u=-\frac12$, where $\sin^2(\pi u)=1$.
:::
