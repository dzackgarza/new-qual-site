---
schema: qual/card@1
id: E-MUN-4-6
kind: problem
title: Laws of exponents for real numbers
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
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 4, Exercise 6; the stored statement matches.
- event: solution-written
  by: gpt-5.6-sol
  date: 2026-09-09
- event: solution-reviewed
  by: gpt-5.6-sol
  date: 2026-09-09
---

::: {.exercise}

Let $a \in \RR$ . Define inductively

$$
\begin{array}{c} {a ^ {1} = a,} \\ {a ^ {n + 1} = a ^ {n} \cdot a} \end{array}
$$

for $n \in \ZZ_{+}$ . (See §7 for a discussion of the process of inductive definition.)
Show that for $n, m \in \ZZ_{+}$ and $a, b \in \RR$,

$$
\begin{array}{l} a ^ {n} a ^ {m} = a ^ {n + m}, \\ (a ^ {n}) ^ {m} = a ^ {n m}, \\ a ^ {m} b ^ {m} = (a b) ^ {m}. \end{array}
$$

These are called the laws of exponents.
[Hint: For fixed $n$, prove the formulas by induction on $m$ .]
:::

::: {.solution}
We prove the three identities by induction.

First fix $n\in\ZZ_+$. For $m=1$,
$$
a^na=a^{n+1}
$$
by definition. If $a^na^m=a^{n+m}$, then
$$
a^na^{m+1}=a^n(a^ma)=(a^na^m)a=a^{n+m}a=a^{n+m+1}.
$$
Thus
$$
\boxed{a^na^m=a^{n+m}}.
$$

Next fix $n$. For $m=1$, $(a^n)^1=a^n$. If $(a^n)^m=a^{nm}$, then using the first identity,
$$
(a^n)^{m+1}=(a^n)^ma^n=a^{nm}a^n=a^{nm+n}=a^{n(m+1)}.
$$
Hence
$$
\boxed{(a^n)^m=a^{nm}}.
$$

Finally, for $m=1$, $a^1b^1=ab=(ab)^1$. If $a^mb^m=(ab)^m$, then commutativity and associativity give
$$
a^{m+1}b^{m+1}=a^mab^mb=(a^mb^m)(ab)=(ab)^m(ab)=(ab)^{m+1}.
$$
Therefore
$$
\boxed{a^mb^m=(ab)^m}.
$$
:::
