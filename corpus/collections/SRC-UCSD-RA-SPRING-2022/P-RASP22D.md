---
schema: qual/card@1
id: P-RASP22D
kind: problem
title: "Von Neumann's Mean Ergodic Theorem"
classification:
  areas:
  - real-analysis
  topics:
  - Real Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Problem 4 of the official UCSD Spring 2022 real-analysis qualifying exam.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: problem
Let $H$ be a Hilbert space and let $U \in L(H, H)$ be unitary, meaning $U$ is invertible and $\langle Ux, y \rangle = \langle x, U^{-1}y \rangle$ for all $x, y \in H$.

1. Let $\operatorname{Ran}(I - U)$ denote the image of $I - U$.
   Prove that $\overline{\operatorname{Ran}(I-U)}^\perp = \ker(I-U)$.

2. Set $S_n = \frac{1}{n} \sum_{j=0}^{n-1} U^j$, and let $P$ be the orthogonal projection map from $H$ to $\ker(I-U)$.
   Prove that $S_n \to P$ in the strong operator topology.
:::


::: solution
<1>1. Identify the orthogonal complement of the range.
::: proof
Let
\[
M:=\ker(I-U)=\{x:Ux=x\}.
\]
Since taking orthogonal complements is unchanged by closure,
\[
\overline{\operatorname{Ran}(I-U)}^\perp
=\operatorname{Ran}(I-U)^\perp.
\]
Now $z\in\operatorname{Ran}(I-U)^\perp$ iff
\[
0=\langle (I-U)y,z\rangle
=\langle y,z\rangle-\langle Uy,z\rangle
=\langle y,z-U^{-1}z\rangle
\]
for every $y\in H$. Hence
\[
z=U^{-1}z,
\]
equivalently $Uz=z$. Thus
\[
\boxed{\overline{\operatorname{Ran}(I-U)}^\perp=M.}
\]
Taking orthogonal complements once more gives
\[
\overline{\operatorname{Ran}(I-U)}=M^\perp.
\]
:::

<1>2. Compute the averages on the fixed-point space and on the range of $I-U$.
::: proof
If $x\in M$, then $U^jx=x$ for every $j$, so
\[
S_nx=x=Px.
\]

If $x=(I-U)y$, then
\[
\begin{aligned}
S_nx
&=\frac1n\sum_{j=0}^{n-1}U^j(I-U)y\\
&=\frac1n\sum_{j=0}^{n-1}(U^jy-U^{j+1}y)\\
&=\frac{y-U^ny}{n}.
\end{aligned}
\]
Since $U$ is unitary,
\[
\|S_nx\|
\le\frac{\|y\|+\|U^ny\|}{n}
=\frac{2\|y\|}{n}\to0.
\]
Thus $S_nx\to0=Px$ for every $x\in\operatorname{Ran}(I-U)$.
:::

<1>3. Extend the convergence to all of $M^\perp$.
::: proof
Each $S_n$ is a contraction:
\[
\|S_n\|
\le\frac1n\sum_{j=0}^{n-1}\|U^j\|=1.
\]
By Step 1, $\operatorname{Ran}(I-U)$ is dense in $M^\perp$. Let $x\in M^\perp$ and choose $x_k\in\operatorname{Ran}(I-U)$ with $x_k\to x$. Then
\[
\|S_nx\|
\le\|S_n(x-x_k)\|+\|S_nx_k\|
\le\|x-x_k\|+\|S_nx_k\|.
\]
First choose $k$ so that $\|x-x_k\|$ is small, then let $n\to\infty$ and use Step 2. Hence $S_nx\to0$ for every $x\in M^\perp$.

Finally decompose
\[
x=Px+(I-P)x,
\qquad
Px\in M,\quad (I-P)x\in M^\perp.
\]
Then
\[
S_nx=S_n(Px)+S_n((I-P)x)\to Px+0=Px.
\]
Therefore
\[
\boxed{S_n\to P\text{ in the strong operator topology}.}
\]
:::
:::
