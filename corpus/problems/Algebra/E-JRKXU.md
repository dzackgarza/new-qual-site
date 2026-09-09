---
schema: qual/card@1
id: E-JRKXU
kind: problem
title: Whether $\mathbb{Q}(\sqrt{3+\sqrt{2}})$ is a splitting field over $\mathbb{Q}$
classification:
  areas:
  - algebra
  topics:
  - Splitting Fields
  - Field Extensions
relations: []
review: draft
audit:
- event: solution-written
  by: OpenAI
  date: 2026-09-09
- event: solution-reviewed
  by: OpenAI
  date: 2026-09-09
---

::: problem
17. Let $u=\sqrt{3+\sqrt{2}}$. Is $\QQ(u)$ the splitting field over $\QQ$ of the minimal polynomial of $u$?
:::

::: {.solution}
Set
\[
E=\QQ(\sqrt2),
\qquad
F=\QQ(u)=E(u).
\]

<1>1. The minimal polynomial of $u$ over $\QQ$ is
\[
f(x)=x^4-6x^2+7.
\]
::: {.proof}
Since
\[
u^2=3+\sqrt2,
\]
we have $\sqrt2=u^2-3\in\QQ(u)$, so $E\subseteq F$. Also
\[
(u^2-3)^2=2,
\]
which gives $f(u)=0$.

It remains to show $[F:\QQ]=4$. We have $[E:\QQ]=2$. If $u\in E$, then $3+\sqrt2$ would be a square in $E$. But for $a\in E$,
\[
N_{E/\QQ}(a^2)=N_{E/\QQ}(a)^2
\]
is a square in $\QQ$, whereas
\[
N_{E/\QQ}(3+\sqrt2)=(3+\sqrt2)(3-\sqrt2)=7
\]
is not a square in $\QQ$. Thus $u\notin E$, so $[F:E]=2$ and therefore $[F:\QQ]=4$. Since $f$ has degree $4$, it is the minimal polynomial of $u$.
:::

<1>2. The roots of $f$ are
\[
\pm u,
\qquad
\pm v,
\qquad
v:=\sqrt{3-\sqrt2}.
\]
::: {.proof}
The equation $f(x)=0$ is
\[
(x^2-3)^2=2,
\]
so
\[
x^2=3\pm\sqrt2.
\]
Taking square roots gives exactly the four displayed roots. Also
\[
uv=\sqrt{(3+\sqrt2)(3-\sqrt2)}=\sqrt7.
\]
:::

<1>3. One has $\sqrt7\notin F$.
::: {.proof}
Because $F/E$ is quadratic with basis $1,u$, write any element of $F$ uniquely as $a+bu$ with $a,b\in E$. Suppose
\[
(a+bu)^2=7.
\]
Then
\[
a^2+b^2u^2+2ab\,u=7.
\]
The first two terms lie in $E$, while $1,u$ are $E$-linearly independent, so $2ab=0$. Hence either $a=0$ or $b=0$.

If $b=0$, then $a^2=7$ in $E=\QQ(\sqrt2)$. Write $a=r+s\sqrt2$ with $r,s\in\QQ$. Comparing the $\sqrt2$ coefficient gives $2rs=0$. If $s=0$, then $r^2=7$; if $r=0$, then $2s^2=7$. Neither equation has a rational solution.

If $a=0$, then
\[
b^2=\frac7{u^2}=\frac7{3+\sqrt2}=3-\sqrt2.
\]
But
\[
N_{E/\QQ}(3-\sqrt2)=7
\]
is not a square in $\QQ$, whereas the norm of $b^2$ would be a square. This is again impossible. Thus $\sqrt7\notin F$.
:::

<1>4. The root $v=\sqrt{3-\sqrt2}$ does not lie in $F$.
::: {.proof}
If $v\in F$, then by <1>2,
\[
\sqrt7=uv\in F,
\]
contradicting <1>3.
:::

<1>5. Therefore $F=\QQ(u)$ is not the splitting field of the minimal polynomial of $u$ over $\QQ$.
::: {.proof}
By <1>1--<1>2, the minimal polynomial is $f(x)=x^4-6x^2+7$ and one of its roots is $v$. By <1>4, $v\notin F$, so $f$ does not split over $F$.
:::
:::
