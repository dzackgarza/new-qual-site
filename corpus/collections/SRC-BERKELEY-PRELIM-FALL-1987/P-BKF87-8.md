---
schema: qual/card@1
id: P-BKF87-8
kind: problem
title: When the complex-number matrix ring over a field is a field
classification: {areas: [prelim], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
---

::: {.problem}
Let $F$ be a field and let $R$ be the set of matrices
\[
\begin{pmatrix}a&-b\\ b&a\end{pmatrix},
\qquad a,b\in F.
\]
Show that $R$ is a commutative ring with identity under the usual matrix operations. Determine for which of
\[
F=\mathbb Q,\qquad \mathbb C,\qquad \mathbb Z_5,\qquad \mathbb Z_7
\]
the ring $R$ is a field.
:::

::: {.solution}
For $a,b\in F$, write
$$
M(a,b)=
\begin{pmatrix}
a&-b\\
b&a
\end{pmatrix}.
$$

<1>1. The set $R$ is closed under addition, additive inverses, and multiplication, and contains the identity matrix.

::: {.proof}
For $a,b,c,d\in F$,
$$
M(a,b)+M(c,d)=M(a+c,b+d),
$$
$$
-M(a,b)=M(-a,-b),
$$
and direct multiplication gives
$$
M(a,b)M(c,d)
=
M(ac-bd,ad+bc).
$$
Also
$$
I=M(1,0).
$$
Thus $R$ is a subring of $M_2(F)$ containing the identity.
:::

<1>2. The ring $R$ is commutative.

::: {.proof}
The multiplication formula from step <1>1 gives
$$
M(a,b)M(c,d)
=
M(ac-bd,ad+bc).
$$
Since multiplication and addition in $F$ are commutative,
$$
ac-bd=ca-db
$$
and
$$
ad+bc=cb+da.
$$
Hence
$$
M(a,b)M(c,d)=M(c,d)M(a,b).
$$
:::

<1>3. A nonzero element $M(a,b)$ of $R$ is invertible in $R$ if and only if
$$
a^2+b^2\neq0.
$$

::: {.proof}
The determinant is
$$
\det M(a,b)=a^2+b^2.
$$
Thus invertibility as a matrix requires and is implied by
$$
a^2+b^2\neq0.
$$
When this holds,
$$
M(a,b)^{-1}
=
\frac1{a^2+b^2}
\begin{pmatrix}
a&b\\
-b&a
\end{pmatrix}
=
M\left(
\frac{a}{a^2+b^2},
-\frac{b}{a^2+b^2}
\right),
$$
which belongs to $R$.
:::

<1>4. The ring $R$ is a field if and only if $-1$ is not a square in $F$.

::: {.proof}
By step <1>3, $R$ fails to be a field exactly when there is a nonzero pair $(a,b)$ such that
$$
a^2+b^2=0.
$$
For such a pair, $b\neq0$, since $b=0$ would force $a=0$. Dividing by $b^2$ gives
$$
\left(\frac ab\right)^2=-1.
$$
Thus failure of fieldness implies that $-1$ is a square.

Conversely, if $c^2=-1$ in $F$, then
$$
M(c,1)\neq0
$$
but
$$
\det M(c,1)=c^2+1=0.
$$
Hence $R$ has a nonzero noninvertible element and is not a field.
:::

<1>5. For $F=\QQ$, the ring $R$ is a field.

::: {.proof}
No rational square equals $-1$, since every rational square is nonnegative as a real number. Apply step <1>4.
:::

<1>6. For $F=\CC$, the ring $R$ is not a field.

::: {.proof}
In $\CC$,
$$
i^2=-1.
$$
Apply step <1>4.
:::

<1>7. For $F=\ZZ_5$, the ring $R$ is not a field.

::: {.proof}
Modulo $5$,
$$
2^2=4=-1.
$$
Apply step <1>4.
:::

<1>8. For $F=\ZZ_7$, the ring $R$ is a field.

::: {.proof}
The nonzero squares modulo $7$ are
$$
1^2=6^2=1,
\qquad
2^2=5^2=4,
\qquad
3^2=4^2=2.
$$
Thus the set of nonzero squares is
$$
\{1,2,4\},
$$
which does not contain
$$
-1=6.
$$
Apply step <1>4.
:::

<1>9. Therefore
$$
\boxed{
R\text{ is a field precisely for }F=\QQ\text{ and }F=\ZZ_7.
}
$$

::: {.proof}
This follows from steps <1>5--<1>8.
:::

<1>10. Q.E.D.

::: {.proof}
Steps <1>1 and <1>2 prove that $R$ is a commutative ring with identity, and step <1>9 gives the requested field classification.
:::
:::
