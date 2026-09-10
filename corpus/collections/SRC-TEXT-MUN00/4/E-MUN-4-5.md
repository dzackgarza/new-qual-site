---
schema: qual/card@1
id: E-MUN-4-5
kind: problem
title: Closure properties of $\mathbb{Z}$ and $\mathbb{Z}_+$
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
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 4, Exercise 5; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Prove the following properties of $\mathbb{Z}$ and $\mathbb{Z}_{+}$ :

(a) $a, b \in \mathbb{Z}_{+} \Rightarrow a + b \in \mathbb{Z}_{+}$ . [Hint: Show that given $a \in \mathbb{Z}_{+}$, the set $X = \{x \mid x \in \mathbb{R} \text{ and } a + x \in \mathbb{Z}_{+}\}$ is inductive.]

(b) $a, b \in \mathbb{Z}_+ \Rightarrow a \cdot b \in \mathbb{Z}_+$ .

(c) Show that $a \in \mathbb{Z}_+ \Rightarrow a - 1 \in \mathbb{Z}_+ \cup \{0\}$ . [Hint: Let $X = \{x \mid x \in \mathbb{R} \text{ and } x - 1 \in \mathbb{Z}_+ \cup \{0\}$ ; show that $X$ is inductive.]

(d) $c, d \in \mathbb{Z} \Rightarrow c + d \in \mathbb{Z}$ and $c - d \in \mathbb{Z}$ . [Hint. Prove it first for $d = 1$ .]

(e) $c, d \in \mathbb{Z} \Rightarrow c \cdot d \in \mathbb{Z}$ .
:::

::: {.solution}
(a) Fix \(a\in\mathbb Z_+\), and define
\[
X=\{x\in\mathbb R:a+x\in\mathbb Z_+\}.
\]
Since \(a+1\in\mathbb Z_+\), we have \(1\in X\). If \(x\in X\), then \(a+x\in\mathbb Z_+\), so
\[
a+(x+1)=(a+x)+1\in\mathbb Z_+,
\]
hence \(x+1\in X\). Thus \(X\) is inductive, so \(\mathbb Z_+\subset X\). In particular, for every \(b\in\mathbb Z_+\),
\[
a+b\in\mathbb Z_+.
\]

(b) Fix \(a\in\mathbb Z_+\), and let
\[
Y=\{x\in\mathbb R:ax\in\mathbb Z_+\}.
\]
Since \(a\cdot1=a\in\mathbb Z_+\), \(1\in Y\). If \(x\in Y\), then by part (a)
\[
a(x+1)=ax+a\in\mathbb Z_+,
\]
so \(x+1\in Y\). Thus \(Y\) is inductive, whence \(b\in Y\) for every \(b\in\mathbb Z_+\). Therefore \(ab\in\mathbb Z_+\).

(c) Let
\[
X=\{x\in\mathbb R:x-1\in\mathbb Z_+\cup\{0\}\}.
\]
Since \(1-1=0\), \(1\in X\). If \(x\in X\), then either \(x-1=0\), in which case \(x=1\in\mathbb Z_+\), or \(x-1\in\mathbb Z_+\), in which case
\[
x=(x-1)+1\in\mathbb Z_+.
\]
Thus in either case
\[
(x+1)-1=x\in\mathbb Z_+,
\]
so \(x+1\in X\). Hence \(X\) is inductive and \(\mathbb Z_+\subset X\), proving
\[
a-1\in\mathbb Z_+\cup\{0\}
\qquad(a\in\mathbb Z_+).
\]

(d) First note that adding or subtracting \(1\) preserves \(\mathbb Z\). For positive integers this follows from inductivity and part (c); for \(0\) it is immediate; for a negative integer \(-a\),
\[
-a+1=-(a-1),\qquad -a-1=-(a+1),
\]
and parts (a),(c) show these are integers. Every \(d\in\mathbb Z\) is \(0\), a positive integer, or the negative of one. Repeatedly adding or subtracting \(1\), and using induction on the positive integer \(|d|\), therefore gives
\[
c+d\in\mathbb Z,
\qquad
c-d\in\mathbb Z.
\]

(e) If either factor is zero, the product is zero. Otherwise write
\[
c=\varepsilon a,\qquad d=\delta b,
\]
with \(a,b\in\mathbb Z_+\) and \(\varepsilon,\delta\in\{1,-1\}\). Part (b) gives \(ab\in\mathbb Z_+\), and the sign laws of Exercise 1 give
\[
cd=(\varepsilon\delta)ab\in\mathbb Z.
\]
:::
