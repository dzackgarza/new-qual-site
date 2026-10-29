---
schema: qual/card@1
id: E-FUIDU
kind: problem
title: A self-map of $\DD$ with $f(1/2)=3/4$ and $f'(1/2)=2/3$
classification:
  areas:
  - complex-analysis
  topics:
  - Schwarz Lemma
  - Blaschke Factors
  - Counterexamples
relations: []
review: draft
audit:
- event: source-corrected
  by: Claude Opus 5.5
  date: 2026-10-29
  note: 'The source asks for "a map $f: \DD\to \DD$" without requiring it holomorphic; without that hypothesis such a map exists. The statement now asks for a holomorphic map.'
---

::: {.exercise}
Does there exist a holomorphic map $f: \DD\to \DD$ with

- $f\qty{1\over 2} = {3\over 4}$

- $f'\qty{1\over 2} = {2\over 3}$?
:::

::: {.solution}

::: pf

::: {.pf-step #pick-bound}
Every holomorphic $f:\DD\to\DD$ with $f\qty(\frac12)=\frac34$ satisfies $\abs{f'\qty(\frac12)}\le\frac7{12}$.

::: pf-proof
By the Schwarz--Pick lemma,
$$
\abs{f'\qty(\tfrac12)}\le\frac{1-\abs{f(1/2)}^2}{1-(1/2)^2}=\frac{1-9/16}{3/4}=\frac7{12}.
$$
:::

:::

::: pf-step
$\boxed{\text{No}}$ such $f$ exists.

::: pf-proof
$\frac23>\frac7{12}$, which step [](#pick-bound){.pf-ref} excludes.
:::

:::

:::

:::
