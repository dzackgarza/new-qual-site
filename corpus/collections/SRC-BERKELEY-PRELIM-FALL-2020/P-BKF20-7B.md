---
schema: qual/card@1
id: P-BKF20-7B
kind: problem
title: Invariant complement for an operator satisfying $A^5=I$
classification:
  areas:
  - prelim
  topics:
  - Linear Algebra
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-11
- event: source-checked
  by: chatgpt
  date: 2026-09-24
  note: >-
    Independently checked the retained Fall 2020 averaging argument and
    supplied the omitted characteristic-5 counterexample: a size-2 unipotent
    Jordan block has fifth power I but its fixed line has no invariant
    complement.
- event: solution-written
  by: chatgpt
  date: 2026-09-24
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-24
  note: >-
    Checked that the averaging operator is a projection onto the fixed space,
    that its kernel is invariant in both directions under A, and that the
    characteristic-5 example has no invariant complementary line.
---

::: {.problem}
Let $A$ be linear on a vector space $W$ over a field $k$, with $A^5=I$.

(a) If $\operatorname{char}k\ne5$, show that $W=U\oplus V$, where $U=\{u:Au=u\}$ and $AV=V$.

(b) Give an example showing this can fail in characteristic $5$.
:::

::: {.solution}
<1>1. Assume
$$
\operatorname{char}k\ne5
$$
and define
$$
P
\coloneqq
\frac15(I+A+A^2+A^3+A^4).
$$
Then
$$
\operatorname{im}P=U.
$$

::: {.proof}
Since $5$ is nonzero in $k$, it is invertible and $P$ is well-defined.
For every $w\in W$,
$$
\begin{aligned}
APw
&=
\frac15(Aw+A^2w+A^3w+A^4w+A^5w)\\
&=
\frac15(Aw+A^2w+A^3w+A^4w+w)\\
&=
Pw.
\end{aligned}
$$
Thus $Pw\in U$, so
$$
\operatorname{im}P\subseteq U.
$$

Conversely, if $u\in U$, then $Au=u$, hence
$$
Pu
=
\frac15(u+u+u+u+u)
=
u.
$$
Therefore every $u\in U$ belongs to $\operatorname{im}P$, proving
equality.
:::

<1>2. The operator $P$ is a projection:
$$
P^2=P.
$$

::: {.proof}
By step <1>1, $Pw\in U$ for every $w\in W$. The same step shows that
$P$ acts as the identity on $U$. Hence
$$
P^2w=P(Pw)=Pw
$$
for every $w$.
:::

<1>3. If
$$
V\coloneqq\ker P,
$$
then
$$
W=U\oplus V.
$$

::: {.proof}
For every $w\in W$,
$$
w
=
Pw+(w-Pw).
$$
By step <1>1,
$$
Pw\in U,
$$
and by step <1>2,
$$
P(w-Pw)
=
Pw-P^2w
=
0,
$$
so $w-Pw\in V$. Thus $W=U+V$.

If $x\in U\cap V$, then step <1>1 gives
$$
Px=x,
$$
while $x\in V$ gives $Px=0$. Hence $x=0$, so the sum is direct.
:::

<1>4. The complement $V$ satisfies
$$
AV=V.
$$

::: {.proof}
The operator $P$ is a polynomial in $A$, so
$$
PA=AP.
$$
If $v\in V$, then
$$
P(Av)
=
A(Pv)
=
0,
$$
so $Av\in V$. Hence
$$
AV\subseteq V.
$$

Also
$$
A^{-1}=A^4
$$
because $A^5=I$. Since $P$ also commutes with $A^4$, the same argument
gives
$$
A^{-1}V\subseteq V.
$$
Applying $A$ yields
$$
V\subseteq AV.
$$
Therefore $AV=V$. This proves part (a).
:::

<1>5. For part (b), let
$$
k=\FF_5,
\qquad
W=k^2,
$$
with basis $e_1,e_2$, and define
$$
Ae_1=e_1,
\qquad
Ae_2=e_1+e_2.
$$
Then
$$
A^5=I.
$$

::: {.proof}
Write
$$
A=I+N,
$$
where
$$
Ne_1=0,
\qquad
Ne_2=e_1.
$$
Then $N^2=0$. Hence in characteristic $5$,
$$
A^5
=(I+N)^5
=
I+5N
=
I.
$$
:::

<1>6. For the operator in step <1>5,
$$
U=\operatorname{span}(e_1).
$$

::: {.proof}
For
$$
v=ae_1+be_2,
$$
one has
$$
Av=(a+b)e_1+be_2.
$$
Thus $Av=v$ exactly when $b=0$, which gives the stated fixed space.
:::

<1>7. The fixed space $U$ in step <1>6 has no $A$-invariant
complement.

::: {.proof}
Any complement $V$ of the one-dimensional subspace $U$ in $W=k^2$
must itself be one-dimensional. Write
$$
V=\operatorname{span}(ae_1+be_2)
$$
with $b\ne0$, since otherwise $V=U$.

If $AV=V$, then for some $\lambda\in k$,
$$
A(ae_1+be_2)
=
\lambda(ae_1+be_2).
$$
Using step <1>6, this becomes
$$
(a+b)e_1+be_2
=
\lambda ae_1+\lambda be_2.
$$
Comparing the $e_2$ coefficients and using $b\ne0$ gives
$$
\lambda=1.
$$
Comparing the $e_1$ coefficients then gives
$$
a+b=a,
$$
so $b=0$, a contradiction. Therefore no such invariant complement
exists.
:::

<1>8. Q.E.D.

::: {.proof}
Steps <1>1--<1>4 prove part (a), and steps <1>5--<1>7 give the required
counterexample for part (b).
:::
:::
