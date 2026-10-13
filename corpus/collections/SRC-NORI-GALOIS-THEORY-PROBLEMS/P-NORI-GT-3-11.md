---
schema: qual/card@1
id: P-NORI-GT-3-11
kind: problem
title: Quartics over $\mathbb Q$ with a quadratic subfield have no cubic factor mod odd primes
classification:
  areas: [algebra]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against problem 3.11 of the retained Nori Galois Theory Problems PDF.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Rewrote the garbled ring R and hint formulas against Problem 3.11 on pp. 2-3 of the Nori Galois Theory Problems PDF, stated the setup of Problems 3.9-3.10, moved the source hint to a hint block, and noted the sign condition in R.
---

::: {.problem}
Let $E = \mathbb{Q}(\theta)$ be a degree four extension of $\mathbb{Q}$ that contains a quadratic extension of $\mathbb{Q}$, and let $f$ be the monic minimal polynomial of $\theta$, written (by Problem 3.10) as $f = Q^2 - cP^2$ where $c \in \mathbb{Q}$ and $P, Q \in \mathbb{Q}[X]$ with $Q$ monic of degree two and $\deg(P) < 2$.
Assume that $f \in \mathbb{Z}[X]$.
Prove that we may choose $P, Q, c$ satisfying

(i) $c$ is a square-free integer, and

(ii) the coefficients of $P$ and $Q$ lie in $R = \{\frac{m}{2^n} : m \geq 0, n \in \mathbb{Z}\}$.

Deduce that if $p$ is an odd prime, then $f$ modulo $p$, i.e. its image $\overline{f} \in \mathbb{F}_p[X]$ does not have an irreducible factor of degree $3$.

(this was an example I gave on Wednesday first week (without a proof) of a degree four extension of $\mathbb{Q}$ that does not contain a quadratic extension)
:::

::: {.hint}
Hint for part (ii).
If $Q(X) = X^2 + uX + v$, on examining the coefficient of $X^3$ in $f$, we see that $2u \in \mathbb{Z}$.
Thus $u \in R$.
Now $f \in \mathbb{Z}[X] \subset R[X]$.
It follows that $f(X - \frac{u}{2}) \in R[X]$.
We put $\widehat{f}(X) = f(X - \frac{u}{2})$, $\widehat{Q}(X) = Q(X - \frac{u}{2})$, $\widehat{P}(X) = P(X - \frac{u}{2})$.
We observe $\widehat{f} = \widehat{Q}^2 - c\widehat{P}^2$.
Note that $\widehat{Q}(X) = X^2 + \widehat{Q}(0)$.

Case 1: $\widehat{Q}(0) \in R$.
It follows that $\widehat{Q} \in R[X]$.
Also $c\widehat{P}^2 = \widehat{Q}^2 - \widehat{f} \in R[X]$.
Because $c$ is a square-free integer, it follows that $\widehat{P}^2 \in R[X]$.
By examining the leading coefficient and constant coefficient of $\widehat{P}^2$, we see that $\widehat{P}$ itself belongs to $R[X]$.
It follows that $P, Q$ belong to $R[X]$, because $P(X) = \widehat{P}(X + \frac{u}{2})$ and $Q(X) = \widehat{Q}(X + \frac{u}{2})$.

Case 2: $\widehat{Q}(0) \notin R$.
In which case, $\widehat{Q}(0) = \frac{a}{b}$ where $a, b \in \mathbb{Z}$, and we have an odd prime $p$ that does not divide $a$, but divides $b$.
Let $k$ be the highest power of $p$ that divides $b$.
Let $\widehat{P} = r_1 X + r_0$ and let $v_1$ and $v_0$ be the highest powers of $p$ that divide the denominator of $r_1$ and $r_0$ (when expressed as reduced fractions).
The equation $\widehat{f}(0) = \widehat{Q}(0)^2 - c\widehat{P}(0)^2$ shows that $p$ does not divide $c$, and also that $k = 2v_0$.
(Here we are using once again the squarefree assumption on $c$).
Examining the degree two coefficient of $f$, we see that $k = v_1$.
Examining the degree one coefficient of $f$, we see that the highest power of $p$ that divides it is $v_0 + v_1$, and that is impossible because $f \in R[X]$.
Thus case 2 does not occur.
:::

::: {.remark}
The source defines $R = \{\frac{m}{2^n} : m \geq 0, n \in \mathbb{Z}\}$, which is not closed under negation; the hint uses $R$ as the ring $\mathbb{Z}[\frac{1}{2}] = \{\frac{m}{2^n} : m \in \mathbb{Z}, n \geq 0\}$ (for instance $f = X^4 - 2X^3 + X^2 - 2 = (X^2 - X)^2 - 2 \cdot 1^2$ is irreducible with $\mathbb{Q}(\sqrt{2}) \subset \mathbb{Q}(\theta)$, and every admissible $Q = X^2 + uX + v$ has $2u = -2$, so $u = -1$ is not in $R$ as printed).
:::

::: {.solution}
The source hint uses
$$
R=\ZZ\left[\frac12\right]
=\left\{\frac{m}{2^n}:m\in\ZZ,\ n\ge0\right\}.
$$
This is the intended meaning of $R$; the literal set with $m\ge0$ printed in the source is not a ring and cannot contain negative coefficients.

Let
$$
\QQ\subset K\subset E=\QQ(\theta)
$$
be the given quadratic subfield.

<1>1. There is a squarefree integer $c$ such that
$$
K=\QQ(\sqrt c).
$$

::: {.proof}
Since $[K:\QQ]=2$ and the characteristic is not $2$, write
$$
K=\QQ(\sqrt d)
$$
for some nonsquare $d\in\QQ^*$. Every nonzero rational number has, modulo multiplication by a rational square, a unique squarefree integer representative up to the usual sign convention: write each prime exponent in the factorization of $d$ modulo $2$. Thus
$$
d=c r^2
$$
for some squarefree integer $c$ and $r\in\QQ^*$. Then
$$
\QQ(\sqrt d)=\QQ(r\sqrt c)=\QQ(\sqrt c).
$$
:::

<1>2. Let
$$
h(X)=X^2+aX+b\in K[X]
$$
be the monic minimal polynomial of $\theta$ over $K$. Then the minimal polynomial $f$ of $\theta$ over $\QQ$ is
$$
f=h\,\sigma(h),
$$
where $\sigma$ is the nontrivial automorphism of $K/\QQ$.

::: {.proof}
By the tower law,
$$
[E:K]=2,
$$
so $h$ has degree $2$. The product $h\sigma(h)$ is fixed coefficientwise by $\sigma$, hence belongs to $\QQ[X]$. It is monic of degree $4$ and vanishes at $\theta$ because $h(\theta)=0$. The monic minimal polynomial $f$ also has degree $4$, since $[E:\QQ]=4$. Therefore
$$
f=h\sigma(h).
$$
:::

<1>3. The coefficients $a,b\in K$ are algebraic integers.

::: {.proof}
The element $\theta$ is an algebraic integer because its minimal polynomial
$$
f\in\ZZ[X]
$$
is monic. Let $\theta'$ be the second root of the quadratic $h$. Since
$$
f=h\sigma(h),
$$
the element $\theta'$ is also a root of the monic integral polynomial $f$, hence is an algebraic integer. From
$$
h(X)=(X-\theta)(X-\theta')
$$
one gets
$$
a=-(\theta+\theta'),
\qquad
b=\theta\theta'.
$$
Sums and products of algebraic integers are algebraic integers.
:::

<1>4. If
$$
\alpha=r+s\sqrt c\in K
$$
is an algebraic integer, then
$$
r\in R.
$$

::: {.proof}
The conjugate
$$
\sigma(\alpha)=r-s\sqrt c
$$
is also an algebraic integer. Hence the trace
$$
\alpha+\sigma(\alpha)=2r
$$
is both a rational number and an algebraic integer. The only rational algebraic integers are the integers, so
$$
2r\in\ZZ.
$$
Therefore $r\in\frac12\ZZ\subset R$.
:::

<1>5. Under the hypotheses of step <1>4,
$$
s\in R.
$$

::: {.proof}
The norm
$$
\alpha\sigma(\alpha)=r^2-cs^2
$$
is likewise a rational algebraic integer, hence an integer. Together with $2r\in\ZZ$, this gives
$$
4cs^2
=(2r)^2-4(r^2-cs^2)
\in\ZZ.
$$
Write $s=A/B$ in lowest terms with $A,B\in\ZZ$ and $B>0$. Suppose an odd prime $\ell$ divides $B$. Then
$$
v_\ell(s)<0.
$$
Because $c$ is squarefree,
$$
v_\ell(c)\in\{0,1\},
$$
and because $\ell$ is odd,
$$
v_\ell(4)=0.
$$
Thus
$$
v_\ell(4cs^2)
=v_\ell(c)+2v_\ell(s)
<0,
$$
contradicting $4cs^2\in\ZZ$. Hence no odd prime divides $B$, so $B$ is a power of $2$ and $s\in R$.
:::

<1>6. Consequently every algebraic integer in $K$ belongs to
$$
R+R\sqrt c.
$$
In particular there exist $a_0,a_1,b_0,b_1\in R$ such that
$$
a=a_0+a_1\sqrt c,
\qquad
b=b_0+b_1\sqrt c.
$$

::: {.proof}
Apply steps <1>4--<1>5 first to an arbitrary algebraic integer of $K$, and then specifically to $a$ and $b$, which are algebraic integers by step <1>3.
:::

<1>7. Define
$$
Q(X)=X^2+a_0X+b_0,
\qquad
P(X)=a_1X+b_1.
$$
Then
$$
Q,P\in R[X],
\qquad
Q\text{ is monic of degree }2,
\qquad
\deg P<2,
$$
and
$$
h=Q+\sqrt c\,P.
$$

::: {.proof}
This follows immediately from the decompositions in step <1>6.
:::

<1>8. The integral polynomial $f$ has the representation
$$
\boxed{f=Q^2-cP^2}
$$
with $c$ squarefree and $P,Q\in R[X]$ as required.

::: {.proof}
The nontrivial automorphism of $K/\QQ$ sends
$$
\sqrt c\longmapsto-\sqrt c.
$$
Thus step <1>2 and step <1>7 give
$$
\begin{aligned}
f
&=h\sigma(h)\\
&=(Q+\sqrt c\,P)(Q-\sqrt c\,P)\\
&=Q^2-cP^2.
\end{aligned}
$$
Step <1>1 makes $c$ squarefree, and step <1>7 gives the dyadic coefficient condition.
:::

<1>9. Let $p$ be an odd prime. Reduction modulo $p$ defines a ring homomorphism
$$
R=\ZZ[1/2]\longrightarrow\FF_p.
$$

::: {.proof}
Since $p\ne2$, the class of $2$ is invertible in $\FF_p$. Therefore every fraction whose denominator is a power of $2$ has a well-defined reduction modulo $p$.
:::

<1>10. Reducing step <1>8 modulo $p$ gives
$$
\overline f
=\overline Q^2-\overline c\,\overline P^2
$$
in $\FF_p[X]$, where $\overline Q$ remains monic of degree $2$ and
$$
\deg\overline P<2.
$$

::: {.proof}
Apply the homomorphism from step <1>9 coefficientwise. The leading coefficient of $Q$ is $1$, so it remains $1$ after reduction and the degree remains $2$. Reduction cannot increase the degree of $P$.
:::

<1>11. The polynomial $\overline f$ has no irreducible factor of degree $3$.

::: {.proof}
Suppose an irreducible monic cubic $g\in\FF_p[X]$ divided $\overline f$. The first assertion of Problem 3.9 applies to the representation in step <1>10 and says that every irreducible monic divisor of degree at least $3$ must equal the entire quartic. Thus
$$
g=\overline f.
$$
But $\deg g=3$ while $\overline f$ is monic of degree $4$, a contradiction.
:::

<1>12. Q.E.D.

::: {.proof}
Steps <1>1--<1>8 prove conditions (i)--(ii), interpreted with the intended ring $R=\ZZ[1/2]$, and steps <1>9--<1>11 prove the asserted absence of cubic irreducible factors modulo every odd prime.
:::
:::
