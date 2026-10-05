---
schema: qual/card@1
id: P-UCLAB16S-06
kind: problem
title: Open and closed balls in an ultrametric
classification:
  areas:
  - prelim
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-13
  note: Checked against the vendored UCLA Basic Examination, Spring 2016, `assets/attachments/basic-16S.pdf`.
---

::: {.problem}
A metric $\rho$ on a metric space $(X,\rho)$ is an ultrametric if
\[
\rho(x,y)\le \max\{\rho(x,z),\rho(y,z)\}
\qquad\text{for all }x,y,z\in X.
\]
Prove that every open ball $\{y:\rho(x,y)<r\}$ is closed and every closed ball $\{y:\rho(x,y)\le r\}$ is open.
:::

::: {.solution}
Fix
\[
x\in X
\qquad\text{and}\qquad
r>0.
\]
Write
\[
B(x,r)
=
\{y\in X:\rho(x,y)<r\}
\]
and
\[
\overline B(x,r)
=
\{y\in X:\rho(x,y)\le r\}.
\]

<1>1. Let
\[
y\notin B(x,r).
\]
Then
\[
\rho(x,y)\ge r.
\]

::: {.proof}
This is exactly the negation of the defining inequality
\[
\rho(x,y)<r.
\]
:::

<1>2. If
\[
z\in B(y,\rho(x,y)),
\]
then
\[
\rho(x,z)=\rho(x,y).
\]

::: {.proof}
The assumption
\[
z\in B(y,\rho(x,y))
\]
means
\[
\rho(y,z)<\rho(x,y).
\]
The ultrametric inequality gives
\[
\rho(x,z)
\le
\max\{\rho(x,y),\rho(y,z)\}
=
\rho(x,y).
\]

Applying the ultrametric inequality in the form
\[
\rho(x,y)
\le
\max\{\rho(x,z),\rho(z,y)\},
\]
and using
\[
\rho(z,y)<\rho(x,y),
\]
forces
\[
\rho(x,z)\ge\rho(x,y).
\]
Thus equality holds.
:::

<1>3. The complement of the open ball $B(x,r)$ is open.

::: {.proof}
Take
\[
y\notin B(x,r).
\]
By step <1>1,
\[
\rho(x,y)\ge r.
\]
For every
\[
z\in B(y,\rho(x,y)),
\]
step <1>2 gives
\[
\rho(x,z)
=
\rho(x,y)
\ge
r.
\]
Hence
\[
z\notin B(x,r).
\]
Therefore
\[
B(y,\rho(x,y))
\subseteq
X\setminus B(x,r).
\]
So every point of the complement has an open neighborhood contained in the complement.
:::

<1>4. Therefore
\[
\boxed{B(x,r)\text{ is closed}.}
\]

::: {.proof}
Step <1>3 shows that its complement is open.
:::

<1>5. Let
\[
y\in\overline B(x,r).
\]
Then
\[
\rho(x,y)\le r.
\]

::: {.proof}
This is the definition of the closed ball.
:::

<1>6. If
\[
z\in B(y,r),
\]
then
\[
z\in\overline B(x,r).
\]

::: {.proof}
The assumptions give
\[
\rho(y,z)<r
\]
and
\[
\rho(x,y)\le r.
\]
By the ultrametric inequality,
\[
\rho(x,z)
\le
\max\{\rho(x,y),\rho(y,z)\}
\le
r.
\]
Thus
\[
z\in\overline B(x,r).
\]
:::

<1>7. Therefore
\[
\boxed{\overline B(x,r)\text{ is open}.}
\]

::: {.proof}
For every
\[
y\in\overline B(x,r),
\]
step <1>6 gives
\[
B(y,r)
\subseteq
\overline B(x,r).
\]
Thus every point of the closed ball has an open neighborhood contained in it.
:::

<1>8. Q.E.D.

::: {.proof}
Step <1>4 proves that every open ball is closed, and step <1>7 proves that every closed ball is open.
:::
:::
