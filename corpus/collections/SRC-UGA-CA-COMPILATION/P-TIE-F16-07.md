---
schema: qual/card@1
id: P-TIE-F16-07
kind: problem
title: Conformal map of the upper half-plane onto a half-strip
classification:
  areas:
  - complex-analysis
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: chatgpt
  date: 2026-09-12
  note: Checked against the retained Questions_from_Tie.pdf compilation, section Fall 2016, question 7.
---

::: {.problem}
Find the conformal map that takes the upper half-plane comformally onto the half-strip $\{ w = x + i y : \ - \pi / 2 < x < \pi / 2 \ y > 0 \}$
:::

Let
$$
S
\coloneqq
\left\{
w=x+iy:
-\frac\pi2<x<\frac\pi2,
\ y>0
\right\}.
$$

::: pf

::: pf-step

The sine function maps $S$ into the upper half-plane $\HH$.


::: pf-proof

For
$$
w=x+iy,
$$
one has
$$
\sin w
=
\sin x\cosh y
+
i\cos x\sinh y.
$$
On $S$,
$$
\cos x>0
\qquad\text{and}\qquad
\sinh y>0.
$$
Therefore
$$
\operatorname{Im}(\sin w)
=
\cos x\sinh y
>0.
$$
Hence
$$
\sin(S)\subset\HH.
$$

:::

:::

::: pf-step

The derivative of $\sin$ does not vanish on $S$.


::: pf-proof

One has
$$
(\sin w)'=\cos w.
$$
The zeros of $\cos w$ are
$$
w=\frac\pi2+k\pi,
\qquad
k\in\ZZ,
$$
all of which lie on the real axis and outside the open half-strip $S$. Thus
$$
\cos w\ne0
$$
for every $w\in S$.

:::

:::

::: pf-step

The map
$$
\sin:S\to\HH
$$
is injective.


::: pf-proof

Suppose
$$
\sin w_1=\sin w_2.
$$
Then
$$
2
\cos\left(\frac{w_1+w_2}{2}\right)
\sin\left(\frac{w_1-w_2}{2}\right)
=0.
$$
Hence either
$$
w_1-w_2=2k\pi
$$
for some $k\in\ZZ$, or
$$
w_1+w_2=(2k+1)\pi.
$$

In the first case,
$$
-\pi
<
\operatorname{Re}(w_1-w_2)
<
\pi,
$$
so $2k\pi$ can only be $0$. Thus $w_1=w_2$.

In the second case,
$$
-\pi
<
\operatorname{Re}(w_1+w_2)
<
\pi,
$$
so it cannot equal any odd multiple of $\pi$. Thus the second case is impossible.

:::

:::

::: pf-step

For every $z\in\HH$, the equation
$$
\sin w=z
$$
has a solution $w\in S$.


::: pf-proof

Set
$$
q=e^{iw}.
$$
Then
$$
\sin w
=
\frac{q-q^{-1}}{2i}.
$$
Thus $\sin w=z$ is equivalent to
$$
q^2-2izq-1=0.
$$
Let $q_1,q_2$ be the two roots. Their product is
$$
q_1q_2=-1,
$$
so
$$
\abs{q_1}\abs{q_2}=1.
$$

No root lies on the unit circle. Indeed, if $\abs q=1$, write
$$
q=e^{ix}
$$
with $x\in\RR$. Then
$$
z
=
\frac{q-q^{-1}}{2i}
=
\sin x
\in\RR,
$$
contradicting $z\in\HH$.

Hence exactly one root, call it $q$, satisfies
$$
\abs q<1.
$$
Write
$$
q=\rho e^{ix},
\qquad
0<\rho<1,
\qquad
-\pi<x<\pi.
$$
Set
$$
y=-\log\rho>0,
\qquad
w=x+iy.
$$
Then
$$
e^{iw}
=
e^{ix-y}
=
q,
$$
so
$$
\sin w=z.
$$

Since $z\in\HH$, step <1>1's formula gives
$$
0
<
\operatorname{Im}z
=
\cos x\sinh y.
$$
Because $y>0$, one has $\sinh y>0$, so
$$
\cos x>0.
$$
With $-\pi<x<\pi$, this implies
$$
-\frac\pi2
<
x
<
\frac\pi2.
$$
Thus
$$
w\in S.
$$

:::

:::

::: pf-step

The map
$$
\sin:S\longrightarrow\HH
$$
is a conformal bijection.


::: pf-proof

Step <1>1 shows that the image lies in $\HH$, step <1>2 gives local conformality, step <1>3 gives injectivity, and step <1>4 gives surjectivity.

:::

:::

::: pf-step

Therefore the required conformal map is the inverse branch
$$
\boxed{
F(z)
\coloneqq
\arcsin z,
}
$$
where $\arcsin$ denotes the branch characterized by
$$
-\frac\pi2
<
\operatorname{Re}F(z)
<
\frac\pi2,
\qquad
\operatorname{Im}F(z)>0
$$
for $z\in\HH$.


::: pf-proof

By step <1>5, $\sin:S\to\HH$ is a conformal bijection. Its inverse is therefore a conformal bijection
$$
F:\HH\to S.
$$
This inverse is precisely the indicated branch of the inverse sine.

:::

:::

::: pf-qed

Step <1>6 gives the requested conformal map.

:::

:::
