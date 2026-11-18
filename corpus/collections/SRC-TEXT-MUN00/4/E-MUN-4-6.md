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
- event: source-checked
  by: claude
  date: 2026-11-10
  note: >-
    Read against Munkres, Topology (2000), §4 Exercise 6, printed p. 35; the inductive
    definition, the three laws and the bracketed hint (fix n, induct on m) are stored as
    printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 4.6,
    printed pp. 53-54 (tmp/sources/munkres-solutions-whitman.pdf), which proves the
    three laws by exactly the book's hint and annotates each line with the axiom used.
    The card's three inductions are his; no defect found.
---

::: {.exercise}

Let $a \in \RR$. Define inductively

$$
\begin{aligned} a^1 &= a,\\ a^{n+1} &= a^n \cdot a \end{aligned}
$$

for $n \in \ZZ_{+}$. (See §7 for a discussion of the process of inductive definition.)
Show that for $n, m \in \ZZ_{+}$ and $a, b \in \RR$,

$$
\begin{aligned} a^n a^m &= a^{n+m},\\ (a^n)^m &= a^{nm},\\ a^m b^m &= (ab)^m. \end{aligned}
$$

These are called the laws of exponents.
[Hint: For fixed $n$, prove the formulas by induction on $m$.]
:::

::: {.solution}

The complete published solution is **Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 4.6, printed pp. 53--54** (`tmp/sources/munkres-solutions-whitman.pdf`), which proves the three laws by the book's hint — fix $n$ and induct on $m$ — and annotates each line with the axiom it uses. The three inductions below are his.

::: pf

::: {.pf-step #first}

$a^{n}a^{m}=a^{n+m}$ for all $n,m\in\ZZ_{+}$.

::: pf-proof

Fix $n\in\ZZ_{+}$ and induct on $m$. For $m=1$ the identity reads $a^{n}a=a^{n+1}$, which is the definition of $a^{n+1}$; the base case is $m=1$ rather than $m=0$ because $a^{0}$ is not defined in the exercise. If $a^{n}a^{m}=a^{n+m}$, then using associativity of multiplication in $\RR$ and the definition,
$$
a^{n}a^{m+1}=a^{n}(a^{m}a)=(a^{n}a^{m})a=a^{n+m}a=a^{n+m+1}.
$$
So the identity holds for $m+1$, and by induction for every $m$.

:::

:::

::: {.pf-step #second}

$(a^{n})^{m}=a^{nm}$ for all $n,m\in\ZZ_{+}$.

::: pf-proof

Fix $n$ and induct on $m$. For $m=1$, $(a^{n})^{1}=a^{n}=a^{n\cdot1}$. If $(a^{n})^{m}=a^{nm}$, then by the recursive definition and step [](#first){.pf-ref},
$$
(a^{n})^{m+1}=(a^{n})^{m}a^{n}=a^{nm}a^{n}=a^{nm+n}=a^{n(m+1)}.
$$
So the identity holds for $m+1$, and hence for all $m$.

:::

:::

::: {.pf-step #third}

$a^{m}b^{m}=(ab)^{m}$ for all $m\in\ZZ_{+}$.

::: pf-proof

Induct on $m$. For $m=1$, $a^{1}b^{1}=ab=(ab)^{1}$. If $a^{m}b^{m}=(ab)^{m}$, then by commutativity and associativity of multiplication in $\RR$,
$$
a^{m+1}b^{m+1}=(a^{m}a)(b^{m}b)=a^{m}(ab^{m})b=(a^{m}b^{m})(ab)=(ab)^{m}(ab)=(ab)^{m+1},
$$
the middle equalities regrouping the four factors and interchanging $a$ with $b^{m}$.

:::

:::

::: {.pf-step #conclusion}

The three laws of exponents hold for all $n,m\in\ZZ_{+}$ and $a,b\in\RR$.

::: pf-proof

Steps [](#first){.pf-ref}, [](#second){.pf-ref} and [](#third){.pf-ref} prove the three identities:
$$
\boxed{a^{n}a^{m}=a^{n+m},\qquad (a^{n})^{m}=a^{nm},\qquad a^{m}b^{m}=(ab)^{m}.}
$$

:::

:::

:::

:::
