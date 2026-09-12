---
schema: qual/card@1
id: E-MUN-4-2
kind: problem
title: Laws of inequalities for $\mathbb{R}$
classification:
  areas:
  - topology
  topics:
  - Integers and Real Numbers
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-09
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 4, Exercise 2; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Prove the following "laws of inequalities" for $\mathbb{R}$, using axioms (1)-(6) along with the results of Exercise 1:

(a) $x > y$ and $w > z \Rightarrow x + w > y + z$ .

(b) $x > 0$ and $y > 0 \Rightarrow x + y > 0$ and $x \cdot y > 0$ .

(c) $x > 0 \Leftrightarrow -x < 0$ .

(d) $x > y \Leftrightarrow -x < -y$ .

(e) $x > y$ and $z < 0 \Rightarrow xz < yz$ .

(f) $x \neq 0 \Rightarrow x^2 > 0$, where $x^2 = x \cdot x$ .

(g) $-1 < 0 < 1$

(h) $xy > 0 \Leftrightarrow x$ and $y$ are both positive or both negative.

(i) $x > 0 \Rightarrow 1 / x > 0$ .

(j) $x > y > 0 \Rightarrow 1 / x < 1 / y.$

(k) $x < y \Rightarrow x < (x + y) / 2 < y$ .
:::

::: {.solution}
Recall that \(x>y\) means \(x-y>0\), and that positive real numbers are closed under addition and multiplication.

(a) Since \(x-y>0\) and \(w-z>0\),
\[
(x+w)-(y+z)=(x-y)+(w-z)>0,
\]
so \(x+w>y+z\).

(b) This is exactly closure of the positive reals under addition and multiplication:
\[
x+y>0,\qquad xy>0.
\]

(c)
\[
-x<0\iff 0-(-x)>0\iff x>0.
\]

(d)
\[
-x<-y\iff (-y)-(-x)=x-y>0\iff x>y.
\]

(e) Since \(x-y>0\) and \(-z>0\),
\[
(x-y)(-z)>0.
\]
But this equals \(yz-xz\). Hence \(yz>xz\), i.e.
\[
xz<yz.
\]

(f) If \(x\ne0\), trichotomy gives either \(x>0\) or \(-x>0\). In the first case \(x^2>0\). In the second,
\[
x^2=(-x)^2>0.
\]
Thus \(x^2>0\) whenever \(x\ne0\).

(g) Since \(1\ne0\), part (f) gives \(1=1^2>0\). Part (c) then gives \(-1<0\). Hence
\[
-1<0<1.
\]

(h) If \(x,y>0\), then \(xy>0\). If \(x,y<0\), then \(-x,-y>0\) and
\[
xy=(-x)(-y)>0.
\]
Conversely suppose \(xy>0\). Neither factor is zero. If \(x>0\) and \(y<0\), then applying part (e) to \(x>0\) and the negative multiplier \(y\) gives \(xy<0\), a contradiction. Hence \(y>0\). Similarly, if \(x<0\), then \(y<0\). Thus \(xy>0\) exactly when the two factors have the same sign.

(i) Let \(x>0\). By Exercise 1(p), \(1/x\ne0\). If \(1/x<0\), then a positive number times a negative number is negative, so
\[
1=x(1/x)<0,
\]
contradicting part (g). Therefore
\[
1/x>0.
\]

(j) If \(x>y>0\), then \(xy>0\), and
\[
\frac1y-\frac1x=\frac{x-y}{xy}>0.
\]
Hence
\[
\frac1x<\frac1y.
\]

(k) If \(x<y\), part (a) gives
\[
2x=x+x<x+y<y+y=2y.
\]
Also \(2=1+1>0\), so part (i) gives \(1/2>0\). Multiplication by the positive number \(1/2\) preserves inequalities, hence
\[
x<\frac{x+y}{2}<y.
\]
:::
