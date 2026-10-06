---
schema: qual/card@1
id: P-WESCA13J-II3
kind: problem
title: 'An entire square root forces constancy — as extracted'
classification:
  areas: [complex-analysis]
  topics: []
relations: []
review: draft
audit:
- event: source-checked
  by: gpt-5.6-sol
  date: 2026-09-14
  note: Checked against Problems, problem 3 in the deterministic MinerU Flash extraction assets/attachments/analysis_2008-2013_extracted.md. This is the deterministic Flash reading. As written it is false (for example $f(z)=z^2$ admits the entire square root $g(z)=z$), so no unrecorded correction has been made.
---

::: {.problem}
Let $f$ be entire and suppose the function
\[
g(z)=\sqrt{f(z)}
\]
is also entire.
Prove that $f$ is constant.
:::

::: {.solution}
The statement is false as printed.

<1>1. Let
$$
g(z)=z.
$$
Then
$$
g
$$
is entire.

::: {.proof}
The identity function
$$
z\mapsto z
$$
is a polynomial, hence entire.
:::

<1>2. Define
$$
f(z)=g(z)^2=z^2.
$$
Then
$$
f
$$
is entire and nonconstant.

::: {.proof}
The function
$$
z^2
$$
is a nonconstant polynomial, hence entire.
:::

<1>3. The function
$$
g
$$
is an entire square root of
$$
f:
$$
$$
\boxed{g(z)^2=f(z)}
$$
for every
$$
z\in\mathbb C.
$$

::: {.proof}
By construction,
$$
g(z)^2
=
z^2
=
f(z).
$$
:::

<1>4. Therefore the hypotheses of the printed problem do not force
$$
f
$$
to be constant.

::: {.proof}
Steps <1>1--<1>3 produce an explicit pair of entire functions
$$
f(z)=z^2,
\qquad
g(z)=z,
$$
with
$$
g^2=f,
$$
while
$$
f
$$
is nonconstant.
:::

<1>5. More generally, every nonconstant entire function
$$
h
$$
produces a counterexample
$$
f=h^2,
\qquad
g=h.
$$

::: {.proof}
If
$$
h
$$
is entire, then both
$$
h
$$
and
$$
h^2
$$
are entire, and
$$
h
$$
is an entire square root of
$$
h^2.
$$
If
$$
h
$$
is nonconstant, then so is
$$
h^2.
$$
:::

<1>6. Hence no proof of the requested conclusion exists without an additional hypothesis.

::: {.proof}
Step <1>4 already contradicts the claimed conclusion, and step <1>5 shows that the failure is not exceptional but occurs for every square of a nonconstant entire function.
:::
:::
