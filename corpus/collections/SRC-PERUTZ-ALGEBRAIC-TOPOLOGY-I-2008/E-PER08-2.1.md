---
schema: qual/card@1
id: E-PER08-2.1
kind: problem
title: Iwasawa decomposition and the topology of SL_2(R)
classification:
  areas: [topology]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Exercise 2.1 of the vendored Perutz Fall 2008 Algebraic Topology I notes.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-13
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Verified the explicit KL formulas, uniqueness, coordinate homeomorphism, strong deformation retraction, and fundamental-group conclusion.
---

::: {.problem}
Show that every matrix $A\in \operatorname{SL}_2(\mathbb R)$ can be written uniquely as a product $KL$, with $K\in\operatorname{SO}(2)$ and $L$ lower triangular with positive diagonal entries.

Use this to construct:

1. a deformation retraction of $\operatorname{SL}_2(\mathbb R)$, topologized as a subspace of $\mathbb R^4$, onto $\operatorname{SO}(2)$; and

2. a homeomorphism
   \[
   S^1\times(0,\infty)\times\mathbb R\longrightarrow \operatorname{SL}_2(\mathbb R).
   \]

Deduce that $\operatorname{SL}_2(\mathbb R)$ is path connected and that
\[
\pi_1(\operatorname{SL}_2(\mathbb R))\cong\mathbb Z.
\]
:::

::: {.solution}
Write
\[
A=\begin{pmatrix}a&b\\ c&d\end{pmatrix}\in\operatorname{SL}_2(\mathbb R),
\qquad
ad-bc=1.
\]

<1>1. Every $A$ has the required factorization.
::: {.proof}
The second column $(b,d)^T$ is nonzero, so set
\[
r=\sqrt{b^2+d^2}>0
\]
and define
\[
K=\frac1r
\begin{pmatrix}
d&b\\
-b&d
\end{pmatrix}.
\]
Its columns are orthonormal and
\[
\det K=\frac{d^2+b^2}{r^2}=1,
\]
so $K\in\operatorname{SO}(2)$.

Now compute
\[
L=K^TA
=\frac1r
\begin{pmatrix}
d&-b\\
b&d
\end{pmatrix}
\begin{pmatrix}
a&b\\
c&d
\end{pmatrix}.
\]
Using $ad-bc=1$ gives
\[
L=
\begin{pmatrix}
r^{-1}&0\\[2mm]
\dfrac{ab+cd}{r}&r
\end{pmatrix}.
\]
Thus $L$ is lower triangular and both diagonal entries are positive. Since $L=K^{-1}A$, we have
\[
A=KL.
\]
:::

<1>2. The factorization is unique.
::: {.proof}
Suppose
\[
A=KL,
\qquad
K\in\operatorname{SO}(2),
\qquad
L=\begin{pmatrix}\lambda&0\\ s&\mu\end{pmatrix},
\]
with $\lambda,\mu>0$.

The second column of $A$ is
\[
\mu k_2,
\]
where $k_2$ is the second column of $K$. Since $\lVert k_2\rVert=1$ and $\mu>0$,
\[
\mu=\sqrt{b^2+d^2}=r
\]
and
\[
k_2=\frac1r\binom bd.
\]
There is exactly one positively oriented orthonormal first column compatible with this $k_2$, namely
\[
k_1=\frac1r\binom d{-b}.
\]
Hence $K$ is forced to be the matrix in <1>1, and then
\[
L=K^{-1}A
\]
is forced as well. Therefore the factorization is unique.
:::

<1>3. The factorization gives a homeomorphism
\[
\operatorname{SO}(2)\times(0,\infty)\times\mathbb R
\xrightarrow{\cong}
\operatorname{SL}_2(\mathbb R).
\]
::: {.proof}
Every lower-triangular matrix in $\operatorname{SL}_2(\mathbb R)$ with positive diagonal has a unique form
\[
L(r,s)=
\begin{pmatrix}
r^{-1}&0\\
s&r
\end{pmatrix},
\qquad
r>0,\ s\in\mathbb R.
\]
Define
\[
\Phi(K,r,s)=K L(r,s).
\]
By <1>1 and <1>2, $\Phi$ is bijective.

It is continuous because matrix multiplication is continuous. Its inverse is also continuous: for
\[
A=\begin{pmatrix}a&b\\c&d\end{pmatrix},
\]
the inverse coordinates are
\[
r=\sqrt{b^2+d^2},
\qquad
s=\frac{ab+cd}{r},
\qquad
K=\frac1r\begin{pmatrix}d&b\\-b&d\end{pmatrix}.
\]
The denominator $r$ never vanishes on $\operatorname{SL}_2(\mathbb R)$, so these formulas are continuous. Thus $\Phi$ is a homeomorphism.

Finally,
\[
S^1\xrightarrow{\cong}\operatorname{SO}(2),
\qquad
(x,y)\longmapsto
\begin{pmatrix}x&y\\-y&x\end{pmatrix}
\]
is a homeomorphism. Composing with $\Phi$ gives
\[
S^1\times(0,\infty)\times\mathbb R
\xrightarrow{\cong}
\operatorname{SL}_2(\mathbb R).
\]
:::

<1>4. There is a strong deformation retraction onto $\operatorname{SO}(2)$.
::: {.proof}
For $A=K L(r,s)$ in the unique coordinates above and $u\in[0,1]$, set
\[
r_u=(1-u)r+u>0,
\qquad
s_u=(1-u)s
\]
and define
\[
H(u,A)=K L(r_u,s_u).
\]
The coordinate homeomorphism in <1>3 shows that $H$ is continuous. At $u=0$,
\[
H(0,A)=A,
\]
and at $u=1$,
\[
H(1,A)=K.
\]
If $A\in\operatorname{SO}(2)$, uniqueness of the factorization gives $L=I$, so $(r,s)=(1,0)$ and
\[
H(u,A)=A
\]
for every $u$. Hence $H$ is a strong deformation retraction of $\operatorname{SL}_2(\mathbb R)$ onto $\operatorname{SO}(2)$.
:::

<1>5. The topological conclusions follow.
::: {.proof}
The factors
\[
S^1,\qquad(0,\infty),\qquad\mathbb R
\]
are path connected, so their product is path connected. By <1>3,
\[
\operatorname{SL}_2(\mathbb R)
\]
is path connected.

By <1>4, inclusion of $\operatorname{SO}(2)$ is a homotopy equivalence, hence
\[
\pi_1(\operatorname{SL}_2(\mathbb R))
\cong
\pi_1(\operatorname{SO}(2)).
\]
Since $\operatorname{SO}(2)\cong S^1$ and
\[
\pi_1(S^1)\cong\mathbb Z,
\]
we obtain
\[
\boxed{\pi_1(\operatorname{SL}_2(\mathbb R))\cong\mathbb Z}.
\]
:::
:::
