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
The statement is Exercise 12 of [@SS03, ch. 3], printed with the prescribed integrand $\pi\cot\pi z/(u+z)^2$ and the circles $\abs{z}=R_N=N+\tfrac12$.


The argument is the card's own: the residues of $\pi\cot(\pi z)/(u+z)^{2}$ inside the circle give the sum minus the cotangent term, and the contour integral is bounded and tends to $0$.

::: pf

::: {.pf-step #residues}

$\operatorname{Res}_{z=n}f(z)=\dfrac{1}{(u+n)^{2}}$ for every integer $n\ne-u$, and $\operatorname{Res}_{z=-u}f(z)=-\dfrac{\pi^{2}}{\sin^{2}(\pi u)}$.

::: pf-proof

Write $g(z)=\pi\cot(\pi z)$, holomorphic near the integers with $\lim_{z\to n}(z-n)g(z)=1$, because $\pi\cot(\pi z)=\pi\cos(\pi z)/\sin(\pi z)$, $\sin(\pi z)$ has a simple zero at $z=n$ with $\sin'(\pi n)=\pi(-1)^{n}$, and $\cos(\pi n)=(-1)^{n}$, so the limit is $\pi\cdot\frac{(-1)^{n}}{\pi(-1)^{n}}=1$. Since $u\notin\ZZ$, the factor $(u+z)^{-2}$ is holomorphic and nonzero at $z=n$, so $f=g\cdot(u+z)^{-2}$ has a simple pole there with residue $g(n)/(u+n)^{2}=1/(u+n)^{2}$. At $z=-u$ the function $g$ is holomorphic (as $u\notin\ZZ$) and $(u+z)^{-2}$ has a double pole, so the residue of the product is $g'(-u)$; and $g'(z)=-\pi^{2}\csc^{2}(\pi z)$, so $g'(-u)=-\pi^{2}/\sin^{2}(\pi u)$.

:::

:::

::: {.pf-step #theorem}

$\displaystyle\int_{C_{N}}f(z)\,dz=2\pi i\Bigl(\sum_{n=-N}^{N}\frac{1}{(u+n)^{2}}-\frac{\pi^{2}}{\sin^{2}(\pi u)}\Bigr)$.

::: pf-proof

For $N\ge\abs{u}$ the poles of $f$ inside $C_{N}$, the circle $\abs{z}=N+\frac12$, are the integers $n$ with $\abs{n}\le N$ together with $-u$, which lies inside because $\abs{u}\le N<N+\frac12$. Apply the residue theorem to $f$ on $C_{N}$ and insert the residues computed in step [](#residues){.pf-ref}.

:::

:::

::: {.pf-step #boundcot}

There is a constant $C$ with $\abs{\cot(\pi z)}\le C$ for every $z$ on every circle $C_{N}$ with $N\ge1$.

::: pf-proof

For $z=x+iy$, $\cot(\pi z)=\frac{\sin2\pi x-i\sinh2\pi y}{\cosh2\pi y-\cos2\pi x}$ and hence
$$
\abs{\cot(\pi z)}^{2}=\frac{\cosh2\pi y+\cos2\pi x}{\cosh2\pi y-\cos2\pi x}.
$$
If $\abs{y}\ge\frac12$ then $\cosh2\pi y-\cos2\pi x\ge\cosh\pi-1>0$ and the quotient is at most $\frac{\cosh2\pi y+1}{\cosh2\pi y-1}$, which is a decreasing function of $\cosh2\pi y\ge\cosh\pi$ and so bounded by $\frac{\cosh\pi+1}{\cosh\pi-1}$. If instead $\abs{y}<\frac12$ and $\abs{z}=N+\frac12$, then $x^{2}=(N+\frac12)^{2}-y^{2}>N^{2}+N$, so $\abs{x}>\sqrt{N^{2}+N}$, and
$$
N+\tfrac12-\sqrt{N^{2}+N}=\frac{1/4}{N+\frac12+\sqrt{N^{2}+N}}\le\frac18
$$
for $N\ge1$; hence $\abs{x}$ lies in $(N+\frac14,N+\frac12]$, so $2\pi x$ is congruent modulo $2\pi$ to a number in $(\frac{\pi}{2},\pi]$ and $\cos2\pi x<0$. Then the numerator is at most the denominator, so $\abs{\cot(\pi z)}\le1$. Taking $C$ to be the maximum of the two bounds gives the claim.

:::

:::

::: {.pf-step #vanish}

$\displaystyle\abs{\int_{C_{N}}f(z)\,dz}\le\frac{2\pi R_{N}C}{(R_{N}-\abs{u})^{2}}\to0$ as $N\to\infty$.

::: pf-proof

On $C_{N}$ we have $\abs{z+u}\ge\abs{z}-\abs{u}=R_{N}-\abs{u}>0$, so $\abs{f(z)}\le C/(R_{N}-\abs{u})^{2}$ by step [](#boundcot){.pf-ref}; the circle has length $2\pi R_{N}$. The standard estimate for a contour integral bounds the modulus of the integral by the supremum of the integrand times the length, giving the displayed inequality, and the right side is $O(1/N)\to0$ because $R_{N}=N+\frac12$.

:::

:::

::: {.pf-step #conclusion}

$\displaystyle\sum_{n=-\infty}^{\infty}\frac{1}{(u+n)^{2}}=\frac{\pi^{2}}{\sin^{2}(\pi u)}$.

::: pf-proof

By steps [](#theorem){.pf-ref} and [](#vanish){.pf-ref} the modulus of $\sum_{n=-N}^{N}\frac{1}{(u+n)^{2}}-\frac{\pi^{2}}{\sin^{2}(\pi u)}$ equals $\frac{1}{2\pi}\abs{\int_{C_{N}}f\,dz}$, which tends to $0$. Hence the symmetric partial sums converge to $\frac{\pi^{2}}{\sin^{2}(\pi u)}$; the terms are positive, so the two-sided series converges absolutely and its sum is that limit:
$$
\boxed{\sum_{n=-\infty}^{\infty}\frac{1}{(u+n)^{2}}=\frac{\pi^{2}}{\sin^{2}(\pi u)},\qquad u\notin\ZZ.}
$$

:::

:::

:::

:::
