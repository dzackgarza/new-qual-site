---
schema: qual/card@1
id: P-UCLARA18S-11
kind: problem
title: Conformally equivalent annuli have equal moduli
classification:
  areas:
  - real-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Transcribed from the official UCLA Analysis Qualifying Exam, Spring 2018, and reconciled with the retained UCLA Analysis Qualifying Exam Solutions compendium.
---

::: {.problem}
Problem 11. For $R>1$, let
\[
A_R=\{z\in\CC:1<|z|<R\}.
\]
Assume there is a conformal (i.e. injective, holomorphic) mapping $F$ from $A_{R_1}$ onto $A_{R_2}$. Prove that $R_1=R_2$.
:::

::: {.solution}

Set
\[
L_j=\log R_j
\qquad(j=1,2)
\]
and define the vertical strips
\[
S_j
=
\{w\in\CC:0<\operatorname{Re}w<L_j\}.
\]

::: pf

::: {.pf-step #s1-1}

The exponential maps
\[
p_j:S_j\longrightarrow A_{R_j},
\qquad
p_j(w)=e^w,
\]
are universal covering maps with deck transformations
\[
w\longmapsto w+2\pi i n,
\qquad
n\in\ZZ.
\]


::: pf-proof

If
\[
w=x+iy\in S_j,
\]
then
\[
|e^w|=e^x
\]
lies strictly between \(1\) and \(R_j=e^{L_j}\), so \(p_j(S_j)=A_{R_j}\).
The strip \(S_j\) is simply connected. Two points in \(S_j\) have the same
exponential exactly when they differ by \(2\pi i n\), giving the stated deck
group.

:::

:::

::: {.pf-step #s1-2}

The biholomorphism
\[
F:A_{R_1}\to A_{R_2}
\]
lifts to a holomorphic map
\[
\widetilde F:S_1\to S_2
\]
satisfying
\[
\boxed{
e^{\widetilde F(w)}
=
F(e^w)}.
\]


::: pf-proof

The strip \(S_1\) is simply connected, and
\[
p_2:S_2\to A_{R_2}
\]
is a covering map. The covering-space lifting theorem therefore gives a
lift of
\[
F\circ p_1:S_1\to A_{R_2}
\]
after choosing one value of the lift at one base point. Since \(p_2\) is a
local biholomorphism and \(F\circ p_1\) is holomorphic, the lift is
holomorphic.

:::

:::

::: {.pf-step #s1-3}

There is an integer \(k\) such that
\[
\boxed{
\widetilde F(w+2\pi i)
=
\widetilde F(w)+2\pi i k
\qquad(w\in S_1)}.
\]


::: pf-proof

Since
\[
e^{w+2\pi i}=e^w,
\]
step [](#s1-2){.pf-ref} gives
\[
e^{\widetilde F(w+2\pi i)}
=
F(e^{w+2\pi i})
=
F(e^w)
=
e^{\widetilde F(w)}.
\]
Hence
\[
\widetilde F(w+2\pi i)-\widetilde F(w)
\in
2\pi i\ZZ.
\]
The left-hand side is continuous in \(w\), while \(2\pi i\ZZ\) is
discrete. Since \(S_1\) is connected, the integer is constant.

:::

:::

::: {.pf-step #s1-4}

In fact,
\[
\boxed{k=\pm1}.
\]


::: pf-proof

The integer \(k\) is the homomorphism induced by \(F\) on
\[
\pi_1(A_{R_1})\cong\ZZ
\longrightarrow
\pi_1(A_{R_2})\cong\ZZ.
\]
Since \(F\) is a biholomorphism, it is a homeomorphism, so its induced map on
fundamental groups is an isomorphism. The only automorphisms of
\(\ZZ\) are multiplication by \(1\) and by \(-1\).

:::

:::

::: {.pf-step #s1-5}

Write
\[
\widetilde F(w)
=
u(w)+iv(w),
\]
where \(u,v\) are real-valued. Then
\[
0<u(w)<L_2
\qquad(w\in S_1),
\]
and
\[
u(x+i(y+2\pi))
=
u(x+iy),
\]
\[
v(x+i(y+2\pi))
=
v(x+iy)+2\pi k.
\]


::: pf-proof

The image of \(\widetilde F\) lies in \(S_2\), so its real part lies between
\(0\) and \(L_2\). The two periodicity identities are the real and imaginary
parts of step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-6}

Define the vertical average
\[
m(x)
=
\frac1{2\pi}
\int_0^{2\pi}
u(x+iy)\,dy,
\qquad
0<x<L_1.
\]
Then
\[
\boxed{m'(x)=k}.
\]


::: pf-proof

The function \(\widetilde F\) is holomorphic, so the Cauchy--Riemann
equations give
\[
u_x=v_y.
\]
Differentiate under the integral:
\[
\begin{aligned}
m'(x)
&=
\frac1{2\pi}
\int_0^{2\pi}
u_x(x+iy)\,dy\\
&=
\frac1{2\pi}
\int_0^{2\pi}
v_y(x+iy)\,dy\\
&=
\frac{
v(x+2\pi i)-v(x)
}{2\pi}\\
&=
k
\end{aligned}
\]
by step [](#s1-5){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

One has
\[
\boxed{L_1\le L_2}.
\]


::: pf-proof

By step [](#s1-5){.pf-ref},
\[
0<m(x)<L_2
\]
for every \(x\in(0,L_1)\). By steps [](#s1-4){.pf-ref} and [](#s1-6){.pf-ref},
\[
|m(x_2)-m(x_1)|
=
|k|\,(x_2-x_1)
=
x_2-x_1
\]
whenever
\[
0<x_1<x_2<L_1.
\]
Since both \(m(x_1)\) and \(m(x_2)\) lie in the interval \((0,L_2)\),
\[
x_2-x_1<L_2.
\]
Let \(x_1\downarrow0\) and \(x_2\uparrow L_1\). This gives
\[
L_1\le L_2.
\]

:::

:::

::: {.pf-step #s1-8}

Applying the same argument to
\[
F^{-1}:A_{R_2}\to A_{R_1}
\]
gives
\[
\boxed{L_2\le L_1}.
\]


::: pf-proof

The inverse of a biholomorphic map is biholomorphic. Interchanging the roles
of the two annuli in steps [](#s1-1){.pf-ref} through [](#s1-7){.pf-ref} therefore yields the reverse
inequality.

:::

:::

::: {.pf-step #s1-9}

Hence
\[
L_1=L_2.
\]


::: pf-proof

Combine steps [](#s1-7){.pf-ref} and [](#s1-8){.pf-ref}.

:::

:::

::: {.pf-step #s1-10}

Therefore
\[
\boxed{R_1=R_2}.
\]


::: pf-proof

By definition,
\[
L_j=\log R_j.
\]
Step [](#s1-9){.pf-ref} gives
\[
\log R_1=\log R_2.
\]
The logarithm is injective on \((0,\infty)\), so \(R_1=R_2\).

:::

:::

::: pf-qed

Step [](#s1-10){.pf-ref} is the required conclusion.

:::

:::

:::
