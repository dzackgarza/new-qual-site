---
schema: qual/card@1
id: P-APAS04M
kind: problem
title: Invariants of the order-four rotation; Molien series and Cohen–Macaulay generators
classification:
  areas:
  - applied-algebra
  topics:
  - Invariant Theory
  - Commutative Algebra
relations: []
review: draft
audit:
- event: solution-written
  by: Codex 5.3 Spark Extra High
  date: 2026-08-30
---

::: problem
Let
\[
A=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
\]

(a) Show that $A$ generates a cyclic group $G$ of order $4$.
Show that if $f\in\mathbb{C}[x,y]^G$, then $f$ can have no monomials of odd degree.

(b) Use Molien's Theorem to show that the Hilbert series of $G$ is
\[
\phi_G(z)=\frac{1+z^4}{(1-z^2)(1-z^4)}.
\]

(c) Show that $\mathbb{C}[x,y]^G$ is Cohen–Macaulay by explicitly finding the generators and separators for $\mathbb{C}[x,y]^G$.
:::

::: solution
**Goal:** Analyze the ring of invariants of the order-4 rotation.

<1>1. Generate the action and part (a):
    ::: {.proof}
    <2>1. $G=\langle A\rangle$ with
        $$A=\begin{pmatrix}0&-1\\ 1&0\end{pmatrix},\qquad A^4=I,$$
        so $|G|=4$ and
        $$A(x,y)=(-y,x).$$
    <2>2. For a monomial $x^iy^j$,
        $$A\cdot x^iy^j=(-y)^i x^j=x^j y^i(-1)^i.$$
    <2>3. The element $A^2=-I$ sends $x^iy^j\mapsto(-1)^{i+j}x^iy^j$.
    <2>4. Invariance under $A^2$ therefore forces $i+j$ even, so no invariant monomial has odd total degree. Hence part (a).

:::
<1>2. Compute the Hilbert series (part (b)):
    ::: {.proof}
    <2>1. Molien gives
        $$\phi_G(z)=\frac1{4}\sum_{g\in G}\frac{1}{\det(I-zg)}.$$
    <2>2. The four determinants are:
        $$\det(I-zI)= (1-z)^2,$$
        $$\det(I-zA)=1+z^2,$$
        $$\det(I-zA^2)=(1+z)^2,$$
        $$\det(I-zA^3)=1+z^2.$$
    <2>3. Therefore
        $$\phi_G(z)=\frac14\left(\frac{1}{(1-z)^2}+\frac{2}{1+z^2}+\frac{1}{(1+z)^2}\right)
        =\frac{1+z^4}{(1-z^2)(1-z^4)}.$$

:::
<1>3. Part (c), Cohen–Macaulay structure:
    ::: {.proof}
    <2>1. Use coordinates
        $$u=x+iy,\qquad v=x-iy.$$
        Then
        $$A\cdot u = i u,\qquad A\cdot v = -i v.$$
    <2>2. A monomial $u^av^b$ is invariant iff $a-b\equiv0\pmod4$.
    <2>3. Put
        $$p=u^4=(x+iy)^4,\qquad q=v^4=(x-iy)^4,\qquad r=uv=x^2+y^2.$$
        Then every invariant is a polynomial in $p,q,r$ with relation
        $$pq=r^4,$$
        so
        $$\mathbb C[x,y]^G\cong \mathbb C[p,q,r]/(pq-r^4).$$
    <2>4. Set $s=p+q$ and $t=p$. Over $S=\mathbb C[r,s]$, we have
        $$t^2-st+r^4=0.$$
    <2>5. So every invariant has a unique decomposition
        $$a(r,s)+t\,b(r,s),\qquad a,b\in\mathbb C[r,s],$$
        and hence
        $$\mathbb C[x,y]^G=\mathbb C[r,s]\oplus t\,\mathbb C[r,s].$$
    <2>6. Therefore $\mathbb C[x,y]^G$ is Cohen–Macaulay, with homogeneous system of parameters
        $r$ (degree $2$), $s$ (degree $4$), and separators $\{1,t\}$.

:::
<1>4. Conclusion: All requested properties hold, and the stated Hilbert series is proved. Q.E.D.
:::
