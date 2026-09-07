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
(a) Give an example of two finitely generated $\mathbb{Z}$-modules $M$ and $N$ such that $M$, $N$ are not isomorphic (as $\mathbb{Z}$-modules) but $\mathbb{Q} \otimes_\mathbb{Z} M \cong \mathbb{Q} \otimes_\mathbb{Z} N$ (as $\mathbb{Q}$-modules).

(b) Let $M$ be a finitely generated $\mathbb{R}[x]$-module, described using the classification of finitely generated modules over a PID. Give a similar description of $\mathbb{C}[x] \otimes_{\mathbb{R}[x]} M$ as a $\mathbb{C}[x]$-module.

(c) Show that if $M$ and $N$ are two finitely generated $\mathbb{R}[x]$-modules, and $\mathbb{C}[x] \otimes_{\mathbb{R}[x]} M \cong \mathbb{C}[x] \otimes_{\mathbb{R}[x]} N$ (as $\mathbb{C}[x]$-modules), then $M \cong N$ (as $\mathbb{R}[x]$-modules).
:::

::: {.solution}
<1>1. Part (a) holds with
\[
M=\mathbb Z,
\qquad
N=\mathbb Z\oplus\mathbb Z/2\mathbb Z.
\]
::: {.proof}
The two modules are not isomorphic because $N$ contains a nonzero element of order $2$, whereas $M$ is torsion-free.
On the other hand,
\[
\mathbb Q\otimes_{\mathbb Z}\mathbb Z\cong\mathbb Q,
\]
while
\[
\mathbb Q\otimes_{\mathbb Z}\mathbb Z/2\mathbb Z=0.
\]
Indeed, if $\bar1$ denotes the generator of $\mathbb Z/2\mathbb Z$, then
\[
1\otimes\bar1
=\frac12\otimes 2\bar1
=0,
\]
and hence every pure tensor vanishes.
Therefore
\[
\mathbb Q\otimes_{\mathbb Z}N
\cong
\mathbb Q\oplus0
\cong\mathbb Q
\cong
\mathbb Q\otimes_{\mathbb Z}M.
\]
:::

<1>2. Complexification is obtained from the real elementary-divisor decomposition by splitting each irreducible real quadratic into its two conjugate linear factors.
::: {.proof}
The ring $\mathbb R[x]$ is a PID.
Thus the structure theorem gives an elementary-divisor decomposition
\[
M\cong \mathbb R[x]^r
\oplus
\bigoplus_{a\in\mathbb R}\bigoplus_{e\ge1}
\left(\mathbb R[x]/((x-a)^e)\right)^{m_{a,e}}
\oplus
\bigoplus_{z\in S}\bigoplus_{e\ge1}
\left(\mathbb R[x]/(q_z(x)^e)\right)^{n_{z,e}},
\]
where only finitely many multiplicities are nonzero, $S$ contains one representative from each conjugate pair of nonreal complex numbers, and
\[
q_z(x):=(x-z)(x-\bar z)
=x^2-2\operatorname{Re}(z)x+|z|^2
\in\mathbb R[x].
\]
These are exactly the monic irreducible polynomials over $\mathbb R$: the linear factors and the quadratics $q_z$.

For every $f\in\mathbb R[x]$,
\[
\mathbb C[x]\otimes_{\mathbb R[x]}\mathbb R[x]/(f)
\cong
\mathbb C[x]/(f).
\]
Also
\[
\mathbb C[x]\otimes_{\mathbb R[x]}\mathbb R[x]^r
\cong\mathbb C[x]^r.
\]
Hence the real linear blocks remain
\[
\mathbb C[x]/((x-a)^e).
\]
For a nonreal $z$, the ideals
\[
((x-z)^e)
\quad\text{and}\quad
((x-\bar z)^e)
\]
are comaximal in $\mathbb C[x]$, and
\[
q_z(x)^e=(x-z)^e(x-\bar z)^e.
\]
The Chinese remainder theorem therefore gives
\[
\mathbb C[x]/(q_z^e)
\cong
\mathbb C[x]/((x-z)^e)
\oplus
\mathbb C[x]/((x-\bar z)^e).
\]
Consequently
\[
\mathbb C[x]\otimes_{\mathbb R[x]}M
\]
has free rank $r$, the same elementary divisors $(x-a)^e$ with multiplicities $m_{a,e}$ for real $a$, and for each nonreal conjugate pair $\{z,\bar z\}$ it has both elementary divisors $(x-z)^e$ and $(x-\bar z)^e$, each with multiplicity $n_{z,e}$.
:::

<1>3. The isomorphism type of a finitely generated $\mathbb R[x]$-module is determined by its complexification.
::: {.proof}
Suppose
\[
\mathbb C[x]\otimes_{\mathbb R[x]}M
\cong
\mathbb C[x]\otimes_{\mathbb R[x]}N.
\]
Since $\mathbb C[x]$ is a PID, the structure theorem over $\mathbb C[x]$ implies that the two complexified modules have the same free rank and exactly the same elementary divisors with the same multiplicities.

By <1>2, the real elementary-divisor data can be recovered uniquely from this complex data.
For each real $a$, every block $(x-a)^e$ comes from the identical real block, so its multiplicity is read off directly.
For each nonreal $z$, the complexification of a real $q_z^e$-block contributes exactly one $(x-z)^e$-block and one $(x-\bar z)^e$-block.
Thus the common multiplicity of the conjugate pair recovers the multiplicity of the real irreducible block
\[
q_z(x)^e=((x-z)(x-\bar z))^e.
\]
The free rank is also unchanged by scalar extension.

Therefore $M$ and $N$ have the same free rank and the same elementary divisors over $\mathbb R[x]$, with the same multiplicities.
The structure theorem for finitely generated modules over the PID $\mathbb R[x]$ then yields
\[
M\cong N.
\]
:::
:::
