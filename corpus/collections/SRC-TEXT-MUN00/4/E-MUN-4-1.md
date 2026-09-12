---
schema: qual/card@1
id: E-MUN-4-1
kind: problem
title: Laws of algebra for $\mathbb{R}$ from the field axioms
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
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 4, Exercise 1; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Prove the following "laws of algebra" for $\mathbb{R}$, using only axioms (1)-(5):

(a) If $x + y = x$, then $y = 0$ .

(b) $0 \cdot x = 0$ . [Hint: Compute $(x + 0) \cdot x$ .]

(c) -0 = 0.

(d) $-(-x) = x$ .

(e) $x(-y) = -(xy) = (-x)y.$

(f) $(-1)x = -x$ .

(g) $x(y - z) = xy - xz.$

(h) $-(x + y) = -x - y; -(x - y) = -x + y.$

(i) If $x \neq 0$ and $x \cdot y = x$, then $y = 1$ .

(j) $x / x = 1$ if $x \neq 0$ .

(k) x/1 = x.

(1) $x \neq 0$ and $y \neq 0 \Rightarrow xy \neq 0$ .

(m) $(1 / y)(1 / z) = 1 / (yz)$ if $y, z \neq 0$ .

(n) $(x / y)(w / z) = (xw) / (yz)$ if $y, z \neq 0$ .

(o) $(x / y) + (w / z) = (xz + wy) / (yz)$ if $y, z \neq 0$ .

(p) $x \neq 0 \Rightarrow 1 / x \neq 0$ .

(q) $1 / (w / z) = z / w$ if $w, z \neq 0$ .

(r) $(x/y)/(w/z)=(xz)/(yw)$ if $y, w, z \neq 0$ .

(s) $(ax)/y = a(x/y)$ if $y \neq 0$ .

(t) $(-x) / y = x / (-y) = -(x / y)$ if $y \neq 0$ .
:::

::: {.solution}
We use only the field axioms, together with earlier parts as they are proved.

(a) From \(x+y=x=x+0\), add \(-x\) to both sides to obtain \(y=0\).

(b) Since \(x+0=x\),
\[
(x+0)x=x^2.
\]
By distributivity the left side is \(x^2+0x\). Hence \(x^2+0x=x^2\), so part (a) gives
\[
0x=0.
\]

(c) Both \(-0\) and \(0\) satisfy \(0+u=0\). By part (a), \(-0=0\).

(d) Since
\[
(-x)+x=x+(-x)=0,
\]
\(x\) is an additive inverse of \(-x\). Additive inverses are unique, so
\[
-(-x)=x.
\]

(e) We have
\[
x(-y)+xy=x((-y)+y)=x0=0,
\]
so \(x(-y)\) is the additive inverse of \(xy\), hence
\[
x(-y)=-(xy).
\]
By commutativity,
\[
(-x)y=y(-x)=-(yx)=-(xy).
\]

(f) Taking \(x=1\) in part (e) gives
\[
(-1)x=-(1x)=-x.
\]

(g) Since \(y-z=y+(-z)\), distributivity and part (e) give
\[
x(y-z)=xy+x(-z)=xy-xz.
\]

(h) The element \(-x-y\) is the additive inverse of \(x+y\), since
\[
(x+y)+(-x-y)=0.
\]
Thus
\[
-(x+y)=-x-y.
\]
Then, using parts (d) and the first identity,
\[
-(x-y)=-(x+(-y))=-x-(-y)=-x+y.
\]

(i) Suppose \(x\ne0\) and \(xy=x\). Multiply by \(1/x\):
\[
(1/x)(xy)=(1/x)x,
\]
so \(y=1\).

(j) By definition \(1/x\) is the multiplicative inverse of \(x\), hence
\[
x/x=x(1/x)=1.
\]

(k) Since \(1\cdot1=1\), the multiplicative inverse of \(1\) is \(1\). Therefore
\[
x/1=x(1/1)=x.
\]

(l) Suppose \(x,y\ne0\). If \(xy=0\), multiplying by \((1/x)(1/y)\) gives
\[
1=0,
\]
contrary to the field axiom \(1\ne0\). Hence \(xy\ne0\).

(m) By part (l), \(yz\ne0\). Moreover
\[
(yz)(1/y)(1/z)=(y(1/y))(z(1/z))=1.
\]
Thus \((1/y)(1/z)\) is the inverse of \(yz\), so
\[
(1/y)(1/z)=1/(yz).
\]

(n) Using the definition of quotient and part (m),
\[
(x/y)(w/z)=xw(1/y)(1/z)=\frac{xw}{yz}.
\]

(o) Since \(z/z=y/y=1\),
\[
\frac{x}{y}+\frac{w}{z}
=\frac{xz}{yz}+\frac{wy}{yz}
=\frac{xz+wy}{yz}.
\]

(p) If \(1/x=0\), then
\[
1=x(1/x)=x0=0,
\]
a contradiction. Hence \(1/x\ne0\).

(q) Since \(w,z\ne0\), part (l) implies \(w/z\ne0\). Also
\[
(w/z)(z/w)=\frac{wz}{zw}=1,
\]
so \(z/w\) is the inverse of \(w/z\). Therefore
\[
\frac1{w/z}=\frac zw.
\]

(r) Using part (q),
\[
\frac{x/y}{w/z}=\frac{x}{y}\frac{z}{w}=\frac{xz}{yw}.
\]

(s) Associativity gives
\[
\frac{ax}{y}=(ax)(1/y)=a(x(1/y))=a(x/y).
\]

(t) By part (e),
\[
\frac{-x}{y}=(-x)(1/y)=-\bigl(x(1/y)\bigr)=-(x/y).
\]
Also \((-y)(-1/y)=1\), so \(1/(-y)=-(1/y)\). Hence
\[
\frac{x}{-y}=x\bigl(-(1/y)\bigr)=-(x/y).
\]
Thus
\[
\boxed{\frac{-x}{y}=\frac{x}{-y}=-\frac{x}{y}}.
\]
:::
