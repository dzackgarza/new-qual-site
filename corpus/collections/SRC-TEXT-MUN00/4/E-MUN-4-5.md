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
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §4 Exercise 5, printed p. 34; the five parts
    and all three bracketed hints are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 4.5,
    printed pp. 51-52 (tmp/sources/munkres-solutions-whitman.pdf). Repaired (d), which
    had argued by "repeatedly adding or subtracting 1" and induction on |d| without
    saying what the induction is over; the card now carries an inductive set
    X_c = {x : c+x and c-x are integers}, whose inductive character is the induction
    step, together with the three-case verification that 1 is in it. That is Whitman's
    argument and it also discharges the book's hint "prove it first for d = 1". Parts
    (a), (b), (c), (e) are his, with (a) and (c) following the hints verbatim.
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
The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 4.5, printed pp. 51--52** (`tmp/sources/munkres-solutions-whitman.pdf`); (a) and (c) follow the book's hints as he does, and (d) is his inductive set $X_c$ below.

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

(d) First, adding or subtracting $1$ preserves $\ZZ$: if $m\in\ZZ_{+}$ then $m+1\in\ZZ_{+}$ because $\ZZ_{+}$ is inductive and $m-1\in\ZZ_{+}\cup\{0\}$ by part (c); the two neighbours of $0$ are $1\in\ZZ_{+}$ and $-1$; and for $a\in\ZZ_{+}$,
$$
-a+1=-(a-1)\in\ZZ,
\qquad
-a-1=-(a+1)\in\ZZ,
$$
because $a-1\in\ZZ_{+}\cup\{0\}$ by part (c) and $a+1\in\ZZ_{+}$.

Now fix $c\in\ZZ$ and put
$$
X_c=\{x\in\RR:c+x\in\ZZ\ \text{and}\ c-x\in\ZZ\}.
$$
Then $1\in X_c$, since $c+1$ and $c-1$ are integers by the previous paragraph. If $x\in X_c$, then $c+x$ and $c-x$ are integers, so
$$
c+(x+1)=(c+x)+1\in\ZZ,
\qquad
c-(x+1)=(c-x)-1\in\ZZ
$$
again by the previous paragraph, hence $x+1\in X_c$. Thus $X_c$ is inductive and therefore $\ZZ_{+}\subset X_c$, so that $c+d$ and $c-d$ are integers for every $d\in\ZZ_{+}$. For $d=0$ both equal $c\in\ZZ$; for $d=-a$ with $a\in\ZZ_{+}$ they are $c+a$ and $c-a$, which are integers by what was just shown. Hence
$$
c+d\in\ZZ,
\qquad
c-d\in\ZZ
$$
for all $c,d\in\ZZ$.

(e) If either factor is zero, the product is zero. Otherwise write
$$
c=\varepsilon a,\qquad d=\delta b,
$$
with $a,b\in\ZZ_+$ and $\varepsilon,\delta\in\{1,-1\}$. Part (b) gives $ab\in\ZZ_+$, and the sign laws of [[E-MUN-4-1]](e) give
$$
cd=(\varepsilon\delta)ab\in\ZZ.
$$
:::
