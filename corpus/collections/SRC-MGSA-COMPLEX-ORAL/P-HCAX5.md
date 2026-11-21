---
schema: qual/card@1
id: P-HCAX5
kind: problem
title: Power series and radius of convergence of the tangent function
classification:
  areas:
  - complex-analysis
  topics:
  - Power Series
relations: []
review: draft
audit:
- event: solution-written
  by: claude
  date: 2026-11-20
  note: >-
    The card stood in queue D: its solution was prose with no numbered step. It is now a `pf`
    with seven steps, each carrying a `pf-proof`; the series, its first four terms and the three
    answers are unchanged. Cited by number only: the definition of the Bernoulli numbers by
    their generating function, and the standard facts that a function holomorphic on a disc has
    a convergent Taylor series there and that the identity theorem extends an equality of
    holomorphic functions. Checked: the algebra turning $\sin/\cos$ into $-i(e^{2iz}-1)/(e^{2iz}+1)$,
    the identity $2/(e^t+1)=2/(e^t-1)-4/(e^{2t}-1)$ over a common denominator, the substitution of
    the two Bernoulli expansions and the resulting coefficient $(-1)^{n-1}2^{2n}(2^{2n}-1)B_{2n}/(2n)!$,
    the four numerical coefficients from $B_2,B_4,B_6,B_8$, and the location and simplicity of the
    zeros of $\cos$.
---

::: {.problem}
(a) Derive the power series of $\tan z$ at the origin.

(b) Determine its radius of convergence.

(c) Prove the location of the zeros of $\cos z$, and explain how they determine this radius.
:::

::: {.solution}

::: pf

::: pf-step

(a) The Bernoulli numbers are defined by the generating function
$$
\frac{t}{e^t-1}=\sum_{n=0}^{\infty}B_n\frac{t^n}{n!},
$$
which converges for $\abs{t}<2\pi$.

::: pf-proof

The function $t/(e^t-1)$ extends to a holomorphic function on $\abs{t}<2\pi$: its only singularities are the zeros of $e^t-1$, namely $2\pi ik$ with $k\in\ZZ\setminus\{0\}$, and the singularity at $0$ is removable because $t/(e^t-1)\to1$ there. A function holomorphic on a disc has a convergent Taylor series there, so the displayed expansion defines the numbers $B_n$ uniquely, with $B_0=1$.

:::

:::

::: pf-step

(a) One has
$$
\tan z=-i\frac{e^{2iz}-1}{e^{2iz}+1}=-i+\frac{2i}{e^{2iz}+1},
$$
and, with $t=2iz$,
$$
\frac{2}{e^t+1}=\frac{2}{e^t-1}-\frac{4}{e^{2t}-1}.
$$

::: pf-proof

$\tan z=\sin z/\cos z$ and $\sin z=(e^{iz}-e^{-iz})/2i$, $\cos z=(e^{iz}+e^{-iz})/2$, so $\tan z=\frac{1}{i}\cdot\frac{e^{iz}-e^{-iz}}{e^{iz}+e^{-iz}}$; multiplying numerator and denominator by $e^{iz}$ gives $\tan z=\frac1i\cdot\frac{e^{2iz}-1}{e^{2iz}+1}=-i\frac{e^{2iz}-1}{e^{2iz}+1}$. Writing $e^{2iz}-1=(e^{2iz}+1)-2$ separates the quotient as $-i+\frac{2i}{e^{2iz}+1}$. For the second identity, put the right side over the common denominator $(e^t-1)(e^t+1)$: $\frac{2(e^t+1)-4}{(e^t-1)(e^t+1)}=\frac{2e^t-2}{e^{2t}-1}=\frac{2}{e^t+1}$, using $e^{2t}-1=(e^t-1)(e^t+1)$.

:::

:::

::: pf-step

(a) Substituting the Bernoulli expansion in the two terms of step 2 gives
$$
\tan z=\sum_{n=1}^{\infty}(-1)^{n-1}\frac{2^{2n}(2^{2n}-1)B_{2n}}{(2n)!}z^{2n-1}.
$$

::: pf-proof

With $t=2iz$, step 2 writes $\tan z=-i+2i\bigl(\frac1{e^t-1}-\frac2{e^{2t}-1}\bigr)$. The generating function of step 1 gives $\frac1{e^t-1}=\frac1t\sum_{n\ge0}B_n\frac{t^n}{n!}$ and, applied to $2t$, gives $\frac2{e^{2t}-1}=\frac1t\sum_{n\ge0}B_n2^n\frac{t^n}{n!}$. The bracket is therefore $\frac1t\sum_{n\ge1}B_n(1-2^n)\frac{t^n}{n!}$, the $n=0$ term vanishing, that is $\sum_{n\ge1}B_n(1-2^n)\frac{t^{n-1}}{n!}$, and multiplying by $2i$ and substituting $t=2iz$ gives $\tan z=-i+2i\sum_{n\ge1}B_n(1-2^n)\frac{(2iz)^{n-1}}{n!}$. The term $n=1$ is $2i\cdot B_1\cdot(1-2)=2i\cdot(-\frac12)(-1)=i$, which cancels $-i$. The odd Bernoulli numbers $B_n$ with $n>1$ vanish, because $t/(e^t-1)+t/2$ is an even function; so only $n=2m$ survive, and for such $n$, $2i(2i)^{n-1}=2^{n}(-1)^{n/2}$ and $(1-2^n)=-(2^n-1)$ give the coefficient $(-1)^{n/2+1}2^{n}(2^{n}-1)B_n/n!$. Writing $n=2m$ and renaming, the coefficient of $z^{2n-1}$ is $(-1)^{n-1}2^{2n}(2^{2n}-1)B_{2n}/(2n)!$, which is the displayed series.

:::

:::

::: pf-step

(a) In particular
$$
\tan z=z+\frac{z^3}{3}+\frac{2z^5}{15}+\frac{17z^7}{315}+\cdots.
$$

::: pf-proof

$B_2=\frac16$, $B_4=-\frac1{30}$, $B_6=\frac1{42}$, $B_8=-\frac1{30}$; substituting $n=1,2,3,4$ in the coefficient of step 3 gives $2^2\cdot3\cdot\frac16/2!=1$, $-2^4\cdot15\cdot\frac1{30}/4!=\frac13$, $2^6\cdot63\cdot\frac1{42}/6!=\frac2{15}$ and $-2^8\cdot255\cdot\frac1{30}/8!=\frac{17}{315}$.

:::

:::

::: pf-step

(c) $\cos z=0$ if and only if $e^{2iz}=-1$; writing $z=x+iy$ this forces $e^{-2y}=1$, hence $y=0$, and then $e^{2ix}=-1$, so
$$
z=\frac\pi2+k\pi,\qquad k\in\ZZ.
$$

::: pf-proof

$\cos z=(e^{iz}+e^{-iz})/2$ vanishes exactly when $e^{iz}=-e^{-iz}$, and multiplying by $e^{iz}$ turns this into $e^{2iz}=-1$. With $z=x+iy$, $e^{2iz}=e^{-2y}e^{2ix}$, so $\abs{e^{2iz}}=e^{-2y}$ and $\abs{-1}=1$ force $y=0$. Then $e^{2ix}=-1$ means $2x\equiv\pi\pmod{2\pi}$, that is $x=\frac\pi2+k\pi$.

:::

:::

::: pf-step

(c) Conversely $\cos(\frac\pi2+k\pi)=0$, these zeros are simple, and they are simple poles of $\tan z$.

::: pf-proof

At $x=\frac\pi2+k\pi$ we have $e^{2ix}=e^{i\pi}=-1$, so $\cos x=0$ by step 5 read backwards. The derivative is $-\sin$, and $\sin(\frac\pi2+k\pi)=(-1)^k\ne0$, so each zero has multiplicity one. Since $\sin$ does not vanish there, $\tan=\sin/\cos$ has a pole of order one at each of them.

:::

:::

::: pf-step

(b) The nearest poles to the origin are at $\pm\pi/2$; hence $\tan z$ is holomorphic on $\abs{z}<\frac\pi2$, so its Taylor series at $0$ has radius at least $\frac\pi2$, and it cannot have larger radius, because a larger Taylor disk would continue $\tan z$ holomorphically across $z=\frac\pi2$. Thus
$$
R=\frac\pi2.
$$

::: pf-proof

By step 5 the zeros of $\cos$ nearest $0$ are $\pm\frac\pi2$, so on the open disc $\abs{z}<\frac\pi2$ the function $\cos$ is nonzero and $\tan=\sin/\cos$ is holomorphic there; the radius of convergence of the Taylor series at $0$ of a holomorphic function is at least the radius of any disc on which it is holomorphic. If the radius were larger, the Taylor series would define a holomorphic extension of $\tan$ to a disc containing $\frac\pi2$, agreeing with $\tan$ on $\abs{z}<\frac\pi2$ and hence, by the identity theorem, on the whole disc; but $\tan$ is unbounded near $\frac\pi2$ by step 6, a contradiction. Hence the radius is exactly $\frac\pi2$.

:::

:::

:::
:::
