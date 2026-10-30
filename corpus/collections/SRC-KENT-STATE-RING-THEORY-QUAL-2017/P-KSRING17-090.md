---
schema: qual/card@1
id: P-KSRING17-090
kind: problem
title: Existence of gcds and lcms in a principal ideal domain
classification:
  areas: [algebra]
  topics:
  - Greatest Common Divisors
  - Least Common Multiples
  - Principal Ideal Domains
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-12
  note: Checked against Problem 90 of the retained Kent State Algebra Qualifying Exam Problems — Ring Theory compilation, version August 29, 2017.
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Removed OCR residue from part (b) and restored the item structure of both parts against problem 90 on Ring_Theory_Qual_Problems.pdf PDF page 12.
---

::: {.problem}
Let $D$ be a principal ideal domain and let $a, b \in D$.

(a) Show that there is an element $d \in D$ that satisfies the properties

(i) $d \divides a$ and $d \divides b$ and

(ii) if $e \divides a$ and $e \divides b$ then $e \divides d$.

(b) Show that there is an element $m \in D$ that satisfies the properties

(i) $a \divides m$ and $b \divides m$ and

(ii) if $a \divides e$ and $b \divides e$ then $m \divides e$.
:::

::: {.solution}

::: pf

::: {.pf-step #s1-1}

Since $D$ is a principal ideal domain, the ideal
$$
(a)+(b)
$$
is principal.
Choose
$$
d\in D
$$
such that
$$
(a)+(b)=(d).
$$


::: pf-proof

The sum
$$
(a)+(b)
$$
is an ideal of $D$.
Every ideal in a PID is principal, so such a generator $d$ exists.

:::

:::

::: {.pf-step #s1-2}

One has
$$
d\mid a
\qquad\text{and}\qquad
d\mid b.
$$


::: pf-proof

Since
$$
a\in(a)
\subseteq
(a)+(b)
=(d),
$$
there exists
$$
r\in D
$$
such that
$$
a=rd.
$$
Thus
$$
d\mid a.
$$

Similarly,
$$
b\in(b)
\subseteq
(d),
$$
so
$$
d\mid b.
$$

:::

:::

::: {.pf-step #s1-3}

If
$$
e\mid a
\qquad\text{and}\qquad
e\mid b,
$$
then
$$
e\mid d.
$$


::: pf-proof

Write
$$
a=er,
\qquad
b=es
$$
for some
$$
r,s\in D.
$$
Because
$$
d\in(d)
=(a)+(b),
$$
there exist
$$
u,v\in D
$$
such that
$$
d=ua+vb.
$$
Substituting the expressions for $a$ and $b$ gives
$$
d
=
u(er)+v(es)
=
e(ur+vs).
$$
Hence
$$
e\mid d.
$$

:::

:::

::: {.pf-step #s1-4}

Thus the element $d$ from step [](#s1-1){.pf-ref} satisfies the two properties in part (a).


::: pf-proof

Step [](#s1-2){.pf-ref} proves property (i), and step [](#s1-3){.pf-ref} proves property (ii).

:::

:::

::: {.pf-step #s1-5}

The ideal
$$
(a)\cap(b)
$$
is principal.
Choose
$$
m\in D
$$
such that
$$
(a)\cap(b)=(m).
$$


::: pf-proof

The intersection of two ideals is an ideal.
Since $D$ is a PID, it is principal.

:::

:::

::: {.pf-step #s1-6}

One has
$$
a\mid m
\qquad\text{and}\qquad
b\mid m.
$$


::: pf-proof

Since
$$
m\in(m)
=(a)\cap(b),
$$
one has
$$
m\in(a)
$$
and
$$
m\in(b).
$$
Thus
$$
a\mid m
\qquad\text{and}\qquad
b\mid m.
$$

:::

:::

::: {.pf-step #s1-7}

If
$$
a\mid e
\qquad\text{and}\qquad
b\mid e,
$$
then
$$
m\mid e.
$$


::: pf-proof

The divisibility assumptions mean
$$
e\in(a)
\qquad\text{and}\qquad
e\in(b).
$$
Hence
$$
e\in(a)\cap(b)
=(m).
$$
Therefore
$$
m\mid e.
$$

:::

:::

::: {.pf-step #s1-8}

Thus the element $m$ from step [](#s1-5){.pf-ref} satisfies the two properties in part (b).


::: pf-proof

Step [](#s1-6){.pf-ref} proves property (i), and step [](#s1-7){.pf-ref} proves property (ii).

:::

:::

::: pf-qed

Step [](#s1-4){.pf-ref} proves part (a), and step [](#s1-8){.pf-ref} proves part (b).

:::

:::

:::
