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
    Read against Munkres, Topology (2000), §4 Exercise 5, printed p. 35; the five parts
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
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps from the retained Whitman solution (Exercise 4.5, printed pp. 51-52); statement and the three bracketed hints unchanged. The unstated fact that (d) needs -- adding or subtracting 1 preserves the integers -- is now its own step, proved from (c) in three cases, because both the base case 1 in X_c and the induction step invoke it; (b) and (e) cite (a) and (b) by reference. Pages added and checked against the retained PDF: the definition of an inductive set and the principle of induction are on printed p. 32 (the earlier note's p. 34 is the exercises page of §3), the exercise on printed p. 35. No mathematical repair was needed.

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

Throughout, $\ZZ_+$ is the set of positive integers, inductive means a subset of $\RR$ containing $1$ and closed under $x\mapsto x+1$, so by the principle of induction $\ZZ_+$ is contained in every inductive set (definition and principle (2), printed p. 32; the exercise is on printed p. 35).

::: pf

::: {.pf-step #sum}
(a) If $a,b\in\ZZ_+$ then $a+b\in\ZZ_+$.

::: pf-proof
Fix $a\in\ZZ_+$ and put $X=\{x\in\RR: a+x\in\ZZ_+\}$, the set named in the book's hint. Then $1\in X$ because $a+1\in\ZZ_+$, $\ZZ_+$ being inductive; and if $x\in X$ then $a+x\in\ZZ_+$, so $a+(x+1)=(a+x)+1\in\ZZ_+$ again because $\ZZ_+$ is closed under adding $1$, that is $x+1\in X$. Hence $X$ is inductive, so $\ZZ_+\subset X$, which says $a+b\in\ZZ_+$ for every $b\in\ZZ_+$.

:::

:::

::: {.pf-step #product}
(b) If $a,b\in\ZZ_+$ then $a\cdot b\in\ZZ_+$.

::: pf-proof
Fix $a\in\ZZ_+$ and put $Y=\{x\in\RR: ax\in\ZZ_+\}$. Then $1\in Y$ because $a\cdot1=a\in\ZZ_+$; and if $x\in Y$ then $a(x+1)=ax+a\in\ZZ_+$ by step [](#sum){.pf-ref}, so $x+1\in Y$. Hence $Y$ is inductive and $\ZZ_+\subset Y$, giving $ab\in\ZZ_+$ for every $b\in\ZZ_+$.

:::

:::

::: {.pf-step #predecessor}
(c) If $a\in\ZZ_+$ then $a-1\in\ZZ_+\cup\{0\}$.

::: pf-proof
Put $X=\{x\in\RR: x-1\in\ZZ_+\cup\{0\}\}$, the set named in the book's hint. Since $1-1=0$ we have $1\in X$. Let $x\in X$. If $x-1=0$ then $x=1\in\ZZ_+$, while if $x-1\in\ZZ_+$ then $x=(x-1)+1\in\ZZ_+$ because $\ZZ_+$ is closed under adding $1$. In either case $x\in\ZZ_+$, so $(x+1)-1=x\in\ZZ_+$ and $x+1\in X$. Hence $X$ is inductive and $\ZZ_+\subset X$, which is the assertion.

:::

:::

::: {.pf-step #neighbours}
Adding or subtracting $1$ carries $\ZZ$ to $\ZZ$: if $m\in\ZZ$ then $m+1\in\ZZ$ and $m-1\in\ZZ$.

::: pf-proof
Three cases. If $m\in\ZZ_+$ then $m+1\in\ZZ_+$ because $\ZZ_+$ is inductive, and $m-1\in\ZZ_+\cup\{0\}\subset\ZZ$ by step [](#predecessor){.pf-ref}. If $m=0$ then $m+1=1\in\ZZ_+$ and $m-1=-1\in\ZZ$. If $m=-a$ with $a\in\ZZ_+$, then $-a+1=-(a-1)$ and $-a-1=-(a+1)$, and $a-1\in\ZZ_+\cup\{0\}$, $a+1\in\ZZ_+$ by step [](#predecessor){.pf-ref} and the inductiveness of $\ZZ_+$, so both lie in $\ZZ$.

:::

:::

::: {.pf-step #difference}
(d) If $c,d\in\ZZ$ then $c+d\in\ZZ$ and $c-d\in\ZZ$.

::: pf-proof
Fix $c\in\ZZ$ and put $X_c=\{x\in\RR: c+x\in\ZZ$ and $c-x\in\ZZ\}$, the set named in the book's hint, which says to prove the case $d=1$ first: that case is the previous step. Then $1\in X_c$ by step [](#neighbours){.pf-ref}; and if $x\in X_c$ then $c+x$ and $c-x$ are integers, so
$$
c+(x+1)=(c+x)+1\in\ZZ,
\qquad
c-(x+1)=(c-x)-1\in\ZZ
$$
by step [](#neighbours){.pf-ref}, that is $x+1\in X_c$. So $X_c$ is inductive and $\ZZ_+\subset X_c$, giving $c+d\in\ZZ$ and $c-d\in\ZZ$ for every $d\in\ZZ_+$. For $d=0$ both equal $c\in\ZZ$. For $d=-a$ with $a\in\ZZ_+$ they are $c+a$ and $c-a$, integers by the case just settled with $d=a$. Hence both lie in $\ZZ$ for every $d\in\ZZ$.

:::

:::

::: {.pf-step #product-integers}
(e) If $c,d\in\ZZ$ then $c\cdot d\in\ZZ$.

::: pf-proof
If $c=0$ or $d=0$ then $cd=0\in\ZZ$. Otherwise write $c=\varepsilon a$ and $d=\delta b$ with $a,b\in\ZZ_+$ and $\varepsilon,\delta\in\{1,-1\}$; this is possible because $c\ne0$ and $d\ne0$. By step [](#product){.pf-ref} $ab\in\ZZ_+$, and the sign laws $(c_1c_2)(d_1d_2)=(c_1d_1)(c_2d_2)$ and $(-c)d=-(cd)$ of Exercise 4.1(e) give $cd=(\varepsilon\delta)ab\in\ZZ$.

:::

:::

:::

:::
