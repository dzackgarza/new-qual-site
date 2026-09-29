---
schema: qual/card@1
id: P-BKF20-4B
kind: problem
title: Zeta values from poles of $\pi/(z^n\tan\pi z)$
classification:
  areas:
  - prelim
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2020 residue argument. The poles
    are the integers, with order n+1 at zero and residue m^{-n} at each
    nonzero integer m; half-integer square contours make the boundary integral
    tend to zero for even n>=2.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked all local pole orders, simple-pole residues, the uniform cotangent
    bound on the chosen contours, passage to the infinite residue sum, and
    rationality of the zero residue after scaling by pi^n.
---

::: {.problem}
(a) For positive integer $n$, find all poles of
\[
\frac{\pi}{z^n\tan(\pi z)}
\]
and the residues of all simple poles.

(b) Prove that for positive even $n$,
\[
\frac{\sum_{m=1}^{\infty}m^{-n}}{\pi^n}
\]
is rational.
:::

::: {.solution}
For a positive integer $n$, set
$$
F_n(z)
\coloneqq
\frac{\pi}{z^n\tan(\pi z)}
=
\frac{\pi\cot(\pi z)}{z^n}.
$$

::: pf

::: {.pf-step #s1}

The poles of $F_n$ are exactly the integers. Every nonzero
integer is a simple pole, while $0$ is a pole of order $n+1$.

::: pf-proof

The function $\cot(\pi z)$ has simple poles exactly at the integers and
zeros at the half-integers. Near an integer $m$,
$$
\sin(\pi z)
=
(-1)^m\pi(z-m)+O((z-m)^3),
$$
while
$$
\cos(\pi z)
=
(-1)^m+O((z-m)^2).
$$
Hence
$$
\pi\cot(\pi z)
=
\frac1{z-m}+O(z-m).
$$

If $m\ne0$, the factor $z^{-n}$ is holomorphic and nonzero at $m$, so
the pole remains simple. At $m=0$,
$$
\pi\cot(\pi z)
=
\frac1z+O(z),
$$
and division by $z^n$ gives a pole of order $n+1$.
There are no other poles.

:::

:::

::: {.pf-step #s2}

For every nonzero integer $m$,
$$
\boxed{
\operatorname{Res}_{z=m}F_n(z)=\frac1{m^n}.
}
$$

::: pf-proof

By the expansion in step [](#s1){.pf-ref},
$$
F_n(z)
=
\frac1{z^n}
\left(
\frac1{z-m}+O(z-m)
\right).
$$
Since $z^{-n}$ is holomorphic at $m$, the coefficient of
$(z-m)^{-1}$ is its value at $m$, namely $m^{-n}$.
This completes part (a).

:::

:::

::: {.pf-step #s3}

Assume from now on that $n$ is positive and even. For
$N\ge1$, put
$$
R_N\coloneqq N+\frac12
$$
and let $\Gamma_N$ be the positively oriented boundary of the square
$$
\{z:|\operatorname{Re}z|\le R_N,\ |\operatorname{Im}z|\le R_N\}.
$$
There is a constant $C>0$, independent of $N$, such that
$$
|\cot(\pi z)|\le C
$$
for every $z\in\Gamma_N$.

::: pf-proof

On a vertical side,
$$
\operatorname{Re}z=\pm\left(N+\frac12\right).
$$
Writing $z=x+iy$ and using the elementary formulas for sine and cosine
of a complex argument gives
$$
|\cot(\pi z)|
=
|\tanh(\pi y)|
\le1.
$$

On a horizontal side,
$$
|\operatorname{Im}z|=R_N\ge\frac12.
$$
For $z=x+iy$,
$$
|\cot(\pi z)|^2
=
\frac{\cos^2(\pi x)+\sinh^2(\pi y)}
{\sin^2(\pi x)+\sinh^2(\pi y)}
\le
\coth^2(\pi|y|)
\le
\coth^2\left(\frac\pi2\right).
$$
Thus one may take
$$
C=\max\left\{1,\coth\left(\frac\pi2\right)\right\}.
$$

:::

:::

::: {.pf-step #s4}

One has
$$
\int_{\Gamma_N}F_n(z)\,dz
\longrightarrow
0.
$$

::: pf-proof

Every point of $\Gamma_N$ satisfies
$$
|z|\ge R_N.
$$
By step [](#s3){.pf-ref},
$$
|F_n(z)|
\le
\frac{\pi C}{R_N^n}
$$
on $\Gamma_N$. The perimeter of the square is $8R_N$, so the
$ML$-estimate gives
$$
\left|
\int_{\Gamma_N}F_n(z)\,dz
\right|
\le
8\pi C R_N^{1-n}.
$$
Because $n\ge2$, the right-hand side tends to $0$.

:::

:::

::: {.pf-step #s5}

If
$$
r_n\coloneqq\operatorname{Res}_{z=0}F_n(z),
$$
then
$$
r_n+2\sum_{m=1}^{\infty}\frac1{m^n}=0.
$$

::: pf-proof

The poles inside $\Gamma_N$ are precisely
$$
-N,-N+1,\ldots,-1,0,1,\ldots,N.
$$
The residue theorem and step [](#s2){.pf-ref} give
$$
\frac1{2\pi i}
\int_{\Gamma_N}F_n(z)\,dz
=
r_n
+
\sum_{\substack{-N\le m\le N\\m\ne0}}
\frac1{m^n}.
$$
Since $n$ is even,
$$
\frac1{(-m)^n}=\frac1{m^n},
$$
so
$$
\frac1{2\pi i}
\int_{\Gamma_N}F_n(z)\,dz
=
r_n
+
2\sum_{m=1}^{N}\frac1{m^n}.
$$
Now let $N\to\infty$. Step [](#s4){.pf-ref} sends the left-hand side to $0$, and
the series converges because $n\ge2$. This proves the identity.

:::

:::

::: {.pf-step #s6}

The residue $r_n$ is a rational multiple of $\pi^n$.

::: pf-proof

Define
$$
h(w)\coloneqq w\cot w.
$$
The functions
$$
\cos w
\qquad\text{and}\qquad
\frac{\sin w}{w}
$$
have power series at $0$ with rational coefficients, and the second
has constant term $1$. Therefore its reciprocal also has a power
series with rational coefficients. Hence
$$
h(w)
=
\frac{\cos w}{\sin w/w}
$$
has a power series with rational coefficients.

Moreover, $h$ is even, so there are rational numbers $c_j$ such that
$$
h(w)
=
\sum_{j=0}^{\infty}c_jw^{2j}
$$
near $0$. Since
$$
\pi\cot(\pi z)
=
\frac{h(\pi z)}z,
$$
we obtain
$$
F_n(z)
=
\frac{h(\pi z)}{z^{n+1}}
=
\sum_{j=0}^{\infty}
c_j\pi^{2j}z^{2j-n-1}.
$$
The residue is the coefficient of $z^{-1}$. Because $n$ is even, this
occurs exactly when
$$
2j=n.
$$
Thus
$$
r_n
=
c_{n/2}\pi^n
$$
with $c_{n/2}\in\QQ$.

:::

:::

::: {.pf-step #s7}

Therefore
$$
\boxed{
\frac{\sum_{m=1}^{\infty}m^{-n}}{\pi^n}\in\QQ.
}
$$

::: pf-proof

By step [](#s5){.pf-ref},
$$
\sum_{m=1}^{\infty}\frac1{m^n}
=
-\frac{r_n}{2}.
$$
By step [](#s6){.pf-ref},
$$
r_n=c_{n/2}\pi^n
$$
with $c_{n/2}\in\QQ$. Hence
$$
\frac{\sum_{m=1}^{\infty}m^{-n}}{\pi^n}
=
-\frac12c_{n/2}
\in
\QQ.
$$
This proves part (b).

:::

:::

::: pf-qed

Steps [](#s1){.pf-ref} and [](#s2){.pf-ref} prove part (a), and steps [](#s3){.pf-ref}, [](#s4){.pf-ref}, [](#s5){.pf-ref}, [](#s6){.pf-ref} and [](#s7){.pf-ref} prove part (b).

:::

:::

:::
