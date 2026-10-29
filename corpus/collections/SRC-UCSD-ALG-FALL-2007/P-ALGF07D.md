---
schema: qual/card@1
id: P-ALGF07D
kind: problem
title: "Finitely generated modules over Z and scalar extension from R[x] to C[x]"
classification:
  areas:
  - algebra
  topics:
  - Module Theory
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Checked against Question 4 of the official UCSD Algebra Qualifying Examination, Fall 2007. Parts (b) and (c) were mistranscribed locally as statements about R-modules and multivariable polynomial rings; the source instead uses finitely generated R[x]-modules and scalar extension C[x] tensor_{R[x]} (-), which has been restored.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-07
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-07
  note: Verified torsion loss after tensoring with Q, the elementary-divisor decomposition after complexification, and recovery of real elementary divisors from conjugate pairs of complex factors.
---

::: {.problem}
(a) Give an example of two finitely generated $\ZZ$-modules $M$ and $N$ such that $M$, $N$ are not isomorphic (as $\ZZ$-modules) but $\QQ \otimes_\ZZ M \cong \QQ \otimes_\ZZ N$ (as $\QQ$-modules).

(b) Let $M$ be a finitely generated $\RR[x]$-module, described using the classification of finitely generated modules over a PID. Give a similar description of $\CC[x] \otimes_{\RR[x]} M$ as a $\CC[x]$-module.

(c) Show that if $M$ and $N$ are two finitely generated $\RR[x]$-modules, and $\CC[x] \otimes_{\RR[x]} M \cong \CC[x] \otimes_{\RR[x]} N$ (as $\CC[x]$-modules), then $M \cong N$ (as $\RR[x]$-modules).
:::

::: {.solution}

::: pf

::: pf-step
Part (a) holds with
$$
M=\ZZ,
\qquad
N=\ZZ\oplus\ZZ/2\ZZ.
$$

::: pf-proof
The two modules are not isomorphic because $N$ contains a nonzero element of order $2$, whereas $M$ is torsion-free.
On the other hand,
$$
\QQ\otimes_{\ZZ}\ZZ\cong\QQ,
$$
while
$$
\QQ\otimes_{\ZZ}\ZZ/2\ZZ=0.
$$
Indeed, if $\bar1$ denotes the generator of $\ZZ/2\ZZ$, then
$$
1\otimes\bar1
=\frac12\otimes 2\bar1
=0,
$$
and hence every pure tensor vanishes.
Therefore
$$
\QQ\otimes_{\ZZ}N
\cong
\QQ\oplus0
\cong\QQ
\cong
\QQ\otimes_{\ZZ}M.
$$
:::

:::

::: {.pf-step #complexification-decomposition}
Complexification is obtained from the real elementary-divisor decomposition by splitting each irreducible real quadratic into its two conjugate linear factors.

::: pf-proof
The ring $\RR[x]$ is a PID.
Thus the structure theorem gives an elementary-divisor decomposition
$$
M\cong \RR[x]^r
\oplus
\bigoplus_{a\in\RR}\bigoplus_{e\ge1}
\left(\RR[x]/((x-a)^e)\right)^{m_{a,e}}
\oplus
\bigoplus_{z\in S}\bigoplus_{e\ge1}
\left(\RR[x]/(q_z(x)^e)\right)^{n_{z,e}},
$$
where only finitely many multiplicities are nonzero, $S$ contains one representative from each conjugate pair of nonreal complex numbers, and
$$
q_z(x):=(x-z)(x-\bar z)
=x^2-2\operatorname{Re}(z)x+|z|^2
\in\RR[x].
$$
These are exactly the monic irreducible polynomials over $\RR$: the linear factors and the quadratics $q_z$.

For every $f\in\RR[x]$,
$$
\CC[x]\otimes_{\RR[x]}\RR[x]/(f)
\cong
\CC[x]/(f).
$$
Also
$$
\CC[x]\otimes_{\RR[x]}\RR[x]^r
\cong\CC[x]^r.
$$
Hence the real linear blocks remain
$$
\CC[x]/((x-a)^e).
$$
For a nonreal $z$, the ideals
$$
((x-z)^e)
\quad\text{and}\quad
((x-\bar z)^e)
$$
are comaximal in $\CC[x]$, and
$$
q_z(x)^e=(x-z)^e(x-\bar z)^e.
$$
The Chinese remainder theorem therefore gives
$$
\CC[x]/(q_z^e)
\cong
\CC[x]/((x-z)^e)
\oplus
\CC[x]/((x-\bar z)^e).
$$
Consequently
$$
\CC[x]\otimes_{\RR[x]}M
$$
has free rank $r$, the same elementary divisors $(x-a)^e$ with multiplicities $m_{a,e}$ for real $a$, and for each nonreal conjugate pair $\{z,\bar z\}$ it has both elementary divisors $(x-z)^e$ and $(x-\bar z)^e$, each with multiplicity $n_{z,e}$.
:::

:::

::: pf-step
The isomorphism type of a finitely generated $\RR[x]$-module is determined by its complexification.

::: pf-proof
Suppose
$$
\CC[x]\otimes_{\RR[x]}M
\cong
\CC[x]\otimes_{\RR[x]}N.
$$
Since $\CC[x]$ is a PID, the structure theorem over $\CC[x]$ implies that the two complexified modules have the same free rank and exactly the same elementary divisors with the same multiplicities.

By step [](#complexification-decomposition){.pf-ref}, the real elementary-divisor data can be recovered uniquely from this complex data.
For each real $a$, every block $(x-a)^e$ comes from the identical real block, so its multiplicity is read off directly.
For each nonreal $z$, the complexification of a real $q_z^e$-block contributes exactly one $(x-z)^e$-block and one $(x-\bar z)^e$-block.
Thus the common multiplicity of the conjugate pair recovers the multiplicity of the real irreducible block
$$
q_z(x)^e=((x-z)(x-\bar z))^e.
$$
The free rank is also unchanged by scalar extension.

Therefore $M$ and $N$ have the same free rank and the same elementary divisors over $\RR[x]$, with the same multiplicities.
The structure theorem for finitely generated modules over the PID $\RR[x]$ then yields
$$
M\cong N.
$$
:::

:::

:::
:::
