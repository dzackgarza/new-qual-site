---
schema: qual/card@1
id: P-VPCUJ
kind: problem
title: The supremum and pointwise limit of measurable functions are measurable
classification:
  areas:
  - real-analysis
  topics:
  - Measure Theory
relations: []
review: draft
audit:
- event: solution-written
  by: gemini-3.7-flash
  date: 2026-08-17
---

::: problem
Let \( \ts{ f_k } _{k=1}^{\infty } \) be a sequence of extended real-valued Lebesgue measurable functions.

a. Prove that \( \sup_k f_k \) is a Lebesgue measurable function.

b. Prove that if \( \lim_{k \to \infty } f_k(x) \) exists for every \( x \in \RR^n \) then \( \lim_{k\to \infty } f_k \) is also a measurable function.
:::
::: {.solution}
<1>1. (a) $\sup_k f_k$ is measurable.
::: {.proof}
for every $a \in \RR$, \[ \Big\{\sup_k f_k \le a\Big\} = \bigcap_k \big\{f_k \le a\big\}, \] a countable intersection of measurable sets (each $f_k$ is measurable), hence measurable.
:::
<1>2. (b) Reduce $\lim_k f_k$ to operations on measurable functions.
::: {.proof}
where the limit exists, \[ \lim_{k\to\infty} f_k = \liminf_{k\to\infty} f_k = \sup_{m} \inf_{k \ge m} f_k, \] so it suffices to show $\inf_k f_k$ and $\sup_k f_k$ are measurable.
:::
<1>3. $\inf_k f_k$ is measurable.
::: {.proof}
$\{\inf_k f_k \ge a\} = \cap_k\{f_k \ge a\}$, a countable intersection of measurable sets.
:::
<1>4. Conclude (b).
::: {.proof}
by <1>1 and <1>3, $\sup_m\inf_{k\ge m} f_k$ is measurable (sup and inf of measurable functions are measurable), and it equals $\lim_k f_k$ on the set where the limit exists — all of $\RR^n$ by hypothesis.
:::
<1>5. Q.E.D.
:::
