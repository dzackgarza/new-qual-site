---
schema: qual/card@1
id: P-CAEXAMPREP-08
kind: problem
title: A monic polynomial is large somewhere on the unit circle
classification: {areas: [complex-analysis], topics: []}
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against the deterministic MinerU Flash extraction assets/attachments/Complex_Analysis_Exam_Prep_Solutions_extracted.md.
---

::: {.problem}
Let
$$
p(z)=z^n+a_{n-1}z^{n-1}+\cdots+a_1z+a_0.
$$
Show that there is at least one point $z_0$ with $|z_0|=1$ such that $|p(z_0)|\ge1$.

Hint: if $|p(z)|<1$ everywhere on $|z|=1$, compare the number of zeros of
$$
q(z)=a_{n-1}z^{n-1}+\cdots+a_1z+a_0
$$
with those of $z^n$.
:::

::: {.solution}

Write
$$
q(z)=p(z)-z^n.
$$

::: pf

::: {.pf-step #s1-1}

If $|p(z)|<1$ for every $|z|=1$, then $q$ and $-z^n$ have the same number of zeros in the unit disc, counted with multiplicity.


::: pf-proof

On $|z|=1$,
$$
|q(z)-(-z^n)|
=|q(z)+z^n|
=|p(z)|
<1
=|-z^n|.
$$
Rouché's theorem therefore gives the same zero count for $q$ and $-z^n$ in $|z|<1$. Since $-z^n$ has a zero of multiplicity $n$ at $0$, that count is $n$.

:::

:::

::: {.pf-step #s1-2}

The hypothesis $|p(z)|<1$ for every $|z|=1$ is impossible.


::: pf-proof

Under that hypothesis, $q$ cannot be the zero polynomial: if $q\equiv0$, then $p(z)=z^n$ and $|p(z)|=1$ on the unit circle. Hence $q$ is a nonzero polynomial of degree at most $n-1$, so it has at most $n-1$ zeros in $\CC$, counted with multiplicity. This contradicts step [](#s1-1){.pf-ref}, which gives $n$ zeros already in the unit disc.

:::

:::

::: {.pf-step #s1-3}

Consequently there exists $z_0$ with $|z_0|=1$ such that
$$
\boxed{|p(z_0)|\ge1}.
$$


::: pf-proof

If no such point existed, then $|p(z)|<1$ at every point of the unit circle, contrary to step [](#s1-2){.pf-ref}.

:::

:::

::: pf-qed

Step [](#s1-3){.pf-ref} is exactly the required conclusion.

:::

:::

:::
