---
schema: qual/card@1
id: P-KSRING17-090
kind: problem
title: Existence of gcds and lcms in a principal ideal domain
classification:
  areas: [algebra]
  topics: []
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

  i. $d \mid a$ and $d \mid b$ and

  ii. if $e \mid a$ and $e \mid b$ then $e \mid d$.

(b) Show that there is an element $m \in D$ that satisfies the properties

  i. $a \mid m$ and $b \mid m$ and

  ii. if $a \mid e$ and $b \mid e$ then $m \mid e$.
:::

::: pf

::: pf-step

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

::: pf-step

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

::: pf-step

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

::: pf-step

Thus the element $d$ from step <1>1 satisfies the two properties in part (a).


::: pf-proof

Step <1>2 proves property (i), and step <1>3 proves property (ii).

:::

:::

::: pf-step

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

::: pf-step

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

::: pf-step

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

::: pf-step

Thus the element $m$ from step <1>5 satisfies the two properties in part (b).


::: pf-proof

Step <1>6 proves property (i), and step <1>7 proves property (ii).

:::

:::

::: pf-qed

Step <1>4 proves part (a), and step <1>8 proves part (b).

:::

:::
