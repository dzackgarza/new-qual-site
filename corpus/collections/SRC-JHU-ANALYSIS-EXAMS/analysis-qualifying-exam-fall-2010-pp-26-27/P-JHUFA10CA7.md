---
schema: qual/card@1
id: P-JHUFA10CA7
kind: problem
title: Entire functions dominated by $|\operatorname{Re}z|^2+|z|^{3/2}$
classification:
  areas:
  - complex-analysis
  topics:
  - Entire Functions
  - Liouville's Theorem
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared the coefficient-one inequality for every modulus greater than one with Fall 2010 problem 7 on PDF page 27."
- event: solution-written
  by: chatgpt
  date: 2026-09-10
- event: solution-reviewed
  by: chatgpt
  date: 2026-09-10
  note: "Proved the affine reduction, necessity and sufficiency of the unit-circle bound, and an explicit finite critical-value test for all permitted coefficient pairs; unrestricted affine functions do not satisfy the source inequality."
- event: source-checked
  by: chatgpt
  date: 2026-09-10
  note: "Compared both complete transcriptions of Fall 2010 problem 7 and retained the exact coefficient classification here. Removed the duplicate P-JHUMAY11ANO and its unsupported May 2011 membership."
---

::: {.problem}
Determine all entire functions $f$ that satisfy

$$
|f(z)|\leq |\operatorname{Re}z|^2+|z|^{3/2}\qquad\text{whenever }|z|>1.
$$
:::

::: {.solution}
The solutions are precisely the affine functions $f(z)=az+b$
whose coefficients satisfy
$$
|aw+b|\leq1+(\operatorname{Re}w)^2\qquad(|w|=1).
\tag{1}
$$
This compact-circle condition has the following finite
algebraic form. For $a,b\in\mathbb C$, define the real
polynomial in the real variable $t$
$$
Q_{a,b}(t)=4(1+t^4)^2-(1+t^2)^2
\left|(a+b)+(b-a)t^2+2iat\right|^2.
\tag{2}
$$
Here the squared modulus means multiplication by the
coefficientwise conjugate polynomial, since $t$ is real.
The exact coefficient test is
$$
|a|^2+|b|^2\leq1,
\qquad Q_{a,b}(t)\geq0\text{ at every real root of }Q_{a,b}'(t).
\tag{3}
$$
Under the first inequality, $Q_{a,b}'$ has degree seven,
so this requires checking at most seven real numbers.
Thus (3) is a necessary-and-sufficient specification of
all coefficients, not merely a growth restriction on the degree.

<1>1. Every solution is affine.

::: {.proof}
On $|z|=R>1$ the hypothesis gives
$|f(z)|\leq R^2+R^{3/2}$. If $c_k$ is the $k$th
Taylor coefficient of $f$ at zero, Cauchy's estimate gives
$$
|c_k|\leq R^{2-k}+R^{3/2-k}
$$
[@SS03]. For $k\geq3$, let $R\to\infty$ to obtain
$c_k=0$. Hence $f(z)=cz^2+az+b$.
On the imaginary ray the given bound is $|f(iR)|\leq R^{3/2}$.
Divide by $R^2$ and let $R\to\infty$. The expression
$f(iR)/R^2=-c+ia/R+b/R^2$ tends to $-c$, whereas
its modulus is at most $R^{-1/2}$. Therefore $c=0$.
:::

<1>2. For affine functions, (1) is equivalent to the original inequality.

::: {.proof}
Necessity follows by setting $z=rw$, $|w|=1$, and letting
$r\downarrow1$ in the original inequality.
Conversely assume (1). At $w=i$ and $w=-i$ it gives
$|ai+b|\leq1$ and $|-ai+b|\leq1$. Adding the squares yields
$$
2(|a|^2+|b|^2)=|ai+b|^2+|-ai+b|^2\leq2,
$$
so in particular $|a|\leq1$.
For any $r>1$ and $|w|=1$, put $x=\operatorname{Re}w$.
Using a convex combination and then (1),
$$
\begin{aligned}
|arw+b|/r
&=\left|(1-r^{-1})aw+r^{-1}(aw+b)\right|\\
&\leq (1-r^{-1})|a|+r^{-1}|aw+b|\\
&\leq1+r^{-1}x^2.
\end{aligned}
$$
Thus $|arw+b|\leq r+x^2\leq r^{3/2}+r^2x^2$
since $r>1$. This last expression is precisely
$|rw|^{3/2}+|\operatorname{Re}(rw)|^2$, proving sufficiency.
:::

<1>3. The finite coefficient test (3) is equivalent to (1).

::: {.proof}
Parametrize the unit circle except $-1$ by
$$
w(t)=\frac{1-t^2+2it}{1+t^2},\qquad t\in\mathbb R.
$$
Then
$$
aw(t)+b=\frac{(a+b)+(b-a)t^2+2iat}{1+t^2},
\qquad
1+(\operatorname{Re}w(t))^2=\frac{2(1+t^4)}{(1+t^2)^2}.
$$
Squaring (1) and multiplying by the strictly positive
$(1+t^2)^4$ gives exactly $Q_{a,b}(t)\geq0$. These
operations are reversible because both sides of (1)
are nonnegative. Continuity supplies (1) also at $w=-1$
by letting $|t|\to\infty$.

Step <1>2 already shows that (1) implies
$|a|^2+|b|^2\leq1$. Under this inequality the leading
coefficient of $Q_{a,b}$ is
$$
4-|b-a|^2\geq4-2(|a|^2+|b|^2)\geq2.
$$
Hence $Q_{a,b}$ has degree eight and tends to positive
infinity as $t\to\pm\infty$. It attains a global minimum
on the real line; differentiability makes each such
minimizer a root of $Q_{a,b}'$. Therefore $Q_{a,b}$ is
nonnegative everywhere exactly when it is nonnegative
at every real critical point. Its degree-seven derivative
has at most seven distinct real roots. This proves (3)
and completes the classification.
:::
:::
