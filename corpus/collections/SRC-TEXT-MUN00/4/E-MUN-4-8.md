---
schema: qual/card@1
id: E-MUN-4-8
kind: problem
title: Greatest lower bound property of $\RR$
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
  note: Checked against Munkres, Topology, 2nd ed., Chapter 1, Section 4, Exercise 8; the stored statement matches.
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
    Read against Munkres, Topology (2000), §4 Exercise 8, printed p. 35; the three parts
    and the hint h = (1-a)/a with (1+h)^n >= 1+nh are stored as printed.
- event: solution-written
  by: claude
  date: 2026-11-10
  note: >-
    Transcribed from the located published solution: Dan Whitman, "Topology, Second
    Edition by James Munkres: Solutions Manual" (30 November 2019), Exercise 4.8,
    printed pp. 59-60 (tmp/sources/munkres-solutions-whitman.pdf). His (a) turns -A into
    a set bounded above and reflects its supremum; (b) and (c) use the Archimedean
    property against an arbitrary positive lower bound, in (c) through Bernoulli's
    inequality for (1+h)^n as the hint directs. The card's arguments are these, and the
    case split on a < 1 versus a >= 1 that he needs in (c) is avoided by bounding B by
    1 + a throughout.
- event: solution-reviewed
  by: claude
  date: 2026-11-18
  note: >-
    Restructured into Lamport steps, transcribing the cited published solution: Dan Whitman,
    Topology, Second Edition by James Munkres: Solutions Manual (2019), Exercise 4.8, printed
    pp. 59-60. Checked against Munkres §4 Exercise 8, whose number is read from the collection
    index. Each part re-read: (a) reflects a set bounded below through -A and shows -sup(-A) is
    the greatest lower bound; (b) uses the Archimedean property to defeat every positive lower
    bound; (c) uses the hint h = (1-a)/a, Bernoulli's inequality by induction, the resulting bound
    a^n <= 1/(1+nh), and the Archimedean property once more. Not claimed: the existence of the
    least upper bound property itself, which is the completeness axiom Munkres takes as given.
---

::: {.exercise}

(a) Show that $\RR$ has the greatest lower bound property.

(b) Show that $\inf \{1 / n \mid n \in \ZZ_+\} = 0$ .

(c) Show that given $a$ with $0 < a < 1$, $\inf \{a^n \mid n \in \ZZ_+\} = 0$ . [Hint: Let $h = (1 - a) / a$, and show that $(1 + h)^n \geq 1 + nh$ .]
:::

::: {.solution}
The argument is transcribed from the published solution of Dan Whitman, *Topology, Second Edition by James Munkres: Solutions Manual* (30 November 2019), Exercise 4.8, printed pp. 59--60 (`tmp/sources/munkres-solutions-whitman.pdf`): (a) is his reflection of a bounded-above set through $-A$, and (b) and (c) are his Archimedean arguments, (c) through Bernoulli's inequality as the hint directs. It is checked against Munkres, Topology (2000), §4 Exercise 8.

::: pf

::: {.pf-step #glb}
$\RR$ has the greatest lower bound property.

::: pf-proof
Let $A\subseteq\RR$ be nonempty and bounded below and put $-A=\{-a:a\in A\}$, which is nonempty and bounded above. Let $s=\sup(-A)$. For $a\in A$ one has $-a\le s$, so $-s\le a$: the number $-s$ is a lower bound of $A$. If $\ell$ is any lower bound of $A$ then $\ell\le a$ for all $a\in A$, so $-a\le-\ell$ for all $a$, which makes $-\ell$ an upper bound of $-A$ and hence $s\le-\ell$, that is $\ell\le-s$. So $-s$ is the greatest lower bound.
:::

:::

::: {.pf-step #reciprocals}
$\inf\{1/n:n\in\ZZ_+\}=0$.

::: pf-proof
Every $1/n$ is positive, so $0$ is a lower bound. If $c>0$ then the Archimedean property gives $n\in\ZZ_+$ with $n>1/c$, hence $0<1/n<c$, so $c$ is not a lower bound. Therefore the greatest lower bound is $0$.
:::

:::

::: {.pf-step #geometric}
For $0<a<1$, $\inf\{a^{n}:n\in\ZZ_+\}=0$.

:::: pf-proof

::: {.pf-step #bernoulli}
With $h=(1-a)/a>0$, one has $(1+h)^{n}\ge1+nh$ for every $n\ge1$.

::: pf-proof
$1+h=1/a$. Induction on $n$: the case $n=1$ is an equality, and $(1+h)^{n+1}\ge(1+nh)(1+h)=1+(n+1)h+nh^{2}\ge1+(n+1)h$.
:::

:::

::: {.pf-step #bound}
$a^{n}\le\dfrac{1}{1+nh}$ for every $n\ge1$.

::: pf-proof
$a=1/(1+h)$, so $a^{n}=1/(1+h)^{n}\le1/(1+nh)$ by step [](#bernoulli){.pf-ref}, all quantities being positive.
:::

:::

::: {.pf-step #small}
For every $\varepsilon>0$ there is $n$ with $a^{n}<\varepsilon$.

::: pf-proof
The Archimedean property gives $n$ with $1+nh>1/\varepsilon$, and then $a^{n}\le1/(1+nh)<\varepsilon$ by step [](#bound){.pf-ref}.
:::

:::

::: {.pf-step}
$\inf\{a^{n}:n\in\ZZ_+\}=0$.

::: pf-proof
All $a^{n}$ are positive, so $0$ is a lower bound, and step [](#small){.pf-ref} shows that no positive number is one.
:::

:::

:::

:::

::: {.pf-step}
Parts (a), (b) and (c) hold.

::: pf-proof
Step [](#glb){.pf-ref} is (a), step [](#reciprocals){.pf-ref} is (b) and step [](#geometric){.pf-ref} is (c):
$$
\boxed{\RR\text{ has the glb property};\quad \inf\{1/n\}=0;\quad \inf\{a^{n}:n\ge1\}=0\text{ for }0<a<1.}
$$
The hint printed with (c) is used exactly in step [](#bernoulli){.pf-ref}, and both (b) and (c) rest on the Archimedean property of $\RR$.
:::

:::

:::
:::
