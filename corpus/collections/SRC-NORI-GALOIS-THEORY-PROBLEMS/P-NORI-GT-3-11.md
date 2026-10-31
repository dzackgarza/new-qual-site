---
schema: qual/card@1
id: P-NORI-GT-3-11
kind: problem
title: Quartics over $\QQ$ with a quadratic subfield have no cubic factor mod odd primes
classification:
  areas: [algebra]
  topics:
  - Quartic Polynomials
  - Reduction Mod p
  - Quadratic Subfields
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
- event: source-checked
  by: claude-opus-5-5
  date: 2026-10-29
  note: 'The source printed R = {m/2^n : m >= 0, n in Z}, which is not a ring. The statement now defines R = {m/2^n : m in Z, n >= 0} = Z[1/2], the ring the hint uses.'
---

::: {.problem}
Let $E = \QQ(\theta)$ be a degree four extension of $\QQ$ that contains a quadratic extension of $\QQ$, and let $f$ be the monic minimal polynomial of $\theta$, written (by [[P-NORI-GT-3-10]]) as $f = Q^2 - cP^2$ where $c \in \QQ$ and $P, Q \in \QQ[X]$ with $Q$ monic of degree two and $\deg(P) < 2$.
Assume that $f \in \ZZ[X]$.
Prove that we may choose $P, Q, c$ satisfying

(i) $c$ is a square-free integer, and

(ii) the coefficients of $P$ and $Q$ lie in $R = \{\frac{m}{2^n} : m \in \ZZ, n \geq 0\}$.

Deduce that if $p$ is an odd prime, then $f$ modulo $p$, i.e. its image $\overline{f} \in \FF_p[X]$ does not have an irreducible factor of degree $3$.

(this was an example I gave on Wednesday first week (without a proof) of a degree four extension of $\QQ$ that does not contain a quadratic extension)
:::

::: {.hint}
Hint for part (ii).
If $Q(X) = X^2 + uX + v$, on examining the coefficient of $X^3$ in $f$, we see that $2u \in \ZZ$.
Thus $u \in R$.
Now $f \in \ZZ[X] \subset R[X]$.
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
In which case, $\widehat{Q}(0) = \frac{a}{b}$ where $a, b \in \ZZ$, and we have an odd prime $p$ that does not divide $a$, but divides $b$.
Let $k$ be the highest power of $p$ that divides $b$.
Let $\widehat{P} = r_1 X + r_0$ and let $v_1$ and $v_0$ be the highest powers of $p$ that divide the denominator of $r_1$ and $r_0$ (when expressed as reduced fractions).
The equation $\widehat{f}(0) = \widehat{Q}(0)^2 - c\widehat{P}(0)^2$ shows that $p$ does not divide $c$, and also that $k = 2v_0$.
(Here we are using once again the squarefree assumption on $c$).
Examining the degree two coefficient of $f$, we see that $k = v_1$.
Examining the degree one coefficient of $f$, we see that the highest power of $p$ that divides it is $v_0 + v_1$, and that is impossible because $f \in R[X]$.
Thus case 2 does not occur.
:::

::: {.solution}

Note that $R=\ZZ[1/2]$. Let
$$
\QQ\subset K\subset E=\QQ(\theta)
$$
be the given quadratic subfield.

::: pf

::: {.pf-step #s1-1}

There is a squarefree integer $c$ such that
$$
K=\QQ(\sqrt c).
$$


::: pf-proof

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

:::

::: {.pf-step #s1-2}

Let
$$
h(X)=X^2+aX+b\in K[X]
$$
be the monic minimal polynomial of $\theta$ over $K$. Then the minimal polynomial $f$ of $\theta$ over $\QQ$ is
$$
f=h\,\sigma(h),
$$
where $\sigma$ is the nontrivial automorphism of $K/\QQ$.


::: pf-proof

By the tower law,
$$
[E:K]=2,
$$
so $h$ has degree $2$. The product $h\sigma(h)$ is fixed coefficientwise by $\sigma$, hence belongs to $\QQ[X]$. It is monic of degree $4$ and vanishes at $\theta$ because $h(\theta)=0$. The monic minimal polynomial $f$ also has degree $4$, since $[E:\QQ]=4$. Therefore
$$
f=h\sigma(h).
$$

:::

:::

::: {.pf-step #s1-3}

The coefficients $a,b\in K$ are algebraic integers.


::: pf-proof

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

:::

::: {.pf-step #s1-4}

If
$$
\alpha=r+s\sqrt c\in K
$$
is an algebraic integer, then
$$
r\in R.
$$


::: pf-proof

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

:::

::: {.pf-step #s1-5}

Under the hypotheses of step [](#s1-4){.pf-ref},
$$
s\in R.
$$


::: pf-proof

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

:::

::: {.pf-step #s1-6}

Consequently every algebraic integer in $K$ belongs to
$$
R+R\sqrt c.
$$
In particular there exist $a_0,a_1,b_0,b_1\in R$ such that
$$
a=a_0+a_1\sqrt c,
\qquad
b=b_0+b_1\sqrt c.
$$


::: pf-proof

Apply steps [](#s1-4){.pf-ref} through [](#s1-5){.pf-ref} first to an arbitrary algebraic integer of $K$, and then specifically to $a$ and $b$, which are algebraic integers by step [](#s1-3){.pf-ref}.

:::

:::

::: {.pf-step #s1-7}

Define
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


::: pf-proof

This follows immediately from the decompositions in step [](#s1-6){.pf-ref}.

:::

:::

::: {.pf-step #s1-8}

The integral polynomial $f$ has the representation
$$
\boxed{f=Q^2-cP^2}
$$
with $c$ squarefree and $P,Q\in R[X]$ as required.


::: pf-proof

The nontrivial automorphism of $K/\QQ$ sends
$$
\sqrt c\longmapsto-\sqrt c.
$$
Thus step [](#s1-2){.pf-ref} and step [](#s1-7){.pf-ref} give
$$
\begin{aligned}
f
&=h\sigma(h)\\
&=(Q+\sqrt c\,P)(Q-\sqrt c\,P)\\
&=Q^2-cP^2.
\end{aligned}
$$
Step [](#s1-1){.pf-ref} makes $c$ squarefree, and step [](#s1-7){.pf-ref} gives the dyadic coefficient condition.

:::

:::

::: {.pf-step #s1-9}

Let $p$ be an odd prime. Reduction modulo $p$ defines a ring homomorphism
$$
R=\ZZ[1/2]\longrightarrow\FF_p.
$$


::: pf-proof

Since $p\ne2$, the class of $2$ is invertible in $\FF_p$. Therefore every fraction whose denominator is a power of $2$ has a well-defined reduction modulo $p$.

:::

:::

::: {.pf-step #s1-10}

Reducing step [](#s1-8){.pf-ref} modulo $p$ gives
$$
\overline f
=\overline Q^2-\overline c\,\overline P^2
$$
in $\FF_p[X]$, where $\overline Q$ remains monic of degree $2$ and
$$
\deg\overline P<2.
$$


::: pf-proof

Apply the homomorphism from step [](#s1-9){.pf-ref} coefficientwise. The leading coefficient of $Q$ is $1$, so it remains $1$ after reduction and the degree remains $2$. Reduction cannot increase the degree of $P$.

:::

:::

::: {.pf-step #s1-11}

The polynomial $\overline f$ has no irreducible factor of degree $3$.


::: pf-proof

Suppose an irreducible monic cubic $g\in\FF_p[X]$ divided $\overline f$. The first assertion of Problem 3.9 applies to the representation in step [](#s1-10){.pf-ref} and says that every irreducible monic divisor of degree at least $3$ must equal the entire quartic. Thus
$$
g=\overline f.
$$
But $\deg g=3$ while $\overline f$ is monic of degree $4$, a contradiction.

:::

:::

::: pf-qed

Steps [](#s1-1){.pf-ref} through [](#s1-8){.pf-ref} prove conditions (i)--(ii), and steps [](#s1-9){.pf-ref} through [](#s1-11){.pf-ref} prove the asserted absence of cubic irreducible factors modulo every odd prime.

:::

:::

:::
