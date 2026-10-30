---
schema: qual/card@1
id: P-BKS17-5B
kind: problem
title: All values of $i^i$
classification:
  areas:
  - prelim
  topics:
  - Complex Analysis
relations: []
review: draft
audit:
- event: source-checked
  by: claude-opus-5
  date: 2026-09-16
  note: Restored spaces around inline math and normalized LaTeX against Sp17_Exam_0.pdf page 16 problem 5B.
- event: source-checked
  by: chatgpt
  date: 2026-10-02
  note: Independently reviewed the supplied Berkeley Spring 2017 logarithm calculation. The branch enumeration and resulting values are correct.
- event: solution-written
  by: chatgpt
  date: 2026-10-02
- event: solution-reviewed
  by: chatgpt
  date: 2026-10-02
  note: Verified that all logarithms of $i$ are enumerated and that exponentiation gives exactly the stated positive real values.
---

::: {.problem}
Write all values of $i^i$ in the form $a + bi$.
:::

::: {.solution}

For $k\in\ZZ$, set
$$
L_k\coloneqq i\left(\frac{\pi}{2}+2\pi k\right).
$$

::: pf

::: {.pf-step #s1-1}

The numbers $L_k$, $k\in\ZZ$, are exactly the complex logarithms of $i$.


::: pf-proof

For every $k\in\ZZ$,
$$
e^{L_k}
=
e^{i(\pi/2+2\pi k)}
=i.
$$
Conversely, if $L=x+iy$ satisfies $e^L=i$, then taking absolute values gives $e^x=1$, hence $x=0$. Thus $e^{iy}=i$, which holds exactly when
$$
y=\frac{\pi}{2}+2\pi k
$$
for some $k\in\ZZ$. Hence $L=L_k$.

:::

:::

::: {.pf-step #s1-2}

The complete set of values of $i^i$ is
$$
\boxed{
\left\{
e^{-(\pi/2+2\pi k)}+0i
\;:\;
k\in\ZZ
\right\}
}.
$$


::: pf-proof

By definition, the multivalued power $i^i$ consists of the values
$$
e^{iL}
$$
as $L$ ranges over all logarithms of $i$. By step [](#s1-1){.pf-ref} these logarithms are precisely the $L_k$, so
$$
e^{iL_k}
=
e^{i\cdot i(\pi/2+2\pi k)}
=
e^{-(\pi/2+2\pi k)}.
$$
Each value is a positive real number, giving the displayed form $a+bi$ with $b=0$.

:::

:::

::: pf-qed

Step [](#s1-2){.pf-ref} lists every value and no others.

:::

:::

:::
