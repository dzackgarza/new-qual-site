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
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-10
  note: Verified the invariant-ring presentation and added the missing algebraic-independence/freeness justification.
- event: solution-written
  by: claude
  date: 2026-11-19
  note: >-
    Every step now carries a pf-proof: the three containers state what their subsections do, and the 13
    leaf steps that asserted their claim with no justification each carry a sentence deriving it. The
    Goal paragraph was removed. The mathematics is unchanged: $A$ has order $4$ and $A^2=-I$, so invariant
    monomials have even total degree; Molien's formula with the four determinants gives
    $(1-z)^{-2}/4+(1+z^2)^{-1}/2+(1+z)^{-2}/4$; and in the coordinates $u=x+iy$, $v=x-iy$ the invariant
    monomials are those with $a-b$ divisible by four, which produces the presentation of the invariant
    ring. Checked against the statement on the card, from the UCSD Spring 2004 applied algebra qualifying
    exam. Nothing in the statement was changed.

---

::: {.problem}
Let
$$
A=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.
$$

(a) Show that $A$ generates a cyclic group $G$ of order $4$.
Show that if $f\in\CC[x,y]^G$, then $f$ can have no monomials of odd degree.

(b) Use Molien's Theorem to show that the Hilbert series of $G$ is
$$
\phi_G(z)=\frac{1+z^4}{(1-z^2)(1-z^4)}.
$$

(c) Show that $\CC[x,y]^G$ is Cohen–Macaulay by explicitly finding the generators and separators for $\CC[x,y]^G$.
:::

::: {.solution}

::: pf

::: pf-step
Generate the action and part (a):

::: pf-proof

::: pf-step
$G=\langle A\rangle$ with
$$A=\begin{pmatrix}0&-1\\ 1&0\end{pmatrix},\qquad A^4=I,$$
so $\cardinality{G}=4$ and
$$A(x,y)=(-y,x).$$

::: pf-proof
Direct computation gives $A^2=-I$ and $A^4=I$, and no smaller positive power is the identity, so the cyclic group generated has order $4$.
:::

:::

::: pf-step
For a monomial $x^iy^j$,
$$A\cdot x^iy^j=(-y)^i x^j=x^j y^i(-1)^i.$$

::: pf-proof
The substitution $(x,y)\mapsto(-y,x)$ replaces $x$ by $-y$ and $y$ by $x$, and a monomial is carried to the monomial displayed.
:::

:::

::: pf-step
The element $A^2=-I$ sends $x^iy^j\mapsto(-1)^{i+j}x^iy^j$.

::: pf-proof
Applying the preceding formula twice, or directly that $A^2$ sends $(x,y)$ to $(-x,-y)$.
:::

:::

::: pf-step
Invariance under $A^2$ therefore forces $i+j$ even, so no invariant monomial has odd total degree. Hence part (a).

::: pf-proof
The monomial is fixed by $A^2$ exactly when $(-1)^{i+j}=1$, that is, when $i+j$ is even.
:::

:::

:::

:::

::: pf-step
Compute the Hilbert series (part (b)):

::: pf-proof

::: pf-step
Molien gives
$$\phi_G(z)=\frac1{4}\sum_{g\in G}\frac{1}{\det(I-zg)}.$$

::: pf-proof
This is Molien's theorem for a finite group acting on a two-dimensional complex space.
:::

:::

::: pf-step
The four determinants are:
$$\det(I-zI)= (1-z)^2,$$
$$\det(I-zA)=1+z^2,$$
$$\det(I-zA^2)=(1+z)^2,$$
$$\det(I-zA^3)=1+z^2.$$

::: pf-proof
Each determinant is computed from the matrix of the corresponding element: $I$, $A$, $A^2=-I$ and $A^3=-A$.
:::

:::

::: pf-step
Therefore
$$\phi_G(z)=\frac14\left(\frac{1}{(1-z)^2}+\frac{2}{1+z^2}+\frac{1}{(1+z)^2}\right)
=\frac{1+z^4}{(1-z^2)(1-z^4)}.$$

::: pf-proof
Substituting the four determinants into Molien's formula.
:::

:::

:::

:::

::: pf-step
Part (c), Cohen–Macaulay structure:

::: pf-proof

::: pf-step
Use coordinates
$$u=x+iy,\qquad v=x-iy.$$
Then
$$A\cdot u = i u,\qquad A\cdot v = -i v.$$

::: pf-proof
Substituting $x\mapsto-y$, $y\mapsto x$ in $u=x+iy$ and $v=x-iy$ gives the two eigenvalues.
:::

:::

::: pf-step
A monomial $u^av^b$ is invariant iff $a-b\equiv0\pmod4$.

::: pf-proof
$A$ multiplies $u^av^b$ by $i^a(-i)^b=i^{a-b}$, which equals $1$ exactly when $a-b$ is divisible by four.
:::

:::

::: pf-step
Put
$$p=u^4=(x+iy)^4,\qquad q=v^4=(x-iy)^4,\qquad r=uv=x^2+y^2.$$
Then every invariant is a polynomial in $p,q,r$ with relation
$$pq=r^4,$$
so
$$\CC[x,y]^G\cong \CC[p,q,r]/(pq-r^4).$$

::: pf-proof
Each of $p,q,r$ is invariant by the preceding step, and every invariant monomial is a product of these three.
:::

:::

::: pf-step
Set $s=p+q$ and $t=p$. The elements $r=uv$ and $s=u^4+v^4$ are algebraically independent: their Jacobian determinant with respect to $u,v$ is
$$\det\begin{pmatrix}v&u\\4u^3&4v^3\end{pmatrix}=4(v^4-u^4),$$
which is not the zero polynomial. Since the ground field has characteristic $0$, any algebraic relation between $r$ and $s$ would force the Jacobian to have rank $<2$ identically. Thus $S=\CC[r,s]$ is a polynomial ring in two variables.

::: pf-proof
The substitution is injective because $r$ and $s$ are algebraically independent, so the map on polynomial rings has trivial kernel.
:::

:::

::: pf-step
In the presentation $\CC[p,q,r]/(pq-r^4)$, write $q=s-t$ and $p=t$. Then
$$t^2-st+r^4=0,$$
so
$$\CC[x,y]^G\cong S[t]/(t^2-st+r^4).$$
Because the defining polynomial is monic of degree $2$ in $t$, Euclidean division in $S[t]$ gives a unique representative
$$a(r,s)+t\,b(r,s),\qquad a,b\in S.$$
Hence
$$\CC[x,y]^G=S\oplus tS$$
as an $S$-module.

::: pf-proof
The relation $pq=r^4$ becomes the displayed equation in $s,t,r$ after substituting $p=t$ and $q=s-t$.
:::

:::

::: pf-step
Therefore $\CC[x,y]^G$ is a free module over the polynomial subring $S=\CC[r,s]$, hence Cohen–Macaulay, with homogeneous system of parameters $r$ (degree $2$), $s$ (degree $4$), and secondary invariants (the requested separators) $\{1,t\}$.

::: pf-proof
The invariant monomials with $a-b$ divisible by four reduce to the displayed basis over the polynomial subring.
:::

:::

:::

:::

::: pf-qed
Conclusion: All requested properties hold, and the stated Hilbert series is proved.
:::

:::

:::
