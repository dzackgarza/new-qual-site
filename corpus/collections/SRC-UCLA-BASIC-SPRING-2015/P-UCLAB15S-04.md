---
schema: qual/card@1
id: P-UCLAB15S-04
kind: problem
title: Intermediate value property plus closed fibers implies continuity
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
  note: Checked against the vendored UCLA Basic Examination, Spring 2015, `assets/attachments/basic-15S.pdf`.
---

::: {.problem}
Let $f:[0,1]\to\RR$ satisfy the intermediate value property: whenever $0\le a<b\le1$ and $y$ lies between $f(a)$ and $f(b)$, there exists $x\in(a,b)$ such that $f(x)=y$.
Assume that for every $y\in\RR$, the preimage $f^{-1}(\{y\})$ is closed.
Prove that $f$ is continuous.
:::

::: {.solution}

Fix
\[
x_0\in[0,1].
\]

::: pf

::: {.pf-step #s1-1}

Suppose, for contradiction, that $f$ is not continuous at $x_0$.
Then there exist
\[
\varepsilon>0
\]
and a sequence
\[
x_n\to x_0
\]
such that
\[
|f(x_n)-f(x_0)|\ge\varepsilon
\]
for every $n$.


::: pf-proof

This is the sequential criterion for failure of continuity in a metric space.

:::

:::

::: {.pf-step #s1-2}

After passing to a subsequence, one of the following alternatives holds for every $n$:
\[
f(x_n)\ge f(x_0)+\varepsilon,
\]
or
\[
f(x_n)\le f(x_0)-\varepsilon.
\]


::: pf-proof

For each $n$, the inequality
\[
|f(x_n)-f(x_0)|\ge\varepsilon
\]
places $f(x_n)$ in one of the two displayed regions.
At least one of these two alternatives occurs infinitely often.
Pass to the corresponding subsequence.

:::

:::

::: {.pf-step #s1-3}

Assume first that
\[
f(x_n)\ge f(x_0)+\varepsilon
\]
for all $n$, and set
\[
y=f(x_0)+\frac{\varepsilon}{2}.
\]
Then for every $n$ there exists a point $z_n$ strictly between $x_0$ and $x_n$ such that
\[
f(z_n)=y.
\]


::: pf-proof

The number $y$ lies strictly between
\[
f(x_0)
\]
and
\[
f(x_n),
\]
because
\[
f(x_0)
<
f(x_0)+\frac{\varepsilon}{2}
<
f(x_0)+\varepsilon
\le
f(x_n).
\]
Apply the intermediate value property on the interval with endpoints $x_0$ and $x_n$.

:::

:::

::: {.pf-step #s1-4}

The sequence $(z_n)$ converges to $x_0$.


::: pf-proof

Because $z_n$ lies between $x_0$ and $x_n$,
\[
|z_n-x_0|
\le
|x_n-x_0|.
\]
Since
\[
x_n\to x_0,
\]
the right-hand side tends to zero.
Hence
\[
z_n\to x_0.
\]

:::

:::

::: {.pf-step #s1-5}

The closedness of the fiber
\[
f^{-1}(\{y\})
\]
forces
\[
f(x_0)=y,
\]
a contradiction.


::: pf-proof

By step [](#s1-3){.pf-ref},
\[
z_n\in f^{-1}(\{y\})
\]
for every $n$.
By step [](#s1-4){.pf-ref},
\[
z_n\to x_0.
\]
The fiber is closed by hypothesis, so it contains its limit point:
\[
x_0\in f^{-1}(\{y\}).
\]
Thus
\[
f(x_0)=y.
\]
But
\[
y=f(x_0)+\frac{\varepsilon}{2},
\]
which is impossible.

:::

:::

::: {.pf-step #s1-6}

The alternative
\[
f(x_n)\le f(x_0)-\varepsilon
\]
also leads to a contradiction.


::: pf-proof

Set
\[
y=f(x_0)-\frac{\varepsilon}{2}.
\]
Then $y$ lies strictly between $f(x_n)$ and $f(x_0)$.
By the intermediate value property, choose $z_n$ between $x_n$ and $x_0$ with
\[
f(z_n)=y.
\]
Again,
\[
z_n\to x_0.
\]
Closedness of
\[
f^{-1}(\{y\})
\]
would force
\[
f(x_0)=y
=
f(x_0)-\frac{\varepsilon}{2},
\]
a contradiction.

:::

:::

::: {.pf-step #s1-7}

Therefore $f$ is continuous at $x_0$.


::: pf-proof

The assumption of discontinuity in step [](#s1-1){.pf-ref} leads, after step [](#s1-2){.pf-ref}, to one of the two alternatives.
Steps [](#s1-3){.pf-ref} through [](#s1-5){.pf-ref} rule out the first, and step [](#s1-6){.pf-ref} rules out the second.
Hence $f$ must be continuous at $x_0$.

:::

:::

::: {.pf-step #s1-8}

Since $x_0$ was arbitrary,
\[
\boxed{f\text{ is continuous on }[0,1].}
\]


::: pf-proof

Step [](#s1-7){.pf-ref} applies at every point of the domain, including the endpoints because the argument uses only points of $[0,1]$ and one-sided sequences there.

:::

:::

::: pf-qed

Step [](#s1-8){.pf-ref} is the required conclusion.

:::

:::

:::
