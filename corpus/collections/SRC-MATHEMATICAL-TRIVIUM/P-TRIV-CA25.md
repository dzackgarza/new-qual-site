---
schema: qual/card@1
id: P-TRIV-CA25
kind: problem
title: Matsubara sums giving the Bose and Fermi distributions
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Complex Analysis, Problem 25, in the deterministic MinerU Flash extraction assets/attachments/Big_List_of_Math_Problems_extracted.md.
---

::: {.problem}
(a) Matsubara summation: in statistical mechanics, one often has to carry out summations over Matsubara frequencies.
These frequencies appear when the system is put at finite temperature, and the summation can be tedious to carry out.
We will consider the expectation value of the number of particles of a bosonic non-interacting gas.
Consider the function $h ( \omega _ { n } ) = - \frac { T } { i \omega _ { n } - \xi }$ Here $\omega _ { n }$ are called Matsubara frequencies.
In this case (the bosonic one) they are given by $\omega _ { n } = 2 \pi n T$

What we want to compute is $\begin{array} { r } { S \equiv \sum _ { n } h ( \omega _ { n } ) } \end{array}$ . To do so, we introduce an auxiliary function $\begin{array} { r } { g ( z ) = \frac { \beta } { e ^ { \beta z } - 1 } } \end{array}$ (setting $k _ { B } = 1 , \beta = T ^ { - 1 } )$ •

•Where are the poles of h? Where are those of $g \smash { ? }$

Consider now the function $g ( z ) h ( - i z )$ . Find a contour for which

$$
\frac { 1 } { 2 \pi i } \oint \mathrm { d } z g ( z ) h ( - i z ) = S .
$$

This contour encompasses an infinite number of poles.

•Since for large z the function decays fast enough the residue at infinity vanishes; inflate the contour and flip its orientation, so that it includes only a finite number of poles, in this case only one.

Carry out the integration.
You should find $- T \sum _ { n } { \frac { 1 } { i \omega _ { n } - \xi } } = { \frac { 1 } { e ^ { \beta \xi } - 1 } } ;$ as expected, this is the Bose distribution.

(b) Redo the previous exercise for fermions: the frequencies are $\omega _ { n } = ( 2 n { + } 1 ) \pi T$

It's convenient to pick $\begin{array} { r } { g ( z ) = \frac { \beta } { e ^ { \beta z } + 1 } } \end{array}$ . You should find

$$
T \sum _ { n } { \frac { 1 } { i \omega _ { n } - \xi } } = { \frac { 1 } { e ^ { \beta \xi } + 1 } }
$$
:::

::: {.remark}
The bilateral Matsubara sums have terms of order $1/n$, so they are not
ordinary absolutely convergent series. The values below are the contour
summation values prescribed by the problem: first sum the residues at the
Matsubara poles inside the chosen finite contour, then enlarge that contour and
replace those residues by the finitely many remaining poles.
:::

Assume $T>0$ and put
$$
\beta=T^{-1}.
$$

::: pf

::: pf-step

In the bosonic case,
$$
h(w)=-\frac{T}{iw-\xi}
$$
has a simple pole at
$$
w=-i\xi.
$$


::: pf-proof

The denominator vanishes exactly when
$$
iw-\xi=0,
$$
equivalently $w=-i\xi$.

:::

:::

::: pf-step

The auxiliary function
$$
g_B(z)=\frac{\beta}{e^{\beta z}-1}
$$
has simple poles at
$$
z=i\omega_n=i2\pi nT,
\qquad
n\in\ZZ,
$$
and each such pole has residue $1$.


::: pf-proof

The poles satisfy
$$
e^{\beta z}=1,
$$
so
$$
\beta z=2\pi i n,
$$
hence
$$
z=i2\pi nT.
$$
At such a point $z_n$,
$$
\operatorname{Res}_{z=z_n}g_B(z)
=
\frac{\beta}{\beta e^{\beta z_n}}
=1.
$$

:::

:::

::: pf-step

Define
$$
F_B(z)
=
g_B(z)h(-iz)
=
-\frac{1}{(e^{\beta z}-1)(z-\xi)}.
$$
At each Matsubara pole $z=i\omega_n$,
$$
\operatorname{Res}_{z=i\omega_n}F_B(z)
=
h(\omega_n).
$$


::: pf-proof

Since
$$
h(-iz)
=
-\frac{T}{z-\xi},
$$
and
$$
T\beta=1,
$$
the displayed formula for $F_B$ follows. By step <1>2, the residue of $g_B$
at $i\omega_n$ is $1$, so multiplying by the holomorphic factor
$h(-iz)$ gives residue $h(\omega_n)$.

:::

:::

::: pf-step

Besides the Matsubara poles, $F_B$ has a simple pole at
$$
z=\xi
$$
with residue
$$
\operatorname{Res}_{z=\xi}F_B(z)
=
-\frac{1}{e^{\beta\xi}-1}.
$$


::: pf-proof

At $z=\xi$, only the factor $z-\xi$ vanishes, so
$$
\operatorname{Res}_{z=\xi}F_B(z)
=
\lim_{z\to\xi}
(z-\xi)F_B(z)
=
-\frac{1}{e^{\beta\xi}-1}.
$$

:::

:::

::: pf-step

Under the contour prescription in the problem,
$$
\sum_{n\in\ZZ} h(\omega_n)
=
-\operatorname{Res}_{z=\xi}F_B(z).
$$


::: pf-proof

For a finite contour enclosing a finite symmetric set of Matsubara poles and
excluding $\xi$, the residue theorem and step <1>3 identify the contour
integral with the corresponding finite Matsubara sum.

Now enlarge and deform the contour as prescribed in the problem. The outer
boundary contribution is discarded in this contour summation prescription,
and reversing orientation leaves a negatively oriented contour around the
remaining finite pole $z=\xi$. Hence the limiting Matsubara residue sum is
the negative of the residue at $\xi$.

:::

:::

::: pf-step

Therefore
$$
\boxed{
-T
\sum_{n\in\ZZ}
\frac{1}{i\omega_n-\xi}
=
\frac{1}{e^{\beta\xi}-1}.
}
$$


::: pf-proof

By definition,
$$
h(\omega_n)
=
-\frac{T}{i\omega_n-\xi}.
$$
Combine steps <1>4 and <1>5.

:::

:::

::: pf-step

This is the Bose distribution.


::: pf-proof

The right-hand side in step <1>6 is the Bose--Einstein occupation factor
$$
n_B(\xi)
=
\frac1{e^{\beta\xi}-1}.
$$

:::

:::

::: pf-step

In the fermionic case,
$$
g_F(z)
=
\frac{\beta}{e^{\beta z}+1}
$$
has simple poles at
$$
z=i\omega_n
=
i(2n+1)\pi T,
\qquad
n\in\ZZ,
$$
and each pole has residue $-1$.


::: pf-proof

The poles satisfy
$$
e^{\beta z}=-1,
$$
so
$$
\beta z=(2n+1)\pi i.
$$
At such a pole $z_n$,
$$
\operatorname{Res}_{z=z_n}g_F(z)
=
\frac{\beta}{\beta e^{\beta z_n}}
=
\frac{\beta}{-\beta}
=
-1.
$$

:::

:::

::: pf-step

Define
$$
F_F(z)
=
g_F(z)h(-iz)
=
-\frac{1}{(e^{\beta z}+1)(z-\xi)}.
$$
At each fermionic Matsubara pole,
$$
\operatorname{Res}_{z=i\omega_n}F_F(z)
=
\frac{T}{i\omega_n-\xi}.
$$


::: pf-proof

As before,
$$
h(-iz)
=
-\frac{T}{z-\xi}.
$$
By step <1>8, the residue of $g_F$ at $i\omega_n$ is $-1$. Hence
$$
\operatorname{Res}_{z=i\omega_n}F_F(z)
=
(-1)
\left(
-\frac{T}{i\omega_n-\xi}
\right)
=
\frac{T}{i\omega_n-\xi}.
$$

:::

:::

::: pf-step

The remaining pole of $F_F$ is at $z=\xi$, with residue
$$
\operatorname{Res}_{z=\xi}F_F(z)
=
-\frac{1}{e^{\beta\xi}+1}.
$$


::: pf-proof

Only the factor $z-\xi$ vanishes at $z=\xi$, so
$$
\operatorname{Res}_{z=\xi}F_F(z)
=
\lim_{z\to\xi}(z-\xi)F_F(z)
=
-\frac{1}{e^{\beta\xi}+1}.
$$

:::

:::

::: pf-step

Under the same contour prescription,
$$
\sum_{n\in\ZZ}
\frac{T}{i\omega_n-\xi}
=
-\operatorname{Res}_{z=\xi}F_F(z).
$$


::: pf-proof

For each finite contour, step <1>9 identifies the enclosed fermionic
Matsubara residues with the corresponding finite sum. Inflate and reverse the
contour as in step <1>5. Under the prescribed regularization, the outer
contribution is discarded and the remaining contour has negative orientation
around $z=\xi$.

:::

:::

::: pf-step

Therefore
$$
\boxed{
T
\sum_{n\in\ZZ}
\frac{1}{i\omega_n-\xi}
=
\frac{1}{e^{\beta\xi}+1}.
}
$$


::: pf-proof

Combine steps <1>10 and <1>11.

:::

:::

::: pf-step

This is the Fermi distribution.


::: pf-proof

The right-hand side in step <1>12 is the Fermi--Dirac occupation factor
$$
n_F(\xi)
=
\frac1{e^{\beta\xi}+1}.
$$

:::

:::

::: pf-qed

Steps <1>1--<1>7 establish the bosonic formula, and steps <1>8--<1>13
establish the fermionic formula.

:::

:::
