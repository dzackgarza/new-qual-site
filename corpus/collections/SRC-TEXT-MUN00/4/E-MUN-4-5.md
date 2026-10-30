---
schema: qual/card@1
id: E-MUN-4-5
kind: problem
title: Closure properties of $\ZZ$ and $\ZZ_+$
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

Prove the following properties of $\ZZ$ and $\ZZ_{+}$ :

(a) $a, b \in \ZZ_{+} \Rightarrow a + b \in \ZZ_{+}$ . [Hint: Show that given $a \in \ZZ_{+}$, the set $X = \{x \mid x \in \RR \text{ and } a + x \in \ZZ_{+}\}$ is inductive.]

(b) $a, b \in \ZZ_+ \Rightarrow a \cdot b \in \ZZ_+$ .

(c) Show that $a \in \ZZ_+ \Rightarrow a - 1 \in \ZZ_+ \cup \{0\}$ . [Hint: Let $X = \{x \mid x \in \RR \text{ and } x - 1 \in \ZZ_+ \cup \{0\}$ ; show that $X$ is inductive.]

(d) $c, d \in \ZZ \Rightarrow c + d \in \ZZ$ and $c - d \in \ZZ$ . [Hint. Prove it first for $d = 1$ .]

(e) $c, d \in \ZZ \Rightarrow c \cdot d \in \ZZ$ .
:::

::: {.solution}
(a) Fix $a\in\ZZ_+$, and define
$$
X=\{x\in\RR:a+x\in\ZZ_+\}.
$$
Since $a+1\in\ZZ_+$, we have $1\in X$. If $x\in X$, then $a+x\in\ZZ_+$, so
$$
a+(x+1)=(a+x)+1\in\ZZ_+,
$$
hence $x+1\in X$. Thus $X$ is inductive, so $\ZZ_+\subset X$. In particular, for every $b\in\ZZ_+$,
$$
a+b\in\ZZ_+.
$$

(b) Fix $a\in\ZZ_+$, and let
$$
Y=\{x\in\RR:ax\in\ZZ_+\}.
$$
Since $a\cdot1=a\in\ZZ_+$, $1\in Y$. If $x\in Y$, then by part (a)
$$
a(x+1)=ax+a\in\ZZ_+,
$$
so $x+1\in Y$. Thus $Y$ is inductive, whence $b\in Y$ for every $b\in\ZZ_+$. Therefore $ab\in\ZZ_+$.

(c) Let
$$
X=\{x\in\RR:x-1\in\ZZ_+\cup\{0\}\}.
$$
Since $1-1=0$, $1\in X$. If $x\in X$, then either $x-1=0$, in which case $x=1\in\ZZ_+$, or $x-1\in\ZZ_+$, in which case
$$
x=(x-1)+1\in\ZZ_+.
$$
Thus in either case
$$
(x+1)-1=x\in\ZZ_+,
$$
so $x+1\in X$. Hence $X$ is inductive and $\ZZ_+\subset X$, proving
$$
a-1\in\ZZ_+\cup\{0\}
\qquad(a\in\ZZ_+).
$$

(d) First note that adding or subtracting $1$ preserves $\ZZ$. For positive integers this follows from inductivity and part (c); for $0$ it is immediate; for a negative integer $-a$,
$$
-a+1=-(a-1),\qquad -a-1=-(a+1),
$$
and parts (a),(c) show these are integers. Every $d\in\ZZ$ is $0$, a positive integer, or the negative of one. Repeatedly adding or subtracting $1$, and using induction on the positive integer $\abs{d}$, therefore gives
$$
c+d\in\ZZ,
\qquad
c-d\in\ZZ.
$$

(e) If either factor is zero, the product is zero. Otherwise write
$$
c=\varepsilon a,\qquad d=\delta b,
$$
with $a,b\in\ZZ_+$ and $\varepsilon,\delta\in\{1,-1\}$. Part (b) gives $ab\in\ZZ_+$, and the sign laws of [[E-MUN-4-1]](e) give
$$
cd=(\varepsilon\delta)ab\in\ZZ.
$$
:::
